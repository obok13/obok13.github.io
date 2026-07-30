---
layout: post
title: "괴델의 불완전성 정리 (Gödel's Incompleteness Theorems)"
date: 2026-07-25
---

## 무모순적이고 완전한 형식체계

형식체계(formal system) $F$가 자연수에 관한 명제들을 다룬다고 하자. $F$가 *consistent*(무모순)하다는 것은 어떤 명제 $\varphi$와 그 부정 $\lnot\varphi$가 $F$ 안에서 동시에 증명되는 일이 없다는 뜻이고, $F$가 *complete*(완전)하다는 것은 모든 (닫힌) 명제 $\varphi$에 대해 $\varphi$ 또는 $\lnot\varphi$ 둘 중 하나는 반드시 $F$ 안에서 증명된다는 뜻이다. 여기서 닫힌 명제는 free variable이 없는 논리식을 말한다. 즉, 모든 변수가 $\forall$이나 $\exists$ 같은 quantifier에 묶여 있어서, 그 자체로 참/거짓이 딱 정해지는 문장이다. Consistency는 굳이 대상을 닫힌 명제로 제한할 필요는 없다.

무모순적이고 완전한 형식체계가 존재할까? Hilbert는 1930년 9월 8일 Königsberg에서 열린 은퇴 연설 "Naturerkennen und Logik"에서 다음과 같은 말을 남겼다 [1].

> "Wir müssen wissen, wir werden wissen." ("우리는 알아야 한다, 우리는 알게 될 것이다.")

이는 완전하고 무모순적인 형식 체계에 대한 Hilbert의 열망을 나타낸다. 그러나 아이러니하게도 이것이 불가능함을 바로 전날인 9월 7일, 같은 도시에서 열린 별개의 학회에서 Gödel이 발표해버리고 말았다.

## True Arithmetic

사실 엄밀히 말하면 무모순적이고 완전한 형식 체계를 구성할 수 있다. 첫번째 예시는 자연수에 관해 참인 모든 명제의 집합(true arithmetic이라 부른다)을 그대로 공리로 삼는 형식 체계이다. 이 "체계"는 완전하다 — 정의상 어떤 명제 $\varphi$에 대해서든 $\varphi$가 참이거나 $\lnot\varphi$가 참이어서 무모순적이고, 모든 참인 명제가 이미 공리로 들어 있어 증명이 자명하기 때문에 완전하다.

하지만 이 체계는 *recursive*(주어진 명제가 공리인지 아닌지 유한 시간 안에 항상 답을 내놓는 알고리즘이 존재)하지 않다는 단점이 있다. 특정 공리에서 출발하는 일반적인 체계에서는 주어진 명제가 공리인지 아닌지 판별하는 것은 그냥 이미 정해진 공리와 해당 명제를 대조해보면 되므로 항상 recursive하다. True arithmetic에서는 "참인 명제 전부"를 공리로 삼기로 정의했으므로, "이 명제가 공리인가"라는 질문과 "이 명제가 참인가"라는 질문이 정의상 완전히 같은 질문이 되어버린다. 따라서 이 공리 집합이 recursive한지를 묻는 것은, 임의의 산술 명제의 참/거짓을 가려주는 알고리즘이 존재하는지를 묻는 것과 정확히 같은 질문이다. 하지만 그런 알고리즘은 존재하지 않는다.

자연수에 관한 명제 중에는 "이 컴퓨터 프로그램 $P$는 언젠가 멈춘다"는 명제도 숨어 있다 — 예를 들어 $P$가 "4보다 큰 짝수를 4, 6, 8, ... 순서로 검사하다가, 두 소수의 합으로 쓸 수 없는 첫 반례를 찾으면 멈춘다"는 프로그램이라면, $P$가 멈추는지 여부는 정확히 골드바흐 추측이 거짓인지와 같은 질문이 된다. 만약 임의의 산술 명제의 참/거짓을 가려주는 만능 알고리즘이 있다면, 그 알고리즘에 이 명제를 넣어보는 것만으로 "$P$가 멈추는가?"까지 전부 판별할 수 있게 된다.

