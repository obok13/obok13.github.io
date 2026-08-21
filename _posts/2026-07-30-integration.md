---
layout: post
title: "실수 함수의 적분"
date: 2026-07-30
mathematicians: [Riemann, Darboux, Lebesgue, Lipschitz, Leibniz, Cauchy, Heine, Cantor, Barrow, Vitali, Newton, Froda]
---

## Riemann 적분

**Definition (Partition).** A *partition* $P$ of $[a,b]$ is a finite set of points $a=x_0<x_1<\cdots<x_n=b$. Write $\Delta x_i := x_i-x_{i-1}$.

**Definition (Riemann Sum, Mesh).** For a partition $$P=\{x_0,\ldots,x_n\}$$ and *tags* $t_i\in[x_{i-1},x_i]$, the *Riemann sum* is $S(f,P,(t_i)):=\sum_{i=1}^n f(t_i)\Delta x_i$. The *mesh* of $P$ is $\Vert P\Vert:=\max_i \Delta x_i$.

**Definition (Riemann Integrability [1]).** $f$ is *Riemann integrable* on $[a,b]$ with integral $I$ if for every $\varepsilon>0$ there exists $\delta>0$ such that, for every partition $P$ with $\Vert P\Vert<\delta$ and every choice of tags $(t_i)$, $\vert S(f,P,(t_i))-I\vert<\varepsilon$.

이 정의는 모든 partition과 모든 tag 선택에 대해 성립해야 하는 형태라 그대로 다루기는 번거롭다. 아래에서 이를 다루기 쉬운 형태로 재정리한 것이 Darboux 적분이다.

## Darboux 적분

**Definition (Upper/Lower Darboux Sums).** Let $f:[a,b]\to\mathbb{R}$ be bounded and $$P=\{x_0,\ldots,x_n\}$$ a partition. With $M_i:=\sup_{[x_{i-1},x_i]}f$ and $m_i:=\inf_{[x_{i-1},x_i]}f$,

$$U(f,P):=\sum_{i=1}^n M_i\,\Delta x_i, \qquad L(f,P):=\sum_{i=1}^n m_i\,\Delta x_i.$$

**Lemma (세분, Refinement).** If $P'\supseteq P$ (즉 $P'$이 $P$의 점을 모두 포함하는 세분), then $L(f,P)\le L(f,P')\le U(f,P')\le U(f,P)$.

