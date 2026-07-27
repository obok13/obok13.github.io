---
layout: post
title: "실수 (Real number)"
date: 2026-07-23
---

## 실수의 정의: Complete Ordered Field

다음 3가지 성질을 만족하는 구조를 실수 (real number)라고 정의한다.

1. **Field.** $(\mathbb{R}, +, \times)$ is a field.
   (덧셈과 곱셈이 결합·교환·분배법칙을 만족하고 항등원·역원을 갖는다는 뜻.)
2. **Order.** $\mathbb{R}$ is a totally ordered set whose order is compatible with the field operations: $x<y \implies x+z<y+z$ for all $z$, and $x,y>0 \implies xy>0$.
   (순서와 사칙연산 구조가 서로 호환된다.)
3. **Completeness (Least Upper Bound Property).** Every non-empty subset of $\mathbb{R}$ that is bounded above has a supremum(최소상계) in $\mathbb{R}$.
   ($\mathbb{Q}$에는 없던, $\mathbb{R}$을 $\mathbb{R}$답게 만드는 핵심 성질.)

위 성질을 실수의 공리라고도 많이 언급하는데, 이는 Hilbert의 1900년 논문 "Über den Zahlbegriff" [1]에서 실수를 공리로 특징지으려는 시도에서 비롯된 것으로 보인다. 정확하게는 이 논문에서 Hilbert가 쓴 completeness 공리(Vollständigkeitsaxiom)는 오늘날의 least upper bound 공리가 아니라 "이 공리들을 모두 만족하면서 이 수 체계를 더 확장할 수 없다"는 극대성(maximality) 형태의 공리였다. 실수의 성질들만으로 모든 정리를 연역하겠다는, 구현 독립적(implementation-independent)인 방법론적 태도를 강조한다는 의미에서 "공리"라는 표현이 어울린다.

위 정의가 well-defined인지 확인하려면 존재성과 유일성을 확인해야 한다. 하나씩 확인해보자.

## Complete Ordered Field의 존재성

> "Die ganzen Zahlen hat der liebe Gott gemacht, alles andere ist Menschenwerk." (신께서는 정수를 만드셨고, 나머지는 모두 인간이 만든 것이다.) — Leopold Kronecker

자연수만 있으면 그 위에 정수, 유리수, 그리고 실수까지도 인간의 손으로 쌓아올릴 수 있다. ZF 공리계 위에서 자연수, 정수, 유리수를 차례로 구성해보자.

**자연수 $\mathbb{N}$.** ZF에 따라 어떤 inductive set $I$가 존재한다. $$\mathcal{A} = \{A \subseteq I : A\text{ is inductive}\}$$라 하고 $\mathbb{N} = \bigcap \mathcal{A}$로 정의하면, $I$의 선택과 무관하게 well-defined이고 그 자신도 inductive함을 쉽게 보일 수 있다. $0=\emptyset$, $$1=\emptyset \cup \{\emptyset\}$$, ... 과 같은 식으로 개별 자연수도 정의된다. 나아가 $\mathbb{N}$은 다음과 같은 Induction Principle도 만족하는데, 이는 수학적 귀납법의 정당성을 확보해주는 자연수의 핵심 성질이다.

**Induction Principle.** If $S \subseteq \mathbb{N}$ satisfies $\emptyset \in S$ and $$\forall n\,(n\in S \to n\cup\{n\}\in S)$$, then $S = \mathbb{N}$.

**정수 $\mathbb{Z}$.** $\mathbb{N} \times \mathbb{N}$ 위에 동치관계 $(a,b) \sim (c,d) \iff a+d=b+c$를 주고, 그 quotient set으로 정의한다. $(a,b)$의 동치류는 직관적으로 $a-b$에 대응한다.

**유리수 $\mathbb{Q}$.** $$\mathbb{Z} \times (\mathbb{Z}\setminus\{0\})$$ 위에 동치관계 $(a,b)\sim(c,d) \iff ad=bc$를 주고 그 quotient set으로 정의한다. $(a,b)$의 동치류는 직관적으로 $a/b$에 대응한다.

