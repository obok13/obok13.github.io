#!/usr/bin/env python3
"""블로그 포스트(_posts/*.md)의 kramdown + MathJax 렌더링 위험을 검사한다.
CLAUDE.md "자동 검사·수정" 절의 규칙을 그대로 구현한 것이다 (규칙 제목은 거기 기준).

사용법:
  python scripts/check_post.py _posts/2026-08-11-foo.md [...]   # 파일 직접 검사
  python scripts/check_post.py --fix _posts/2026-08-11-foo.md    # [자동수정] 규칙만 파일에 직접 적용 후 검사
  python scripts/check_post.py                                   # 인자 없으면
      Claude Code hook의 stdin JSON에서 편집된 file_path를 읽어 검사 (--fix는 여기선 절대 자동 적용 안 됨)

동작:
  - ERROR/REVIEW가 하나라도 있으면 exit code 2로 끝난다.
    (PostToolUse hook에서 exit 2이면 stderr가 Claude에게 피드백되어 곧바로 대응할 수 있다.)
  - --fix는 사람 또는 Claude가 명시적으로 CLI에서 호출할 때만 동작한다. hook은 파일을
    몰래 다시 쓰지 않는다 (Claude의 Edit 결과와 diff가 어긋나는 걸 피하기 위해).

계층 (CLAUDE.md 참고):
  [자동수정] -- 의미 손실 없는 순수 delimiter/문자 치환. --fix로 직접 고침.
    - [렌더링-집합기호] 단일 $ 안에 \\{ 또는 \\}  -> \\lbrace, \\rbrace 로 치환
    - [렌더링-아래첨자] 단일 $ 안에 )_ 또는 ]_     -> 그 밑줄만 \\_ 로 escape
    - [렌더링-별표]     단일 $ 안의 (escape 안 된) * -> \\ast 로 치환
    - [렌더링-행렬]     단일 $ 안에 행렬/\\ 줄바꿈 -> $$ 로 감싸기 (안전한 단일 $ 대안을 못 찾음)
    - [렌더링-파이프]   수식($ 또는 $$) 안의 |     -> \\vert 로

  집합기호/아래첨자/별표는 예전엔 $$로 감싸는 게 유일한 해법인 줄 알았는데, kramdown의
  markdown escape 규칙(\\+문장부호 -> 문장부호만 남김, \\+글자 -> 안 건드림)을 이용하면
  단일 $를 유지한 채로도 고칠 수 있다는 게 밝혀져 fix 방식이 바뀌었다(2026-09-07). 행렬의
  \\ 줄바꿈만 검증된 단일 $ 대안이 없어 여전히 $$로 감싼다.
  [자동검사] -- 기계적으로 찾을 수는 있지만 고치려면 문맥 판단(문장 재구성, 대체 표현
    선택, 동명이인 구분 등)이 필요해서 REVIEW/ERROR로 보고만 하고 자동으로 고치지 않는다.
    - [렌더링-문단시작] 문단이 $$ 로 시작 -> 앞 문장에 붙이기
    - [렌더링-em대시]   em dash(—) 사용 -> 제거 (인용 출처면 무시)
    - [표현-비속어]     "죽이다" 류 속어/비격식 은유 -> 정확한 수학적 표현으로
    - [정합성-참고문헌 번호] 본문 [n] 인용 <-> 참고문헌 항목 번호 불일치
    - [정합성-mathematicians] front matter 이름과 본문/참고문헌 불일치 (substring 매칭 힌트일 뿐)
    - [정합성-포스트링크] "OOO 글" 텍스트 인용이 markdown link로 안 바뀐 채 남은 곳 (휴리스틱 힌트일 뿐)
    - [서식-나열] Definition/Theorem/Proposition/Corollary/Lemma 진술이 (a)(b)... 또는
      (i)(ii)... 나열을 인라인 한 문장에 욱여넣은 곳 (휴리스틱 힌트일 뿐 — "(x,0)" 같은
      순서쌍이나 우연한 수식 겹침으로 오탐할 수 있어 Claude가 실제 나열인지 확인한다)

[용어-한영 변환](한국어/영어 수학 용어 처리)는 문맥 판단이 필요해 여기서 다루지 않는다
-- CLAUDE.md의 "용어" 절에서 Claude가 직접 판단해서 처리한다.
"""
import sys, os, re, json

try:  # Windows 콘솔 인코딩
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

BS = "\\"
ROWBREAK = BS + BS          # LaTeX 행 바꿈 '\\'
EMDASH = "\u2014"           # — (en dash '–' U+2013 은 이름/범위에 허용되므로 검사 안 함)

