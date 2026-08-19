---
layout: post
title: "Riemann–Stieltjes 적분"
date: 2026-07-31
mathematicians: [Riemann, Stieltjes, Cantor, Lebesgue, Lipschitz, Leibniz, Riesz, Jordan, Heine, Darboux]
---

## Riemann–Stieltjes 적분

**Definition (Upper/Lower Sums with respect to $\alpha$).** Let $\alpha$ be monotonically increasing on $[a,b]$ and $f$ bounded. With $\Delta\alpha_i:=\alpha(x_i)-\alpha(x_{i-1})\ge0$,

$$U(f,P,\alpha):=\sum_{i=1}^n M_i\,\Delta\alpha_i, \qquad L(f,P,\alpha):=\sum_{i=1}^n m_i\,\Delta\alpha_i.$$

**Definition (Riemann–Stieltjes Integrability).** $\overline{\int_a^b}f\,d\alpha := \inf_P U(f,P,\alpha)$, $\underline{\int_a^b}f\,d\alpha := \sup_P L(f,P,\alpha)$이라 하고, 둘이 같으면 $f$가 $\alpha$에 대해 *Riemann–Stieltjes 적분가능*하다고 하며 공통값을 $\int_a^b f\,d\alpha$로 쓴다.

Riemann–Stieltjes 적분은 Thomas Jan Stieltjes가 연속분수(continued fraction)의 모멘트 문제(moment problem)를 다루는 과정에서 필요해서 만든 도구였다 [1].

**Proposition.** Let $c\in(a,b)$ and

$$\alpha(x) := \begin{cases} 0 & x<c \\ 1 & x\ge c \end{cases}.$$

If $f$ is continuous at $c$, then $\int_a^b f\,d\alpha = f(c)$.

*Proof.* $c$를 partition의 점으로 포함하는 (즉 어떤 $k$에 대해 $x_k=c$인) partition만 생각해도 충분하다 (그런 partition들의 상합·하합의 inf, sup이 전체와 같은데, 이는 $c$를 포함하도록 세분해도 Refinement Lemma에 의해 상합은 늘지 않고 하합은 줄지 않기 때문이다). 이런 partition에서 $i<k$이면 $x_{i-1},x_i<c$이므로 $\Delta\alpha_i=0$이고, $i>k$이면 $x_{i-1},x_i\ge c$이므로 역시 $\Delta\alpha_i=0$이다. $i=k$일 때만 $\alpha(x_{k-1})=0$ ($x_{k-1}<c$), $\alpha(x_k)=\alpha(c)=1$이라 $\Delta\alpha_k=1$이다. 따라서 $U(f,P,\alpha)=M_k$, $L(f,P,\alpha)=m_k$인데, 여기서 $M_k,m_k$는 $[x_{k-1},c]$에서의 $f$의 상·하한이다. $f$가 $c$에서 연속이므로, $x_{k-1}\to c^-$로 이 구간을 좁히면 $M_k,m_k$ 모두 $f(c)$로 수렴한다. 따라서 $\overline{\int}f\,d\alpha=\underline{\int}f\,d\alpha=f(c)$이다. $\blacksquare$

$f$가 $c$에서 불연속이면 이 결론은 일반적으로 성립하지 않는다. 심지어 적분 자체가 존재하지 않을 수 있다. 예를 들어 $f(x):=0$ ($x<c$), $f(x):=1$ ($x\ge c$)로 두면 ($f$도 $\alpha$와 정확히 같은 점에서 뛴다), $c=x_k$를 포함하는 모든 partition에서 $M_k=f(c)=1$, $m_k=\inf_{[x_{k-1},c)}f=0$이므로 $U(f,P,\alpha)=1$, $L(f,P,\alpha)=0$이 항상 성립해 $\overline{\int}f\,d\alpha=1\ne0=\underline{\int}f\,d\alpha$이다. $f$와 $\alpha$가 같은 점에서 불연속이면 적분이 존재하지 않을 수 있다는 전형적인 예다.

