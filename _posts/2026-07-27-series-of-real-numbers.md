---
layout: post
title: "실수 급수의 수렴"
date: 2026-07-27
---

## 급수와 그 수렴

**Definition (Series, Partial Sum).** Given a sequence of real numbers $$(a_n)_{n\ge1}$$, let $s_n := a_1+a_2+\cdots+a_n$ be its $n$-th partial sum. The series $\sum_{n=1}^\infty a_n$ *converges* if $(s_n)$ converges, and the limit is called the sum of the series; otherwise the series *diverges*.

**Proposition.** If $\sum a_n$ converges, then $a_n \to 0$.

*Proof.* $s_n \to L$이라 하면 $s_{n-1}\to L$이기도 하므로 $a_n = s_n-s_{n-1} \to L-L=0$이다. $\blacksquare$

이 조건은 충분조건은 아니다. 조화급수(harmonic series) $\sum 1/n$이 대표적인 반례다 — 항 $1/n$은 $0$으로 수렴하지만 급수 자체는 발산한다. 이 사실의 가장 오래된 증명은 14세기 프랑스의 스콜라 철학자 Nicole Oresme의 저작 *Quaestiones super Geometriam Euclidis* (약 1350~1360년경)까지 거슬러 올라간다 [6]. 항을 $2$의 거듭제곱 길이로 묶는 방식인데,

$$1+\frac12+\left(\frac13+\frac14\right)+\left(\frac15+\frac16+\frac17+\frac18\right)+\cdots$$

에서 괄호 안의 각 블록은 항상 $\dfrac12$ 이상이다 — 예를 들어 $\dfrac13+\dfrac14 > \dfrac14+\dfrac14=\dfrac12$이고, $\dfrac15+\cdots+\dfrac18 > 4\cdot\dfrac18=\dfrac12$이다. 이런 블록이 무한히 이어지므로 부분합은 한계 없이 커진다. 이 증명은 17세기에 Mengoli와 Jacob Bernoulli가 각각 독립적으로 재발견했다 [7, 8].

## 절대수렴과 조건수렴

**Definition (Absolute and Conditional Convergence).** $\sum a_n$ is *absolutely convergent* if $\sum \vert a_n\vert$ converges. If $\sum a_n$ converges but $\sum\vert a_n\vert$ diverges, $\sum a_n$ is *conditionally convergent*.

**Theorem.** If $\sum a_n$ is absolutely convergent, then $\sum a_n$ converges.

*Proof.* $p_n := \max(a_n,0)$, $q_n:=\max(-a_n,0)$이라 하면 $a_n=p_n-q_n$, $\vert a_n\vert=p_n+q_n$이고 $0\le p_n,q_n\le\vert a_n\vert$이다. $\sum\vert a_n\vert$이 수렴한다고 가정하면, $\sum p_n$과 $\sum q_n$의 부분합은 각각 단조증가하면서 $\sum\vert a_n\vert$의 부분합(수렴하므로 유계)에 의해 위로 유계이므로, 지난 글의 Monotone Convergence Theorem에 의해 둘 다 수렴한다. 따라서 $\sum a_n = \sum p_n - \sum q_n$도 두 수렴하는 수열의 차이이므로 수렴한다. $\blacksquare$

역은 성립하지 않는다 — 대표적인 예가 교대조화급수(alternating harmonic series) $\sum (-1)^{n+1}/n = 1-\frac12+\frac13-\frac14+\cdots$다. $\sum 1/n$이 발산하므로 절대수렴하지는 않지만, 다음과 같이 정확한 수렴값을 직접 계산할 수 있다.

**Proposition.** $\displaystyle\sum_{n=1}^\infty \frac{(-1)^{n+1}}{n} = \ln 2$.

*Proof.* $t\ne-1$인 임의의 실수 $t$와 자연수 $n$에 대해

$$\frac{1}{1+t} = \sum_{k=0}^{n-1}(-t)^k + \frac{(-t)^n}{1+t}$$

이 성립한다 (우변에 $1+t$를 곱하면 가운데 항들이 telescoping되어 좌변과 같아짐을 바로 확인할 수 있다). 양변을 $t=0$부터 $t=1$까지 적분하면

