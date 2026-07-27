---
layout: post
title: "선택 공리 (Axiom of Choice)"
date: 2026-07-22
---

## Zermelo–Fraenkel (ZF) 공리계

현대 집합론의 표준 토대인 ZF 공리계는 다음 8개로 이루어진다.

1. **Extensionality.** Two sets are equal if they have the same elements.
   $$\forall x \forall y\, [\forall z\,(z \in x \leftrightarrow z \in y) \to x = y]$$
   (집합의 같음을 정의.)

2. **Regularity (Foundation).** Every non-empty set has an element disjoint from itself.
   $$\forall x\, [x \neq \emptyset \to \exists y \in x\,(y \cap x = \emptyset)]$$
   (자기 자신을 원소로 갖는 집합은 없다.)

3. **Specification (Separation).** For every formula $\varphi$, there is a subset of $x$ consisting exactly of the elements satisfying $\varphi$.
   $$\forall x\, \exists y\, \forall z\,[z \in y \leftrightarrow (z \in x \wedge \varphi(z))]$$
   (조건을 만족하는 원소들만 모아 부분집합을 만들 수 있다. 교집합도 이렇게 만들 수 있다.)

4. **Pairing.** For any $a, b$, the set $$\{a, b\}$$ exists.
   (두 집합을 원소로 하는 집합을 만들 수 있다. Pair를 정의할 수 있다.)

5. **Union.** For any family of sets $F$, the union $\bigcup F$ exists.
   (합집합이 가능하다.)

6. **Replacement.** The image of a set under a definable function is itself a set.
   (함수의 image도 집합이 된다.)

7. **Infinity.** There exists an inductive set (a set from which the natural numbers can be built).
   $$\exists x\,[\emptyset \in x \wedge \forall y \in x\,(y \cup \{y\} \in x)]$$
   (자연수 집합의 존재성. 무한 집합의 존재성. 적어도 하나의 집합이 존재함.)

8. **Power Set.** For every set $x$, the set of all subsets of $x$, $\mathcal{P}(x)$, exists.
   (멱집합의 존재성.)

## 선택 공리 (Axiom of Choice)

$$\{A_i\}_{i \in I}$$가 공집합이 아닌 집합들로 이루어진 family of sets라고 하자. Axiom of Choice(AC)는 다음과 같다.

$$
\exists\, f : I \to \bigcup_{i \in I} A_i \quad \text{such that} \quad f(i) \in A_i \ \text{ for all } i \in I.
$$

즉, 각 $A_i$에서 원소를 하나씩 "동시에" 골라내는 choice function $f$가 존재한다는 것이다.

AC가 ZF 공리계에서 정말 필요한 추가 공리인지, 아니면 ZF에서 증명되거나 반증되는지는 20세기 집합론의 핵심 질문이었다.

먼저 Gödel에 의해 AC가 ZF로부터 반증될 수 없음이 증명되었다 [1, 2]. [1]에서 결과만 공표하고 [2]에서 증명했다. 사실 [1, 2]에서 증명한 것은 ZF가 아니라 von Neumann의 공리체계 S*(오늘날 NBG의 전신이 되는, 집합 대신 class를 다루는 체계)에서 AC가 반증될 수 없음이 증명된 것이었는데 결국 아이디어는 비슷하다.

Cohen에 의해 AC가 ZF로부터 증명될 수 없음도 증명되었다 [3, 4]. forcing이라는 기법이 이 두 논문에서 처음 도입되었고, [3]에서 기법과 핵심 아이디어를 제시하고 [4]에서 이를 이어받아 완성했다. 사실 [3, 4]에서 직접 다룬 것은 AC 자체라기보다 연속체 가설(Continuum Hypothesis)의 독립성이었는데, 같은 forcing 기법으로 실수들의 쌍으로 이루어진 countable family of sets가 choice function을 갖지 않는 ZF의 모델(이른바 *basic Cohen model*)이 구성되면서 AC의 독립성도 함께 정리되었다.

두 결과를 합치면 AC는 ZF와 독립인 9번째 공리이다. ZF에 AC까지 묶은 것을 ZFC 공리체계라고 한다.

## 선택 공리를 채택할 것인가?

AC는 (ZF 위에서) 다음과 동치임이 알려져 있다.

**Zorn's Lemma.** Every partially ordered set in which every chain has an upper bound contains a maximal element.

**Well-Ordering Theorem (Zermelo).** Every set can be well-ordered.

보통 Zorn's Lemma가 여러 수학 분야에서 증명에 쓰이곤 하는데, 이를 증명에 사용한다면 ZFC 공리계를 가정하고 있다는 뜻이다.

이 세 명제는 서로 완전히 동치이지만 수학자들이 이들에 대해 느끼는 직관은 사뭇 다르다.

> "The Axiom of Choice is obviously true, the well-ordering principle obviously false, and who can tell about Zorn's Lemma?" — Jerry Bona

심지어 AC를 받아들이면 다음과 같은 반직관적인 결과도 따라온다.

**Banach–Tarski Paradox.** A solid ball in $\mathbb{R}^3$ can be decomposed into finitely many pieces, which can then be reassembled using only rotations and translations into two balls identical to the original.