*Proof.* $P'$이 $P$에 점 하나($x_{i-1}<z<x_i$)를 추가한 경우만 보이면 충분하다(일반적인 세분은 이를 반복 적용한 것이다). $[x_{i-1},x_i]$가 $[x_{i-1},z]$와 $[z,x_i]$로 나뉘면, 각 조각의 sup은 $M_i$ 이하이므로 $M_i\Delta x_i$가 그 두 조각의 상합 기여분의 합 이상이 되어 $U(f,P')\le U(f,P)$이다. $L$도 대칭적으로 $L(f,P)\le L(f,P')$이다. $L(f,P')\le U(f,P')$는 각 소구간에서 $m_i\le M_i$이므로 자명하다. $\blacksquare$

**Corollary.** For any two partitions $P_1,P_2$ of $[a,b]$, $L(f,P_1)\le U(f,P_2)$.

*Proof.* $P_1\cup P_2$는 둘 다의 세분이므로, $L(f,P_1)\le L(f,P_1\cup P_2)\le U(f,P_1\cup P_2)\le U(f,P_2)$이다. $\blacksquare$

**Definition (Upper/Lower Integral, Darboux Integrability [2]).**

$$\overline{\int_a^b} f := \inf_P U(f,P), \qquad \underline{\int_a^b} f := \sup_P L(f,P)$$

위 Corollary에 의해 $\underline{\int_a^b} f \le \overline{\int_a^b} f$이다. 등호가 성립할 때 $f$가 $[a,b]$에서 *Darboux 적분가능*하다고 하고, 그 공통값을 $\int_a^b f$로 쓴다.

**Theorem (적분가능성 판정).** A bounded $f:[a,b]\to\mathbb{R}$ is Darboux integrable if and only if, for every $\varepsilon>0$, there exists a partition $P$ such that $U(f,P)-L(f,P)<\varepsilon$.

*Proof.* ($\Leftarrow$) 모든 $\varepsilon>0$에 대해 $U(f,P)-L(f,P)<\varepsilon$인 $P$가 있으면, $0\le\overline{\int}f-\underline{\int}f \le U(f,P)-L(f,P)<\varepsilon$이므로 (임의의 $\varepsilon$에 대해 성립하니) $\overline{\int}f=\underline{\int}f$이다.

($\Rightarrow$) $\overline{\int}f=\underline{\int}f=:I$라 하자. $\varepsilon>0$이 주어지면, $\inf$, $\sup$의 정의에 의해 $U(f,P_1)<I+\varepsilon/2$인 $P_1$과 $L(f,P_2)>I-\varepsilon/2$인 $P_2$가 존재한다. $P:=P_1\cup P_2$라 하면, Refinement Lemma에 의해 $U(f,P)\le U(f,P_1)<I+\varepsilon/2$이고 $L(f,P)\ge L(f,P_2)>I-\varepsilon/2$이므로 $U(f,P)-L(f,P)<\varepsilon$이다. $\blacksquare$

위 Theorem은 Riemann's Criterion 혹은 Cauchy's Criterion이라는 이름으로 알려져 있다.

**Theorem.** $f$ is Riemann integrable on $[a,b]$ with integral $I$ if and only if $f$ is bounded and Darboux integrable on $[a,b]$ with $\int_a^b f = I$.

*Proof.* ($\Leftarrow$) $f$가 유계이고 Darboux 적분가능하다 하자 ($\int_a^b f=I$). $\varepsilon>0$이 주어지면, 적분가능성 판정에 의해 $U(f,P_0)-L(f,P_0)<\varepsilon/2$인 partition $$P_0=\{y_0,\ldots,y_m\}$$이 존재한다. $K:=\sup_{[a,b]}\vert f\vert$라 하고 $\delta:=\dfrac{\varepsilon}{8mK+1}$로 두자 (분모에 $1$을 더해 $K=0$인 경우도 처리한다). $\Vert P\Vert<\delta$인 임의의 partition $P$에 대해, $P\cup P_0$는 $P$에 (많아야) $P_0$의 내부점 $m-1$개를 추가한 세분인데, 점 하나를 추가할 때마다 상합·하합이 각각 최대 $2K\Vert P\Vert$만큼만 바뀌므로

$$U(f,P) \le U(f,P\cup P_0) + 2K(m-1)\Vert P\Vert \le U(f,P_0) + 2K(m-1)\delta < I+\frac{\varepsilon}2+\frac{\varepsilon}4 < I+\varepsilon$$

이고 (Refinement Lemma로 $U(f,P\cup P_0)\le U(f,P_0)<L(f,P_0)+\varepsilon/2\le I+\varepsilon/2$을 썼다), 대칭적으로 $L(f,P)>I-\varepsilon$이다. 임의의 tag 선택에 대해 $L(f,P)\le S(f,P,(t_i))\le U(f,P)$이므로 $\vert S(f,P,(t_i))-I\vert<\varepsilon$이다.

($\Rightarrow$) $f$가 Riemann 적분가능하다 하자 ($\int_a^b f=I$가 되도록). 먼저 $f$가 유계임을 보이자. 그렇지 않다면, $\varepsilon=1$에 대응하는 $\delta$를 잡고 mesh가 $\delta$ 미만인 partition $P$를 하나 고정하면, $f$가 $[a,b]$에서 유계가 아니므로 어떤 소구간 $[x_{k-1},x_k]$에서 유계가 아니다. 다른 소구간의 tag는 고정하고 $t_k$만 그 소구간 안에서 움직이면 $\vert f(t_k)\vert$를 얼마든지 크게 만들 수 있어 $S(f,P,(t_i))$가 $I$ 근방 $\varepsilon=1$ 안에 머무를 수 없다. 모순이다. 따라서 $f$는 유계다.

이제 $\varepsilon>0$에 대응하는 $\delta$를 잡고, mesh가 $\delta$ 미만인 partition $P$를 하나 고정하자. 각 $i$에 대해 $t_i$를 $[x_{i-1},x_i]$ 안에서 $f(t_i)>M_i-\eta/(b-a)$가 되도록 잡을 수 있으므로 ($\eta>0$ 임의), $\sup$을 tag에 대해 취하면 $\sup_{(t_i)} S(f,P,(t_i)) = U(f,P)$이고 대칭적으로 $\inf_{(t_i)}S(f,P,(t_i))=L(f,P)$이다. 모든 tag에서 $\vert S(f,P,(t_i))-I\vert<\varepsilon$이므로, sup, inf를 취하면 $U(f,P)\le I+\varepsilon$, $L(f,P)\ge I-\varepsilon$이 되어 $U(f,P)-L(f,P)\le2\varepsilon$이다. 적분가능성 판정에 의해 $f$는 Darboux 적분가능하고, $L(f,P)\le\underline{\int}f\le\overline{\int}f\le U(f,P)$가 둘 다 $I$와의 차이가 $2\varepsilon$ 이하이므로, $\varepsilon\to0$으로 보내면 $\int_a^b f=I$이다. $\blacksquare$

즉 "Riemann 적분"이 원조이고, "Darboux 적분"은 그것을 다루기 쉽게 재정리한 (그리고 결국 동치임이 밝혀진) 버전이다. 이 동치성 덕분에 교과서에는 Riemann 적분과 Darboux 적분의 구분이 없는 경우가 많다.

한편, Riemann sum 버전의 적분가능성 판정법도 있다.

**Corollary (적분가능성 판정, Riemann sum 버전).** A bounded $f:[a,b]\to\mathbb{R}$ is integrable if and only if, for every $\varepsilon>0$, there exists $\delta>0$ such that for any two partitions $P,P'$ with $\Vert P\Vert,\Vert P'\Vert<\delta$ and any choice of tags, $\vert S(f,P,(t_i)) - S(f,P',(t_i'))\vert<\varepsilon$.