그런데 바로 이 문제(오늘날 흔히 정지 문제, Halting Problem이라 부른다)를 항상 옳게 풀어주는 알고리즘은 존재할 수 없다는 것이 Turing에 의해 밝혀졌다 [2]. 사실 Turing의 원 논문은 오늘날 교과서에서 쓰이는 "정지하는가"라는 표현 대신 machine이 "circular"한지 "circle-free"한지를 다루는, 조금 다른 형태의 diagonal argument로 서술되어 있지만, 증명의 핵심 아이디어는 같다. 핵심 논증은 사실 Russell's Paradox와 똑같은 자기지시 트릭이다.

만능 정지-판별 알고리즘 $H$가 있다고 해보자. 이제 다음과 같은 새 프로그램 $D$를 만든다: "입력으로 받은 프로그램 $X$에 대해 $H$에게 물어봐서, $H$가 '멈춘다'고 답하면 $D$는 일부러 영원히 멈추지 않고, $H$가 '안 멈춘다'고 답하면 $D$는 즉시 멈춘다." 그리고 $D$ 자신을 $D$에게 입력으로 줘보자. $D$가 (자기 자신에 대해) 멈춘다면, 그건 $H$가 "$D$는 안 멈춘다"고 답했다는 뜻인데 — 방금 $D$가 멈췄으니 $H$가 틀렸다. $D$가 안 멈춘다면, 그건 $H$가 "멈춘다"고 답해서 $D$가 일부러 안 멈추기로 한 것인데 — 이번에도 $H$가 틀렸다. 어느 쪽이든 모순이므로, 애초에 그런 $H$는 존재할 수 없다.

True arithmetic은 형태만 형식체계일 뿐, 실제로 증명이라는 절차를 수행할 수 있는 대상이 못 된다 — 정리를 "증명"하려면 먼저 무엇이 공리인지를 기계적으로 확인할 수 있어야 하는데, 그것이 안 되기 때문이다.

## Presburger Arithmetic

두번째 예시는 Presburger arithmetic이다. 이는 자연수에 덧셈만 있고 곱셈은 없는 체계 위에서 몇 가지 공리들로 구성된다. Presburger가 1929년에 이 체계가 consistent하고 recursive한 공리 집합을 가지며 complete하다는 것을 직접 증명했다 [3]. 사실 consistency의 증명은 자연수가 정의된 체계 위에서 하는 것이므로, 이 체계가 consistent하다는 가정 하에서 하는 것이다. 그렇다면 이 상위 체계가 과연 정말 consistent한가? 후술하겠지만 그걸 체계 내에서 증명 또는 반증하는 것이 불가능하다. 따라서 이 상위 체계의 consistency는 그냥 믿고 갈 때 나오는 결론이다.

더 나아가서, Presburger arithmetic이 decidable하다는 것(임의의 명제의 참/거짓을 판별하는 알고리즘이 존재한다는 것)까지 보일 수 있다. 참고로 consistent + recursive + complete 조합으로 decidability는 곧바로 따라오지만, Presburger는 이보다 훨씬 구체적이고 효율적인 판별 알고리즘이 있다는 것을 보였다.

다만 이 체계에도 단점이 있는데, 곱셈이 없기 때문에 primitive recursive function이라는 함수를 일반적으로 표현할 수 없다는 점이다.

## Gödel의 제1불완전성 정리

그렇다면 recursive하고 primitive recursive function을 표현할 수 있는 체계 중에 완전하고 무모순한 체계가 있을까? 그것이 불가능함을 보인 것이 괴델의 제1불완전성 정리이다.