이 사실은 확률론에서 요긴하게 쓰인다. 확률변수 $X$의 누적분포함수(CDF) $F_X$에 대해 기댓값을 $E[f(X)]=\int f\,dF_X$로 정의하면, $X$가 이산형이든(그러면 $F_X$는 계단함수이고, 위 명제를 각 도약점에 적용하면 익숙한 급수 $\sum f(x_i)P(X=x_i)$가 나온다) 연속형이든($F_X$가 미분가능하면 $d\alpha = F_X'(x)\,dx$가 밀도함수를 곱한 보통의 적분이 된다) 심지어 둘이 섞인 경우든, 같은 하나의 정의로 통일해서 다룰 수 있다.

위 정의는 Darboux의 방식을 쓰기 때문에 $\alpha$가 증가한다는 조건에 의존하는데, Riemann의 방식을 택하면 더 일반적인 $\alpha$에 대해서도 정의할 수 있다.

**Definition (Riemann–Stieltjes Sum, 일반).** For a partition $$P=\{x_0,\ldots,x_n\}$$, tags $(t_i)$, and *any* bounded $\alpha:[a,b]\to\mathbb{R}$ (증가할 필요 없다), the *Riemann–Stieltjes sum* is $S(f,P,\alpha,(t_i)):=\sum_{i=1}^n f(t_i)\Delta\alpha_i$.

**Definition (Riemann–Stieltjes Integrability, 일반).** $f$ is *Riemann–Stieltjes integrable* with respect to $\alpha$ with integral $I$ (in this general sense) if for every $\varepsilon>0$ there exists $\delta>0$ such that, for every partition $P$ with $\Vert P\Vert<\delta$ and every choice of tags, $\vert S(f,P,\alpha,(t_i))-I\vert<\varepsilon$.

이 두 가지 방식으로 정의한 Riemann-Stieltjes 적분이 $\alpha$가 increasing일 때 동치라는 사실을 어렵지 않게 보일 수 있다. 즉, 두 번째 방식은 첫 번째 방식의 일반화라고 할 수 있다.

## Riemann–Stieltjes 적분의 성질

Riemann 적분의 성질은 Riemann–Stieltjes 적분으로 거의 다 그대로 확장된다. 다만 성질마다 $\alpha$가 증가해야 하는지가 다르다.

**Proposition (선형성).** Let $f,g$ be Riemann–Stieltjes integrable with respect to $\alpha$, and $c\in\mathbb{R}$. Then $f+g$ and $cf$ are R-S integrable with respect to $\alpha$, with $\int_a^b(f+g)\,d\alpha=\int_a^b f\,d\alpha+\int_a^b g\,d\alpha$ and $\int_a^b cf\,d\alpha=c\int_a^b f\,d\alpha$.

*Proof.* 임의의 partition $P$와 tag $(t_i)$에서 $S(f+g,P,\alpha,(t_i))=S(f,P,\alpha,(t_i))+S(g,P,\alpha,(t_i))$가 정확히 성립하므로 (뒤에 나올 $\alpha$에 대한 선형성과 똑같은 논증으로) mesh$\to0$일 때 양변이 각각의 극한으로 수렴해 원하는 식을 얻는다. $cf$도 $S(cf,P,\alpha,(t_i))=c\cdot S(f,P,\alpha,(t_i))$에서 마찬가지다. $\blacksquare$

**Proposition (단조성).** Let $\alpha$ be increasing on $[a,b]$, and let $f,g$ be Riemann–Stieltjes integrable with respect to $\alpha$. If $f\le g$ on $[a,b]$, then $\int_a^b f\,d\alpha\le\int_a^b g\,d\alpha$.

*Proof.* 모든 partition에서 $M_i(f)\le M_i(g)$이고 $\Delta\alpha_i\ge0$이므로 $U(f,P,\alpha)\le U(g,P,\alpha)$, 즉 $\overline{\int}f\,d\alpha\le\overline{\int}g\,d\alpha$이고 둘 다 적분가능하므로 $\int f\,d\alpha\le\int g\,d\alpha$이다. $\blacksquare$

$\alpha$가 증가하지 않으면 이 결론은 완전히 깨질 수 있다. $\alpha(x):=-x$ (감소함수)라 하고 $f\equiv0\le g\equiv1$이라 하면, 상수함수의 적분은 (일반적인 정의에서 항상 성립하는 telescoping을 통해) $\int_0^1 f\,d\alpha=0$, $\int_0^1 g\,d\alpha=\alpha(1)-\alpha(0)=-1$인데, $-1<0$이므로 $f\le g$인데도 $\int f\,d\alpha>\int g\,d\alpha$가 되어 부등식의 방향이 통째로 뒤집힌다.

**Proposition (구간에 대한 덧셈성).** If $f$ is Riemann–Stieltjes integrable with respect to $\alpha$ on $[a,b]$ (일반적인 의미로), then for every $a\le c\le b$, $f$ is R-S integrable with respect to $\alpha$ on $[a,c]$ and $[c,b]$, and $\int_a^b f\,d\alpha=\int_a^c f\,d\alpha+\int_c^b f\,d\alpha$.

*Proof.* $c$를 항상 포함하는 partition만 생각해도 충분한데(그런 partition들에서의 극한이 전체와 같다), 그런 partition에서는 Stieltjes sum이 $[a,c]$ 부분과 $[c,b]$ 부분의 합으로 정확히 쪼개진다. $\blacksquare$

**Corollary.** $\alpha$가 증가한다고 하자. $f,g$가 $\alpha$에 대해 적분가능하면 $\vert f\vert,f^2,fg$도 $\alpha$에 대해 적분가능하고, $\left\vert\int_a^b f\,d\alpha\right\vert\le\int_a^b\vert f\vert\,d\alpha$이다.

*Proof.* (φ∘f에 대한 Lemma를 $\Delta x_i\to\Delta\alpha_i$로 옮기면) 앞의 두 성질과 똑같은 방식으로 나온다.

$\alpha$가 증가한다는 조건은 여기서 증명 방식의 장식이 아니라 핵심이다. $\Delta\alpha_i$가 음수일 수 있으면 $M_i\Delta\alpha_i\ge f(t_i)\Delta\alpha_i\ge m_i\Delta\alpha_i$라는 (상합·하합이 실제로 상·하한이 되게 하는) 부등식 자체가 방향이 뒤집혀서, $U(f,P,\alpha)$가 더 이상 실제 값의 상한이 아니게 된다. 실제로 결론이 깨지는 예를 보자: $[0,1]$에서 $\alpha(x):=2x$ ($x\le1/2$), $\alpha(x):=2(1-x)$ ($x>1/2$)인 (증가하다가 감소하는, $\alpha(0)=0,\alpha(1/2)=1,\alpha(1)=0$) 연속함수를 생각하고, $f(x):=1$ ($x<1/2$), $f(x):=-1$ ($x\ge1/2$)라 하자. $f$가 $[0,1/2]$, $[1/2,1]$ 위에서 각각 상수이므로 (그 구간 위에서 $\alpha$가 연속이라 경계점 하나의 값은 영향이 없다) $\int_0^{1/2}f\,d\alpha=1\cdot(\alpha(1/2)-\alpha(0))=1$, $\int_{1/2}^1 f\,d\alpha=(-1)\cdot(\alpha(1)-\alpha(1/2))=(-1)(0-1)=1$이라 $\int_0^1 f\,d\alpha=2$인데, $\vert f\vert\equiv1$이므로 $\int_0^1\vert f\vert\,d\alpha=\alpha(1)-\alpha(0)=0$이다. 즉 $\left\vert\int_0^1 f\,d\alpha\right\vert=2>0=\int_0^1\vert f\vert\,d\alpha$로, 부등식이 정반대로 깨진다.

**Theorem (Mean Value Theorem for Riemann–Stieltjes 적분).** Let $f$ be continuous and $\alpha$ be increasing on $[a,b]$ with $\alpha(a)<\alpha(b)$. Then there exists $c\in[a,b]$ such that

$$\int_a^b f\,d\alpha = f(c)\big(\alpha(b)-\alpha(a)\big).$$

*Proof.* $m,M$을 $f$의 (Extreme Value Theorem에 의한) 최솟값·최댓값이라 하자. 상수함수의 Stieltjes 적분은 $\int_a^b k\,d\alpha=k(\alpha(b)-\alpha(a))$이므로(상합·하합 모두 $k\cdot(\alpha(b)-\alpha(a))$), 단조성에 의해

$$m\big(\alpha(b)-\alpha(a)\big) \le \int_a^b f\,d\alpha \le M\big(\alpha(b)-\alpha(a)\big),$$

즉 $m\le\dfrac{1}{\alpha(b)-\alpha(a)}\displaystyle\int_a^b f\,d\alpha\le M$이다. $f$가 $m,M$을 각각 어떤 점에서 달성하므로, IVT를 그 두 점 사이에 적용하면 원하는 $c$를 얻는다. $\blacksquare$

이 성질들은 모두 지난 글에서 이미 (보통 Riemann 적분에 대해) 증명한 것을 $\Delta x_i\to\Delta\alpha_i$로 옮긴 것이다. 이제 보통의 적분에는 없는, R-S 적분만의 새로운 성질을 보자. 피적분함수 $f$가 아니라 "적분소" $\alpha$ 자체에 대한 선형성이다.

**Proposition ($\alpha$에 대한 선형성).** Let $f$ be Riemann–Stieltjes integrable with respect to both $\alpha$ and $\beta$ (일반적인 의미로), and $c\in\mathbb{R}$ (어떤 실수든 상관없다). Then $f$ is R-S integrable with respect to $\alpha+\beta$ and $c\alpha$, with

$$\int_a^b f\,d(\alpha+\beta) = \int_a^b f\,d\alpha + \int_a^b f\,d\beta, \qquad \int_a^b f\,d(c\alpha) = c\int_a^b f\,d\alpha.$$

*Proof.* 임의의 partition $P$와 tag $(t_i)$에 대해 $$\Delta(\alpha+\beta)_i=\Delta\alpha_i+\Delta\beta_i$$이므로

$$S(f,P,\alpha+\beta,(t_i)) = \sum_i f(t_i)\big[\Delta\alpha_i+\Delta\beta_i\big] = S(f,P,\alpha,(t_i))+S(f,P,\beta,(t_i))$$

이 (모든 partition·tag에서) 정확히 성립한다. $\varepsilon>0$이 주어지면, $f$가 $\alpha,\beta$에 각각 적분가능하므로 대응하는 $\delta_1,\delta_2>0$이 있어 mesh가 각각 그보다 작으면 $\vert S(f,P,\alpha,(t_i))-\int f\,d\alpha\vert<\varepsilon/2$, $\vert S(f,P,\beta,(t_i))-\int f\,d\beta\vert<\varepsilon/2$이다. $\delta:=\min(\delta_1,\delta_2)$로 두면, mesh$(P)<\delta$인 임의의 partition·tag에서 삼각부등식에 의해

$$\left\vert S(f,P,\alpha+\beta,(t_i)) - \left(\int f\,d\alpha+\int f\,d\beta\right)\right\vert < \varepsilon$$

이므로 원하는 결론을 얻는다. $c\alpha$에 대해서도 $$\Delta(c\alpha)_i=c\Delta\alpha_i$$에서 같은 방식으로 나온다 (부호와 무관하게 그대로 성립한다). $\blacksquare$

## 적분 가능한 함수들

**Theorem.** If $f$ is continuous on $[a,b]$ and $\alpha$ is monotonically increasing on $[a,b]$, then $f$ is Riemann–Stieltjes integrable with respect to $\alpha$.

*Proof.* $\alpha(a)=\alpha(b)$이면 모든 $\Delta\alpha_i=0$이 되어 자명하므로 $\alpha(a)<\alpha(b)$라 하자. $f$는 (Heine–Cantor에 의해) 균등연속이므로, $\varepsilon>0$에 대해 어떤 $\delta>0$이 있어 $\vert x-y\vert<\delta$이면 $\vert f(x)-f(y)\vert<\dfrac{\varepsilon}{\alpha(b)-\alpha(a)}$이다. 소구간 길이가 모두 $\delta$ 미만인 partition $P$를 잡으면 각 소구간에서 $M_i-m_i<\dfrac{\varepsilon}{\alpha(b)-\alpha(a)}$이므로

$$U(f,P,\alpha)-L(f,P,\alpha) = \sum_{i=1}^n(M_i-m_i)\Delta\alpha_i < \frac{\varepsilon}{\alpha(b)-\alpha(a)}\sum_{i=1}^n\Delta\alpha_i = \varepsilon$$

이다. $\blacksquare$

위 Theorem과 $\alpha$에 대한 선형성을 통해서, $\alpha$가 두 증가함수의 차로 나타낼 수 있는 함수 (bounded variation)이기만 해도 $f$가 연속이면 적분 가능하다. 사실 더 놀라운 것이 성립한다. 모든 연속함수 $f$에 대해 $\int f\,d\alpha$가 유계인 선형함수로 잘 정의되려면 $\alpha$가 bounded variation이어야 한다는 것도 역방향으로 성립한다. 이는 아직 다루지 않았지만 Riesz representation theorem의 특수한 케이스이다. ($C[a,b]$의 dual space가 bounded variation 함수들로 표현 가능)

예를 들어 $\alpha(x):=x\sin(1/x)$ ($x\ne0$), $\alpha(0):=0$은 $[0,1]$에서 연속이지만 bounded variation은 아닌 함수이다. 따라서 $f$가 연속이더라도 $\int f\,d\alpha$는 적분 가능하지 않다.

**Theorem.** If $f$ is monotonic on $[a,b]$ and $\alpha$ is continuous and increasing on $[a,b]$, then $f$ is Riemann–Stieltjes integrable with respect to $\alpha$.

*Proof.* $f$가 증가하는 경우만 보면 충분하다 (감소하면 $-f$에 적용). $\alpha(a)=\alpha(b)$이면 자명하므로 $\alpha(a)<\alpha(b)$라 하자. $\varepsilon>0$이 주어지면, $n$을 하나 고정하고 $y_i:=\alpha(a)+\dfrac{i}{n}\big(\alpha(b)-\alpha(a)\big)$ ($i=0,\ldots,n$)이라 하자. $\alpha$가 연속이고 증가하므로 Intermediate Value Theorem에 의해 각 $y_i$에 대해 $\alpha(x_i)=y_i$인 $x_i\in[a,b]$가 존재하는데, $y_0<y_1<\cdots<y_n$이고 $\alpha$가 증가하므로 (같은 점이면 $\alpha$값도 같아야 하니) $x_0<x_1<\cdots<x_n$이다. $$P:=\{x_0,\ldots,x_n\}$$이라 하면 $\Delta\alpha_i=y_i-y_{i-1}=\dfrac{\alpha(b)-\alpha(a)}{n}$이 모든 $i$에서 같다. $f$가 증가하므로 $M_i=f(x_i)$, $m_i=f(x_{i-1})$이고,

$$U(f,P,\alpha)-L(f,P,\alpha) = \frac{\alpha(b)-\alpha(a)}{n}\sum_{i=1}^n\big(f(x_i)-f(x_{i-1})\big) = \frac{\alpha(b)-\alpha(a)}{n}\big(f(b)-f(a)\big)$$

(망원급수)인데, $n$을 충분히 크게 잡으면 이 값은 $\varepsilon$보다 작아진다. $\blacksquare$

여기서도 마찬가지로 $\alpha$가 증가한다는 조건을 bounded variation으로 교체할 수 있다. 그런데 연속이라는 조건은 꼭 필요하다. $\alpha(x):=0$ ($x<c$), $\alpha(x):=1$ ($x\ge c$)라 하고 $f(x):=0$ ($x<c$), $f(x):=1$ ($x\ge c$)라 하자. $f$는 실제로 (약하게) 증가하는 단조함수다. $c=x_k$를 partition의 점으로 포함하는 (그렇지 않은 partition은 세분해서 $c$를 넣어도 Refinement Lemma에 의해 상합은 늘지 않고 하합은 줄지 않으므로 이런 partition만 봐도 충분한) 모든 partition에서, $i\ne k$인 소구간에서는 $\alpha$가 상수라 $\Delta\alpha_i=0$이고, $i=k$인 소구간 $[x_{k-1},c]$에서는 $\Delta\alpha_k=\alpha(c)-\alpha(x_{k-1})=1-0=1$이다. 이 구간에서 $f$는 $x_{k-1}\le x<c$일 때 $0$, $x=c$일 때 $1$이라는 두 값만 가지므로 $M_k=\sup_{[x_{k-1},c]}f=1$, $m_k=\inf_{[x_{k-1},c]}f=0$이다. 따라서 partition을 아무리 세밀하게 잡아도 $U(f,P,\alpha)=M_k\cdot1=1$, $L(f,P,\alpha)=m_k\cdot1=0$이 항상 성립하여

$$\overline{\int_a^b}f\,d\alpha=\inf_P U(f,P,\alpha)=1, \qquad \underline{\int_a^b}f\,d\alpha=\sup_P L(f,P,\alpha)=0$$

이다. $1\ne0$이므로 (단조함수인) $f$가 (증가하는) $\alpha$에 대해 적분가능하지 않다. $\alpha$가 $c$에서 불연속이라는 사실이 결정적이다.

Lebesgue's Criterion의 Riemann–Stieltjes 적분 버전도 있다. 이때 measure zero를 재는 measure가 Lebesgue-Stieltjes measure로 확장된다.

## Change of Variables

지난 글에서 다룬 Substitution Rule을 Riemann–Stieltjes 적분으로 일반화한 것이 **Change of Variables**이다.

**Theorem (Change of Variables).** Let $\alpha$ be of bounded variation on $[c,d]$, let $f$ be bounded on $[c,d]$, and let $g:[a,b]\to[c,d]$ be continuous with $\alpha\circ g$ of bounded variation. If $f$ is Riemann–Stieltjes integrable with respect to $\alpha$, then $f\circ g$ is Riemann–Stieltjes integrable with respect to $\alpha\circ g$, and

$$\int_a^b (f\circ g)\,d(\alpha\circ g) = \int_{g(a)}^{g(b)} f\,d\alpha.$$

If in addition $g$ is onto $[c,d]$, then the converse holds as well, so that $f\circ g\in\mathcal{R}(\alpha\circ g)$ and $f\in\mathcal{R}(\alpha)$ are equivalent.

증명은 측도론적 논증이 필요하기 때문에 생략한다.

**Corollary.** Let $g:[a,b]\to\mathbb{R}$ be continuous and of bounded variation, and let $f$ be Riemann integrable on the range of $g$. Then

$$\int_a^b (f\circ g)\,dg = \int_{g(a)}^{g(b)} f(u)\,du.$$

이 등식이 $g$의 미분가능성을 전혀 요구하지 않는다는 점이 핵심이다. $g$가 미분 불가능할 때도 위 두 가지 조건을 만족하면 substitution rule을 적용할 수는 없을지라도 change of variables를 적용할 수는 있다. 대표적인 예가 **Cantor function**이다.

**Cantor function.** 표준 Cantor 집합 $C$는 $[0,1]$에서 매 단계 남아 있는 각 구간의 가운데 열린 삼등분 구간을 제거하며 얻는 집합이다 (measure $0$). $n$번째 단계에서 제거되는 $2^{n-1}$개의 열린 구간에 왼쪽부터 값 $\frac{1}{2^n},\frac{3}{2^n},\ldots,\frac{2^n-1}{2^n}$을 부여하고 각 구간 위에서 $c$를 그 상수로 정의하면, $c$가 $[0,1]\setminus C$ (measure $1$) 전체에서 non-decreasing으로 정해지고 값들이 조밀하므로 $C$ 위로 연속적으로 유일하게 확장된다. 그 확장 $c:[0,1]\to[0,1]$이 **Cantor function**이며, 연속이고 non-decreasing, $c(0)=0$, $c(1)=1$이다. 각 빠진 구간에서 상수라 measure $1$인 $[0,1]\setminus C$에서 $c'=0$이지만, 그럼에도 $c$는 $0$에서 $1$까지 증가한다.

$f\equiv1$이라 하면, 위 Corollary에 의해

$$\int_0^1 (f\circ c)\,dc = \int_{c(0)}^{c(1)} f(u)\,du = \int_0^1 1\,du = 1$$

이다 (좌변은 $f\circ c\equiv1$이므로 $\int_0^1 1\,dc=c(1)-c(0)=1$로 직접 확인된다). 반면 Substitution Rule은 $c$에 적용할 수 없다. 설령 $c'=0$ (거의 모든 곳)을 그대로 대입해 $\int_0^1 f(c(x))c'(x)\,dx$를 계산해도 값이 $0$이 되어 $1\ne0$으로 틀린다.

Change of variables가 substitution rule의 일반화라는 것은 change of variables에서 $g'$이 Riemann integrable일 경우 substitution rule이 유도된다는 뜻이다. 이를 보이기 위해 일단 다음 theorem이 필요하다.

**Theorem.** Let $\alpha$ be differentiable on $[a,b]$ with $\alpha'$ Riemann integrable, and let $f$ be bounded on $[a,b]$. Then $f$ is Riemann–Stieltjes integrable with respect to $\alpha$ if and only if $f\alpha'$ is Riemann integrable, in which case

$$\int_a^b f\,d\alpha = \int_a^b f(x)\alpha'(x)\,dx.$$

*Proof.* $\alpha'$이 Riemann 적분가능하므로 유계이고, MVT에 의해 $\alpha$는 Lipschitz, 따라서 bounded variation이라 $\int f\,d\alpha$를 (일반적인 의미로) 논할 수 있다. 각 소구간에 MVT를 적용하면 $\Delta\alpha_i=\alpha'(s_i)\Delta x_i$인 $s_i\in(x_{i-1},x_i)$가 존재하므로, 임의의 partition $P$와 tag $(t_i)$에 대해

$$\left\vert \sum_i f(t_i)\Delta\alpha_i - \sum_i f(t_i)\alpha'(t_i)\Delta x_i \right\vert = \left\vert \sum_i f(t_i)\big[\alpha'(s_i)-\alpha'(t_i)\big]\Delta x_i \right\vert \le \sup\vert f\vert \sum_i \omega_i(\alpha')\,\Delta x_i$$

