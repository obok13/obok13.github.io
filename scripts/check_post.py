#!/usr/bin/env python3
"""블로그 포스트(_posts/*.md)의 kramdown + MathJax 렌더링 위험을 검사한다.

사용법:
  python scripts/check_post.py _posts/2026-08-11-foo.md [...]   # 파일 직접 검사
  python scripts/check_post.py                                   # 인자 없으면
      Claude Code hook의 stdin JSON에서 편집된 file_path를 읽어 검사

동작:
  - ERROR가 하나라도 있으면 exit code 2로 끝난다.
    (PostToolUse hook에서 exit 2이면 stderr가 Claude에게 피드백되어 곧바로 고칠 수 있다.)

검사 대상(모두 CLAUDE.md의 규칙에서 온 것):
  - 단일 $ 안에 \\{ 또는 \\}          -> $$ 로 감싸기
  - 단일 $ 안에 )_ 또는 ]_            -> $$ 로 감싸기
  - 단일 $ 안에 행렬/\\ 줄바꿈        -> $$ 로 감싸기
  - 수식($ 또는 $$) 안의 |            -> \\vert 로
  - 문단이 $$ 로 시작                 -> 앞 문장에 붙이기
  - em dash(—)                        -> 제거 (인용 출처면 무시)
  - "죽이다" 류 속어/비격식 은유       -> 정확한 수학적 표현으로 (예: "0으로 만드는")

한국어/영어 수학 용어 처리(어느 게 허용되고 어느 게 금지인지, 새 용어를 어떻게
분류할지)는 문맥 판단이 필요해 여기서 다루지 않는다 — CLAUDE.md의 "한국어 수학
용어 처리" 절에서 Claude가 직접 판단해서 처리한다.
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
                errors.append((i, r"단일 $ 안에 \{ 또는 \} → $$ 로 감싸기", seg))
            if re.search(r"[)\]]_", seg):
                errors.append((i, r"단일 $ 안에 )_ 또는 ]_ → $$ 로 감싸기", seg))
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


def main():
    paths = list(sys.argv[1:])
    if not paths:  # hook 모드: stdin JSON에서 file_path
        try:
            data = json.load(sys.stdin)
            fp = (data.get("tool_input") or {}).get("file_path")
            if fp:
                paths = [fp]
        except Exception:
            return 0
    paths = [p for p in paths if is_post(p)]
    if not paths:
        return 0

    any_error = False
    for p in paths:
        try:
            text = open(p, encoding="utf-8").read()
        except OSError:
            continue
        errors = check_text(text)
        if not errors:
            continue
        print(f"[check_post] {os.path.basename(p)}", file=sys.stderr)
        for (i, msg, seg) in errors:
            any_error = True
            extra = f"   |  {seg.strip()[:80]}" if seg else ""
            print(f"  ERROR L{i}: {msg}{extra}", file=sys.stderr)
    return 2 if any_error else 0


if __name__ == "__main__":
    sys.exit(main())