이것이 가능한 이유는 AC를 이용해 만든 조각들이 non-measurable 집합이기 때문이다 (Lebesgue measure가 정의되지 않는 집합). 즉 "부피가 보존된다"는 직관 자체가 애초에 적용되지 않는 대상들이다. 이에 대해 시각적으로 잘 설명한 영상으로 [이 유튜브 영상](https://www.youtube.com/watch?v=5RdsN4XeOyU&t=1560s)이 있다.

이런 반직관적인 결과 때문에 AC를 채택하지 않는 수학자들도 일부 있지만, ZFC 위에서 얻어지는 유용한 결과가 워낙 많기 때문에 대다수는 AC를 받아들이는 쪽을 택한다. 물론 AC를 채택할지는 정해진 답이 있는 문제라기보다 자유의 영역에 가깝다.

> "The essence of mathematics lies in its freedom." — Georg Cantor

## Euclid의 평행선 공준

이와 같은 공리의 독립성 논의는 이미 수학사에 등장한 사례가 있다.

Euclid는 *Elements*에서 공리(axiom)와 공준(postulate)을 구분해서 썼다. 공리는 기하학뿐 아니라 어떤 논증에도 통하는 일반적인 자명한 원칙("같은 것과 같은 것은 서로 같다" 같은 것)이었고, 공준은 기하학이라는 분야에 국한된 구성적 가정이었다. (오늘날에는 이 구분이 사실상 사라져서 ZF의 여덟 개나 AC도 전부 axiom이라고 부른다. "Euclid's postulates"라는 이름만 역사적 관용으로 남아있다.)

Euclid 기하학은 다음 다섯 개의 공준으로 이루어진다.

1. To draw a straight line from any point to any point.
2. To produce a finite straight line continuously in a straight line.
3. To describe a circle with any centre and distance.
4. That all right angles are equal to one another.
5. **Parallel Postulate.** For any line and a point not on it, there is exactly one line through the point parallel to the given line.

앞의 네 개에 비해 다섯 번째가 훨씬 복잡하고 부자연스러워 보였다. 2000년 넘게 수학자들은 다섯 번째 공준을 나머지 네 공준으로부터 증명하려 시도했지만 모두 실패했다.

19세기에 Bolyai [5]와 Lobachevsky [6]가 각각 독립적으로, 평행선 공준을 부정해도 (나머지 네 공준을 만족하는) 무모순적인 기하학 — hyperbolic geometry — 이 존재함을 발표했다. Gauss도 이와 동등한 결과를 사적으로 얻어 두었던 것으로 알려져 있는데, 그는 논란을 우려해 이를 평생 출판하지 않았고, 이 사실은 사후에 공개된 편지와 노트를 통해서만 확인된다 [7]. 이후 Beltrami가 pseudosphere를 이용해 hyperbolic geometry의 (평면 전체가 아닌 일부만을 담아내는) 국소적인 모델을 처음 구성했고 [8], 이어서 Klein이 projective disk model을 [9], Poincaré가 (Fuchsian group에 대한 연구 과정에서) disk model을 각각 제시하며 hyperbolic plane 전체를 담아내는 모델을 완성해 그 무모순성을 확정지었다 [10]. 즉 평행선 공준은 나머지 네 공준으로부터 독립적이다. 평행선 공준 없이 나머지 4개로 전개한 기하학을 비유클리드 기하학이라고 한다.

## 참고문헌

1. Gödel, K. (1938). *The Consistency of the Axiom of Choice and of the Generalized Continuum-Hypothesis*. Proceedings of the National Academy of Sciences, 24(12), 556–557.
2. Gödel, K. (1940). *The Consistency of the Continuum Hypothesis*. Annals of Mathematics Studies, No. 3. Princeton University Press.
3. Cohen, P. J. (1963). *The Independence of the Continuum Hypothesis*. Proceedings of the National Academy of Sciences, 50(6), 1143–1148.
4. Cohen, P. J. (1964). *The Independence of the Continuum Hypothesis, II*. Proceedings of the National Academy of Sciences, 51(1), 105–110.
5. Bolyai, J. (1832). *Appendix Scientiam Spatii Absolute Veram Exhibens*. In F. Bolyai, *Tentamen Juventutem Studiosam in Elementa Matheseos Purae Introducendi*. Maros Vásárhely.
6. Lobachevsky, N. I. (1829–1830). О началах геометрии [On the Foundations of Geometry]. *Kazanskii Vestnik* (Kazan Messenger).
7. O'Connor, J. J., & Robertson, E. F. *Carl Friedrich Gauss*. MacTutor History of Mathematics Archive. https://mathshistory.st-andrews.ac.uk/Biographies/Gauss/
8. Beltrami, E. (1868). Saggio di interpretazione della geometria non-euclidea. *Giornale di Matematiche*, 6, 284–312.
9. Klein, F. (1871). Über die sogenannte nicht-euklidische Geometrie. *Mathematische Annalen*, 4, 573–625.
10. Poincaré, H. (1882). Théorie des groupes fuchsiens. *Acta Mathematica*, 1, 1–63.

---