이다 ($s_i,t_i$가 같은 소구간에 있어 $\vert\alpha'(s_i)-\alpha'(t_i)\vert\le\omega_i(\alpha')$, 여기서 $\omega_i(\alpha')$은 그 소구간에서 $\alpha'$의 oscillation). $\alpha'$이 Riemann 적분가능하므로 Riemann's Criterion에 의해 mesh$\to0$일 때 $\sum_i\omega_i(\alpha')\Delta x_i\to0$이고, 따라서 우변이 $0$으로 간다. 즉 $f$에 대한 Stieltjes sum $\sum_i f(t_i)\Delta\alpha_i$와 $f\alpha'$에 대한 보통의 Riemann sum $\sum_i f(t_i)\alpha'(t_i)\Delta x_i$의 차가 (tag와 무관하게 균등하게) $0$으로 수렴하여, 한쪽이 수렴하는 것과 다른 쪽이 수렴하는 것이 동치이고 그 값도 같다. $\blacksquare$

위 theorem에 의해 $g'$이 Riemann integrable일 경우 다음과 같이 substitution rule이 유도된다.

$$\int_{g(a)}^{g(b)} f(u)\,du = \int_a^b (f\circ g)\,dg = \int_a^b f(g(x))\,g'(x)\,dx$$


## Fundamental Theorem of Calculus

