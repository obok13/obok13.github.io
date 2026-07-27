---
layout: post
title: "무한집합의 크기: Cardinality"
date: 2026-07-24
---

## Cardinality

Cantor는 무한집합 사이의 크기를 비교하는 방법으로 두 집합 사이에 bijection이 존재하는지를 기준으로 삼는 것을 제안했다.

**Definition (Cardinality).** Two sets $A$ and $B$ have the same cardinality, written $\vert A\vert=\vert B\vert$, if there exists a bijection $f: A \to B$. If there exists an injection $f: A \to B$, we write $\vert A\vert \le \vert B\vert$.

유한집합에서 원소 개수의 정의를 무한집합으로 확장한 것이라고 볼 수 있다. Cardinality는 다음과 같은 성질을 만족한다.

**Theorem (Cantor–Schröder–Bernstein).** If $\vert A\vert\le\vert B\vert$ and $\vert B\vert\le\vert A\vert$, then $\vert A\vert=\vert B\vert$.

즉 양방향으로 injection이 존재하면 bijection도 존재한다. 증명이 쉬워 보이지만 막상 엄밀하게 하려면 꽤 까다롭다. 실제로 엄밀한 증명을 얻기까지의 과정은 복잡했다. Cantor는 1895년 논문에서 이 명제를 증명 없이 언급했는데 [1], 그의 논증은 임의의 두 cardinality가 항상 비교 가능하다는 trichotomy($\vert A\vert<\vert B\vert$, $\vert A\vert=\vert B\vert$, $\vert A\vert>\vert B\vert$ 중 하나가 성립)에 의존하고 있었다. 그런데 이 trichotomy 자체가 실질적으로 선택 공리와 동치라는 사실이 훗날 Hartogs에 의해 밝혀졌다 [2] — 즉 Cantor의 논증은 사실상 AC를 암묵적으로 쓰고 있었던 셈이다. Dedekind는 1887년 (well-ordering에 기대지 않는) 독자적인 증명을 chain theory로 얻었지만 발표하지 않았고, 이는 그의 사후 전집에 실리고 나서야 알려지게 되었다 [3, 4]. Schröder는 1896–97년에 증명을 발표했지만 1902년 Korselt가 그 증명의 결함을 발견했고 (논문은 1911년) [5], 결국 최초로 인정받는 완전한 증명은 1897년 Cantor의 세미나에서 당시 19세였던 학생 Felix Bernstein이 낸 것이었다 — Cantor가 이를 Borel에게 전달해 Borel의 1898년 저서에 처음 소개되었다 [6, 7]. 오늘날 정리 이름에 Cantor, Schröder, Bernstein이 함께 붙어 있는 것은 이런 사정 때문이다.

## 가산 집합 (Countable Set)

**Definition.** A set $A$ is *countable* if it is finite or there exists a bijection $f:\mathbb{N}\to A$. In the latter case we say $A$ is *countably infinite*, and write $\vert A\vert=\aleph_0$ (aleph-null).

**$\mathbb{Z}$는 가산이다.** $f:\mathbb{N}\to\mathbb{Z}$를

$$
f(n) = \begin{cases} n/2 & n \text{이 짝수일 때} \\ -(n+1)/2 & n \text{이 홀수일 때} \end{cases}
$$

로 정의하면, $0,-1,1,-2,2,-3,3,\dots$ 순서로 정수 전체를 나열하는 bijection이 된다.

**$\mathbb{N}\times\mathbb{N}$은 가산이다.** $(1,1),(1,2),(2,1),(1,3),(2,2),(3,1),\dots$처럼 $p+q$가 작은 순서대로(같으면 그 안에서 정해진 순서로) 대각선을 따라 나열하면 $\mathbb{N}\times\mathbb{N}$의 모든 원소를 빠짐없이, 중복 없이 나열할 수 있다.

**$\mathbb{Q}$는 가산이다.** 모든 유리수는 기약분수 $p/q$ ($p\in\mathbb{Z}$, $q\in\mathbb{N}$)로 유일하게 나타난다. 이 대응은 $\mathbb{Q}$에서 $\mathbb{Z}\times\mathbb{N}$으로의 injection을 주고, $\mathbb{Z}\times\mathbb{N}$은 ($\mathbb{Z}$와 $\mathbb{N}$이 각각 가산이므로 위와 같은 대각선 나열로) 가산이다. 반대로 $\mathbb{N}\subset\mathbb{Q}$인 자연스러운 injection도 있으므로, Cantor–Schröder–Bernstein에 의해 $\vert\mathbb{Q}\vert=\vert\mathbb{N}\vert=\aleph_0$.

## 비가산 집합 (Uncountable Set)의 존재성

그렇다면 모든 무한집합은 $\mathbb{N}$과 같은 cardinality를 가질까? 그렇지 않다는 것을 Cantor가 처음 증명했다.

