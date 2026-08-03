---
layout: post
title: "실수 수열의 극한"
date: 2026-07-26
---

## 실수 수열의 극한

**Definition (Limit of a Sequence).** A sequence $ (a_n)_{n=1}^\infty$ of real numbers *converges* to $L \in \mathbb{R}$, written $\lim_{n\to\infty} a_n = L$ or $a_n \to L$, if for every $\varepsilon > 0$ there exists $N \in \mathbb{N}$ such that $\vert a_n - L\vert < \varepsilon$ for all $n \ge N$.

극한의 개념을 다룰 때 주로 등장하는 수학자는 Cauchy인데, Cauchy가 위의 정의를 엄밀하게 한 것은 아니지만, 1821년 *Cours d'Analyse*에서 극한의 개념을 명시적으로 정식화하고, 그 위에 미적분학의 모든 핵심 개념을 체계적으로 재건축했다. 위와 같은 형태의 정의는 Bolzano가 1817년 논문에서, 그리고 Weierstrass가 1870년대 베를린에서의 강의를 통해 각각 독자적으로 다듬은 것으로 알려져 있다 [1].

**Proposition (극한의 유일성).** If $a_n \to L$ and $a_n \to L'$, then $L = L'$.

*Proof.* $L \neq L'$이라 하고 $\varepsilon = \vert L-L'\vert/2 > 0$으로 두자. 어떤 $N$ 이후로는 $\vert a_n-L\vert<\varepsilon$이고 어떤 $N'$ 이후로는 $\vert a_n-L'\vert<\varepsilon$이므로, $n\ge\max(N,N')$인 $n$에 대해 삼각부등식으로 $\vert L-L'\vert \le \vert L-a_n\vert+\vert a_n-L'\vert < 2\varepsilon = \vert L-L'\vert$이 되어 모순. $\blacksquare$

$(a_n)$이 수렴하지 않으면 발산한다(diverges)고 하는데, 발산하는 수열 중에서도 특별한 두 가지를 다음과 같이 정의한다.

**Definition.** $a_n \to \infty$ iff $\forall M > 0\ \exists N$ such that $a_n > M\ \forall n \geq N$. $a_n \to -\infty$ iff $\forall M < 0\ \exists N$ such that $a_n < M\ \forall n \geq N$.

## 유계이고 단조인 수열

수열 $(a_n)$이 *bounded*라는 것은 어떤 $M$이 있어 모든 $n$에 대해 $\vert a_n\vert \le M$이라는 뜻이고, *monotone increasing*이라는 것은 모든 $n$에 대해 $a_n \le a_{n+1}$이라는 뜻이다.

실수의 완비성 덕분에 다음과 같은 아주 중요하고 자주 쓰이는 성질이 보장된다.

**Theorem (Monotone Convergence Theorem).** A bounded, monotone increasing sequence $(a_n)$ converges, and $\lim_{n\to\infty} a_n = \sup_n a_n$.

*Proof.* $L := \sup_n a_n$이라 하자 (수열이 bounded이므로 이 sup은 실수로 존재한다 — 여기서 실수의 완비성, 즉 위로 유계인 집합은 상한을 갖는다는 성질이 쓰인다). 임의의 $\varepsilon>0$에 대해, sup의 정의상 $L-\varepsilon < a_N \le L$인 $N$이 존재한다. 수열이 monotone increasing이므로 $n\ge N$이면 $L-\varepsilon < a_N \le a_n \le L$이고, 따라서 $\vert a_n - L\vert < \varepsilon$. $\blacksquare$

같은 논리로, bounded monotone decreasing sequence $(a_n)$은 $\inf_n a_n$으로 수렴한다.

## limsup과 liminf

**Definition (limsup, liminf).**

$$\limsup_{n\to\infty} a_n := \lim_{N\to\infty} \Big(\sup_{n\ge N} a_n\Big) = \inf_{N} \sup_{n\ge N} a_n,$$

$$\liminf_{n\to\infty} a_n := \lim_{N\to\infty} \Big(\inf_{n\ge N} a_n\Big) = \sup_{N} \inf_{n\ge N} a_n.$$

$\lim$은 항상 존재하는 것은 아니지만, $\limsup, \liminf$는 (유한한 값이든 $\infty$나 $-\infty$든) 항상 존재한다. 모든 $N$에 대해 $\sup_{n\ge N} a_n=\infty$라면 $\limsup a_n = \infty$이고, 그렇지 않다면 $\sup_{n\ge N} a_n$은 (모든 $N$에 대해 유한하며) $N$에 대해 monotone decreasing이므로 MCT에 의해 극한을 갖는다. $\liminf a_n$도 마찬가지 논리로 $-\infty$이거나 어떤 값을 갖는다.

**Proposition.** For any sequence $(a_n)$, $\liminf_{n\to\infty} a_n \le \limsup_{n\to\infty} a_n$.

*Proof.* 모든 $N$에 대해 $\inf_{n\ge N} a_n \le \sup_{n\ge N} a_n$이므로, 양변에 각각 $N\to\infty$ 극한(왼쪽은 증가하는 극한, 오른쪽은 감소하는 극한)을 취해도 부등호는 유지된다. $\blacksquare$

**Proposition (수렴 판정).** $(a_n)$ converges to $L \in \mathbb{R}$ if and only if $\liminf_{n\to\infty} a_n = \limsup_{n\to\infty} a_n = L$.

이 성질이 실전에서 가장 유용하다 — 수열이 수렴하는지, 수렴한다면 그 값이 무엇인지를 liminf와 limsup을 각각 계산해서 확인할 수 있다.

**Proposition (Duality).** $\limsup_{n\to\infty}(-a_n) = -\liminf_{n\to\infty} a_n$.

*Proof.* $\sup_{n\ge N}(-a_n) = -\inf_{n\ge N} a_n$이 모든 $N$에 대해 성립하므로, $N\to\infty$ 극한을 취하면 된다. $\blacksquare$

**Proposition (단조성).** If $a_n \le b_n$ for all sufficiently large $n$, then $\limsup_{n\to\infty} a_n \le \limsup_{n\to\infty} b_n$ and $\liminf_{n\to\infty} a_n \le \liminf_{n\to\infty} b_n$.

**Proposition (Subadditivity).** $\limsup_{n\to\infty}(a_n+b_n) \le \limsup_{n\to\infty} a_n + \limsup_{n\to\infty} b_n$ and $\liminf_{n\to\infty}(a_n+b_n) \ge \liminf_{n\to\infty} a_n + \liminf_{n\to\infty} b_n$ (우변이 $\infty-\infty$ 꼴이 아닌 한).

*Proof (limsup 쪽만).* 각 $N$에 대해 $n\ge N$인 모든 $n$에 대해 $a_n \le \sup_{n\ge N} a_n$이고 $b_n \le \sup_{n\ge N} b_n$이므로 $a_n+b_n \le \sup_{n\ge N} a_n + \sup_{n\ge N} b_n$이다. 따라서 $\sup_{n\ge N}(a_n+b_n) \le \sup_{n\ge N} a_n + \sup_{n\ge N} b_n$이고, $N\to\infty$ 극한을 취하면 원하는 부등식을 얻는다. $\blacksquare$

이 부등식은 일반적으로 등호가 성립하지 않는다. $a_n = (-1)^n$, $b_n = (-1)^{n+1} = -a_n$이라 하면 $a_n+b_n=0$이니 $\limsup(a_n+b_n)=0$이지만, $\limsup a_n = \limsup b_n = 1$이라 우변은 $2$다. 다만 $(a_n)$과 $(b_n)$ 중 하나가 실제로 수렴하면 등호가 성립한다는 것도 어렵지 않게 보일 수 있다.

**Proposition.** $\limsup_{n\to\infty} a_n < a \implies \exists N$ such that $a_n < a\ \forall n \geq N$.

*Proof.* $r:=\limsup a_n < a$라 하자. $\limsup a_n = \inf_N \sup_{n\ge N} a_n$이 $a$보다 작으므로, 어떤 $N$에 대해 $\sup_{n\ge N} a_n < a$이다. 그러면 $n\ge N$인 모든 $n$에 대해 $a_n \le \sup_{n\ge N} a_n < a$. $\blacksquare$

참고로 가정을 $\limsup a_n<a$에서 $\limsup a_n\le a$로 완화하면 결론은 더 이상 성립하지 않는다 (예: $a_n=a+1/n$이면 $\limsup a_n=a$이지만 모든 $n$에 대해 $a_n>a$다).

**Proposition.** $\liminf_{n\to\infty} a_n > a \implies \exists N$ such that $a_n > a\ \forall n \geq N$.

*Proof.* 앞서 본 Duality를 쓰거나, 위 증명에서 부등호와 sup/inf를 전부 뒤집으면 된다. $\blacksquare$

## 실수 수열 극한의 여러 가지 성질과 관계성

$\lim$은 항상 존재하는 것은 아니므로, 그보다 약하지만 유용한 성질들을 알아보자. 자연스럽게 등장하는 네 가지 성질 — **수렴한다(convergent)**, **유계다(bounded)**, **$\limsup, \liminf$ 중 하나 이상이 유한하다**, **수렴하는 부분수열을 갖는다** — 사이의 관계를 하나씩 밝혀나가보자.

**Proposition.** If $(a_n)$ converges, then $(a_n)$ is bounded.

*Proof.* $a_n\to L$이라 하자. $\varepsilon=1$로 두면 어떤 $N$이 있어 $n\ge N$이면 $\vert a_n-L\vert<1$이다. $a_1,\dots,a_{N-1}$은 유한히 많으므로, 전체 수열은 $\max(\vert a_1\vert,\dots,\vert a_{N-1}\vert,\vert L\vert+1)$로 bound된다. $\blacksquare$

역은 성립하지 않는다 — $a_n=(-1)^n$은 bounded이지만 발산한다.

한편, boundedness는 다음 성질과 동치다.

**Proposition.** $(a_n)$ is bounded if and only if both $\limsup_{n\to\infty} a_n$ and $\liminf_{n\to\infty} a_n$ are finite (i.e., in $\mathbb{R}$, not $\pm\infty$).

*Proof.* ($\Rightarrow$) $(a_n)$이 bounded이면 모든 $N$에 대해 $\sup_{n\ge N}a_n$과 $\inf_{n\ge N}a_n$이 이미 유한하므로, 그 극한인 $\limsup, \liminf$도 유한하다. ($\Leftarrow$) 대우를 보이자. $(a_n)$이 위로 유계가 아니라면, 임의의 $N$에 대해 $$\{a_n : n\ge N\}$$도 위로 유계가 아니다 — 그렇지 않다면 앞의 유한히 많은 항 $a_1,\dots,a_{N-1}$을 더해도 전체 수열이 위로 유계가 되어 모순이기 때문이다. 따라서 모든 $N$에 대해 $\sup_{n\ge N} a_n=\infty$이고, $\limsup a_n=\infty$. 아래로 유계가 아닌 경우도 대칭적으로 $\liminf a_n=-\infty$가 된다. $\blacksquare$

이제 boundedness보다는 약하지만 매우 유용한 다음 성질을 살펴보자.

**Theorem (Bolzano–Weierstrass).** Every bounded sequence of real numbers has a convergent subsequence.

Bolzano가 1817년 논문에서 실질적으로 이와 동등한 내용을 다뤘고, Weierstrass가 1860년대 강의에서 이를 명시적인 정리로 다듬어 오늘날의 이름이 붙었다 [1].

*Proof.* $(a_n)$이 bounded이면 앞의 Proposition에 의해 $\limsup_{n\to\infty} a_n$은 (무한대가 아니라) 유한한 실수이다. 다음 Proposition에 의해, 이 값으로 수렴하는 부분수열이 실제로 존재한다.

**Proposition.** $\limsup_{n\to\infty} a_n = a \implies$ there exists a subsequence of $(a_n)$ converging to $a$.

*Proof.* $b_N:=\sup_{n\ge N}a_n$은 $N$에 대해 감소하며 $a$로 수렴한다. 귀납적으로 $n_1<n_2<\cdots$를 다음과 같이 고른다: $k$번째 단계에서, $b_N < a+1/k$인 $N$을 하나 골라 $N_k:=\max(N, n_{k-1}+1)$로 두면 $b_{N_k}<a+1/k$이고, 한편 $b_{N_k}=\sup_{n\ge N_k}a_n \ge a$이므로 (감소하며 $a$로 수렴하는 수열의 각 항은 극한 이상이다) sup의 정의상 $a-1/k < a_{n_k} \le b_{N_k} < a+1/k$인 $n_k\ge N_k$가 존재한다. 그러면 $\vert a_{n_k}-a\vert<1/k\to0$이므로 $a_{n_k}\to a$. $\blacksquare$

이 Proposition을 $a=\limsup_{n\to\infty}a_n$에 적용하면 Bolzano–Weierstrass의 증명이 끝난다. $\blacksquare$

Boundedness가 "$\limsup,\liminf$ 둘 다 유한"과 동치이므로, 방금 보인 것은 사실상 "$\limsup,\liminf$ 둘 다 유한하면 수렴하는 부분수열이 있다"는 것과 같은 말이다. 그런데 증명을 다시 보면 실제로는 $\limsup$ 하나가 유한하다는 것만 썼다 — 즉 둘 중 하나만 유한해도 이미 충분하다.

그리고 $\limsup$과 $\liminf$는 정확히 이 convergent subsequence들이 수렴할 수 있는 값의 범위를 특징짓는다.

**Proposition (subsequential limit로서의 특징).** $\limsup_{n\to\infty} a_n$ is the largest element of $\overline{\mathbb{R}}$ that is the limit of some subsequence of $(a_n)$, and $\liminf_{n\to\infty} a_n$ is the smallest such element.

지금까지의 관계를 한 번에 정리하면 다음과 같다.

$$\text{수렴} \implies \text{bounded} \;(=\; \limsup,\liminf \text{ 둘 다 유한}) \implies \limsup,\liminf \text{ 중 하나 이상 유한} \implies \text{수렴하는 부분수열을 가짐}$$

점점 약해지는 성질들의 사슬이고, 표시된 각 함의는 역이 성립하지 않는 엄격한 함의다.

흥미롭게도, 이 사슬에서 가장 약한 성질인 "수렴하는 부분수열을 가짐"도, 원래 수열의 **모든** 부분수열에 대해 성립하도록 강화하면 다시 수렴과 동치가 된다.

**Proposition.** $a_n \to a$ if and only if every subsequence of $(a_n)$ has a further subsequence that converges to $a$.

*Proof.* ($\Rightarrow$) 자명하다 — $a_n\to a$이면 모든 부분수열도 $a$로 수렴하니, 그 부분수열 자신을 "더 나아간 부분수열"로 잡으면 된다. ($\Leftarrow$) 대우를 보이자. $a_n\not\to a$라 하면, 어떤 $\varepsilon>0$이 있어 $\vert a_n-a\vert\ge\varepsilon$인 $n$이 무한히 많다. 이 $n$들만 모아 부분수열 $(a_{n_k})$를 만들면, 이 부분수열의 **어떤 부분수열도** $\vert\cdot-a\vert\ge\varepsilon$을 유지하므로 $a$로 수렴할 수 없다. $\blacksquare$

## $\limsup$, $\liminf$의 응용

limsup, liminf가 실전에서 어떻게 위력을 발휘하는지 보여주는 대표적인 예가 하나 있다. $a_n = n$이나 $a_n = \sqrt[n]{n!}/n$처럼, $a_n^{1/n}$의 극한을 직접 계산하기는 까다롭지만 $a_{n+1}/a_n$의 극한은 계산하기 쉬운 경우가 많다. 다음 lemma는 후자로부터 전자를 얻어낼 수 있음을 보장한다.

**Lemma.** Let $(a_n)$ be a sequence of positive real numbers. Then

$$\liminf_{n\to\infty} \frac{a_{n+1}}{a_n} \;\le\; \liminf_{n\to\infty} a_n^{1/n} \;\le\; \limsup_{n\to\infty} a_n^{1/n} \;\le\; \limsup_{n\to\infty} \frac{a_{n+1}}{a_n}.$$

특히 $\lim_{n\to\infty} a_{n+1}/a_n = L$이 존재하면 $\lim_{n\to\infty} a_n^{1/n} = L$도 존재하고 같은 값을 갖는다.

*Proof.* 가운데 부등식은 이미 보인 일반적인 사실이다. 오른쪽 부등식만 보이면 왼쪽은 대칭적인 논증(모든 부등호 방향을 뒤집고 $\sup$/$\inf$를 바꾸면 된다)으로 얻어진다.

$r := \limsup_{n\to\infty} a_{n+1}/a_n$이라 하고, $r=\infty$이면 부등식이 자명하므로 $r<\infty$라 가정하자. 임의의 $\varepsilon>0$에 대해, $\limsup$의 정의상 어떤 $N$이 있어 모든 $n\ge N$에 대해 $a_{n+1}/a_n < r+\varepsilon$이다. 그러면 $n>N$에 대해

$$a_n = a_N \cdot \prod_{k=N}^{n-1} \frac{a_{k+1}}{a_k} < a_N (r+\varepsilon)^{n-N}$$

이고, 양변에 $1/n$ 제곱을 취하면 $a_n^{1/n} < a_N^{1/n} (r+\varepsilon)^{(n-N)/n}$이다. $N$은 고정되어 있으므로 $n\to\infty$일 때 $a_N^{1/n}\to 1$이고 $(n-N)/n \to 1$이니, $\limsup_{n\to\infty} a_n^{1/n} \le r+\varepsilon$. $\varepsilon>0$이 임의였으므로 $\limsup_{n\to\infty} a_n^{1/n} \le r$. $\blacksquare$

이 lemma를 이용하면 몇 가지 극한을 손쉽게 얻는다.

**$\lim_{n\to\infty} n^{1/n} = 1$.** $a_n = n$으로 두면 $a_{n+1}/a_n = (n+1)/n \to 1$이므로, lemma에 의해 $n^{1/n} \to 1$이다. ($a_n^{1/n}$을 직접 이항정리 등으로 다뤄서 보이는 것보다 훨씬 간결하다.)

**$\lim_{n\to\infty} \dfrac{\sqrt[n]{n!}}{n} = \dfrac{1}{e}$.** $a_n = n^n/n!$로 두면

$$\frac{a_{n+1}}{a_n} = \frac{(n+1)^{n+1}/(n+1)!}{n^n/n!} = \left(\frac{n+1}{n}\right)^n = \left(1+\frac1n\right)^n \to e$$

이므로 (마지막 극한은 $e$의 정의 그 자체다), lemma에 의해 $a_n^{1/n} = n/\sqrt[n]{n!} \to e$, 즉 $\sqrt[n]{n!}/n \to 1/e$이다.

이 lemma는 흔히 미적분학에서 급수의 수렴을 판정할 때 쓰는 ratio test(비율판정법)와 root test(거듭제곱근판정법)가 왜 서로 호환되는지 — ratio test가 통하는 급수라면 root test도 항상 같은 결론을 준다는 것 — 를 설명해준다. 이 이야기는 나중에 멱급수를 다룰 때 다시 등장할 것이다.

## Stolz–Cesàro Theorem

Stolz–Cesàro Theorem은 이산적인 상황에서의 L'Hôpital's Rule이라고 봐도 된다. 이 정리는 Stolz가 1885년 저서에서, Cesàro가 1888년 논문에서 각각 다뤘다 [4, 5].

**Theorem (Stolz–Cesàro).** Let $(b_n)$ be strictly increasing with $b_n \to \infty$. If

$$\lim_{n\to\infty} \frac{a_{n+1}-a_n}{b_{n+1}-b_n} = L \in \overline{\mathbb{R}}$$

exists, then $\lim_{n\to\infty} a_n/b_n$ also exists and equals $L$.

*Proof.* $L$이 유한하다고 하자 (무한대인 경우도 같은 논증이 통한다). $\varepsilon>0$이 주어지면, 어떤 $N$이 있어 $n\ge N$이면 $(L-\varepsilon)(b_{n+1}-b_n) < a_{n+1}-a_n < (L+\varepsilon)(b_{n+1}-b_n)$이다 ($b_n$이 strictly increasing이므로 $b_{n+1}-b_n>0$이라 부등호 방향이 유지된다). $n>N$에 대해 $k=N,\dots,n-1$로 telescoping하면

$$(L-\varepsilon)(b_n-b_N) < a_n - a_N < (L+\varepsilon)(b_n-b_N).$$

충분히 큰 $n$에 대해 (그때는 $b_n>0$) 양변을 $b_n$으로 나누면

$$(L-\varepsilon)\Big(1-\frac{b_N}{b_n}\Big) + \frac{a_N}{b_n} < \frac{a_n}{b_n} < (L+\varepsilon)\Big(1-\frac{b_N}{b_n}\Big) + \frac{a_N}{b_n}.$$

$N$은 고정되어 있고 $b_n\to\infty$이므로, $n\to\infty$일 때 $b_N/b_n\to 0$이고 $a_N/b_n\to 0$이다. 따라서 $\limsup_n a_n/b_n \le L+\varepsilon$이고 $\liminf_n a_n/b_n \ge L-\varepsilon$. $\varepsilon>0$이 임의였으므로 $\lim_n a_n/b_n = L$. $\blacksquare$

이를 사용하면 다음과 같은 어려운 극한을 구할 수 있다.

**Corollary (약한 형태의 Stirling 공식).** $\dfrac{\ln(n!)}{n\ln n} \to 1$.

*Proof.* $a_n:=\ln(n!)=\displaystyle\sum_{k=1}^n\ln k$, $b_n:=n\ln n$으로 두면 둘 다 $\infty$로 발산하고 $b_n$은 strictly increasing이다. $a_{n+1}-a_n=\ln(n+1)$이고, $(n+1)\ln(n+1)$에서 $\ln(n+1)=\ln n+\ln(1+1/n)$을 대입해 전개하면

$$b_{n+1}-b_n = (n+1)\ln(n+1)-n\ln n = \ln n + (n+1)\ln(1+1/n)$$

을 얻는다. $\ln(1+x)/x\to1$ ($x\to0$)에 $x=1/n$을 대입하면 $n\ln(1+1/n)\to1$이므로 $(n+1)\ln(1+1/n) = n\ln(1+1/n)+\ln(1+1/n) \to 1+0=1$이고, $b_{n+1}-b_n$은 $\ln n$에 유계인 항 하나를 더한 꼴이다. $a_{n+1}-a_n=\ln(n+1)$도 마찬가지로 $\ln n$에 $0$으로 수렴하는 항을 더한 꼴이므로, 분자·분모를 $\ln n$으로 나누면

$$\frac{a_{n+1}-a_n}{b_{n+1}-b_n} = \frac{\ln(n+1)/\ln n}{1+(n+1)\ln(1+1/n)/\ln n} \to \frac{1}{1+0} = 1$$

이다. Stolz–Cesàro($\infty/\infty$ 버전)에 의해 $\ln(n!)/(n\ln n) \to 1$. $\blacksquare$

즉 $n!$의 로그는 $n\ln n$과 같은 속도로 자란다 — Stirling의 공식 $n!\sim\sqrt{2\pi n}\,(n/e)^n$에서 지수 부분만 남긴 가장 거친(leading-order) 형태다.

Stolz–Cesàro Theorem의 다음과 같은 0/0 버전도 생각해볼 수 있다.

**Theorem.** Let $(a_n)$ and $(b_n)$ be sequences with $a_n\to0$ and $b_n\to0$, where $(b_n)$ is strictly decreasing. If

$$\lim_{n\to\infty} \frac{a_{n+1}-a_n}{b_{n+1}-b_n} = L \in \overline{\mathbb{R}}$$

exists, then $\lim_{n\to\infty} a_n/b_n$ also exists and equals $L$.

가정이 $\infty/\infty$ 버전과 정반대($b_n\to\infty$ 대신 $b_n\to0$)라는 점을 빼면 진술은 똑같아 보이지만, 증명은 단순히 뒤집어서 되는 게 아니다. $b_n$이 이제 감소하므로 $b_{n+1}-b_n<0$이고, 부등식을 정리할 때 부등호 방향이 뒤집힌다:

$$(L+\varepsilon)(b_{n+1}-b_n) < a_{n+1}-a_n < (L-\varepsilon)(b_{n+1}-b_n)$$

이걸 telescoping하면 $(L+\varepsilon)(b_n-b_N) < a_n-a_N < (L-\varepsilon)(b_n-b_N)$을 얻는다. 여기서 $\infty/\infty$ 버전과 결정적으로 다른 지점이 나온다 — 그쪽에서는 $b_n\to\infty$이므로 양변을 $b_n$으로 나누고 $n\to\infty$를 보내 $b_N/b_n\to0$을 활용했는데, 여기서는 그 대신 $N$을 **고정한 채** $n\to\infty$로 보낸다 ($a_n\to0$, $b_n\to0$이므로): 부등식이 $(L+\varepsilon)(-b_N) \le -a_N \le (L-\varepsilon)(-b_N)$, 즉 $(L-\varepsilon)b_N \le a_N \le (L+\varepsilon)b_N$으로 정리되고, $b_N>0$으로 나누면 $\vert a_N/b_N-L\vert\le\varepsilon$을 얻는다. 이는 임의로 크게 잡을 수 있는 모든 $N$에 대해 성립하므로 $a_N/b_N\to L$이다.

즉 $\infty/\infty$ 쪽은 "$n\to\infty$, 그다음 $N\to\infty$"라는 이중 극한 구조인 반면, $0/0$ 쪽은 "고정된 $N$에 대해 다른 변수를 $\infty$로 보내는" 다른 구조의 증명이다 — 그래서 두 버전은 단순히 서로 뒤집어서 되는 관계가 아니다. $\infty/\infty$ 버전이 부분합(더할수록 커져서 $\infty$로 발산하는 방향)에 자연스럽게 대응된다면, $0/0$ 버전은 그 거울상 — 나머지항(뒤로 갈수록 작아져서 $0$으로 수렴하는 방향) — 에 대응된다.

## Fekete's Subadditive Lemma

마지막으로 소개할 결과는 앞의 둘과는 결이 조금 다르다. 수열 $ (a_n)_{n\ge1}$이 *subadditive*라는 것은 모든 $n,m\ge1$에 대해 $a_{n+m} \le a_n+a_m$이 성립한다는 뜻이다.

**Theorem (Fekete's Subadditive Lemma, 1923 [6]).** If $(a_n)_{n\ge1}$ is subadditive, then $\lim_{n\to\infty} \dfrac{a_n}{n}$ exists in $[-\infty,\infty)$ and equals $\inf_{n\ge1} \dfrac{a_n}{n}$.

*Proof.* $L := \inf_{n\ge1} a_n/n \in [-\infty,\infty)$라 하자. inf의 정의상 모든 $n$에 대해 $a_n/n \ge L$이므로 $\liminf_n a_n/n \ge L$은 자명하다.

반대 방향을 보이자. $a_0:=0$으로 약속하면 subadditivity는 $m=0$일 때도 성립한다. 임의의 $m\ge1$을 고정하고, 각 $n$을 $n=qm+r$ ($q,r$은 $n$에 따라 정해지는, $0$부터 $m-1$ 사이의 정수)로 나누면, subadditivity를 $q$번 반복 적용해 $a_n = a_{qm+r} \le q\,a_m + a_r$을 얻는다. 양변을 $n$으로 나누면

$$\frac{a_n}{n} \le \frac{q}{n}\,a_m + \frac{a_r}{n}.$$

$m$을 고정한 채 $n\to\infty$이면 $q/n \to 1/m$이고, $r$은 $0$부터 $m-1$ 사이의 유한한 값만 가지므로 $a_r/n \to 0$이다. 따라서 $\limsup_n a_n/n \le a_m/m$. 이것이 임의의 $m$에 대해 성립하므로 $\limsup_n a_n/n \le \inf_m a_m/m = L$.

$L \le \liminf_n a_n/n \le \limsup_n a_n/n \le L$이므로 모두 같고, $\lim_n a_n/n = L$이다. $\blacksquare$

Subadditivity라는 순전히 대수적인 조건 하나만으로 극한의 존재성이 보장된다는 게 이 lemma의 매력이다.

이 lemma의 가장 인상적인 응용 중 하나는 self-avoiding walk(자기회피보행)의 connective constant다. 격자 $\mathbb{Z}^d$ 위에서 원점을 출발해 $n$걸음 동안 같은 자리를 두 번 지나지 않는 경로의 개수를 $c_n$이라 하자. $n$걸음짜리 경로 하나와, 그 끝점에서 새로 시작하는 $m$걸음짜리 경로 하나를 이어붙이면 $n+m$걸음짜리 경로의 후보가 되는데, 이 중 실제로 자기회피인 것만 남기면 되므로 $c_{n+m} \le c_n\, c_m$이다. 즉 $\log c_n$은 subadditive이고, Fekete's Lemma에 의해

$$\mu := \lim_{n\to\infty} c_n^{1/n} = \inf_{n\ge1} c_n^{1/n}$$

이 항상 존재한다 (이 $\mu$를 connective constant라 부른다). 그런데 이 극한의 *존재*는 이렇게 손쉽게 보장되는 반면, 정작 그 *값*은 대부분의 격자에서 여전히 정확히 알려져 있지 않다 — 흔히 다루는 $\mathbb{Z}^2$(사각격자)도 마찬가지다. 예외적으로 육각격자(hexagonal lattice)에 대해서는 Duminil-Copin과 Smirnov가 2012년에 $\mu=\sqrt{2+\sqrt2}$임을 증명해, Nienhuis가 물리학적 논증(Coulomb gas 방법)으로 예측했던 값을 엄밀하게 확인했다 [7].

## 참고문헌

1. Grabiner, J. V. (1983). Who Gave You the Epsilon? Cauchy and the Origins of Rigorous Calculus. *The American Mathematical Monthly*, 90(3), 185–194.
2. Cauchy, A.-L. (1821). *Cours d'analyse de l'École royale polytechnique; I.re Partie. Analyse algébrique*. Paris: Imprimerie Royale.
3. Rudin, W. (1976). *Principles of Mathematical Analysis* (3rd ed.). McGraw-Hill.
4. Stolz, O. (1885). *Vorlesungen über allgemeine Arithmetik: nach den neueren Ansichten*. Teubner, Leipzig. pp. 173–175.
5. Cesàro, E. (1888). Sur la convergence des séries. *Nouvelles annales de mathématiques*, Series 3, 7, 49–59.
6. Fekete, M. (1923). Über die Verteilung der Wurzeln bei gewissen algebraischen Gleichungen mit ganzzahligen Koeffizienten. *Mathematische Zeitschrift*, 17, 228–249.
7. Duminil-Copin, H., & Smirnov, S. (2012). The Connective Constant of the Honeycomb Lattice Equals $\sqrt{2+\sqrt2}$. *Annals of Mathematics*, 175(3), 1653–1665.

---
