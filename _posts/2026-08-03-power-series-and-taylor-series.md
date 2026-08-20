---
layout: post
title: "매끄러움과 멱급수, Taylor 급수 (Power Series and Taylor Series)"
date: 2026-08-03
mathematicians: [Taylor, Maclaurin, Cauchy, Hadamard, Abel, Lagrange, Weierstrass, Borel, Leibniz, Newton, Cesàro]
---

## 미분가능성의 위계

**Definition ($C^k$).** Let $k\ge0$ be an integer. A function $f$ on an open interval $I$ is of class $C^k$ if $f$ is $k$ times differentiable on $I$ and $f^{(k)}$ is continuous on $I$. We write $f\in C^k(I)$. Here $C^0$ means continuous, and $f$ is of class $C^\infty$ (*smooth*) if $f\in C^k(I)$ for every $k$.

정의에서 곧바로 포함관계

$$C^0 \supset C^1 \supset C^2 \supset \cdots \supset C^\infty = \bigcap_{k=0}^\infty C^k$$

가 나온다. $f^{(k)}$가 미분가능하면 연속이므로 $C^k\supset C^{k+1}$이기 때문이다. 이 포함은 모두 진부분집합 관계다.

**Example (위계가 진짜로 좁아진다).** $f(x):=x\vert x\vert$를 보자. $x>0$에서 $f(x)=x^2$, $x<0$에서 $f(x)=-x^2$이고, 미분하면 $f'(x)=2\vert x\vert$이다($f'(0)=0$도 정의에서 직접 확인된다). $f'=2\vert x\vert$은 연속이므로 $f\in C^1$이지만, $\vert x\vert$은 $0$에서 미분 불가능하므로 $f\notin C^2$이다. 이 함수를 $k-1$번 적분하면 $C^k$이지만 $C^{k+1}$은 아닌 함수를 얻으므로, 위 위계의 모든 칸이 실제로 서로 다르다.

가장 위의 $C^\infty$조차 끝이 아니다. 무한히 매끄러운 함수 중에서도 자신의 Taylor 급수로 복원되는 것과 그렇지 않은 것이 갈리는데, 이를 이해하려면 먼저 멱급수를 봐야 한다.

## 멱급수

**Definition (Power Series).** A *power series* centered at $c$ is a series of the form
$$\sum_{n=0}^\infty a_n(x-c)^n, \qquad a_n\in\mathbb{R}.$$

멱급수로 함수를 다루는 발상은 Newton까지 거슬러 올라간다. 그는 1669년 《De Analysi》에서 일반화된 이항정리

$$(1+x)^\alpha = \sum_{n=0}^\infty \binom{\alpha}{n}x^n, \qquad \binom{\alpha}{n}=\frac{\alpha(\alpha-1)\cdots(\alpha-n+1)}{n!}$$

를 무한급수로 자유롭게 다루며 계산의 동력으로 삼았다 [8]. 정수가 아닌 $\alpha$에서는 이 급수가 다항식으로 끝나지 않고 무한히 이어지므로, "어디서 수렴하는가"라는 질문이 비로소 절실해진다. 그 답은 계수의 증가 속도 하나로 완전히 결정된다.

**Theorem (Cauchy–Hadamard).** For the power series $\sum a_n(x-c)^n$, set
$$\frac{1}{R} := \limsup_{n\to\infty}\vert a_n\vert^{1/n} \qquad (\text{with } 1/0:=\infty,\ 1/\infty:=0).$$
Then the series converges absolutely for $\vert x-c\vert<R$ and diverges for $\vert x-c\vert>R$. The number $R\in[0,\infty]$ is the *radius of convergence*.

*Proof.* $x$를 고정하고 $b_n:=a_n(x-c)^n$에 root test를 적용하면

$$\limsup_{n\to\infty}\vert b_n\vert^{1/n} = \vert x-c\vert\,\limsup_{n\to\infty}\vert a_n\vert^{1/n} = \frac{\vert x-c\vert}{R}$$

이다. 이 값이 $1$보다 작으면(즉 $\vert x-c\vert<R$) root test에 의해 $\sum b_n$은 절대수렴하고, $1$보다 크면($\vert x-c\vert>R$) 일반항이 $0$으로 가지 않아 발산한다. $\blacksquare$

Cauchy–Hadamard 공식을 몇 가지에 적용해보자.