자연수, 정수, 유리수에서 모두 사칙연산과 순서를 잘 정의할 수 있지만, 유리수까지는 $\sqrt{2}$와 같은 수를 담을 자리가 없다는 결정적인 빈틈이 있다. 이 빈틈에 대한 논의는 이미 고대 그리스 Pythagoras 학파로 거슬러 올라간다. Pythagoras 학파는 "만물은 수(정수와 그 비)"라는 세계관을 가지고 있었는데, 정사각형의 대각선과 변처럼 정수의 비로 나타낼 수 없는 양(incommensurable magnitude) — 오늘날 말로 무리수 — 이 존재한다는 사실이 발견되며 이 세계관 자체가 흔들렸다. 흔히 이 발견은 Hippasus of Metapontum이라는 인물의 이름과 함께, 그가 이 "금기"를 누설한 죄로 물에 빠뜨려 죽임당했다는 이야기로 전해진다.

다만 이 이야기의 출처를 따져보면 신중해질 필요가 있다. Hippasus를 구체적으로 지목하는 가장 이른 자료는 그의 활동 시기로부터 700년 넘게 지난 Iamblichus의 *De Vita Pythagorica* [2]이고, 그보다 이른 Pappus는 "누설한 자가 물에 빠져 죽었다"는 이야기만 전할 뿐 이름조차 밝히지 않는다. 즉 Hippasus가 실제로 이 발견을 했는지, 정말 처벌을 받았는지는 역사적으로 확인된 사실이라기보다 후대에 덧붙여진 전설에 가깝다. 심지어 최초로 발견된 incommensurable magnitude가 정사각형의 대각선($\sqrt{2}$)이었는지, 아니면 Pythagoras 학파가 상징으로 여겼던 정오각형(pentagram)의 대각선과 변의 비(황금비)였는지에 대해서도 역사학자들 사이에 이견이 있다 — von Fritz는 기하학적으로 더 자연스러운 후자 쪽 가설을 제시했다 [3].

전설의 사실 여부와 무관하게, 정수의 비로 나타낼 수 없는 양이 존재한다는 발견 자체는 실재했고, 이는 이후 수학사에서 무리수와 실수의 개념이 정식으로 다뤄지게 되는 중요한 계기가 되었다. 이 빈틈을 메우는 것이 실수의 구성이며, 대표적으로 두 가지 방법이 있다.

**Dedekind cut.** $\alpha \subset \mathbb{Q}$가 다음을 만족하면 cut이라 부른다.

1. $\alpha \neq \emptyset$ and $\alpha \neq \mathbb{Q}$.
2. If $p \in \alpha$ and $q < p$, then $q \in \alpha$.
3. $\alpha$ has no greatest element.

$\mathbb{R}$을 이런 cut들의 모임으로 정의하고, 순서는 $\alpha < \beta \iff \alpha \subsetneq \beta$로 준다. 덧셈은 $$\alpha+\beta = \{p+q : p\in\alpha,\ q\in\beta\}$$로 정의하고, 곱셈은 부호에 따라 경우를 나누어 정의한다. 유리수 $r$은 cut $$\{q \in \mathbb{Q} : q < r\}$$과 동일시되어 $\mathbb{Q} \subset \mathbb{R}$인 embedding을 얻는다. 이 방법은 Dedekind가 1872년에 처음 제시했다 [4].

**Cauchy sequence.** 유리수로 이루어진 수열 $(a_n)$ 중, for every $\varepsilon \in \mathbb{Q}_{>0}$ there exists $N$ such that $m,n>N \implies \vert a_m-a_n\vert<\varepsilon$을 만족하는 것들(Cauchy sequence)을 모은다. 두 Cauchy sequence $(a_n),(b_n)$을 $a_n-b_n \to 0$일 때 동치로 보는 동치관계로 quotient를 취해 $\mathbb{R}$을 정의하고, 사칙연산은 성분별로 정의한다. 이 방법은 Cantor가 1872년 논문에서 제시했다 [5].