# 수학적 동작을 속어/비격식으로 은유하는 표현. 정확한 표현으로 바꿔 쓴다.
SLANG_HINTS = ["죽이", "죽여", "박살", "날려버리", "날려 버리"]

SINGLE_DOLLAR = re.compile(r"(?<!\$)\$(?!\$)[^$]*\$(?!\$)")
MATH_REGION = re.compile(r"\${1,2}[^$]*\${1,2}")
MATRIX_ENV = re.compile(r"\\begin\{[a-zA-Z]*matrix")


def check_text(text):
    errors = []
    lines = text.split("\n")
    for i, line in enumerate(lines, 1):
        # $$...$$ 를 마스킹해 단일 $ 구간만 분리
        masked = re.sub(r"\$\$.*?\$\$", "\u00a7", line)
        for seg in SINGLE_DOLLAR.findall(masked):
            if BS + "{" in seg or BS + "}" in seg:
                errors.append((i, r"단일 $ 안에 \{ 또는 \} → \lbrace, \rbrace 로 치환", seg))
            if re.search(r"[)\]}]_", seg):
                errors.append((i, r"단일 $ 안에 )_ ]_ 또는 }_ → 그 밑줄만 \_ 로 escape", seg))
            if re.search(r"(?<!\\)\*", seg):
                errors.append((i, r"단일 $ 안의 별표 * → \ast 로 치환", seg))
            if MATRIX_ENV.search(seg) or ROWBREAK in seg:
                errors.append((i, r"단일 $ 안에 행렬/\\ 줄바꿈 → $$ 로 감싸기", seg))
        # 수식 안의 파이프 | (\vert / \| 는 예외) — $$ 안에서도 kramdown이 표로 깨뜨림
        for seg in MATH_REGION.findall(line):
            for j, ch in enumerate(seg):
                if ch == "|" and (j == 0 or seg[j - 1] != BS):
                    errors.append((i, r"수식 안 | → \vert 사용", seg))
                    break
        # 문단이 $$ 로 시작
        if line.startswith("$$") and i > 1 and lines[i - 2].strip() == "":
            errors.append((i, "문단이 $$ 로 시작 → 앞 문장에 붙이기", line))
        # em dash
        if EMDASH in line:
            errors.append((i, "em dash — 사용 (인용 출처가 아니면 제거)", line))
        # 속어/비격식 은유 표현
        for s in SLANG_HINTS:
            if s in line:
                errors.append((i, f'속어/비격식 표현 "{s}" → 정확한 수학적 표현으로 (예: "0으로 만드는")', line))
                break
    return errors


def is_post(path):
    p = path.replace("\\", "/")
    return p.endswith(".md") and "/_posts/" in ("/" + p)


DOLLAR2_SPLIT = re.compile(r"(\$\$.*?\$\$)")


def _fix_pipes(s):
    """수식 구간 문자열(delimiter 포함) 안의 미이스케이프 | -> \\vert. [렌더링-파이프]"""
    out = []
    for j, ch in enumerate(s):
        if ch == "|" and (j == 0 or s[j - 1] != BS):
            out.append(r"\vert")
        else:
            out.append(ch)
    return "".join(out)


def _fix_braces(inner):
    """단일 $ 안의 \\{ \\} -> \\lbrace \\rbrace. [렌더링-집합기호]
    (\\{는 kramdown이 문장부호 escape 규칙으로 backslash를 지워버려 맨 { 만
    남고 그러면 MathJax에선 안 보이는 grouping 문자가 된다. \\lbrace는
    backslash+글자라 kramdown이 안 건드리고 그대로 살아남는다. 뒤에 글자가
    바로 붙으면 명령어 이름에 먹혀버리므로(예: \\lbracea) 공백 하나를 둔다 -
    TeX가 명령어 뒤 공백은 무시하므로 렌더링엔 영향이 없다.)"""
    return inner.replace(BS + "{", BS + "lbrace ").replace(BS + "}", BS + "rbrace ")


def _fix_subscript_after_bracket(inner):
    """단일 $ 안의 )_ ]_ }_ -> )\\_ ]\\_ }\\_. [렌더링-아래첨자]
    (밑줄을 escape하면 kramdown이 backslash만 지우고 밑줄 문자 하나를 그대로
    출력하므로, 그 밑줄은 더 이상 kramdown 이탤릭 델리미터 후보가 아니게 되고
    MathJax는 평범한 아래첨자로 읽는다. }_ 도 )_ ]_ 와 같은 이유로 위험하다 -
    kramdown에게는 그냥 비-단어문자 뒤에 오는 밑줄일 뿐이다, 예: \\operatorname{ev}_c.)"""
    return re.sub(r"([)\]}])_", lambda m: m.group(1) + BS + "_", inner)