**Example ($R=\infty$).** $\sum_{n=0}^\infty \dfrac{x^n}{n!}$에서는 $(n!)^{1/n}\to\infty$이므로 $\vert a_n\vert^{1/n}=(1/n!)^{1/n}\to0$, 즉 $R=\infty$이다. 실직선 전체에서 수렴하며 이것이 $e^x$의 급수다.

**Example ($R=0$).** $\sum_{n=0}^\infty n!\,x^n$에서는 거꾸로 $(n!)^{1/n}\to\infty$라 $1/R=\infty$, 즉 $R=0$이다. $x=0$ 말고는 어디서도 수렴하지 않는다.

**Example ($\limsup$이 필요한 경우).** $\sum_{n=0}^\infty \big(3+(-1)^n\big)^n x^n$에서는 계수의 $n$제곱근 $3+(-1)^n$이 $n$의 홀짝에 따라 $2$와 $4$를 오가고 그 $\limsup$은 $4$이므로 $R=1/4$이다. 계수의 비 $a_{n+1}/a_n$은 진동해 ratio test로는 값이 안 나오지만, $\limsup$을 쓰는 Cauchy–Hadamard는 곧바로 $R$을 준다.

수렴반지름을 계수만으로 주는 이 공식은 Cauchy가 처음 적었고 Hadamard가 다시 정리해 두 사람의 이름이 붙었다 [5]. 수렴반지름 안쪽에서 멱급수는 단순히 수렴하는 데 그치지 않고, uniform convergence까지 누린다. 이것이 멱급수를 항별로 미분하고 적분할 수 있게 해주는 열쇠다.

**Theorem.** Suppose $\sum a_n(x-c)^n$ has radius of convergence $R>0$, with sum $f(x)$ on $(c-R,c+R)$. Then:
1. The series converges uniformly on every closed interval $[c-r,c+r]$ with $0<r<R$.
2. $f$ is of class $C^\infty$ on $(c-R,c+R)$, and may be differentiated and integrated term by term:
$$f'(x)=\sum_{n=1}^\infty n\,a_n(x-c)^{n-1}, \qquad \int_c^x f(t)\,dt=\sum_{n=0}^\infty \frac{a_n}{n+1}(x-c)^{n+1}.$$
3. The differentiated series has the same radius of convergence $R$, and consequently $a_n=\dfrac{f^{(n)}(c)}{n!}$.

*Proof.* **(1)** $0<r<R$에 대해 $r<\rho<R$인 $\rho$를 잡으면 $\sum a_n\rho^n$이 절대수렴하므로 $\vert a_n\vert\rho^n$은 유계다. $\vert x-c\vert\le r$이면

$$\vert a_n(x-c)^n\vert \le \vert a_n\vert r^n = \vert a_n\vert\rho^n\left(\frac{r}{\rho}\right)^n$$

인데 $r/\rho<1$이라 우변은 수렴하는 등비급수로 지배된다. 지난 글의 Weierstrass M-test에 의해 멱급수는 $[c-r,c+r]$에서 uniformly 수렴한다.

**(3, 먼저)** 미분된 급수 $\sum n a_n(x-c)^{n-1}$의 수렴반지름은 $\limsup\vert n a_n\vert^{1/n}=\limsup\vert a_n\vert^{1/n}$($n^{1/n}\to1$이므로)이라 원래와 같은 $R$이다. 따라서 미분된 급수도 (1)에 의해 컴팩트한 부분구간에서 uniformly 수렴한다.

**(2)** $[c-r,c+r]$에서 원래 급수가 수렴하고 항별로 미분한 급수가 uniformly 수렴하므로, 지난 글의 미분·극한 교환 정리를 부분합 $s_N$에 적용하면 $f$가 미분가능하고 $f'(x)=\sum n a_n(x-c)^{n-1}$이다. $f'$ 또한 같은 꼴의 멱급수이므로 같은 논증을 반복하면 $f$는 몇 번이든 미분가능하고, 각 도함수가 멱급수의 합으로 연속이다. 즉 $f\in C^\infty$이다. 항별 적분도 마찬가지로 uniform convergence에서 나오는 지난 글의 항별 적분 정리로 얻는다.