이 두 구성 모두 complete ordered field의 세 조건을 만족함을 보일 수 있다 — 즉 존재성이 증명된 것이다.

## Complete Ordered Field의 유일성

이 세 가지 성질을 만족하는 두 구조가 항상 동형임을 실제로 증명한 것은 Huntington의 1903년 논문 [6]이다.

**Theorem (Uniqueness, Huntington 1903 [6], Theorem II/II′).** Any two complete ordered fields are isomorphic as ordered fields.

이 논문은 공리 집합을 두 벌 제시하는데, 앞의 10개(postulates 1–10)는 순서와 덧셈만으로 이루어진, 위로 유계인 증가수열은 항상 극한을 갖는다는 형태의 completeness를 가진 순서군을 정의하고, 뒤의 14개(postulates 1–14)는 곱셈을 더해 오늘날의 complete ordered field에 해당하는 공리계를 이룬다. 그리고 각 공리계에 대해 (1) Dedekind cut·Cantor의 Cauchy sequence·기하학적 직선 등을 모델로 삼아 무모순성(Theorem I/I′)을, (2) 이를 만족하는 두 대상은 항상 "equivalent"(순서와 연산을 보존하는 전단사, 즉 오늘날 말로 isomorphic)함(Theorem II/II′)을, (3) Padoa의 방법으로 각 공리가 나머지로부터 독립임(Theorem III/III′)을 각각 증명한다. 이 중 (2)가 바로 오늘날 categoricity라 부르는 것에 해당한다.

즉 Dedekind cut으로 만들든 Cauchy sequence로 만들든 결과는 isomorphism을 기준으로 유일하고, 그 공통된 동형류를 $\mathbb{R}$이라 부른다. 실수를 complete ordered field로 정의하고 존재성과 유일성을 증명하는 현대적인 서술은 예를 들어 Rudin의 교재 [7]에서도 찾아볼 수 있다.

## 실수의 정의에서 Completeness 대신 Cauchy Completeness를 쓰면?

실수의 공리 3번을 "모든 Cauchy sequence는 수렴한다(Cauchy completeness)"로 바꿔도 같은 결과를 얻을까? 답은 아니다 — 그것만으로는 부족하다.

먼저 completeness(Least Upper Bound Property)로부터 다음이 따라 나온다는 점을 짚어야 한다.

**Archimedean Property.** For every $x \in \mathbb{R}$, there exists $n \in \mathbb{N}$ such that $x < n$.

증명은 간단하다. 만약 $\mathbb{N}$이 위로 유계라면 completeness에 의해 $s=\sup \mathbb{N}$이 존재하는데, $s-1$은 상계가 아니므로 어떤 $n\in\mathbb{N}$에 대해 $n>s-1$이고, 그러면 $n+1\in\mathbb{N}$이면서 $n+1>s$가 되어 $s$가 상계라는 가정에 모순된다.

문제는 이 함의가 Cauchy completeness에 대해서는 성립하지 않는다는 것이다. 즉 Archimedean이 아니면서도 (그 field 자신의 순서로 정의한 $\varepsilon$ 기준으로는) Cauchy complete인 ordered field가 존재한다.

**반례: 실수 계수 formal Laurent series field $\mathbb{R}((t))$.** 계수가 실수이고 $t$의 지수가 유한히 많은 음수 항과 무한히 많은 양수 항으로 이루어진 급수들의 field를, 0이 아닌 최저차항 계수의 부호로 사전식(lexicographic) 순서를 주면 ordered field가 된다. 이 field에서 $t$는 모든 $n\in\mathbb{N}$에 대해 $nt<1$을 만족하는 양의 무한소(infinitesimal)이므로 Archimedean property가 깨진다. 그런데 이 field는 자기 자신의 $t$-adic한 순서 구조에 대해 Cauchy complete하다 — 급수의 차수가 계속 커지는 Cauchy sequence는 항상 그 field 안의 극한 급수로 수렴한다. 즉 field + order + Cauchy completeness라는 공리계는 $\mathbb{R}$뿐 아니라 이 $\mathbb{R}((t))$도 만족시키므로, 이 공리계만으로는 실수를 유일하게 특징짓지 못한다.