*Proof.* ($\Rightarrow$) $f$가 적분가능하다면(적분값 $I$) $\varepsilon/2$에 대응하는 $\delta$가 있어 mesh$<\delta$인 모든 partition·tag에서 $\vert S-I\vert<\varepsilon/2$이므로, 삼각부등식에 의해 그런 두 Riemann sum의 차는 $\varepsilon$ 미만이다.

($\Leftarrow$) 조건이 성립한다 하자. 먼저 $f$가 유계임을 보이자. 그렇지 않다면 mesh$<\delta$인 partition을 하나 고정하고 (Riemann 적분의 정의를 증명할 때와 같은 논증으로) 유계가 아닌 소구간의 tag만 움직여 같은 partition에서 나온 두 Riemann sum의 차를 임의로 크게 만들 수 있어 모순이다. 이제 mesh$<\delta$인 partition $P$를 하나 고정하면, 앞서 본 대로 $\sup_{(t_i)}S(f,P,(t_i))=U(f,P)$이고 $\inf_{(t_i)}S(f,P,(t_i))=L(f,P)$인데, $P=P'$로 두고 tag만 바꾼 경우에도 가정이 적용되므로 $U(f,P)-L(f,P)\le\varepsilon$이다. 적분가능성 판정에 의해 $f$는 (Darboux, 그러므로 Riemann) 적분가능하다. $\blacksquare$

## 적분 가능한 함수들

**Theorem.** If $f$ is continuous on $[a,b]$, then $f$ is Darboux integrable.

*Proof.* Heine–Cantor Theorem에 의해 $f$는 $[a,b]$에서 균등연속이다. $\varepsilon>0$이 주어지면, 어떤 $\delta>0$이 있어 $\vert x-y\vert<\delta$이면 $\vert f(x)-f(y)\vert<\dfrac{\varepsilon}{b-a}$이다. 소구간의 길이가 모두 $\delta$보다 작은 partition $P$를 하나 잡으면(예: $n$을 $\dfrac{b-a}{n}<\delta$이도록 크게 잡고 $n$등분), 각 소구간 $[x_{i-1},x_i]$은 (Extreme Value Theorem에 의해 $f$가 그 위에서 최댓값·최솟값을 가지며, 두 값을 내는 점 사이의 거리가 $\delta$ 미만이므로) $M_i-m_i<\dfrac{\varepsilon}{b-a}$를 만족한다. 따라서

$$U(f,P)-L(f,P) = \sum_{i=1}^n (M_i-m_i)\Delta x_i < \frac{\varepsilon}{b-a}\sum_{i=1}^n \Delta x_i = \varepsilon$$

이므로, 적분가능성 판정에 의해 $f$는 적분가능하다. $\blacksquare$

**Example.** $\displaystyle\int_0^1 x^2\,dx = \frac13$.

*Proof.* $x^2$은 연속이므로 앞의 정리에 의해 적분가능하고, 값은 다음과 같이 직접 계산된다. $n$등분한 partition $P_n$(소구간 길이 $1/n$)에서 $x^2$은 증가하므로 $M_i=(i/n)^2$, $m_i=((i-1)/n)^2$이고,

$$U(x^2,P_n) = \frac1n\sum_{i=1}^n \left(\frac{i}{n}\right)^2 = \frac{1}{n^3}\sum_{i=1}^n i^2 = \frac{1}{n^3}\cdot\frac{n(n+1)(2n+1)}{6} \to \frac13$$