**Theorem (Cantor, 1874 [8]).** $\mathbb{R}$ is uncountable.

*Proof.* 임의의 수열 $(x_n)_{n\in\mathbb{N}} \subset \mathbb{R}$이 주어졌다고 하자. 닫힌 구간 $[a_0,b_0]$에서 시작해서, $x_1, x_2$를 피하는 부분구간 $[a_1,b_1]\subset[a_0,b_0]$를 고르고, 그 안에서 다시 $x_3,x_4$를 피하는 $[a_2,b_2]$를 고르는 식으로 구간을 계속 좁혀 나간다. 이렇게 얻은 nested closed interval $[a_0,b_0]\supset[a_1,b_1]\supset\cdots$는 completeness에 의해 공통으로 포함하는 점을 적어도 하나 갖는데, 그 점은 구성 방법상 어떤 $x_n$과도 같을 수 없다. 즉 임의의 수열은 $\mathbb{R}$의 모든 점을 나열하지 못하므로 $\mathbb{R}$은 가산이 아니다.

오늘날 이 정리는 흔히 대각선 논법으로 증명되는데, 이는 17년 뒤인 1891년에 가서야 등장하며, 그것도 애초 목적은 실수의 비가산성 자체보다 더 일반적인 정리를 증명하는 데 있었다.

## Cantor의 대각선 논법

Cantor의 대각선 논법은 다음과 같다 [9]. $$\{0,1\}^{\mathbb{N}}$$ (자연수에서 $$\{0,1\}$$로 가는 함수 전체의 집합)이 비가산임을 보이자. 임의의 함수열 $$f_1,f_2,f_3,\dots \in \{0,1\}^{\mathbb{N}}$$이 주어졌다고 하자. $g(n) = 1-f_n(n)$으로 새 함수 $$g\in\{0,1\}^{\mathbb{N}}$$을 정의하면, $g$는 모든 $n$에 대해 $g(n)\neq f_n(n)$이므로 $g\neq f_n$이다. 즉 어떤 수열도 $$\{0,1\}^{\mathbb{N}}$$ 전체를 나열할 수 없으므로 $$\{0,1\}^{\mathbb{N}}$$은 비가산이다. $$\{0,1\}^{\mathbb{N}}$$은 $\mathcal{P}(\mathbb{N})$과 자연스럽게 대응되며, 실수의 이진 전개를 생각하면 $(0,1)$ 구간의 실수와도 자연스럽게 대응된다. 따라서 $\vert\mathbb{R}\vert=\vert\mathcal{P}(\mathbb{N})\vert=:2^{\aleph_0}$임을 알 수 있다.

Cantor의 대각선 논법을 확장한 것이 Cantor's Theorem이다.