**Theorem (Fundamental Theorem of Calculus, Part 1).** Let $\alpha$ be differentiable on $[a,b]$ with $\alpha'$ bounded, and let $f$ be continuous on $[a,b]$. Then $\Phi(x):=\int_a^x f\,d\alpha$ is differentiable on $[a,b]$ with

$$\Phi'(x)=f(x)\alpha'(x).$$

*Proof.* 도함수의 정의와 구간에 대한 덧셈성에 의해

$$\Phi'(t)=\lim_{h\to0}\frac{\Phi(t+h)-\Phi(t)}{h}=\lim_{h\to0}\frac1h\int_t^{t+h} f\,d\alpha$$

이므로, 이 극한이 $f(t)\alpha'(t)$와 같음을 보이면 된다. $\alpha'$이 $M$으로 bounded된다고 하면 MVT에 의해 $\vert\alpha(x)-\alpha(y)\vert\le M\vert x-y\vert$ (Lipschitz)이므로, 임의의 구간에서 $\alpha$의 total variation은 그 구간 길이의 $M$배를 넘지 않는다 (모든 partition에서 $\sum\vert\Delta\alpha_i\vert\le M\sum\vert\Delta x_i\vert$). 특히 $\alpha$는 bounded variation이고, 앞서 다룬 (연속함수 + BV ⟹ 적분가능) 사실에 의해 $h$가 작을 때 $\int_t^{t+h}f\,d\alpha$가 존재한다. 이제