이고, $L(x^2,P_n)=U(x^2,P_n)-\dfrac{1}{n^2}$이므로(맨 끝 항 하나만큼 차이가 난다) 역시 $\dfrac13$으로 수렴한다. $L(x^2,P_n)\le\int_0^1 x^2\,dx\le U(x^2,P_n)$이고 양쪽 다 $\dfrac13$으로 수렴하므로 $\int_0^1 x^2\,dx=\dfrac13$이다. $\blacksquare$

**Theorem.** If $f$ is monotonic on $[a,b]$, then $f$ is Darboux integrable.

*Proof.* $f$가 증가하는 경우만 보면 충분하다. $f(a)=f(b)$이면 $f$는 상수함수라 자명하므로 $f(a)<f(b)$라 하자. $\varepsilon>0$이 주어지면, $n$등분한 partition $P$(소구간 길이 $\dfrac{b-a}{n}$)에 대해, $f$가 증가하므로 각 소구간에서 $M_i=f(x_i)$, $m_i=f(x_{i-1})$이고,

$$U(f,P)-L(f,P) = \frac{b-a}{n}\sum_{i=1}^n \big(f(x_i)-f(x_{i-1})\big) = \frac{b-a}{n}\big(f(b)-f(a)\big)$$

(망원급수처럼 중간 항이 소거된다)인데, $n$을 충분히 크게 잡으면 이 값은 $\varepsilon$보다 작아진다. $\blacksquare$

사실 더 나아가서 아래와 같이 Darboux integrability를 불연속점 집합의 크기로 판가름할 수도 있다.