**(3, 계수)** $f^{(n)}(x)=\sum_{m\ge n} m(m-1)\cdots(m-n+1)a_m(x-c)^{m-n}$에 $x=c$를 대입하면 $m=n$ 항만 남아 $f^{(n)}(c)=n!\,a_n$이다. $\blacksquare$

세 번째 결론이 특히 중요하다. 멱급수의 계수는 그 합함수의 도함수 값으로 유일하게 결정되므로, 한 함수를 중심 $c$에서 멱급수로 나타내는 방법은 (있다면) 오직 하나뿐이다. 이 유일성은 다음과 같이 훨씬 강한 형태로 성립한다.

**Theorem (Identity Theorem).** Suppose $\sum a_n(x-c)^n$ and $\sum b_n(x-c)^n$ both have positive radius of convergence, and their sums agree at every point of a sequence $$(x_k)_{k=1}^\infty$$ with $x_k\to c$ and $x_k\ne c$. Then $a_n=b_n$ for all $n$.

*Proof.* $d_n:=a_n-b_n$, $h(x):=\sum_{n=0}^\infty d_n(x-c)^n$이라 하자. $h$는 공통 수렴구간에서 멱급수의 합이므로 연속이고, 가정에서 모든 $k$에 대해 $h(x_k)=0$이다. $x_k\to c$이고 $h$가 연속이므로 $d_0=h(c)=\lim_k h(x_k)=0$이다. $d_0=0$이니 $h(x)=(x-c)\,h_1(x)$로 쓸 수 있는데, 여기서 $h_1(x):=\sum_{n=0}^\infty d_{n+1}(x-c)^n$은 계수를 한 칸 민 것이라 $\limsup\vert d_{n+1}\vert^{1/n}=\limsup\vert d_n\vert^{1/n}$에 의해 같은 수렴반지름을 가진 멱급수이고, 따라서 연속이다. $x_k\ne c$에서 $h_1(x_k)=h(x_k)/(x_k-c)=0$이므로 다시 $d_1=h_1(c)=\lim_k h_1(x_k)=0$이다. 이를 반복하면 모든 $n$에서 $d_n=0$, 즉 $a_n=b_n$이다. $\blacksquare$

즉 두 멱급수가 $c$로 다가가는 점렬 위에서만 같아도(하물며 한 구간에서 같으면 당연히) 계수가 통째로 일치한다. 특히 어떤 근방에서 합이 항등적으로 $0$이면 모든 계수가 $0$이다.

멱급수끼리의 곱도 계수 수준에서 깔끔하게 닫힌다.

**Theorem (멱급수의 곱).** Suppose $f(x)=\sum_{n=0}^\infty a_n(x-c)^n$ and $g(x)=\sum_{n=0}^\infty b_n(x-c)^n$ both converge for $\vert x-c\vert<r$. Then for $\vert x-c\vert<r$,
$$f(x)g(x)=\sum_{n=0}^\infty c_n(x-c)^n, \qquad c_n=\sum_{k=0}^n a_k b_{n-k},$$
and this series also converges for $\vert x-c\vert<r$. The coefficients $c_n$ are the *Cauchy product* of $$(a_n)$$ and $$(b_n)$$.

*Proof.* Cauchy–Hadamard 정리에서 보았듯 수렴반지름 안에서 멱급수는 절대수렴하므로, $\vert x-c\vert<r$에서 이중합 $\sum_{i,j}a_ib_j(x-c)^{i+j}$의 절댓값 합은 $\big(\sum_i\vert a_i\vert\vert x-c\vert^i\big)\big(\sum_j\vert b_j\vert\vert x-c\vert^j\big)<\infty$이다. 급수 글에서 본 대로 절대수렴하는 급수는 항을 어떤 순서로 더해도 같은 값이 되므로, 이 이중합을 전체 차수 $n=i+j$가 같은 것끼리 모으면 $(x-c)^n$의 계수가 $\sum_{k=0}^n a_kb_{n-k}=c_n$이 되어 주장한 식을 얻는다. $\blacksquare$

예를 들어 $\dfrac{1}{1-x}=\sum_{n=0}^\infty x^n$을 자기 자신과 곱하면 $c_n=\sum_{k=0}^n 1=n+1$이므로 $\dfrac{1}{(1-x)^2}=\sum_{n=0}^\infty (n+1)x^n$ ($\vert x\vert<1$)을 곧바로 얻는다.