**Theorem (Cantor's Theorem, 1891 [9]).** For every set $A$, there is no surjection from $A$ onto $\mathcal{P}(A)$; equivalently, $\vert A\vert < \vert\mathcal{P}(A)\vert$.

*Proof.* $f:A\to\mathcal{P}(A)$가 임의의 함수라 하자. $$D=\{a\in A : a\notin f(a)\}$$로 정의하면 $D\in\mathcal{P}(A)$이다. 만약 어떤 $a_0\in A$에 대해 $D=f(a_0)$라면, $a_0\in D \iff a_0\notin f(a_0)=D$가 되어 모순이다. 즉 $D$는 $f$의 치역에 속하지 않으므로 $f$는 surjection이 아니다. $\blacksquare$

또 하나의 흥미로운 결론은 **가장 큰 cardinality를 가진 집합은 존재하지 않는다는 것이다.** $\mathbb{N}, \mathcal{P}(\mathbb{N}), \mathcal{P}(\mathcal{P}(\mathbb{N})),\dots$는 cardinality가 끝없이 커지는 사슬을 이루므로, 무한에도 서로 다른 "크기"가 무한히 많이 존재한다.

## 연속체 가설 (Continuum Hypothesis)

연속체 가설은 "자연수와 실수 사이에 중간 크기의 cardinality가 있을까?"라는 물음이다.

**Continuum Hypothesis (CH).** There is no set $S$ with $\aleph_0 < \vert S\vert < 2^{\aleph_0}$.

Cantor는 1878년 논문에서 "$\mathbb{R}$의 모든 무한 부분집합은 가산이거나 $\mathbb{R}$과 같은 cardinality를 가진다"는 형태로 이미 이 추측의 약한 버전(weak CH)을 제시했다 [10] — 이것이 오늘날 우리가 아는 일반적인 형태(어떤 무한 부분집합이든 상관없이 $\aleph_0$과 $2^{\aleph_0}$ 사이에 다른 cardinality가 없다는 명제)와 구별된다는 점은 집합론사학자 Gregory Moore의 연구에 기반한다 [11]. 오늘날의 형태로 다듬어진 것은 1882년 Mittag-Leffler에게 보낸 편지에서라고 알려져 있다 [12]. Hilbert는 1900년 국제수학자대회 연설에서 이를 첫 번째 문제로 꼽으며 "Cantors Problem von der Mächtigkeit des Continuums"라 불렀다 [13].

CH가 참인지 거짓인지는 20세기 집합론의 오랜 난제였다. 그 답은, CH가 ZF로부터 독립일 뿐 아니라 ZFC로부터도 독립이라는 것이다. Gödel은 [14, 15]에서 constructible universe $L$을 구성하는 방법으로 ZF 위에서 AC와 CH가 모두 성립하는 모델을 구성했다 (정확히는 ZF가 아니라 von Neumann의 공리체계 S*, 오늘날 NBG의 전신이 되는 체계 위에서 구성한 것이었지만, ZF 위에서 구성해도 핵심 아이디어는 같다). Cohen은 forcing 기법으로 ZFC 위에서 CH가 성립하지 않는 모델을 구성했다 [16, 17]. 두 결과를 합치면 ZFC와 CH는 독립이고, 더 적은 공리로는 결정할 수 없으니 그보다 약한 ZF에서도 당연히 독립이다.

그렇다면 ZF+CH와 AC는 독립일까? 이것 역시 독립이다. 한쪽 방향은 이미 확인했다 — Gödel의 모델은 ZF 위에서 CH와 AC가 모두 성립하는 모델이었다. 반대로 ZF+CH이면서 AC는 성립하지 않는 모델도 존재하는데, Keremedis, Tachtsis, Wajch가 2021년 논문에서 실제로 이런 모델을 구성했다 [18]. 즉 ZF 위에서 AC와 CH는 서로에 대해서도 독립이다.

## 참고문헌

1. Cantor, G. (1895). Beiträge zur Begründung der transfiniten Mengenlehre. *Mathematische Annalen*, 46, 481–512.
2. Hartogs, F. (1915). Über das Problem der Wohlordnung. *Mathematische Annalen*, 76, 438–443.
3. Dedekind, R. (1932). Ähnliche (deutliche) Abbildung und ähnliche Systeme. In *Gesammelte mathematische Werke*, Vol. 3 (R. Fricke, E. Noether, & Ø. Ore, Eds., pp. 447–449). Vieweg.
4. Sieg, W. (2019). The Cantor–Bernstein theorem: how many proofs? *Philosophical Transactions of the Royal Society A*, 377, 20180031.
5. Korselt, A. (1911). Über einen Beweis des Äquivalenzsatzes. *Mathematische Annalen*, 70, 294–296.
6. Borel, É. (1898). *Leçons sur la théorie des fonctions*. Gauthier-Villars.
7. O'Connor, J. J., & Robertson, E. F. *Felix Bernstein*. MacTutor History of Mathematics Archive.
8. Cantor, G. (1874). Über eine Eigenschaft des Inbegriffes aller reellen algebraischen Zahlen. *Journal für die reine und angewandte Mathematik*, 77, 258–262.
9. Cantor, G. (1891). Über eine elementare Frage der Mannigfaltigkeitslehre. *Jahresbericht der Deutschen Mathematiker-Vereinigung*, 1, 75–78.
10. Cantor, G. (1878). Ein Beitrag zur Mannigfaltigkeitslehre. *Journal für die reine und angewandte Mathematik*, 84, 242–258.
11. Moore, G. H. (1990). Introductory note. In S. Feferman et al. (Eds.), *Kurt Gödel: Collected Works, Vol. II* (pp. 154–175). Oxford University Press.
12. Moore, G. H. (1989). Towards a History of Cantor's Continuum Problem. In D. E. Rowe & J. McCleary (Eds.), *The History of Modern Mathematics*, Vol. 1 (pp. 79–122). Academic Press.
13. Hilbert, D. (1900). Mathematische Probleme. *Nachrichten von der Königl. Gesellschaft der Wissenschaften zu Göttingen*, 253–297.
14. Gödel, K. (1938). The Consistency of the Axiom of Choice and of the Generalized Continuum-Hypothesis. *Proceedings of the National Academy of Sciences*, 24(12), 556–557.
15. Gödel, K. (1940). *The Consistency of the Continuum Hypothesis*. Annals of Mathematics Studies, No. 3. Princeton University Press.
16. Cohen, P. J. (1963). The Independence of the Continuum Hypothesis. *Proceedings of the National Academy of Sciences*, 50(6), 1143–1148.
17. Cohen, P. J. (1964). The Independence of the Continuum Hypothesis, II. *Proceedings of the National Academy of Sciences*, 51(1), 105–110.
18. Keremedis, K., Tachtsis, E., & Wajch, E. (2021). Several results on compact metrizable spaces in ZF. *Monatshefte für Mathematik*. https://doi.org/10.1007/s00605-021-01582-0

---