**Theorem. (Lebesgue's Criterion [3])** Let $f$ be a bounded on $[a,b]$. Then, $f$ is Darboux integrable iff the set of discontinuous points of $f$ has measure zero.

Measure zero라는 개념은 아직 배우지 않았으나, 아무튼 불연속점이 굉장히 적다는 말이다. 심지어는 이 불연속점들이 조밀해도, measure zero라면 적분 가능하다.

**Example (조밀한 불연속점을 가지지만 적분가능한 함수).** $$(r_n)_{n\ge1}$$을 $\mathbb{Q}\cap[0,1]$의 나열이라 하고(가산성에 의해 가능하다),

$$f(x) := \sum_{n\,:\,r_n\le x} 2^{-n} \qquad (x\in[0,1])$$

이라 하자 (합은 $x$ 이하인 $r_n$들에 대한 것이다). $x$가 커질수록 더 많은 항을 더할 뿐이므로 $f$는 단조증가하고, $0\le f(x)\le\sum_{n=1}^\infty 2^{-n}=1$이므로 유계다. 따라서 앞의 정리에 의해 $f$는 $[0,1]$에서 적분가능하다.

그런데 $f$는 각 유리수 $r_n$에서 정확히 $2^{-n}$만큼 뛰어오른다. 즉 $[0,1]$에 조밀한(dense) 가산집합 전체(모든 유리수)에서 불연속이다. Froda's Theorem에 의해 단조함수의 불연속점은 항상 가산 개인데, 이 예는 그 가산 개의 불연속점이 실제로 조밀할 수도 있다는 것과, 그런 극단적인 경우조차 적분가능성을 해치지 않는다는 것을 동시에 보여준다.

그렇다면 적분 불가능한 함수의 예시는 뭐가 있을까?

**Example (적분 불가능한 함수).** $f(x):=\mathbb{1}_{\mathbb{Q}}(x)$ (유리수면 $1$, 무리수면 $0$), $x\in[0,1]$이라 하자. $\mathbb{Q}$와 $\mathbb{R}\setminus\mathbb{Q}$가 둘 다 $\mathbb{R}$에서 조밀하므로, 아무리 짧은 소구간에도 유리수와 무리수가 모두 있어 $M_i=1$, $m_i=0$이다. 따라서 *모든* partition $P$에서 $U(f,P)=1$, $L(f,P)=0$이므로 $\overline{\int}f=1\ne0=\underline{\int}f$이고, $f$는 적분가능하지 않다. 참고로 이 함수는 $[0,1]$의 모든 점에서 불연속이다(앞의 예와 비교해보면 좋다).

## 적분의 기본 성질

**Proposition (선형성과 단조성).** Let $f,g$ be integrable on $[a,b]$ and $c\in\mathbb{R}$. Then $f+g$ and $cf$ are integrable on $[a,b]$, with $\int_a^b(f+g)=\int_a^b f+\int_a^b g$ and $\int_a^b cf = c\int_a^b f$. Moreover, if $f\le g$ on $[a,b]$, then $\int_a^b f\le\int_a^b g$.

*Proof.* (합) $\varepsilon>0$이 주어지면 적분가능성 판정에 의해 $U(f,P_1)-L(f,P_1)<\varepsilon/2$인 $P_1$과 $U(g,P_2)-L(g,P_2)<\varepsilon/2$인 $P_2$가 있다. $P:=P_1\cup P_2$라 하면 Refinement Lemma에 의해 두 부등식이 $P$에서도 유지된다. 각 소구간에서 $\sup(f+g)\le\sup f+\sup g$, $\inf(f+g)\ge\inf f+\inf g$이므로 $U(f+g,P)\le U(f,P)+U(g,P)$, $L(f+g,P)\ge L(f,P)+L(g,P)$가 되어

$$U(f+g,P)-L(f+g,P) \le \big[U(f,P)-L(f,P)\big]+\big[U(g,P)-L(g,P)\big]<\varepsilon$$

이므로 $f+g$는 적분가능하다. 값도 $L(f,P)+L(g,P)\le\int f+\int g\le U(f,P)+U(g,P)$와 $L(f+g,P)\le\int(f+g)\le U(f+g,P)$를 비교하면 $\left\vert\int(f+g)-(\int f+\int g)\right\vert<\varepsilon$이므로, $\varepsilon$이 임의였으니 등호가 성립한다.

(스칼라배) $c\ge0$이면 $M_i(cf)=cM_i(f)$, $m_i(cf)=cm_i(f)$이므로 자명하다. $c=-1$인 경우, $M_i(-f)=-m_i(f)$, $m_i(-f)=-M_i(f)$이므로 $U(-f,P)=-L(f,P)$, $L(-f,P)=-U(f,P)$가 되어 $\overline{\int}(-f)=-\underline{\int}f=-\int f=\underline{\int}(-f)$이므로 $-f$는 적분가능하고 값도 맞다. 일반적인 $c$는 $c=\vert c\vert$ 또는 $c=-\vert c\vert$로 이 두 경우의 조합이다.

(단조성) 모든 partition에서 $M_i(f)\le M_i(g)$이므로 $U(f,P)\le U(g,P)$, 즉 $\overline{\int}f\le\overline{\int}g$이고 둘 다 적분가능하므로 $\int f\le\int g$이다. $\blacksquare$

**Proposition.** If $f$ is integrable on $[a,b]$, then for every $a\le c\le b$, $f$ is integrable on $[a,c]$ and $[c,b]$, and $\int_a^b f = \int_a^c f + \int_c^b f$.

*Proof.* $c$를 (필요하면) 추가해도 상합·하합의 차이가 늘지 않는다는 Refinement Lemma에서 바로 따라온다. $\blacksquare$

곱셈에 대해서는 이렇게 간단하지 않다. 두 적분가능한 함수의 곱이 적분가능하다는 것부터 별도로 보여야 한다. 다음 Lemma가 그 열쇠다.

**Lemma.** If $f$ is integrable on $[a,b]$ with $\vert f\vert\le K$, and $\varphi:[-K,K]\to\mathbb{R}$ is continuous, then $\varphi\circ f$ is integrable on $[a,b]$.

*Proof.* $\varphi$가 $[-K,K]$(콤팩트)에서 연속이므로 Extreme Value Theorem에 의해 유계하고(어떤 $N$에 대해 $\vert\varphi\vert\le N$), Heine–Cantor Theorem에 의해 균등연속이다. $\varepsilon>0$이 주어지면, 균등연속성에 의해 어떤 $\delta\in(0,\varepsilon)$이 있어 $s,t\in[-K,K]$, $\vert s-t\vert<\delta$이면 $\vert\varphi(s)-\varphi(t)\vert<\varepsilon$이다.

$f$가 적분가능하므로, 적분가능성 판정에 의해 $U(f,P)-L(f,P)<\delta^2$인 partition $$P=\{x_0,\ldots,x_n\}$$이 존재한다. 각 소구간에서 $f$의 상·하한을 $M_i,m_i$라 하고, 첨수를 $$A:=\{i: M_i-m_i<\delta\}$$, $$B:=\{i:M_i-m_i\ge\delta\}$$로 나누자. $B$에 대해서만 모으면

$$\delta\sum_{i\in B}\Delta x_i \le \sum_{i\in B}(M_i-m_i)\Delta x_i \le U(f,P)-L(f,P) < \delta^2$$

이므로 $\sum_{i\in B}\Delta x_i<\delta$이다. $\varphi\circ f$의 $i$번째 소구간에서의 상·하한을 $M_i',m_i'$라 하면, $i\in A$인 소구간에서는 $f$값들의 차이가 항상 $\delta$ 미만이므로 균등연속성에 의해 $M_i'-m_i'\le\varepsilon$이고, $i\in B$인 소구간에서는 그냥 $\vert\varphi\vert\le N$을 써서 $M_i'-m_i'\le2N$이다. 따라서

$$U(\varphi\circ f,P)-L(\varphi\circ f,P) = \sum_{i\in A}(M_i'-m_i')\Delta x_i + \sum_{i\in B}(M_i'-m_i')\Delta x_i \le \varepsilon\sum_{i\in A}\Delta x_i + 2N\sum_{i\in B}\Delta x_i \le \varepsilon(b-a)+2N\delta < \varepsilon\big[(b-a)+2N\big]$$

이다 ($\delta<\varepsilon$을 썼다). $\varepsilon>0$을 얼마든지 작게 잡을 수 있으므로 우변도 임의로 작게 만들 수 있고, 적분가능성 판정에 의해 $\varphi\circ f$는 적분가능하다. $\blacksquare$

**Corollary.** If $f,g$ are integrable on $[a,b]$, then $\vert f\vert$, $f^2$, and $fg$ are integrable on $[a,b]$.

*Proof.* $\varphi(t):=\vert t\vert$와 $\varphi(t):=t^2$은 모두 연속이므로 (위 Lemma에 의해) $\vert f\vert=\varphi\circ f$와 $f^2=\varphi\circ f$ 모두 적분가능하다. 앞의 선형성에 의해 $f+g$도 적분가능하므로 $(f+g)^2$도 적분가능하고, 따라서

$$fg = \frac12\Big[(f+g)^2-f^2-g^2\Big]$$

도 (선형성에 의해) 적분가능하다. $\blacksquare$

**Corollary.** If $f$ is integrable on $[a,b]$, then $\left\vert\int_a^b f\right\vert \le \int_a^b \vert f\vert$.

*Proof.* $-\vert f\vert\le f\le\vert f\vert$이므로 단조성에 의해 $\int_a^b(-\vert f\vert)\le\int_a^b f\le\int_a^b\vert f\vert$인데, 선형성에 의해 좌변은 $-\int_a^b\vert f\vert$이다. 즉 $-\int_a^b\vert f\vert\le\int_a^b f\le\int_a^b\vert f\vert$이고, 이는 정확히 $\left\vert\int_a^b f\right\vert\le\int_a^b\vert f\vert$라는 말이다. $\blacksquare$

## 미적분학의 기본정리

**Theorem (Fundamental Theorem of Calculus, Part 1).** Let $f$ be integrable on $[a,b]$ and $F(x):=\int_a^x f$. Then $F$ is Lipschitz continuous on $[a,b]$. If moreover $f$ is continuous at $c\in[a,b]$, then $F$ is differentiable at $c$ with $F'(c)=f(c)$.

*Proof.* $K:=\sup_{[a,b]}\vert f\vert$라 하면, $x<y$에 대해 $-K\le f\le K$이므로 앞의 단조성에 의해 $-K(y-x)\le\displaystyle\int_x^y f\le K(y-x)$, 즉 $\vert F(y)-F(x)\vert = \left\vert\displaystyle\int_x^y f\right\vert \le K\vert y-x\vert$이다. 즉 $F$는 Lipschitz constant $K$로 Lipschitz 연속이다.

$f$가 $c$에서 연속이라 하자. $h\ne0$에 대해

$$\frac{F(c+h)-F(c)}{h} - f(c) = \frac1h\int_c^{c+h}\big(f(t)-f(c)\big)\,dt$$

인데 ($f(c)$는 상수이므로 $\frac1h\int_c^{c+h}f(c)\,dt=f(c)$이다), $\varepsilon>0$이 주어지면 $f$가 $c$에서 연속이므로 어떤 $\delta>0$이 있어 $\vert t-c\vert<\delta$이면 $\vert f(t)-f(c)\vert<\varepsilon$이다. $0<\vert h\vert<\delta$이면 $c$와 $c+h$ 사이의 모든 $t$가 이를 만족하므로, 같은 방식으로(앞의 단조성에 의해)

$$\left\vert\frac1h\int_c^{c+h}\big(f(t)-f(c)\big)\,dt\right\vert \le \frac{1}{\vert h\vert}\cdot\varepsilon\vert h\vert = \varepsilon$$

이다. 즉 $\left\vert\dfrac{F(c+h)-F(c)}{h}-f(c)\right\vert\le\varepsilon$이 $0<\vert h\vert<\delta$인 모든 $h$에서 성립하므로 $F'(c)=f(c)$이다. $\blacksquare$

**Theorem (Fundamental Theorem of Calculus, Part 2).** Let $f$ be integrable on $[a,b]$, and suppose $G:[a,b]\to\mathbb{R}$ satisfies $G'=f$ on $[a,b]$ (one-sided at the endpoints). Then

$$\int_a^b f = G(b)-G(a).$$

*Proof.* 임의의 partition $$P=\{x_0,\ldots,x_n\}$$을 잡자. $G$는 각 $[x_{i-1},x_i]$에서 미분가능(따라서 연속)하므로, 지난 글의 Mean Value Theorem에 의해 $G(x_i)-G(x_{i-1})=G'(t_i)\Delta x_i=f(t_i)\Delta x_i$인 $t_i\in(x_{i-1},x_i)$가 존재한다. 이를 $i=1,\ldots,n$에 대해 더하면 (망원급수)

$$G(b)-G(a) = \sum_{i=1}^n f(t_i)\Delta x_i.$$

우변은 $t_i\in[x_{i-1},x_i]$이므로 $L(f,P)\le G(b)-G(a)\le U(f,P)$를 만족한다. 이것이 *임의의* partition $P$에 대해 성립하므로, $L(f,P)$의 sup과 $U(f,P)$의 inf를 취하면 $\underline{\int}f \le G(b)-G(a) \le \overline{\int}f$인데, $f$가 적분가능하므로 이 둘은 같은 값 $\int_a^b f$이고, 따라서 $G(b)-G(a)=\int_a^b f$이다. $\blacksquare$

이 정리의 두 부분을 합치면, $f$가 연속이면 $F(x):=\int_a^x f$는 $f$ 자신의 (한) 부정적분(antiderivative)이 되고, 거꾸로 어떤 부정적분으로도 정적분값을 계산할 수 있으며, 결국 미분과 적분은 서로의 역연산이라는 잘 알려진 사실을 얻는다.

미적분학은 Newton과 Leibniz가 각자 독자적인 표기와 체계로 발전시킨 것으로 알려져 있는데, 미적분학의 기본정리에 해당하는 개념 자체는 이미 Isaac Barrow가 접선과 넓이를 구하는 문제가 서로 역관계에 있음을 기하학적으로 보인 바 있다 [4].

## Leibniz's Rule

적분의 양 끝점이 모두 변수인 경우, 위의 Fundamental Theorem of Calculus와 Chain Rule을 합치면 다음을 얻는다.

**Theorem (Leibniz's Rule).** Let $f$ be continuous on an interval $I$, and let $u,v$ be differentiable with values in $I$. Then

$$\frac{d}{dx}\int_{u(x)}^{v(x)} f(t)\,dt = f(v(x))\,v'(x) - f(u(x))\,u'(x).$$

*Proof.* 고정된 기준점 $p\in I$에 대해 $F(t):=\displaystyle\int_p^t f$ (앞의 Fundamental Theorem of Calculus, Part 1에 의해 $F'=f$)라 하면

$$\int_{u(x)}^{v(x)} f = F(v(x)) - F(u(x))$$

이므로, Chain Rule에 의해 양변을 미분하면 $F'(v(x))v'(x) - F'(u(x))u'(x) = f(v(x))v'(x)-f(u(x))u'(x)$이다. $\blacksquare$

## Integration by Parts

**Theorem (Integration by Parts).** If $f,g$ have continuous derivatives on $[a,b]$, then

$$\int_a^b f(x)g'(x)\,dx = f(b)g(b)-f(a)g(a) - \int_a^b f'(x)g(x)\,dx.$$

*Proof.* $(fg)'=f'g+fg'$ (미분의 사칙연산)이고 이는 연속함수들의 곱·합이라 연속이므로, 위의 Fundamental Theorem of Calculus, Part 2에 의해

$$\int_a^b (fg)' = f(b)g(b)-f(a)g(a).$$

좌변은 선형성에 의해 $\displaystyle\int_a^b f'g + \int_a^b fg'$이므로, 정리하면 원하는 식을 얻는다. $\blacksquare$

## Substitution Rule

**Theorem (Substitution Rule).** Let $g:[a,b]\to\mathbb{R}$ be differentiable on $[a,b]$ with $g'$ Riemann integrable, and let $f$ be Riemann integrable on the range of $g$. Then $(f\circ g)\,g'$ is Riemann integrable on $[a,b]$ and

$$\int_a^b f(g(x))\,g'(x)\,dx = \int_{g(a)}^{g(b)} f(u)\,du.$$

일단 $f$가 연속인 경우에 한해 FTC를 이용하여 증명해 보자.

*Proof.* $F(u):=\displaystyle\int_{g(a)}^u f(t)\,dt$라 하면($f$가 연속이므로 앞의 Fundamental Theorem of Calculus, Part 1에 의해 $F'=f$), Chain Rule에 의해

$$\frac{d}{dx}\big[F(g(x))\big] = F'(g(x))\,g'(x) = f(g(x))\,g'(x)$$

이다. $f\circ g$는 연속이고 $g'$은 Riemann 적분가능하므로 그 곱 $x\mapsto f(g(x))g'(x)$도 Riemann 적분가능하고, $F\circ g$가 그 부정적분이므로 앞의 Fundamental Theorem of Calculus, Part 2에 의해

$$\int_a^b f(g(x))g'(x)\,dx = F(g(b))-F(g(a)) = \int_{g(a)}^{g(b)} f(t)\,dt - \int_{g(a)}^{g(a)} f(t)\,dt = \int_{g(a)}^{g(b)} f(t)\,dt$$

이다 (마지막 적분은 구간 길이가 $0$이라 $0$). $\blacksquare$

$f$가 Riemann integrable일 때는 $F'=f$를 모든 점에서 쓸 수 없어 위의 FTC 증명이 통하지 않는다. $f$가 Riemann integrable일 때의 증명은 측도론적 논증이 필요하기 때문에 여기서는 다루지 않는다.

## 적분의 Mean Value Theorem

**Theorem (Mean Value Theorem for Integrals).** If $f$ is continuous on $[a,b]$, then there exists $c\in[a,b]$ such that

$$\int_a^b f = f(c)(b-a).$$

*Proof.* $a=b$이면 자명하므로 $a<b$라 하자. Extreme Value Theorem에 의해 $f$는 $[a,b]$에서 최솟값 $m$과 최댓값 $M$을 가진다. 상수함수의 적분은 그 값에 구간 길이를 곱한 것이므로(Darboux sum에서 바로 나온다), 앞의 단조성에 의해

$$m(b-a) = \int_a^b m \le \int_a^b f \le \int_a^b M = M(b-a),$$

즉 $m \le \dfrac{1}{b-a}\displaystyle\int_a^b f \le M$이다. $f$가 최솟값 $m$과 최댓값 $M$을 각각 어떤 점에서 달성하므로, Intermediate Value Theorem을 그 두 점 사이의 구간에 적용하면 $f(c)=\dfrac{1}{b-a}\displaystyle\int_a^b f$인 $c$가 (그 두 점 사이, 따라서 $[a,b]$ 안에) 존재한다. $\blacksquare$

가중치를 곱해도 비슷한 결과를 얻는다.

**Corollary (Weighted Mean Value Theorem for Integrals).** If $f$ is continuous on $[a,b]$ and $g$ is integrable on $[a,b]$ with $g\ge0$, then there exists $c\in[a,b]$ such that $\int_a^b fg = f(c)\int_a^b g$.

*Proof.* $m,M$을 앞과 같이 $f$의 최솟값·최댓값이라 하자. $g\ge0$이므로 $mg\le fg\le Mg$가 (부등식의 양변에 $g\ge0$을 곱해도 방향이 유지되므로) 성립하고, 단조성에 의해 $m\displaystyle\int_a^b g \le \int_a^b fg \le M\int_a^b g$이다. $\int_a^b g=0$이면 이 부등식이 바로 $\int_a^b fg=0=f(c)\cdot0$ (임의의 $c$)를 준다. $\int_a^b g>0$이면 양변을 나눠 $m\le\dfrac{\int fg}{\int g}\le M$을 얻고, 앞과 같이 IVT로 $f(c)=\dfrac{\int fg}{\int g}$인 $c$를 얻는다. $\blacksquare$

## 참고문헌

1. Riemann, B. (1868, 집필은 1854). Über die Darstellbarkeit einer Function durch eine trigonometrische Reihe. *Abhandlungen der Königlichen Gesellschaft der Wissenschaften zu Göttingen*, 13, 87–132.
2. Darboux, G. (1875). Mémoire sur les fonctions discontinues. *Annales scientifiques de l'École Normale Supérieure*, 2e série, 4, 57–112.
3. Lebesgue, H. (1902). Intégrale, longueur, aire. *Annali di Matematica Pura ed Applicata*, Series 3, 7, 231–359. (Vitali도 비슷한 시기에 관련 결과를 독립적으로 얻었다고 알려져 있다.)
4. Barrow, I. (1670). *Lectiones Geometricae*. London. Lecture 10, Proposition 11.