$$\ln2 = \int_0^1 \frac{dt}{1+t} = \sum_{k=0}^{n-1}\frac{(-1)^k}{k+1} + \int_0^1 \frac{(-t)^n}{1+t}\,dt = s_n + R_n$$

인데, 여기서 $s_n:=\sum_{k=1}^n \dfrac{(-1)^{k+1}}{k}$은 교대조화급수의 $n$번째 부분합이고 $R_n:=\int_0^1 \dfrac{(-t)^n}{1+t}\,dt$이다. $0\le t\le1$에서 $\left\vert(-t)^n/(1+t)\right\vert \le t^n$이므로 $\vert R_n\vert \le \int_0^1 t^n\,dt = \dfrac1{n+1}\to0$이다. 따라서 $s_n = \ln2-R_n \to \ln2$이다. $\blacksquare$

절대수렴과 조건수렴의 흥미로운 차이는 재배열(rearrangement, 항을 더하는 순서를 바꾸는 것)에 대해 수렴값이 안정적인지에 있다. 절대수렴하는 급수는 재배열해도 수렴값이 달라지지 않는다.

**Theorem.** Let $\sum a_n$ be absolutely convergent with sum $S$. Then for every permutation $\sigma:\mathbb{N}\to\mathbb{N}$, the rearranged series $\sum a_{\sigma(n)}$ also converges, to the same sum $S$.

*Proof.* $\varepsilon>0$이 주어졌다 하자. $\sum\vert a_n\vert$이 수렴하므로 그 나머지항은 $0$으로 수렴하니, 어떤 $N$이 있어 $\sum_{n>N}\vert a_n\vert<\varepsilon$이다. $\sigma$가 전단사이므로 $1,\ldots,N$은 모두 $\sigma(1),\ldots,\sigma(M)$ 중 어딘가에 나타나는 $M$(예를 들어 $$M:=\max\{\sigma^{-1}(1),\ldots,\sigma^{-1}(N)\}$$)이 존재한다. $m\ge M$이면 $$\{\sigma(1),\ldots,\sigma(m)\}\supseteq\{1,\ldots,N\}$$이므로

$$\sum_{k=1}^m a_{\sigma(k)} - \sum_{n=1}^N a_n = \sum_{j\,\in\,\{\sigma(1),\ldots,\sigma(m)\}\setminus\{1,\ldots,N\}} a_j$$

인데, 우변은 지표가 모두 $N$보다 큰 유한 개의 항의 합이므로 그 절댓값은 $\sum_{n>N}\vert a_n\vert$ 이하, 즉 $\varepsilon$ 미만이다. 한편 $\left\vert S-\sum_{n=1}^N a_n\right\vert = \left\vert\sum_{n>N}a_n\right\vert \le \sum_{n>N}\vert a_n\vert<\varepsilon$이므로, 삼각부등식에 의해 모든 $m\ge M$에 대해

$$\left\vert\sum_{k=1}^m a_{\sigma(k)} - S\right\vert < 2\varepsilon$$

이다. $\varepsilon>0$이 임의였으므로 $\sum a_{\sigma(n)} \to S$. $\blacksquare$

이와 달리 조건수렴하는 급수는 재배열하면 다른 값에 수렴해버린다. 교대조화급수의 항을 양수 항 한 개, 음수 항 두 개씩을 번갈아 묶는 재배열을 생각해보자:

$$1-\frac12-\frac14+\frac13-\frac16-\frac18+\frac15-\frac1{10}-\frac1{12}+\cdots$$

**Proposition.** 위 재배열은 $\dfrac12\ln2$로 수렴한다.

*Proof.* $H_n := \sum_{k=1}^n \dfrac1k$이라 하자. 위 재배열의 $m$번째 블록까지의 부분합을

$$T_m := \sum_{j=1}^m\left(\frac1{2j-1}-\frac1{4j-2}-\frac1{4j}\right)$$

이라 하면, $\dfrac1{4j-2}+\dfrac1{4j} = \dfrac12\left(\dfrac1{2j-1}+\dfrac1{2j}\right)$이므로

$$T_m = \sum_{j=1}^m\frac1{2j-1} - \frac12\sum_{j=1}^m\left(\frac1{2j-1}+\frac1{2j}\right) = \frac12\sum_{j=1}^m\frac1{2j-1} - \frac12\sum_{j=1}^m\frac1{2j}$$