경계 $\vert x-c\vert=R$에서는 (1)의 uniform convergence는커녕 pointwise convergence조차 보장되지 않는다. 경계점에서 급수는 수렴할 수도, 발산할 수도 있으며, 이는 전적으로 그 점에서 급수 자체가 어떻게 행동하느냐의 문제다.

**Example.** $\log(1+x)=\sum_{n=1}^\infty\frac{(-1)^{n-1}}{n}x^n$은 수렴반지름이 $1$이다. 두 경계점의 운명은 정반대다. $x=1$에서는 $\sum\frac{(-1)^{n-1}}{n}$이 alternating series로 수렴하지만, $x=-1$에서는 대입하면 $\sum\frac{(-1)^{n-1}}{n}(-1)^n=-\sum\frac1n$, 즉 harmonic series가 되어 발산한다. 같은 멱급수인데 한쪽 끝에서는 수렴하고 다른 쪽 끝에서는 발산하는 것이다.

경계에서 급수가 수렴할 때, 그 합이 안쪽에서 다가간 극한 $\lim_{x\to R^-}f(x)$와 실제로 일치하는지는 한 단계 더 미묘한 문제다. 경계점에서 급수가 수렴하면 그 합은 반드시 이 극한과 같다는 것이 Abel's theorem인데 [6], 증명은 이 글에서 다루지 않는다. 이를 $x=1$에 적용하면

$$1-\frac12+\frac13-\frac14+\cdots=\log 2, \qquad 1-\frac13+\frac15-\frac17+\cdots=\frac{\pi}{4}$$

같은 고전적 등식(뒤엣것은 Leibniz의 공식)이 정당화된다. 한 걸음 더 나아가 발산하는 경계 급수에까지 값을 배정하려는 물음은 Abel summation, Cesàro summation 같은 summability 이론으로 이어지며, Fourier 해석과 해석적 정수론에서 핵심 도구가 된다.

## Taylor 급수

멱급수의 계수가 $a_n=f^{(n)}(c)/n!$로 강제된다는 사실은, 거꾸로 임의의 $C^\infty$ 함수에 대해 그 도함수 값들로 멱급수를 써 볼 동기를 준다.

**Definition (Taylor Series).** For $f\in C^\infty$ near $c$, its *Taylor series* at $c$ is
$$\sum_{n=0}^\infty \frac{f^{(n)}(c)}{n!}(x-c)^n.$$
When $c=0$ this is also called the *Maclaurin series*.

함수를 그 도함수 값으로 이렇게 펼치는 공식은 1715년 Brook Taylor가 제시했고 [1], $c=0$인 특수한 경우를 널리 활용한 Colin Maclaurin의 이름이 그 형태에 남았다 [2]. 다만 두 사람은 이 급수가 수렴하는지, 수렴한다면 원래 함수와 같은지를 따지지 않았다. 실제로 이 급수가 (a) 수렴하는지, (b) 수렴한다면 그 합이 정말 $f$인지는 전혀 자명하지 않고, 이 두 질문을 가르는 것이 나머지항(remainder)이다.

**Theorem (Taylor's Theorem, Lagrange Remainder).** Let $f\in C^{n+1}$ on an open interval containing $c$ and $x$. Then there exists $\xi$ strictly between $c$ and $x$ such that
$$f(x) = \sum_{k=0}^n \frac{f^{(k)}(c)}{k!}(x-c)^k + \frac{f^{(n+1)}(\xi)}{(n+1)!}(x-c)^{n+1}.$$

*Proof.* $x$를 고정하고 상수 $M$을 $f(x)=\sum_{k=0}^n\frac{f^{(k)}(c)}{k!}(x-c)^k + M(x-c)^{n+1}$이 성립하도록 정한다. 이제

$$g(t):=f(x)-\sum_{k=0}^n\frac{f^{(k)}(t)}{k!}(x-t)^k - M(x-t)^{n+1}$$

로 두면 $g$는 $C^1$이고, $M$을 그렇게 잡았으므로 $g(c)=0$, 또 $(x-x)$ 항들이 사라져 $g(x)=0$이다. Rolle's Theorem에 의해 $c$와 $x$ 사이 어떤 $\xi$에서 $g'(\xi)=0$이다. $g'(t)$를 계산하면 합 부분이 망원경처럼 소거되어

$$g'(t) = -\frac{f^{(n+1)}(t)}{n!}(x-t)^n + M(n+1)(x-t)^n$$

만 남는다. $g'(\xi)=0$이고 $x-\xi\ne0$이므로 $M=\dfrac{f^{(n+1)}(\xi)}{(n+1)!}$이고, 이를 $M$의 정의에 넣으면 원하는 식을 얻는다. $\blacksquare$

나머지항을 이렇게 도함수 하나의 값으로 정량적으로 통제하는 형태는 Lagrange가 처음 주었다 [3]. 이는 어떻게 보면 mean value theorem의 일반화라고 할 수도 있다.

$n\to\infty$일 때 나머지항 $R_n(x)=\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-c)^{n+1}$이 $0$으로 가는 바로 그 $x$에서, 그리고 그때에만, Taylor 급수의 부분합이 $f(x)$로 수렴한다. 이 조건이 성립하는 함수에 특별한 이름을 준다.