$$\frac1h\int_t^{t+h} f\,d\alpha - f(t)\alpha'(t) = \underbrace{\frac1h\int_t^{t+h}\big(f(s)-f(t)\big)\,d\alpha(s)}_{(\ast)} + f(t)\left[\frac{\alpha(t+h)-\alpha(t)}{h}-\alpha'(t)\right]$$

인데 (상수함수 $f(t)$의 적분은 $f(t)(\alpha(t+h)-\alpha(t))$이므로 이렇게 분리된다), 둘째 항은 $\alpha$가 $t$에서 미분가능하므로 $h\to0$일 때 $0$으로 간다. $(\ast)$는, Jordan decomposition ($\alpha=\alpha^+-\alpha^-$)과 (증가함수에 대한) $\vert\int g\,d\alpha^{\pm}\vert\le\sup\vert g\vert\cdot(\alpha^{\pm}(t+h)-\alpha^{\pm}(t))$를 합쳐서 얻는 부등식 $\vert\int_t^{t+h} g\,d\alpha\vert\le\sup_{[t,t+h]}\vert g\vert\cdot V_t^{t+h}(\alpha)$ (여기서 $V_t^{t+h}(\alpha)\le M\vert h\vert$)에 의해

$$\vert(\ast)\vert \le \frac{1}{\vert h\vert}\cdot\sup_{s\in[t,t+h]}\vert f(s)-f(t)\vert\cdot M\vert h\vert = M\cdot\sup_{s\in[t,t+h]}\vert f(s)-f(t)\vert$$