def _fix_asterisk(inner):
    """단일 $ 안의 (escape 안 된) * -> \\ast. [렌더링-별표]
    (\\ast는 backslash+글자라 kramdown이 markdown 이탤릭으로 오인하지 않는다.
    뒤에 글자가 바로 붙으면 명령어 이름에 먹히므로(예: \\astb) 공백을 둔다.)"""
    return re.sub(r"(?<!\\)\*", lambda m: BS + "ast ", inner)


def _needs_dollar_wrap(inner):
    """행렬 \\ 줄바꿈만 검증된 단일 $ 대안이 없어 여전히 $$로 감싼다. [렌더링-행렬]"""
    return bool(MATRIX_ENV.search(inner) or ROWBREAK in inner)


def fix_line(line):
    """[렌더링-집합기호]/[렌더링-아래첨자]/[렌더링-별표]/[렌더링-행렬]/[렌더링-파이프]를 직접 고친다."""
    parts = DOLLAR2_SPLIT.split(line)
    for i, part in enumerate(parts):
        if i % 2 == 1:  # $$...$$ 블록: 파이프만 고치면 됨(이미 $$로 감싸여 있음)
            parts[i] = _fix_pipes(part)
        else:
            def repl(m):
                seg = m.group(0)
                inner = seg[1:-1]
                inner = _fix_pipes(inner)
                inner = _fix_braces(inner)
                inner = _fix_subscript_after_bracket(inner)
                inner = _fix_asterisk(inner)
                return f"$${inner}$$" if _needs_dollar_wrap(inner) else f"${inner}$"
            parts[i] = SINGLE_DOLLAR.sub(repl, part)
    return "".join(parts)


def fix_text(text):
    return "\n".join(fix_line(l) for l in text.split("\n"))


FRONT_MATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
MATH_BLOCK_RE = re.compile(r"\$\$.*?\$\$", re.DOTALL)
MATH_INLINE_RE = re.compile(r"\$[^$\n]*\$")
CITATION_RE = re.compile(r"\[(\d+(?:\s*,\s*\d+)*)\]")
REF_ENTRY_RE = re.compile(r"^(\d+)\.\s")
MATHEMATICIANS_RE = re.compile(r"mathematicians:\s*\[(.*?)\]")
REFERENCES_HEADING_RE = re.compile(r"^##\s*참고문헌\s*$", re.MULTILINE)

# "OOO 글" 텍스트 인용 휴리스틱. 링크로 바뀌면 "글"이라는 단어 자체가 사라지므로
# (예: "[Foo]({% post_url ... %})의"), 남아 있는 "글"은 아직 안 바뀐 후보다.
# "이 글"/"앞 절" 같은 자기지시는 제목이 아니라서 걸러진다.
POST_REF_RE = re.compile(r"([A-Za-z가-힣][\w가-힣\-–—' ]{0,60}?)\s글(?:에서|의|을|이|은|에|로)?")
POST_REF_SELF = {
    "이", "그", "저", "이번", "다음", "앞", "위", "같은", "어떤", "그런", "이런", "본", "나중",
}


def check_post_links(text):
    reviews = []
    for m in POST_REF_RE.finditer(text):
        title = m.group(1).strip()
        last_word = title.split()[-1] if title.split() else title
        if last_word in POST_REF_SELF or len(title) < 2:
            continue
        line_no = text.count("\n", 0, m.start()) + 1
        reviews.append(f'L{line_no}: "{title} 글" 텍스트 인용 → 다른 포스트면 [{title}]({{% post_url ... %}}) 링크로')
    return reviews


BOLD_HEADER_RE = re.compile(r"^\*\*(?:Definition|Theorem|Proposition|Corollary|Lemma|Axiom)\b")
# "(a)...(b)", "(i)...(ii)", "(1)...(2)" 처럼 실제 나열 순서로 이어지는 경우만 잡는다
# (임의의 (x) 2개를 세면 "\sigma(1)"이 두 번 나오는 것 같은 수식 우연으로 오탐하기 쉽다).
ENUM_SEQUENCE_RES = [
    re.compile(r"\(a\).*\(b\)"),
    re.compile(r"\(i\).*\(ii\)"),
    re.compile(r"\(1\).*\(2\)"),
]


def check_inline_lists(text):
    """[서식-나열] Definition/Theorem/... 진술이 (a)(b)... 나열을 한 문장에 인라인으로
    담고 있으면 REVIEW. 실제로 불렛으로 쪼갤지, 오탐(순서쌍 등)인지는 Claude가 판단한다."""
    reviews = []
    for i, line in enumerate(text.split("\n"), 1):
        if not BOLD_HEADER_RE.match(line):
            continue
        if any(p.search(line) for p in ENUM_SEQUENCE_RES):
            reviews.append(f'L{i}: Definition/Theorem 등의 진술이 (a)(b)... 나열을 인라인으로 담고 있음 → 불렛 목록으로 (리드 문장만 남기고 각 항목을 "- (a) ..." 줄로)')
    return reviews