이 둘 사이의 정확한 관계는 다음과 같이 알려져 있다.

**Theorem.** An ordered field is Dedekind complete if and only if it is Archimedean and Cauchy complete.

따라서 completeness 공리를 굳이 Cauchy completeness로 바꾸고 싶다면, Archimedean property를 별도의 공리로 추가하면 된다. 즉 "field + order + completeness" 세 공리 대신 "field + order + Archimedean + Cauchy completeness" 네 공리를 쓰면 다시 $\mathbb{R}$을 유일하게 특징지을 수 있다.

그런데 앞서 Cauchy sequence로 $\mathbb{R}$을 구성했을 때는 왜 이 문제가 생기지 않았을까? 그 construction은 임의의 non-Archimedean field가 아니라, 이미 Archimedean인 $\mathbb{Q}$를 completion한 것이었기 때문이다. Archimedean인 ordered field를 Cauchy sequence로 completion하면 Archimedean property가 그대로 보존된다 — 모든 Cauchy sequence는 유계이고, $\mathbb{Q}$ 안에서 유계라는 것 자체가 이미 어떤 자연수로도 유계라는 뜻이기 때문이다. 그러므로 $\mathbb{Q}$를 completion해서 얻은 $\mathbb{R}$은 Archimedean이면서 동시에 Cauchy complete이고, 앞의 정리에 의해 이는 Dedekind complete과 같은 말이 된다. 반면 반례로 든 $\mathbb{R}((t))$가 문제가 되는 것은, 애초에 완비화하기 전의 순서 자체가 non-Archimedean이었기 때문이다.

참고로 "field + order" 두 공리만으로 $\mathbb{Q}$가 유일하게 정해지는 것은 아니다 — $\mathbb{R}$이나 $\mathbb{R}((t))$처럼 다른 ordered field들도 이 두 공리는 만족한다. 다만 앞서 존재성 파트에서 실수를 구성할 때는 아무 ordered field나 골랐던 게 아니라 ZF 위에서 직접 만든 구체적인 $\mathbb{Q}$를 사용하고, 이 $\mathbb{Q}$가 Archimedean이라는 것은 정수가 $\mathbb{Q}$ 안에서 cofinal하다는(임의의 유리수보다 큰 정수가 항상 존재한다는) 사실에서 곧바로 나온다. 따라서 그 위에서 Cauchy sequence로 completion해도 충분했던 것이다.

## 참고문헌

1. Hilbert, D. (1900). Über den Zahlbegriff. *Jahresbericht der Deutschen Mathematiker-Vereinigung*, 8, 180–183.
2. Iamblichus. *De Vita Pythagorica* [On the Pythagorean Life] (c. 4th century CE).
3. von Fritz, K. (1945). The Discovery of Incommensurability by Hippasus of Metapontum. *Annals of Mathematics*, 46(2), 242–264.
4. Dedekind, R. (1872). *Stetigkeit und irrationale Zahlen*. Friedrich Vieweg und Sohn.
5. Cantor, G. (1872). Über die Ausdehnung eines Satzes aus der Theorie der trigonometrischen Reihen. *Mathematische Annalen*, 5(1), 123–132.
6. Huntington, E. V. (1903). Complete Sets of Postulates for the Theory of Real Quantities. *Transactions of the American Mathematical Society*, 4(3), 358–370.
7. Rudin, W. (1976). *Principles of Mathematical Analysis* (3rd ed.). McGraw-Hill.

---