이다. $O_m:=\sum_{j=1}^m\frac1{2j-1}$(처음 $m$개 홀수 역수의 합), $E_m:=\sum_{j=1}^m\frac1{2j}=\frac12H_m$(처음 $m$개 짝수 역수의 합)이라 하면 $O_m+E_m=H_{2m}$이므로 $O_m=H_{2m}-\frac12H_m$이고, 따라서

$$T_m = \frac12(O_m-E_m) = \frac12\left(H_{2m}-\frac12H_m-\frac12H_m\right) = \frac12\big(H_{2m}-H_m\big) = \frac12 s_{2m}$$

이다 (마지막 등호는 앞의 Proposition의 증명에서 보인 $s_{2n}=H_{2n}-H_n$을 $n=m$에 대입한 것). $s_{2m}\to\ln2$이므로 $T_m \to \dfrac12\ln2$이다. 블록 안에서 실제로 더해지는 항 $\frac1{2j-1},\frac1{4j-2},\frac1{4j}$은 모두 $0$으로 수렴하므로, 블록 경계 사이의 중간 부분합들도 같은 값 $\dfrac12\ln2$로 수렴한다. $\blacksquare$

심지어 재배열 방식을 어떻게 조작하느냐에 따라 원하는 어떤 값으로도 수렴하게, 또는 아예 발산하도록도 만들 수 있다는 정리가 Riemann이 1854년에 쓴 교수자격논문(Habilitationsschrift) *Über die Darstellbarkeit einer Function durch eine trigonometrische Reihe*에 실려 있다. 정작 이 논문은 Riemann 사후인 1867년(또는 1868년으로 표기되기도 한다)에야 Dedekind의 편집으로 출판되었다 [5].