def strip_math(text):
    text = MATH_BLOCK_RE.sub(" ", text)
    text = MATH_INLINE_RE.sub(" ", text)
    return text


def parse_mathematicians(text):
    m = FRONT_MATTER_RE.match(text)
    if not m:
        return []
    nm = MATHEMATICIANS_RE.search(m.group(1))
    if not nm:
        return []
    return [n.strip() for n in nm.group(1).split(",") if n.strip()]


def split_sections(text):
    m = FRONT_MATTER_RE.match(text)
    body = text[m.end():] if m else text
    hm = REFERENCES_HEADING_RE.search(body)
    if hm:
        return body[:hm.start()], body[hm.end():]
    return body, ""


def check_citations(narrative, references):
    reviews = []
    used = set()
    for m in CITATION_RE.finditer(strip_math(narrative)):
        for n in m.group(1).split(","):
            used.add(int(n.strip()))
    defined = set()
    for line in references.split("\n"):
        m = REF_ENTRY_RE.match(line.strip())
        if m:
            defined.add(int(m.group(1)))
    for n in sorted(used - defined):
        reviews.append(f"인용 번호 [{n}]이 본문에 있지만 참고문헌에 해당 항목이 없음")
    for n in sorted(defined - used):
        reviews.append(f"참고문헌 {n}번 항목이 있지만 본문 어디서도 인용되지 않음")
    return reviews


def check_mathematicians(text, filepath):
    own = parse_mathematicians(text)
    narrative, references = split_sections(text)
    haystack = (narrative + references).lower()
    narrative_lower = narrative.lower()
    reviews = []
    for name in own:
        if name.lower() not in haystack:
            reviews.append(f'mathematicians의 "{name}"이(가) 본문/참고문헌 어디에도 보이지 않음')

    posts_dir = os.path.dirname(os.path.abspath(filepath))
    registry = set()
    try:
        for fn in os.listdir(posts_dir):
            if not fn.endswith(".md"):
                continue
            try:
                t = open(os.path.join(posts_dir, fn), encoding="utf-8").read()
            except OSError:
                continue
            registry.update(parse_mathematicians(t))
    except OSError:
        pass
    own_lower = {n.lower() for n in own}
    for name in sorted(registry):
        if name.lower() in own_lower:
            continue
        if name and name.lower() in narrative_lower:
            reviews.append(f'"{name}"이(가) 본문에 등장하지만 mathematicians 목록에는 없음(다른 포스트에 등재된 이름 기준)')
    return reviews


def main():
    argv = list(sys.argv[1:])
    do_fix = "--fix" in argv
    paths = [a for a in argv if a != "--fix"]
    if not paths:  # hook 모드: stdin JSON에서 file_path (--fix는 여기선 무시됨 - hook은 절대 파일을 직접 안 고침)
        try:
            data = json.load(sys.stdin)
            fp = (data.get("tool_input") or {}).get("file_path")
            if fp:
                paths = [fp]
        except Exception:
            return 0
        do_fix = False
    paths = [p for p in paths if is_post(p)]
    if not paths:
        return 0

    any_flag = False
    for p in paths:
        try:
            text = open(p, encoding="utf-8").read()
        except OSError:
            continue
        if do_fix:
            fixed = fix_text(text)
            if fixed != text:
                with open(p, "w", encoding="utf-8") as f:
                    f.write(fixed)
                print(f"[check_post] {os.path.basename(p)}: [자동수정] 규칙 적용됨", file=sys.stderr)
                text = fixed
        errors = check_text(text)
        narrative, references = split_sections(text)
        reviews = (check_citations(narrative, references) + check_mathematicians(text, p)
                   + check_post_links(text) + check_inline_lists(text))
        if not errors and not reviews:
            continue
        print(f"[check_post] {os.path.basename(p)}", file=sys.stderr)
        for (i, msg, seg) in errors:
            any_flag = True
            extra = f"   |  {seg.strip()[:80]}" if seg else ""
            print(f"  ERROR L{i}: {msg}{extra}", file=sys.stderr)
        for msg in reviews:
            any_flag = True
            print(f"  REVIEW: {msg} (자동 수정 강제 아님 — 판단 필요)", file=sys.stderr)
    return 2 if any_flag else 0


if __name__ == "__main__":
    sys.exit(main())