**Definition (Real-Analytic).** $f$ is *real-analytic* at $c$ if there is a neighborhood of $c$ on which $f$ equals the sum of its Taylor series at $c$.

**Theorem.** $e^x$, $\sin x$, $\cos x$ are real-analytic on all of $\mathbb{R}$, with
$$e^x=\sum_{n=0}^\infty\frac{x^n}{n!}, \quad \sin x=\sum_{n=0}^\infty\frac{(-1)^n}{(2n+1)!}x^{2n+1}, \quad \cos x=\sum_{n=0}^\infty\frac{(-1)^n}{(2n)!}x^{2n}.$$

*Proof.* $f(x)=e^x$의 경우 $f^{(n+1)}=e^x$이므로, 임의의 $x$에 대해 $c=0$에서의 나머지항은 $0$과 $x$ 사이 어떤 $\xi$에 대해 $\vert R_n(x)\vert=\dfrac{e^\xi}{(n+1)!}\vert x\vert^{n+1}\le\dfrac{e^{\vert x\vert}\vert x\vert^{n+1}}{(n+1)!}$이다. 고정된 $x$에서 $\dfrac{\vert x\vert^{n+1}}{(n+1)!}\to0$이므로 $R_n(x)\to0$이고, 따라서 Taylor 급수가 $e^x$로 수렴한다. $\sin,\cos$은 도함수가 $\pm\sin,\pm\cos$을 순환해 항상 $\vert f^{(n+1)}\vert\le1$이므로 $\vert R_n(x)\vert\le\vert x\vert^{n+1}/(n+1)!\to0$으로 같은 결론을 얻는다. $\blacksquare$

수렴반지름이 유한한 예도 흔하다. $\dfrac{1}{1-x}=\sum_{n=0}^\infty x^n$은 $\vert x\vert<1$에서만 성립하는데, 좌변은 $x=1$을 뺀 실직선 전체에서 $C^\infty$인데도 멱급수는 반지름 $1$을 넘지 못한다. 수렴반지름이 $x=1$의 특이점까지 거리로 묶이기 때문인데, 이 현상은 함수를 복소평면으로 확장해야 온전히 설명된다.

이렇게 확보한 표준적인 전개들은 그 자체로 강력한 계산 도구가 된다. L'Hôpital's Rule로는 몇 번을 미분해도 풀리지 않는 극한이 Taylor 전개 앞에서는 계수 몇 개를 맞춰보는 산수로 끝나는 일이 흔하다.

**Example (Taylor 급수로 극한 계산).** 극한 $\displaystyle\lim_{x\to0}\left(\frac{\sin x}{x}\right)^{1/x^2}$을 보자. $x\to0$에서 밑은 $1$로, 지수는 $+\infty$로 가는 $1^\infty$ 꼴이라 값을 짐작하기 어렵다. 로그를 취한 뒤 위에서 얻은 $\sin$의 전개를 넣으면

$$\frac{\sin x}{x} = 1 - \frac{x^2}{6} + \frac{x^4}{120} - \cdots$$

이고, 여기에 $\log(1+u)=u-\frac{u^2}{2}+\cdots$를 $u=-\frac{x^2}{6}+\cdots$에 적용하면

$$\log\frac{\sin x}{x} = -\frac{x^2}{6} + O(x^4)$$