이고, $f$가 $t$에서 연속이므로 $h\to0$일 때 우변이 $0$으로 간다. $\blacksquare$

Riemann 적분 버전 FTC Part 1이 $f$의 연속성만 요구했던 것과 달리, 여기서는 $\alpha$의 미분가능성이 추가로 필요하다.

**Theorem (Fundamental Theorem of Calculus, Part 2).** Let $\alpha$ be differentiable on $[a,b]$ with $\alpha'$ Riemann integrable, and let $f$ be bounded on $[a,b]$ with $f\alpha'$ Riemann integrable. If $G:[a,b]\to\mathbb{R}$ satisfies $G'(x)=f(x)\alpha'(x)$ for all $x\in[a,b]$, then

$$\int_a^b f\,d\alpha = G(b)-G(a).$$

*Proof.* $\alpha$가 미분가능하고 $\alpha'$이 Riemann 적분가능하며 $f$가 유계이고 $f\alpha'$이 Riemann 적분가능하므로, $f$는 $\alpha$에 대해 R-S 적분가능하고 $\int_a^b f\,d\alpha=\int_a^b f(x)\alpha'(x)\,dx$이다. 한편 $G'=f\alpha'$이 Riemann 적분가능하므로 $\int_a^b f(x)\alpha'(x)\,dx=G(b)-G(a)$이다. 두 식을 이으면 원하는 등식을 얻는다. $\blacksquare$