**Theorem (Gödel's First Incompleteness Theorem, 1931 [4]).** Let $F$ be a formal system such that (i) the set of axioms of $F$ is recursive, (ii) $F$ is $\omega$-consistent, and (iii) $F$ contains enough elementary arithmetic to represent primitive recursive functions and relations. Then there is a closed formula $G_F$ in the language of $F$ such that neither $F \vdash G_F$ nor $F \vdash \lnot G_F$.

여기서 *$\omega$-consistent*하다는 조건은 단순한 consistency보다 강하다. $F$가 $\omega$-inconsistent하다는 것은, 어떤 논리식 $A(x)$가 있어서 각 자연수 $n$마다 $F \vdash \lnot A(n)$이면서(즉 "$n$은 $A$를 만족하지 않는다"가 개별적으로 모두 증명되면서) 동시에 $F \vdash \exists x\, A(x)$인 경우("$A$를 만족하는 무언가가 있다"도 증명되는 경우)를 말한다. $\omega$-consistent란 이런 상황이 없다는 것이다. 단순 consistency는 어떤 하나의 명제와 그 부정이 동시에 증명되지만 않으면 충족되므로, $\omega$-consistency가 더 강한 조건이다.

사실 괴델은 정확하게 위를 증명하지는 않았고, simple type theory 위에 자연수를 기본 타입으로 얹은 체계 $P$에 대해서 위 결과를 증명했다. $P$는 위 조건 (i), (iii)을 만족하며, $\omega$-consistency는 가정이었다. Gödel은 논문에서 이 결과가 $P$뿐 아니라 ZFC 같은 다른 표준적인 체계에도 적용될 수 있으리라고 언급했지만, 이를 엄밀하게 증명하지는 않았다. 후에 Church [5], Turing [2], Kleene [6, 7]에 의해 위와 같은 형태로 일반화가 되었다.

이후 Rosser가 1936년에 $\omega$-consistency 조건을 단순 consistency로 약화시킬 수 있음을 보였다 [8]. 오늘날에는 이 개선된 버전을 Gödel–Rosser 정리라고 부르기도 한다.

Gödel–Rosser 버전은 다음과 같이 다시 쓸 수도 있다: 공리 집합이 recursive, consistent, primitive recursive function 표현 가능, complete — 이 4개를 동시에 만족하는 체계는 없다.

| recursive | consistent | primitive recursive function | complete | 예시 |
|:---:|:---:|:---:|:---:|---|
| ✗ | ✓ | ✓ | ✓ | True Arithmetic |
| ✓ | ✗ | ✓ | ✓ | ZF + "$0=1$" |
| ✓ | ✓ | ✗ | ✓ | Presburger arithmetic |
| ✓ | ✓ | ✓ | ✗ | Consistency를 가정한 ZF |

ZF에 $0=1$이라는 공리를 추가하면 즉각적인 모순이 생기므로 inconsistent하다. 그리고 inconsistent한 체계에서는 뭐든지 증명 가능하므로 complete도 만족한다.

ZF가 consistent하다면 제1불완전성 정리에 의해 반드시 incomplete하다. 실제로 ZF에는 AC나 CH 등 증명 또는 반증이 불가한 명제가 있다. (이것이 ZF가 consistent하다는 의미는 아니다.) 이들을 공리로 추가하더라도 또 다른 증명 또는 반증이 불가한 명제가 생겨난다.

## Gödel의 제2불완전성 정리

Hilbert의 "Wir müssen wissen, wir werden wissen"은 단순히 완전한 체계를 향한 열망만은 아니었다. Hilbert는 수학 전체에 모순이 없다는 것도 증명하고 싶었다. 그렇다면 형식체계가 스스로 "나는 무모순이다"라는 것을 증명하는 건 가능할까? 괴델은 이 질문에조차 아니라고 답한다.

**Theorem (Gödel's Second Incompleteness Theorem, 1931 [4]).** Let $F$ satisfy conditions (i) and (iii) of the first incompleteness theorem (note: consistency, condition (ii), is deliberately not assumed here — it appears only in the final clause below). Let $\mathrm{Prf}_F(x,y)$ be the syntactic relation "$x$ is (the Gödel number of) a proof whose last line has Gödel number $y$", let $G_F$ be the sentence — constructed via the Diagonal Lemma — satisfying $F \vdash G_F \leftrightarrow \lnot\exists x\, \mathrm{Prf}_F(x, \ulcorner G_F\urcorner)$, and let $\mathrm{Con}(F) :\equiv \lnot\exists x\, \mathrm{Prf}_F(x, \ulcorner 0=1 \urcorner)$. Suppose in addition that $F$ can prove the following about its own provability predicate $\mathrm{Prov}_F(y) :\equiv \exists x\, \mathrm{Prf}_F(x,y)$ (today known as the Hilbert–Bernays–Löb derivability conditions):

- D1. If $F\vdash\varphi$, then $F\vdash\mathrm{Prov}_F(\ulcorner\varphi\urcorner)$.
- D2. $F\vdash \mathrm{Prov}_F(\ulcorner\varphi\to\psi\urcorner)\to(\mathrm{Prov}_F(\ulcorner\varphi\urcorner)\to\mathrm{Prov}_F(\ulcorner\psi\urcorner))$.
- D3. $F\vdash \mathrm{Prov}_F(\ulcorner\varphi\urcorner)\to\mathrm{Prov}_F(\ulcorner\mathrm{Prov}_F(\ulcorner\varphi\urcorner)\urcorner)$.

Then $F \vdash \mathrm{Con}(F) \to G_F$ — this holds regardless of whether $F$ is actually consistent. In particular, if $F$ is also consistent, then $F \nvdash \mathrm{Con}(F)$.

복잡해 보이지만 핵심은 어떤 형식체계의 공리가 recursive하고, primitive recursive function을 표현 가능하고, $F$의 provability predicate가 Hilbert–Bernays–Löb derivability conditions를 만족하면, (그 체계가 실제로 consistent한 한) 자기 자신의 무모순성을 증명할 수 없다는 것이다.

Gödel은 1931년 논문에서 이 정리의 완전한 증명은 스케치 수준으로만 남겼다. $F$의 provability predicate가 만족해야 할 조건들을 엄밀하게 정리하고 이로부터 제2불완전성 정리를 완전하게 증명한 것은 훗날 Hilbert와 Bernays의 1939년 저작에서였다 [9]. 다만 이때의 증명은 70쪽에 달하는 다소 임기응변적인 조건들에 의존했는데, 이를 오늘날 널리 쓰이는 깔끔한 D1–D3 형태로 다듬고 이로부터 얻어지는 일반적인 결과(Löb's Theorem)를 정리한 것은 Löb의 1955년 논문이었다 [10].

## 참고문헌

1. Hilbert, D. (1930). Naturerkennen und Logik. *Die Naturwissenschaften*, 18(4), 959–963.
2. Turing, A. M. (1936/1937). On Computable Numbers, with an Application to the Entscheidungsproblem. *Proceedings of the London Mathematical Society*, s2-42(1), 230–265. (1936년 5월 28일 투고, 같은 해 11월 12일 학회에서 발표되었으나, 학술지의 공식 서지 정보상 수록된 42권은 1937년 발행이다.)
3. Presburger, M. (1929). Über die Vollständigkeit eines gewissen Systems der Arithmetik ganzer Zahlen, in welchem die Addition als einzige Operation hervortritt. *Comptes Rendus du I congrès de Mathématiciens des Pays Slaves, Warszawa*, 92–101.
4. Gödel, K. (1931). Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I. *Monatshefte für Mathematik und Physik*, 38, 173–198.
5. Church, A. (1936). An Unsolvable Problem of Elementary Number Theory. *American Journal of Mathematics*, 58(2), 345–363.
6. Kleene, S. C. (1936). General Recursive Functions of Natural Numbers. *Mathematische Annalen*, 112, 727–742.
7. Kleene, S. C. (1943). Recursive Predicates and Quantifiers. *Transactions of the American Mathematical Society*, 53(1), 41–73.
8. Rosser, J. B. (1936). Extensions of some theorems of Gödel and Church. *The Journal of Symbolic Logic*, 1(3), 87–91.
9. Hilbert, D., & Bernays, P. (1939). *Grundlagen der Mathematik II*. Springer.
10. Löb, M. H. (1955). Solution of a Problem of Leon Henkin. *The Journal of Symbolic Logic*, 20(2), 115–118.

---