이다(여기서 $O(x^4)$는 $x^4$ 이상 차수의 항을 뭉뚱그린 것이다). 따라서

$$\frac{1}{x^2}\log\frac{\sin x}{x} = -\frac16 + O(x^2) \longrightarrow -\frac16 \quad (x\to0)$$

이고, 지수함수와 로그가 연속이므로 원래 극한은 $e^{-1/6}$이다. L'Hôpital's Rule을 아무리 반복해도 엄두가 안 나는 극한이 전개 계수 비교 몇 줄로 끝난다.

## 매끄럽지만 해석적이지 않은 함수

$C^\infty$와 real-analytic은 같지 않다. Taylor 급수가 멀쩡히 수렴하고도 원래 함수와 다른 함수로 수렴할 수 있다는 사실이 그 간극을 극적으로 보여준다.

**Example (Cauchy).** 
$$f(x):=\begin{cases} e^{-1/x^2} & x\ne0 \\ 0 & x=0\end{cases}$$
라 하자. 이 함수는 $\mathbb{R}$ 전체에서 $C^\infty$이고 모든 $n$에 대해 $f^{(n)}(0)=0$이다.

*확인.* $x\ne0$에서 귀납법으로 $f^{(n)}(x)=p_n(1/x)\,e^{-1/x^2}$ 꼴임을 보일 수 있다(여기서 $p_n$은 다항식). $t\to\infty$일 때 임의의 다항식보다 $e^{-t^2}$이 빨리 $0$으로 가므로 $\lim_{x\to0}p_n(1/x)e^{-1/x^2}=0$이고, 이를 차분몫에 쓰면 $f^{(n)}(0)=0$이 귀납적으로 따라온다.

따라서 $f$의 $0$에서의 Taylor 급수는 $\sum 0\cdot x^n=0$으로 모든 $x$에서 수렴하지만, $x\ne0$에서 그 합 $0$은 $f(x)=e^{-1/x^2}>0$과 다르다. $f$는 $0$에서 $C^\infty$이면서 real-analytic이 아니다. Taylor 정리와 나머지항 논의를 오늘날 수준의 엄밀함으로 세우고, 바로 이 예로 "$C^\infty$이지만 해석적이지 않은" 세계를 분명히 드러낸 사람이 Cauchy다 [4].

이 예는 결코 병리적 예외가 아니다. Borel은 훨씬 강한 사실을 증명했다.

**Theorem (Borel).** For every sequence $$(a_n)_{n=0}^\infty$$ of real numbers, there exists a $C^\infty$ function $f$ on $\mathbb{R}$ with $f^{(n)}(0)=a_n$ for all $n$.

즉 도함수 값들은 아무렇게나 주어져도 좋고, 그것들이 만드는 Taylor 급수의 수렴반지름이 $0$이어도 상관없이 그런 $C^\infty$ 함수가 항상 존재한다 [7]. $C^\infty$라는 조건은 함수의 국소적 형태를 거의 아무것도 옭아매지 못하는 반면, real-analytic이라는 조건은 한 점 근방의 도함수 값들만으로 함수 전체를 못박는다. 이 대비가 실해석과 복소해석을 가르는 근본적인 분기점 중 하나다.

## 참고문헌

1. Taylor, B. (1715). *Methodus Incrementorum Directa et Inversa*. London.
2. Maclaurin, C. (1742). *A Treatise of Fluxions*. Edinburgh.
3. Lagrange, J.-L. (1797). *Théorie des fonctions analytiques*. Paris.
4. Cauchy, A.-L. (1823). *Résumé des leçons données à l'École royale polytechnique sur le calcul infinitésimal*. Paris.
5. Hadamard, J. (1888). Sur le rayon de convergence des séries ordonnées suivant les puissances d'une variable. *Comptes rendus de l'Académie des sciences*, 106, 259–262.
6. Abel, N. H. (1826). Untersuchungen über die Reihe $1+\frac{m}{1}x+\frac{m(m-1)}{1\cdot2}x^2+\cdots$. *Journal für die reine und angewandte Mathematik*, 1, 311–339.
7. Borel, É. (1895). Sur quelques points de la théorie des fonctions. *Annales scientifiques de l'École Normale Supérieure*, 12, 9–55.
8. Newton, I. (written 1669, published 1711). *De Analysi per Aequationes Numero Terminorum Infinitas*. London.