## Leibniz's Rule

**Corollary (Leibniz's Rule).** Let $\alpha$ be differentiable on $[a,b]$ with $\alpha'$ bounded, let $f$ be continuous on $[a,b]$, and let $u,v$ be differentiable with values in $[a,b]$. Then

$$\frac{d}{dx}\int_{u(x)}^{v(x)} f(t)\,d\alpha(t) = f(v(x))\alpha'(v(x))v'(x) - f(u(x))\alpha'(u(x))u'(x).$$

*Proof.* $\Phi(t):=\displaystyle\int_a^t f\,d\alpha$라 하면 (위 FTC Part 1에 의해) $\Phi'(t)=f(t)\alpha'(t)$이다. 앞의 (구간에 대한) 덧셈성에 의해 $\int_{u(x)}^{v(x)}f\,d\alpha=\Phi(v(x))-\Phi(u(x))$이므로, Chain Rule에 의해 양변을 미분하면

$$\frac{d}{dx}\int_{u(x)}^{v(x)} f\,d\alpha = \Phi'(v(x))v'(x)-\Phi'(u(x))u'(x) = f(v(x))\alpha'(v(x))v'(x)-f(u(x))\alpha'(u(x))u'(x)$$

이다. $\blacksquare$

## Integration by parts

**Theorem (Integration by parts).** Suppose $f,\alpha:[a,b]\to\mathbb{R}$ are bounded, and $f$ is Riemann–Stieltjes integrable with respect to $\alpha$. Then $\alpha$ is Riemann–Stieltjes integrable with respect to $f$, and

$$\int_a^b f\,d\alpha + \int_a^b \alpha\,df = f(b)\alpha(b)-f(a)\alpha(a).$$

*Proof.* $I:=\int_a^b f\,d\alpha$라 하자. Partition $$P=\{x_0,\ldots,x_n\}$$과 tag $(t_i)$ ($t_i\in[x_{i-1},x_i]$)가 주어졌다 하자 ($\alpha\,df$의 Stieltjes sum을 계산할 tag다). $x_0\le t_1\le x_1\le t_2\le\cdots\le t_n\le x_n$을 그대로 늘어놓으면 $[a,b]$의 (더 세밀한) partition $Q$가 되는데, $Q$에서 $[x_{i-1},t_i]$에는 tag $x_{i-1}$, $[t_i,x_i]$에는 tag $x_i$를 주어 (적분소는 $\alpha$인) Stieltjes sum을 계산하면

$$T := \sum_{i=1}^n\Big[f(x_{i-1})\big(\alpha(t_i)-\alpha(x_{i-1})\big) + f(x_i)\big(\alpha(x_i)-\alpha(t_i)\big)\Big]$$

인데, 이를 전개하면

$$T = \sum_{i=1}^n \alpha(t_i)\big[f(x_{i-1})-f(x_i)\big] + \sum_{i=1}^n\big[f(x_i)\alpha(x_i)-f(x_{i-1})\alpha(x_{i-1})\big] = -\sum_{i=1}^n \alpha(t_i)\big[f(x_i)-f(x_{i-1})\big] + \big[f(b)\alpha(b)-f(a)\alpha(a)\big]$$

이다 (뒤 항은 망원급수). 즉

$$\sum_{i=1}^n \alpha(t_i)\big[f(x_i)-f(x_{i-1})\big] = f(b)\alpha(b)-f(a)\alpha(a) - T$$

이고, 좌변은 정확히 $\alpha\,df$에 대한 (원래 $P,(t_i)$에서의) Stieltjes sum이다. $Q$의 소구간들은 모두 $P$의 소구간에 포함되므로 $\Vert Q\Vert\le\Vert P\Vert$이고, $f$가 $\alpha$에 대해 (일반적인 의미로) 적분가능하므로 $\Vert P\Vert\to0$이면 $\Vert Q\Vert\to0$이라 (tag와 무관하게 균등하게) $T\to I$이다. 따라서

$$\sum_{i=1}^n \alpha(t_i)\big[f(x_i)-f(x_{i-1})\big] \to f(b)\alpha(b)-f(a)\alpha(a) - I$$

이고, 이는 (원래 $P,(t_i)$의) 임의의 선택에서 성립하므로, $\alpha$는 $f$에 대해 적분가능하고 $\int_a^b\alpha\,df = f(b)\alpha(b)-f(a)\alpha(a)-I$이다. $\blacksquare$

이 부분적분 공식은 $f$가 증가할 필요가 전혀 없다는 점에서, 앞서 다룬 일반화된 (tagged partition 기반) 정의가 있어야만 의미가 통하는 서술이다. $\int\alpha\,df$에서 "적분소" 역할을 하는 $f$는 애초에 증가하는 함수라는 가정이 전혀 없기 때문이다.

## 참고문헌

1. Stieltjes, T. J. (1894–1895). Recherches sur les fractions continues. *Annales de la Faculté des Sciences de Toulouse*, 8, J1–J122; 9, A5–A47.