**Theorem (Riemann's Rearrangement Theorem).** Let $\sum a_n$ be a conditionally convergent series of real numbers. For any $$s\in\mathbb{R}\cup\{-\infty,\infty\}$$, there exists a permutation $\sigma:\mathbb{N}\to\mathbb{N}$ such that the rearranged series $\sum a_{\sigma(n)}$ converges to $s$. There also exists a rearrangement along which the partial sums converge to no value at all, oscillating instead.

*Proof (아이디어).* 앞의 정리 증명에서 쓴 $p_n=\max(a_n,0)$, $q_n=\max(-a_n,0)$을 다시 쓰자. $\sum a_n$이 조건수렴하므로 $\sum\vert a_n\vert=\sum(p_n+q_n)$은 발산하는데, 만약 $\sum p_n$, $\sum q_n$ 둘 다 수렴한다면 그 합인 $\sum(p_n+q_n)$도 수렴해야 하므로 모순이고, 둘 중 하나만 발산한다면 $\sum a_n=\sum p_n-\sum q_n$ 자체가 발산(또는 $\pm\infty$로 발산)해야 하므로 이 역시 모순이다. 따라서 $\sum p_n$, $\sum q_n$은 (0이 아닌 항들만 모으면) 둘 다 $+\infty$로 발산한다.

이제 목표값 $s$를 향해 다음을 반복한다: 현재 부분합이 $s$보다 작으면 (아직 쓰지 않은) 양수 항 $p_n$들을 순서대로 더해 부분합이 $s$를 넘을 때까지 더하고, $s$보다 크면 음수 항 $-q_n$들을 순서대로 더해 부분합이 $s$ 아래로 내려갈 때까지 더한다. $\sum p_n$과 $\sum q_n$이 둘 다 $\infty$로 발산하므로 이 과정은 무한히 반복 가능하고, 원래 급수의 모든 항이 결국 한 번씩은 다 쓰인다. $a_n\to0$이므로 (수렴하는 급수의 필요조건) 방향을 바꿀 때마다 $s$를 넘거나 못 미치는 정도(overshoot)는 $0$으로 줄어들므로, 이렇게 재배열한 급수의 부분합은 $s$로 수렴한다. $s=\pm\infty$이거나 진동하도록 만드는 것도 같은 방식으로 목표를 "계속 커지게" 또는 "번갈아 크게 작게" 잡으면 된다. $\blacksquare$

## $p$-Series Test

앞서 조화급수의 발산을 보일 때 썼던 논증(항을 $2$의 거듭제곱 길이 블록으로 묶기)을 일반화하면, $\sum 1/n^p$의 수렴성은 물론 감소하는 음이 아닌 수열이라면 무엇에든 적용할 수 있는 일반적인 도구를 얻는다.

**Theorem (Cauchy Condensation Test [1]).** Let $$(a_n)_{n\ge1}$$ be a decreasing sequence of nonnegative real numbers. Then $\displaystyle\sum_{n=1}^\infty a_n$ converges if and only if $\displaystyle\sum_{k=0}^\infty 2^k a_{2^k}$ converges.

*Proof.* Oresme의 블록 묶기와 같은 방식으로, $k=0,1,2,\ldots$에 대해 $n$이 $2^k\le n\le2^{k+1}-1$ 범위(길이 $2^k$인 블록)에 있는 항들을 묶자. $(a_n)$이 감소하므로 블록의 첫 항은 $a_{2^k}$, 마지막 항은 $a_{2^{k+1}-1}\ge a_{2^{k+1}}$이고 블록 안 모든 항이 그 사이에 있으므로

$$2^k a_{2^{k+1}} \le \sum_{n=2^k}^{2^{k+1}-1} a_n \le 2^k a_{2^k}$$

이다. $S_N:=\sum_{n=1}^N a_n$, $C_K:=\sum_{k=0}^K 2^ka_{2^k}$이라 하고 위 부등식을 $k=0,\ldots,K$에 대해 더하면, 왼쪽은 $\sum_{k=0}^K 2^ka_{2^{k+1}} = \frac12\sum_{k=0}^K 2^{k+1}a_{2^{k+1}} = \frac12(C_{K+1}-a_1)$이 되고 오른쪽은 정확히 $C_K$가 되며, 가운데는 블록들을 모두 합친 $S_{2^{K+1}-1}$이 되어

$$\frac12\big(C_{K+1}-a_1\big) \le S_{2^{K+1}-1} \le C_K$$

를 얻는다.

($\Rightarrow$) $\sum a_n$이 수렴하면 $(S_N)$이 어떤 $S$로 유계이므로, 왼쪽 부등식에 의해 모든 $K$에서 $C_{K+1}\le 2S+a_1$이 되어 $(C_K)$도 위로 유계다. $(C_K)$는 단조증가하므로 지난 글의 Monotone Convergence Theorem에 의해 $\sum 2^ka_{2^k}$도 수렴한다.

($\Leftarrow$) $\sum 2^ka_{2^k}$가 어떤 $C$로 수렴하면, 오른쪽 부등식에 의해 $S_{2^{K+1}-1}\le C_K\le C$이다. $(S_N)$은 단조증가하므로, 임의의 $N$에 대해 $2^{K+1}-1\ge N$인 $K$를 잡으면 $S_N\le S_{2^{K+1}-1}\le C$가 되어 $(S_N)$ 전체가 위로 유계다. Monotone Convergence Theorem에 의해 $\sum a_n$도 수렴한다. $\blacksquare$

**Corollary ($p$-Series).** $\displaystyle\sum_{n=1}^\infty \frac{1}{n^p}$ converges if $p>1$, and diverges if $p\le1$.

*Proof.* $p\le0$이면 $n^p=n^{-\vert p\vert}\le1$이므로 $\dfrac1{n^p}\ge1$이 되어 $a_n\not\to0$이고, 급수 수렴의 필요조건에 의해 발산한다.

$p>0$이면 $a_n:=1/n^p$은 감소하고 음이 아니므로 Cauchy Condensation Test를 적용할 수 있다:

$$\sum_{k=0}^\infty 2^k a_{2^k} = \sum_{k=0}^\infty 2^k\cdot\frac1{(2^k)^p} = \sum_{k=0}^\infty \left(2^{1-p}\right)^k$$

는 공비 $r:=2^{1-p}>0$인 등비급수이므로, $r<1$(즉 $p>1$)이면 수렴하고 $r\ge1$(즉 $0<p\le1$)이면 발산한다. Cauchy Condensation Test에 의해 원래 급수 $\sum 1/n^p$도 정확히 같은 조건에서 수렴·발산한다. $p\le0$인 경우와 합치면, $\sum 1/n^p$은 $p>1$이면 수렴하고 $p\le1$이면 발산한다. $\blacksquare$

## 비율판정법과 거듭제곱근판정법

절대수렴을 판정하는 가장 널리 쓰이는 두 도구를 보자.

**Lemma (Comparison Test).** If $0\le a_n\le b_n$ for all $n$ and $\sum b_n$ converges, then $\sum a_n$ converges.

*Proof.* $\sum a_n$의 부분합은 단조증가하고, $\sum b_n$의 부분합(수렴하므로 유계)에 의해 위로 유계이므로 Monotone Convergence Theorem에 의해 수렴한다. $\blacksquare$

**Theorem (Ratio Test [2]).** Let $(a_n)$ be a sequence of nonzero real numbers.

(i) If $\limsup_n \left\vert\dfrac{a_{n+1}}{a_n}\right\vert < 1$, then $\sum a_n$ is absolutely convergent.

(ii) If $\liminf_n \left\vert\dfrac{a_{n+1}}{a_n}\right\vert > 1$, then $\sum a_n$ diverges.

*Proof.* (i) $\limsup\vert a_{n+1}/a_n\vert < r < 1$인 $r$을 잡으면, limsup의 정의에 의해 어떤 $N$이 있어 $n\ge N$이면 $\vert a_{n+1}/a_n\vert < r$이다. $n>N$에 대해 telescoping하면 $\vert a_n\vert < \vert a_N\vert r^{n-N}$이고, $\sum r^{n-N}$은 $0<r<1$인 등비급수이므로 수렴하니 비교판정법에 의해 $\sum\vert a_n\vert$도 수렴한다.

(ii) $\liminf\vert a_{n+1}/a_n\vert > 1$이면 어떤 $N$이 있어 $n\ge N$일 때 $\vert a_{n+1}/a_n\vert > 1$, 즉 $\vert a_n\vert$은 $n\ge N$부터 strictly increasing이다. 특히 모든 $n\ge N$에 대해 $\vert a_n\vert \ge \vert a_N\vert > 0$이므로 $a_n\not\to0$이고, 수렴의 필요조건에 의해 $\sum a_n$은 발산한다. $\blacksquare$

**Theorem (Root Test [1]).** Let $(a_n)$ be a real sequence and $L:=\limsup_n \vert a_n\vert^{1/n}$.

(i) If $L<1$, then $\sum a_n$ is absolutely convergent.

(ii) If $L>1$, then $\sum a_n$ diverges.

(iii) If $L=1$, the test is inconclusive.

*Proof.* (i) $L<r<1$인 $r$을 잡으면 어떤 $N$이 있어 $n\ge N$이면 $\vert a_n\vert^{1/n}<r$, 즉 $\vert a_n\vert<r^n$이다. $\sum r^n$이 수렴하므로 비교판정법에 의해 $\sum\vert a_n\vert$도 수렴한다.

(ii) $L>1$이면, 지난 글에서 보인 대로 $\limsup$은 항상 어떤 부분수열의 극한으로 실현되므로, $\vert a_{n_k}\vert^{1/n_k}\to L>1$인 부분수열이 있다. 충분히 큰 $k$에 대해 $\vert a_{n_k}\vert^{1/n_k}>1$, 즉 $\vert a_{n_k}\vert>1$이므로 $a_n\not\to0$이고, 급수는 발산한다.

(iii) $\sum 1/n$과 $\sum 1/n^2$은 둘 다 $L=1$이지만 각각 발산·수렴한다. $\blacksquare$

두 판정법을 나란히 놓고 보면 자연스러운 질문이 생긴다 — 둘 중 어느 쪽이 더 강력한가?

**Corollary.** Whenever the Ratio Test determines convergence or divergence, the Root Test reaches the same conclusion — i.e., the Root Test is at least as strong.

*Proof.* 지난 글의 Lemma를 $b_n:=\vert a_n\vert$에 적용하면

$$\liminf_n \frac{\vert a_{n+1}\vert}{\vert a_n\vert} \le \liminf_n \vert a_n\vert^{1/n} \le \limsup_n \vert a_n\vert^{1/n} \le \limsup_n \frac{\vert a_{n+1}\vert}{\vert a_n\vert}$$

을 얻는다. 비율판정법이 수렴을 판정한다면($\limsup\vert a_{n+1}/a_n\vert<1$) 위 부등식의 가장 오른쪽이 $1$보다 작으므로 $\limsup\vert a_n\vert^{1/n}<1$도 성립해 거듭제곱근판정법도 수렴을 판정한다. 비율판정법이 발산을 판정한다면($\liminf\vert a_{n+1}/a_n\vert>1$) 가장 왼쪽이 $1$보다 크므로 $\liminf\vert a_n\vert^{1/n}>1$, 따라서 $\limsup\vert a_n\vert^{1/n}\ge\liminf\vert a_n\vert^{1/n}>1$이 되어 거듭제곱근판정법도 발산을 판정한다. $\blacksquare$

역은 성립하지 않는다 — 거듭제곱근판정법은 판정 가능한데 비율판정법은 완전히 무력한 경우가 있다. $a_n := 1/2^k$ ($n=2k-1$, 홀수항)와 $a_n:=1/3^k$ ($n=2k$, 짝수항)로 정의된 수열, 즉

$$\frac12+\frac13+\frac1{2^2}+\frac1{3^2}+\frac1{2^3}+\frac1{3^3}+\cdots$$

을 생각해보자. 짝수항에서는 $a_n^{1/n}=(1/3^k)^{1/2k}=1/\sqrt3$로 정확히 일정하고, 홀수항에서는 $a_n^{1/n}=(1/2^k)^{1/(2k-1)}\to1/\sqrt2$이므로, $\limsup a_n^{1/n}=1/\sqrt2<1$이 되어 거듭제곱근판정법에 의해 이 급수는 절대수렴한다. 반면 비율은

$$\frac{a_{2k}}{a_{2k-1}} = \left(\frac23\right)^k \to 0, \qquad \frac{a_{2k+1}}{a_{2k}} = \frac{3^k}{2^{k+1}} \to \infty$$

로 번갈아 진동하므로 $\liminf\vert a_{n+1}/a_n\vert=0$, $\limsup\vert a_{n+1}/a_n\vert=\infty$가 되어 비율판정법은 이 급수에 대해 아무 정보도 주지 못한다.

## Summation by Parts

이제 절대수렴하지 않는 급수의 수렴을 다루는 대표적인 도구를 보자. 유한합에 대한 부분적분(integration by parts)의 이산 버전이라 할 만하다.

**Lemma (Summation by Parts, Abel's Transformation [3]).** For sequences $(a_n)$, $(b_n)$ and $B_n:=b_1+\cdots+b_n$ (with $B_0:=0$),

$$\sum_{k=1}^n a_k b_k = a_n B_n + \sum_{k=1}^{n-1}(a_k-a_{k+1})B_k.$$

*Proof.* $b_k=B_k-B_{k-1}$이므로

$$\sum_{k=1}^n a_kb_k = \sum_{k=1}^n a_k(B_k-B_{k-1}) = \sum_{k=1}^n a_kB_k - \sum_{k=1}^n a_kB_{k-1}.$$

두 번째 합에서 $j=k-1$로 치환하면 $\sum_{k=1}^n a_kB_{k-1}=\sum_{j=0}^{n-1}a_{j+1}B_j = \sum_{j=1}^{n-1}a_{j+1}B_j$ ($B_0=0$이므로 $j=0$ 항은 사라진다)이고, 이를 대입해 정리하면 원하는 식을 얻는다. $\blacksquare$

이 항등식을 발산할 수도 있는 $b_n$과, $0$으로 줄어드는 $a_n$을 짝지을 때 쓰면 다음 판정법이 나온다.

**Theorem (Dirichlet's Test [4]).** Let $(b_n)$ have bounded partial sums $B_n:=\sum_{k=1}^n b_k$ (i.e. $\vert B_n\vert\le M$ for all $n$, for some $M$), and let $(a_n)$ be monotonically decreasing with $a_n\to0$. Then $\sum a_nb_n$ converges.

*Proof.* Summation by Parts에 의해 $\sum_{k=1}^n a_kb_k = a_nB_n + \sum_{k=1}^{n-1}(a_k-a_{k+1})B_k$이다. $a_n\to0$이고 $\vert B_n\vert\le M$이므로 $a_nB_n\to0$이다. 한편 $(a_n)$이 단조감소하므로 $a_k-a_{k+1}\ge0$이고 $\vert(a_k-a_{k+1})B_k\vert\le M(a_k-a_{k+1})$인데, $\sum_{k=1}^{n-1}M(a_k-a_{k+1})=M(a_1-a_n)\to Ma_1$로 수렴(telescoping)하므로 비교판정법에 의해 $\sum(a_k-a_{k+1})B_k$는 절대수렴한다. 두 수렴하는 항의 합이므로 $\sum a_kb_k$도 수렴한다. $\blacksquare$

**Corollary (Alternating Series Test / Leibniz's Test).** If $(c_n)$ satisfies $c_n\ge0$, is monotonically decreasing, and $c_n\to0$, then $\sum(-1)^{n+1}c_n$ converges.

*Proof.* $a_n:=c_n$, $b_n:=(-1)^{n+1}$로 두면 $$B_n\in\{0,1\}$$이므로 유계이고, Dirichlet's Test에 의해 바로 따라온다. $\blacksquare$

Dirichlet's Test의 진짜 힘은 $b_n$이 부호를 규칙적으로 바꾸지 않는 경우에도 통한다는 데 있다. 예를 들어 임의의 $\theta\in\mathbb{R}$에 대해 $\sum_{n=1}^\infty \dfrac{\sin(n\theta)}{n}$이 수렴함을 보이자. $\theta \equiv 0 \pmod{2\pi}$이면 모든 항이 $0$이라 자명하므로, $\theta\not\equiv0\pmod{2\pi}$인 경우만 보면 된다. 곱을 합으로 바꾸는 항등식 $2\sin(\theta/2)\sin(k\theta)=\cos\big((k-\tfrac12)\theta\big)-\cos\big((k+\tfrac12)\theta\big)$을 $k=1,\ldots,n$에 대해 더하면 telescoping에 의해

$$2\sin(\theta/2)\sum_{k=1}^n \sin(k\theta) = \cos(\theta/2)-\cos\big((n+\tfrac12)\theta\big)$$

이고, 우변의 절댓값은 $2$ 이하이므로

$$\left\vert\sum_{k=1}^n \sin(k\theta)\right\vert \le \frac{1}{\vert\sin(\theta/2)\vert}$$

로 부분합이 유계임을 알 수 있다. $a_n=1/n$은 단조감소하며 $0$으로 수렴하므로, Dirichlet's Test에 의해 $\sum \sin(n\theta)/n$은 (모든 실수 $\theta$에 대해) 수렴한다. 이 급수는 대부분의 $\theta$에서 절대수렴하지 않으므로 — $\vert\sin(n\theta)\vert$는 평균적으로 $0$에서 멀리 떨어져 있어 $\sum\vert\sin(n\theta)\vert/n$은 조화급수처럼 발산한다 — 비율판정법이나 거듭제곱근판정법으로는 손댈 수 없는, summation by parts가 아니면 잡아내기 어려운 결과다.

## 참고문헌

1. Cauchy, A.-L. (1821). *Cours d'analyse de l'École royale polytechnique; I.re Partie. Analyse algébrique*. Chapitre VI. Paris: Imprimerie Royale.
2. d'Alembert, J. (1768). *Opuscules mathématiques, ou Mémoires sur différens sujets de géométrie, de méchanique, d'optique, d'astronomie*.
3. Abel, N. H. (1826). Untersuchungen über die Reihe $1+\frac{m}{1}x+\cdots$. *Journal für die reine und angewandte Mathematik*, 1, 311–339.
4. Dirichlet, P. G. L. (1862). Démonstration d'un théorème d'Abel. *Journal de Mathématiques Pures et Appliquées*, Series 2, 7, 253–255.
5. Riemann, B. (1867/1868, 집필은 1854). Über die Darstellbarkeit einer Function durch eine trigonometrische Reihe. *Abhandlungen der Königlichen Gesellschaft der Wissenschaften zu Göttingen*, 13.
6. Oresme, N. (c. 1350–1360). *Quaestiones super Geometriam Euclidis*.
7. Mengoli, P. (1650). *Novae quadraturae arithmeticae, seu de additione fractionum*. Bologna.
8. Bernoulli, Jacob (1689). *Tractatus de seriebus infinitis*.
