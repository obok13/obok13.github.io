---
layout: post
title: "Uniform convergence"
date: 2026-08-02
mathematicians: [Weierstrass, Cauchy, Abel, Dini, Sergei Bernstein, Seidel, Stokes, Stone, Arzelà, Ascoli, Fourier, Cantor, Lebesgue, van der Waerden]
---

함수의 수열 $f_n$을 생각해보자. 각 $f_n$이 연속이거나 미분가능하거나 적분가능할 때, 그 극한 $f$도 그 성질을 물려받는가? 답은 "수렴을 어떻게 정의하느냐"에 달려 있다.

## Pointwise convergence

**Definition (Pointwise Convergence).** Let $f_n,f:E\to\mathbb{R}$. The sequence $$(f_n)_{n=1}^\infty$$ *converges pointwise* to $f$ on $E$ if $\lim_{n\to\infty}f_n(x)=f(x)$ for every $x\in E$.

즉 각 점 $x$를 고정할 때마다 실수열 $$(f_n(x))_{n=1}^\infty$$이 $f(x)$로 수렴한다는 뜻이다. 이것이 극한 함수를 정의하는 가장 소박한 방법이지만, 아래 예처럼 함수의 좋은 성질을 전혀 보존하지 못한다.

**Example (연속성이 깨진다).** $f_n(x):=x^n$ on $[0,1]$이라 하자. $0\le x<1$이면 $x^n\to0$이고 $x=1$이면 $x^n\to1$이므로, pointwise limit은

$$f(x)=\begin{cases}0 & 0\le x<1 \\ 1 & x=1\end{cases}$$

이다. 각 $f_n$은 연속이지만 극한 $f$는 $x=1$에서 불연속이다.

**Example (적분과 극한이 안 바뀐다).** 각 $n$에 대해 $[0,1]$ 위에서 $g_n$을 밑변 $[0,1/n]$, 높이 $2n$, 꼭짓점 $x=1/(2n)$인 이등변삼각형 모양의 연속함수로 두고 그 밖에서는 $0$이라 하자. 임의의 고정된 $x>0$에서는 $n$이 커지면 삼각형이 $x$의 왼쪽으로 빠져나가 $g_n(x)=0$이 되고 $x=0$에서도 $g_n(0)=0$이므로, $g_n\to0$으로 pointwise 수렴한다. 그러나 삼각형의 넓이는 항상 $\tfrac12\cdot\tfrac1n\cdot2n=1$이므로

$$\int_0^1 g_n = 1 \not\to 0 = \int_0^1 \lim_{n\to\infty} g_n.$$

극한과 적분의 순서를 바꿀 수 없다.

이 두 예가 보여주는 병리는 모두 "$N$을 얼마나 크게 잡아야 $f_n(x)$가 $f(x)$에 가까워지는가"가 점 $x$마다 제각각이라는 데서 온다. $x^n$의 경우 $x$가 $1$에 가까울수록 한없이 큰 $n$이 필요하다. 이 결함을 없앤 것이 uniform convergence이다.

## Uniform convergence

**Definition (Uniform Convergence).** $$(f_n)_{n=1}^\infty$$ *converges uniformly* to $f$ on $E$ if for every $\varepsilon>0$ there exists $N$ such that
$$\vert f_n(x)-f(x)\vert<\varepsilon \quad\text{for all } n\ge N \text{ and all } x\in E.$$

pointwise convergence의 정의와 글자는 거의 같지만 결정적 차이가 있다. pointwise convergence에서는 $N$이 $\varepsilon$과 $x$ 둘 다에 의존해도 되지만, uniform convergence에서는 하나의 $N$이 모든 $x$에 대해 동시에 통해야 한다.

함수해석적으로는 $E$ 위의 함수 $g$에 대해

$$\lVert g\rVert_E := \sup_{x\in E}\vert g(x)\vert$$

를 정의했을 때 uniform convergence는 곧 $\lVert f_n-f\rVert_E\to0$과 같은 말이다. 기하학적으로는, 극한 함수 $f$의 그래프 둘레에 폭 $2\varepsilon$짜리 띠를 두르면 충분히 큰 $n$부터 $f_n$의 그래프 전체가 그 띠 안에 들어간다는 뜻이다.

**Example.** 위의 $f_n(x)=x^n$은 $[0,1]$에서 uniformly 수렴하지 않는다. 극한 $f$에 대해 $0\le x<1$에서 $\vert f_n(x)-f(x)\vert=x^n$이고 $\sup_{0\le x<1}x^n=1$이므로 $\lVert f_n-f\rVert_{[0,1]}=1\not\to0$이다. 반면 $0<a<1$인 $[0,a]$로 정의역을 좁히면 $\lVert f_n-f\rVert_{[0,a]}=a^n\to0$이므로 uniformly 수렴한다. uniform convergence 여부는 정의역에 민감하다.

## Uniform Cauchy criterion

극한 함수를 미리 알지 못해도 uniform convergence를 판정할 수 있으면 유용하다. 수열의 완비성에서와 똑같은 역할을 하는 것이 다음 판정법이다.

**Theorem (Uniform Cauchy Criterion).** $$(f_n)_{n=1}^\infty$$ converges uniformly on $E$ to some function if and only if for every $\varepsilon>0$ there exists $N$ such that
$$\vert f_n(x)-f_m(x)\vert<\varepsilon \quad\text{for all } m,n\ge N \text{ and all } x\in E.$$

*Proof.* ($\Rightarrow$) $f_n\to f$ uniformly 수렴하면, $\varepsilon>0$에 대해 $n\ge N$이면 $\lVert f_n-f\rVert_E<\varepsilon/2$이 되는 $N$을 잡아 $m,n\ge N$에서 $\vert f_n(x)-f_m(x)\vert\le\vert f_n(x)-f(x)\vert+\vert f(x)-f_m(x)\vert<\varepsilon$을 얻는다.

($\Leftarrow$) 각 고정된 $x$에서 $$(f_n(x))_{n=1}^\infty$$은 실수의 Cauchy 수열이므로, 실수의 완비성에 의해 극한이 존재한다. 그 극한을 $f(x)$라 하면 $f_n\to f$ pointwise 수렴한다. 이제 $\varepsilon>0$에 대해 가정에서 $N$을 잡으면, $m,n\ge N$과 모든 $x$에서 $\vert f_n(x)-f_m(x)\vert<\varepsilon$이다. 여기서 $x$를 고정하고 $m\to\infty$로 보내면 $f_m(x)\to f(x)$이므로 $\vert f_n(x)-f(x)\vert\le\varepsilon$을 얻는다. 이것이 모든 $x$에서 성립하므로 $n\ge N$에서 $\lVert f_n-f\rVert_E\le\varepsilon$, 즉 $f_n\to f$ uniformly 수렴한다. $\blacksquare$

## Weierstrass M-test

함수들의 급수 $\sum_{n=1}^\infty f_n$은 부분합 $s_N:=\sum_{n=1}^N f_n$의 극한으로 정의한다. 급수의 uniform convergence는 다음의 단순하면서 강력한 판정법으로 대부분 처리된다.

**Theorem (Weierstrass M-test).** Suppose $\vert f_n(x)\vert\le M_n$ for all $x\in E$ and all $n$, and $\sum_{n=1}^\infty M_n<\infty$. Then $\sum_{n=1}^\infty f_n$ converges uniformly (and absolutely) on $E$.

*Proof.* $m<n$인 부분합의 차는 모든 $x\in E$에서

$$\left\vert s_n(x)-s_m(x)\right\vert = \left\vert\sum_{k=m+1}^n f_k(x)\right\vert \le \sum_{k=m+1}^n \vert f_k(x)\vert \le \sum_{k=m+1}^n M_k$$

이다. $\sum M_n$이 수렴하므로 그 꼬리합 $\sum_{k=m+1}^n M_k$은 $m,n$이 커지면 $0$으로 가고, 이는 $x$와 무관하므로 $$(s_N)$$은 Uniform Cauchy Criterion을 만족한다. 따라서 $\sum f_n$은 $E$에서 uniformly 수렴한다. $\blacksquare$

## 연속성의 보존

이제 uniform convergence가 실제로 좋은 성질을 보존함을 보인다. 먼저 연속성이다.

**Theorem.** Let $f_n\to f$ uniformly on $E$. If each $f_n$ is continuous at $x_0\in E$, then $f$ is continuous at $x_0$. In particular, a uniform limit of continuous functions is continuous.

*Proof.* $\varepsilon>0$이 주어졌다고 하자. uniform convergence에 의해 어떤 $n$을 골라 모든 $x\in E$에서 $\vert f_n(x)-f(x)\vert<\varepsilon/3$이 되게 할 수 있다. 이 $n$을 고정하면 $f_n$이 $x_0$에서 연속이므로, 어떤 $\delta>0$이 있어 $x\in E$이고 $\vert x-x_0\vert<\delta$이면 $\vert f_n(x)-f_n(x_0)\vert<\varepsilon/3$이다. 그러면 그런 $x$에 대해

$$\vert f(x)-f(x_0)\vert \le \vert f(x)-f_n(x)\vert + \vert f_n(x)-f_n(x_0)\vert + \vert f_n(x_0)-f(x_0)\vert < \frac{\varepsilon}{3}+\frac{\varepsilon}{3}+\frac{\varepsilon}{3}=\varepsilon$$

이므로 $f$는 $x_0$에서 연속이다. $\blacksquare$

첫 번째 예의 $x^n$은 정확히 이 정리의 대우다. 극한이 불연속이었으므로 그 수렴은 uniform convergence일 수 없었던 것이다.

사실 이 정리는 uniform convergence 개념이 왜 필요했는지를 보여주는 역사적 사건의 핵심에 놓여 있다. Cauchy는 1821년 《Cours d'analyse》에서 "수렴하는 연속함수 급수의 합은 연속이다"라고 정리로 적었다 [6]. 그러나 1826년 Abel은 삼각급수(Fourier 급수)

$$\sum_{n=1}^\infty \frac{(-1)^{n-1}}{n}\sin(nx) = \frac{x}{2} \quad (-\pi<x<\pi)$$

를 반례로 지적했다 [7]. 각 항은 연속이고 급수는 모든 점에서 수렴하지만, 그 합은 $x$가 $\pi$의 홀수배를 지날 때마다 뛰어 불연속이다. Cauchy의 급수가 pointwise convergence일 뿐 uniform convergence가 아니었기 때문이다. 이 역설을 해소한 것이 바로 두 수렴의 구별이었고, 1847년 Seidel과 Stokes가 독립적으로 그 조건을 짚었으며 [8][9] Weierstrass가 1850~60년대 강의에서 오늘날의 uniform convergence 개념으로 확립했다. 위 정리는 uniform convergence를 가정하면 Cauchy의 주장이 정확히 옳아짐을 말해준다.

이 정리는 또한 연속함수들의 공간을 하나의 거리공간으로 세우는 출발점이다. 연속함수는 닫힌구간에서 유계이므로(Extreme Value Theorem) $C[a,b]$(닫힌구간 위 연속함수들의 공간)의 함수는 $\lVert f\rVert_{[a,b]}$가 유한하고, $d(f,g):=\lVert f-g\rVert_{[a,b]}$는 $C[a,b]$ 위의 metric이 된다. 이 거리 아래에서 uniform convergence는 정확히 이 metric space에서의 수렴이고 uniform Cauchy criterion 덕분에 $C[a,b]$는 complete라는 것도 알 수 있다. 이 관점은 함수해석에서 본격적으로 전개되므로 여기서는 언급만 해둔다.


## 어디서도 미분 불가능한 연속함수

**Theorem (Weierstrass).** Let $0<a<1$ and let $b$ be an odd integer with $ab>1+\tfrac32\pi$. Then
$$W(x):=\sum_{n=0}^\infty a^n\cos(b^n\pi x)$$
is continuous on $\mathbb{R}$ but is differentiable at no point.

*연속성.* 각 항은 $\vert a^n\cos(b^n\pi x)\vert\le a^n$으로 지배되고 $0<a<1$이라 $\sum a^n<\infty$이므로, Weierstrass M-test에 의해 급수는 $\mathbb{R}$에서 uniformly 수렴한다. 부분합은 유한 개 연속함수의 합이라 연속이므로, 연속성 보존 정리에 의해 극한 $W$도 연속이다. $\blacksquare$

정작 놀라운 것은 $W$가 단 한 점에서도 미분 불가능하다는 사실이다. 직관은 이렇다. $n$이 커질수록 $\cos(b^n\pi x)$은 점점 빠르게 진동하는데, 진폭 $a^n$이 줄어드는 속도보다 진동수 $b^n$이 빨리 커지도록 $ab>1+\tfrac32\pi$를 걸어두면, 아무리 작은 $h$에 대해서도 차분몫 $\frac{W(x+h)-W(x)}{h}$을 지배하는 항이 계속 바뀌어 하나의 극한으로 모이지 못한다. 완전한 증명은 이 글의 도구를 넘어서므로 밝히고 넘어간다 [10]. 이것이 1872년 Weierstrass가 내놓아, "연속함수는 고립된 예외를 빼면 미분가능하리라"는 당대의 통념을 무너뜨린 유명한 반례다. 뒤에 van der Waerden은 $\cos$ 대신 가장 가까운 정수까지의 거리 함수 $\varphi(t):=\operatorname{dist}(t,\mathbb{Z})$를 써서

$$V(x):=\sum_{n=0}^\infty \frac{\varphi(2^n x)}{2^n}$$

라는 더 간단한 예를 주었는데 [11], $\vert\varphi(2^nx)/2^n\vert\le 2^{-n-1}$이라 연속성은 똑같이 M-test에서 곧바로 나온다.

### Cantor–Lebesgue function

**Construction.** $f_0(x):=x$에서 시작해, $[0,1]$ 위 연속함수열을

$$f_{n+1}(x):=\begin{cases}\tfrac12\,f_n(3x) & 0\le x\le\tfrac13,\\[4pt] \tfrac12 & \tfrac13\le x\le\tfrac23,\\[4pt] \tfrac12+\tfrac12\,f_n(3x-2) & \tfrac23\le x\le1\end{cases}$$

로 정의한다. 각 $f_n$은 연속이고 nondecreasing이며 $f_n(0)=0$, $f_n(1)=1$이다.

**Theorem.** 이 $$(f_n)_{n=0}^\infty$$은 $[0,1]$에서 어떤 연속함수 $c$로 uniformly 수렴한다. 극한 $c$를 Cantor–Lebesgue function이라 부른다 [12]. $c$는 nondecreasing이고 $c(0)=0$, $c(1)=1$이며 Cantor 집합의 여집합(제거된 가운데 삼등분 구간들, 길이의 합이 $1$)에서 국소적으로 상수다. $c$는 uniformly 연속까지는 만족하지만 Lipschitz 연속은 아니다.

*Proof.* $n\ge1$에서 가운데 구간 $[\tfrac13,\tfrac23]$에서는 $f_{n+1}=f_n=\tfrac12$이라 차가 $0$이고, 양옆 구간에서는 $f_{n+1}(x)-f_n(x)$이 각각 $\tfrac12\big(f_n-f_{n-1}\big)(3x)$와 $\tfrac12\big(f_n-f_{n-1}\big)(3x-2)$ 꼴이므로

$$\lVert f_{n+1}-f_n\rVert_{[0,1]}\le\tfrac12\,\lVert f_n-f_{n-1}\rVert_{[0,1]}$$

이다. 따라서 $\lVert f_{n+1}-f_n\rVert_{[0,1]}\le 2^{-n}\lVert f_1-f_0\rVert_{[0,1]}$이고 이 상한들의 합이 유한하므로 $$(f_n)$$은 Uniform Cauchy Criterion을 만족한다. 그러므로 $f_n\to c$ uniformly 수렴하고, 연속성 보존 정리에 의해 $c$가 연속이다. nondecreasing성, 끝점 값, 가운데 구간에서의 상수성은 모든 $f_n$이 공유하는 성질이라 극한에서도 유지된다. 특히 $c$는 닫힌구간 $[0,1]$ 위의 연속함수이므로 Heine–Cantor Theorem에 의해 uniformly 연속이다.

이제 $c$가 Lipschitz는 아님을 보이자. 구성에서 Cantor 집합을 덮는 $n$단계 구간 $[a,b]$(길이 $b-a=3^{-n}$)마다 $c$는 정확히 $c(b)-c(a)=2^{-n}$만큼 오른다. 그러면

$$\frac{\vert c(b)-c(a)\vert}{\vert b-a\vert}=\frac{2^{-n}}{3^{-n}}=\Big(\frac32\Big)^n\longrightarrow\infty \quad(n\to\infty)$$

이므로, 어떤 상수 $L$을 잡아도 $n$을 충분히 키우면 $\vert c(b)-c(a)\vert>L\vert b-a\vert$인 구간이 나온다. 즉 $c$는 어떤 Lipschitz 조건도 만족할 수 없다. $\blacksquare$

이 $c$는 단조증가하니 거의 모든 점에서 미분가능하고 그 도함수가 $0$인데도 $0$에서 $1$까지 올라가는, 이른바 singular function이다. 이 사실을 정확히 재려면 측도론이 필요하므로 다른 글로 미룬다.

## 적분과 극한의 교환

**Theorem.** Let $f_n$ be Riemann integrable on $[a,b]$ and $f_n\to f$ uniformly on $[a,b]$. Then $f$ is Riemann integrable on $[a,b]$ and
$$\lim_{n\to\infty}\int_a^b f_n = \int_a^b f = \int_a^b \Big(\lim_{n\to\infty} f_n\Big).$$

*Proof.* 먼저 $f$의 적분가능성을 보인다. $\varepsilon>0$이 주어지면 $\varepsilon_n:=\lVert f_n-f\rVert_{[a,b]}\to0$이므로 $\varepsilon_n<\varepsilon$인 $n$을 하나 고정할 수 있고, 모든 $x$에서 $f_n(x)-\varepsilon<f(x)<f_n(x)+\varepsilon$이다. 임의의 분할 $P$에 대해 각 소구간에서 $f$의 진동(oscillation)은 $f_n$의 진동보다 많아야 $2\varepsilon$만큼 크므로, upper sum과 lower sum에 대해

$$U(f,P)-L(f,P) \le \big(U(f_n,P)-L(f_n,P)\big) + 2\varepsilon(b-a)$$

가 성립한다. $f_n$이 적분가능하므로 Riemann 적분가능성의 판정조건에 의해 $U(f_n,P)-L(f_n,P)<\varepsilon$이 되는 분할 $P$가 있고, 그러면 $U(f,P)-L(f,P)<\varepsilon+2\varepsilon(b-a)$이다. $\varepsilon>0$이 임의였으므로 $f$는 적분가능하다.

수렴은 곧바로 나온다. 적분의 단조성에서

$$\left\vert \int_a^b f_n - \int_a^b f\right\vert = \left\vert\int_a^b (f_n-f)\right\vert \le \int_a^b \vert f_n-f\vert \le (b-a)\,\lVert f_n-f\rVert_{[a,b]} \to 0. \qquad\blacksquare$$

**Corollary (항별 적분).** If $f_n$ are Riemann integrable and $\sum_{n=1}^\infty f_n$ converges uniformly on $[a,b]$, then
$$\int_a^b \sum_{n=1}^\infty f_n = \sum_{n=1}^\infty \int_a^b f_n.$$

*Proof.* 부분합 $s_N=\sum_{n=1}^N f_n$은 적분가능하고 uniformly 수렴하므로 위 정리를 $s_N$에 적용하면 된다. $\blacksquare$

## 미분과 극한의 교환

미분은 사정이 다르다. $f_n\to f$의 uniform convergence만으로는 $f_n'\to f'$을 결코 보장하지 못한다.

**Example.** $f_n(x):=\dfrac{\sin(nx)}{\sqrt{n}}$이라 하자. $\lVert f_n\rVert_{\mathbb{R}}\le 1/\sqrt{n}\to0$이므로 $f_n\to0$으로 uniformly 수렴한다. 그러나 $f_n'(x)=\sqrt{n}\cos(nx)$이고, 예컨대 $x=0$에서 $f_n'(0)=\sqrt{n}\to\infty$이므로 $$(f_n')$$은 극한 $0=f'$은커녕 아무 데로도 수렴하지 않는다.

따라서 미분과 극한을 바꾸려면 극한 함수가 아니라 도함수열에 uniform convergence 조건을 걸어야 한다. 그러면 정작 원래 함수열은 한 점에서만 수렴해도 충분하다.

**Theorem.** Let $f_n$ be differentiable on $[a,b]$, suppose $$(f_n(x_0))_{n=1}^\infty$$ converges for some $x_0\in[a,b]$, and suppose $$(f_n')_{n=1}^\infty$$ converges uniformly on $[a,b]$. Then $$(f_n)$$ converges uniformly on $[a,b]$ to a function $f$, and $f$ is differentiable with
$$f'(x)=\lim_{n\to\infty} f_n'(x) \quad\text{for every } x\in[a,b].$$

*Proof.* $\varepsilon>0$이 주어졌다고 하자. $$(f_n(x_0))$$이 수렴하고 $$(f_n')$$이 uniformly 수렴하므로, 어떤 $N$이 있어 $m,n\ge N$이면 $\vert f_n(x_0)-f_m(x_0)\vert<\varepsilon$이고 모든 $t\in[a,b]$에서 $\vert f_n'(t)-f_m'(t)\vert<\varepsilon$이다. 함수 $f_n-f_m$은 미분가능하므로 Mean Value Theorem을 $[x,t]$(또는 $[t,x]$)에 적용하면, 임의의 $x,t\in[a,b]$에 대해 그 사이 어떤 점 $\xi$가 있어

$$\big(f_n(x)-f_m(x)\big)-\big(f_n(t)-f_m(t)\big) = \big(f_n'(\xi)-f_m'(\xi)\big)(x-t)$$

이고, 따라서

$$\left\vert \big(f_n(x)-f_m(x)\big)-\big(f_n(t)-f_m(t)\big)\right\vert \le \varepsilon\,\vert x-t\vert \le \varepsilon(b-a) \tag{$*$}$$

이다. $(*)$에서 $t:=x_0$으로 두면 $m,n\ge N$과 모든 $x$에서

$$\vert f_n(x)-f_m(x)\vert \le \vert f_n(x_0)-f_m(x_0)\vert + \varepsilon(b-a) < \varepsilon\big(1+(b-a)\big)$$

이므로 $$(f_n)$$은 Uniform Cauchy Criterion을 만족해 어떤 $f$로 uniformly 수렴한다.

이제 미분가능성을 보이자. $x\in[a,b]$를 고정하고, $t\ne x$에 대해

$$\varphi_n(t):=\frac{f_n(t)-f_n(x)}{t-x}, \qquad \varphi(t):=\frac{f(t)-f(x)}{t-x}$$

로 두자. $(*)$의 양변을 $\vert t-x\vert$로 나누면 $m,n\ge N$과 모든 $t\ne x$에서 $\vert\varphi_n(t)-\varphi_m(t)\vert\le\varepsilon$이므로, $$(\varphi_n)$$은 $$\{t\in[a,b]:t\ne x\}$$ 위에서 uniformly 수렴하고 그 극한은 $\varphi$이다. 한편 $f_n$이 $x$에서 미분가능하므로 $\lim_{t\to x}\varphi_n(t)=f_n'(x)$이다. uniformly 수렴하는 함수열은 극한 연산과 순서를 바꿀 수 있으므로(아래 Lemma), $\varphi$의 $t\to x$ 극한이 존재하고

$$f'(x)=\lim_{t\to x}\varphi(t) = \lim_{n\to\infty}\Big(\lim_{t\to x}\varphi_n(t)\Big) = \lim_{n\to\infty} f_n'(x)$$

이다. $\blacksquare$

이 증명에서 쓴 극한 교환은 연속성 보존 정리와 뿌리가 같은 다음 사실이다.

**Lemma (극한의 교환).** Let $g_n\to g$ uniformly on $E$, let $x_0$ be a limit point of $E$, and suppose $A_n:=\lim_{t\to x_0}g_n(t)$ exists for each $n$. Then $$(A_n)$$ converges and
$$\lim_{t\to x_0}g(t)=\lim_{n\to\infty}A_n, \quad\text{i.e.}\quad \lim_{t\to x_0}\lim_{n\to\infty}g_n(t)=\lim_{n\to\infty}\lim_{t\to x_0}g_n(t).$$

*Proof.* $\varepsilon>0$에 대해 균등 Cauchy 성질로 $m,n\ge N$에서 $\lVert g_n-g_m\rVert_E<\varepsilon$을 얻고, $t\to x_0$ 극한을 취하면 $\vert A_n-A_m\vert\le\varepsilon$이므로 $$(A_n)$$은 Cauchy, 즉 수렴한다. 그 극한을 $A$라 하자. 이제 $n$을 크게 잡아 $\lVert g_n-g\rVert_E<\varepsilon/3$이고 $\vert A_n-A\vert<\varepsilon/3$이 되게 하고, 이 $n$에 대해 $\lim_{t\to x_0}g_n(t)=A_n$이므로 $0<\vert t-x_0\vert$가 충분히 작으면 $\vert g_n(t)-A_n\vert<\varepsilon/3$이다. 그런 $t$에서

$$\vert g(t)-A\vert \le \vert g(t)-g_n(t)\vert+\vert g_n(t)-A_n\vert+\vert A_n-A\vert<\varepsilon$$

이므로 $\lim_{t\to x_0}g(t)=A$이다. $\blacksquare$

## Dini's Theorem

일반적으로 pointwise convergence는 uniform convergence보다 훨씬 약하지만, 조건이 갖춰지면 둘이 일치한다. 극한이 연속이고 수렴이 단조로우며 정의역이 닫힌구간이면 그렇다.

**Theorem (Dini).** Let $f_n:[a,b]\to\mathbb{R}$ be continuous and $f_n\to f$ pointwise with $f$ continuous. If $$(f_n(x))_{n=1}^\infty$$ is monotone in $n$ for each fixed $x$, then $f_n\to f$ uniformly on $[a,b]$.

*Proof.* $g_n:=\vert f_n-f\vert$라 하면 각 $g_n$은 연속이고 $g_n\to0$으로 pointwise 수렴하며, 단조성 가정에 의해 각 $x$에서 $$(g_n(x))$$은 $0$으로 감소한다(즉 $m\le n$이면 $g_m(x)\ge g_n(x)$). uniformly 수렴하지 않는다고 가정하자. 그러면 어떤 $\varepsilon>0$과 지표 $n_1<n_2<\cdots$ 및 점 $x_k\in[a,b]$가 있어 $g_{n_k}(x_k)\ge\varepsilon$이다. Bolzano–Weierstrass에 의해 $$(x_k)$$의 부분수열이 어떤 $x^*\in[a,b]$로 수렴하는데, 표기를 아껴 그 부분수열도 $x_k\to x^*$라 하자.

$m$을 하나 고정하자. $k$가 충분히 크면 $n_k\ge m$이므로 감소성에 의해 $g_m(x_k)\ge g_{n_k}(x_k)\ge\varepsilon$이다. $g_m$이 연속이므로 $k\to\infty$로 보내면 $g_m(x^*)=\lim_k g_m(x_k)\ge\varepsilon$이다. 이것이 모든 $m$에서 성립하므로 $g_m(x^*)\ge\varepsilon$인데, 이는 $g_m(x^*)\to0$과 모순이다. 따라서 $f_n\to f$ uniformly 수렴한다. $\blacksquare$

세 조건은 모두 필요하다. $[0,1]$에서 $f_n(x)=x^n$은 단조수렴하지만 극한이 불연속이라 uniformly 수렴하지 않고, 앞의 삼각형 예 $g_n$은 극한이 연속이지만 단조수렴이 아니라 uniformly 수렴하지 않는다. 정의역이 닫힌구간이라는 조건도 마찬가지로 뺄 수 없다.

**Example (정의역이 닫힌구간이 아니면 깨진다).** 같은 $f_n(x)=x^n$을 이번에는 열린구간 $(0,1)$ 위에서 보자. 고정된 $x\in(0,1)$에서 $x^n$은 $n$에 대해 감소하며 $0$으로 수렴하고, 그 극한 $f\equiv0$은 $(0,1)$에서 연속이다. 즉 각 $f_n$이 연속, 극한이 연속, 수렴이 단조라는 Dini의 가정 중 정의역이 닫혔다는 것만 빠졌다. 그런데 $\lVert f_n-f\rVert_{(0,1)}=\sup_{0<x<1}x^n=1\not\to0$이므로 $f_n$은 $(0,1)$에서 uniformly 수렴하지 않는다. $[0,1]$에서는 극한의 불연속이 문제였다면, 여기서는 극한이 연속인데도 수렴 속도를 좌우하는 '가장 나쁜' 점 $x=1$이 정의역에서 빠져 있어 하나의 $N$으로 묶을 수 없는 것이다. Dini's Theorem의 증명이 Bolzano–Weierstrass로 극한점 $x^*$를 정의역 안에 붙잡는 데 정의역의 닫힘과 유계를 쓴다는 점을 되짚어 보면, 이 가정이 어디서 본질적으로 개입하는지 분명해진다.

## Weierstrass Approximation Theorem

uniform convergence가 주는 가장 놀라운 결과 중 하나는, 아무리 복잡한 연속함수라도 다항식으로 원하는 만큼 uniformly 근사할 수 있다는 것이다.

**Theorem (Weierstrass Approximation).** For every continuous $f:[a,b]\to\mathbb{R}$ and every $\varepsilon>0$, there exists a polynomial $p$ such that
$$\sup_{x\in[a,b]}\vert f(x)-p(x)\vert<\varepsilon.$$
Equivalently, every continuous function on a closed bounded interval is a uniform limit of polynomials.

이 정리는 연속성만으로 다항식 근사가 가능함을 말한다. 미분가능성 같은 추가 조건은 전혀 필요 없어서, 어디서도 미분되지 않는 극단적으로 험한 연속함수조차 매끄러운 다항식들의 uniform limit으로 표현된다. Weierstrass가 1885년에 처음 증명했고 [1], Bernstein은 1912년에 근사하는 다항식을 명시적으로 써 내려가는 구성적 증명을 주었다 [2]. $[0,1]$ 위의 $f$에 대해 그 Bernstein polynomial

$$B_n(f)(x):=\sum_{k=0}^n f\!\left(\frac{k}{n}\right)\binom{n}{k}x^k(1-x)^{n-k}$$

이 $f$로 uniformly 수렴한다는 것이 그 내용이다. 증명은 확률론적으로 읽으면 자연스럽지만(이항분포의 대수의 법칙) 이 글의 도구를 넘어서므로 다른 글로 미룬다. 이 정리는 나중에 Stone에 의해 더 일반적인 정의역과, 다항식을 대신하는 함수 대수(subalgebra)로 크게 일반화되어 Stone–Weierstrass Theorem으로 불린다 [3].

## Arzelà–Ascoli

마지막으로, 어떤 함수열이 uniformly 수렴하는 부분수열을 가지려면 무엇이 필요한지 묻는 것은 자연스럽다. 실수열에서 그 답이 유계성(Bolzano–Weierstrass)이었다면, 함수열에서는 유계성만으로 부족하고 "함수들이 한꺼번에 고르게 연속"이라는 조건이 더 필요하다.

**Definition (Equicontinuity).** A family $\mathscr{F}$ of functions on $[a,b]$ is *equicontinuous* if for every $\varepsilon>0$ there exists $\delta>0$ such that $\vert f(x)-f(y)\vert<\varepsilon$ for all $f\in\mathscr{F}$ and all $x,y\in[a,b]$ with $\vert x-y\vert<\delta$.

정의에서 $\delta$가 점뿐 아니라 함수 $f$에도 무관하게 하나로 통한다는 점이 핵심이다. 이는 각 함수의 uniform continuity를 함수족 전체에 대해 한꺼번에 요구하는 것과 같다.

**Theorem (Arzelà–Ascoli).** A sequence of functions on $[a,b]$ has a uniformly convergent subsequence if and only if it is uniformly bounded and equicontinuous.

이 정리는 유계성만으로 부분수열의 수렴을 보장하던 유한차원의 직관이 함수공간에서 왜 무너지는지, 그리고 무엇을 보태야 회복되는지를 정확히 짚어준다. 증명은 유리수 점들에서 대각선 논법으로 수렴하는 부분수열을 뽑은 뒤 equicontinuity로 그 수렴을 구간 전체로 고르게 퍼뜨리는 방식으로 이루어지는데 [4][5], 이 글의 범위를 넘어 다른 글로 미룬다. 이 정리는 미분방정식 해의 존재성(Peano)이나 정규족(normal family) 이론 등 해석학 곳곳에서 수렴하는 부분수열을 뽑아내는 핵심 도구다.

## 참고문헌

1. Weierstrass, K. (1885). Über die analytische Darstellbarkeit sogenannter willkürlicher Functionen einer reellen Veränderlichen. *Sitzungsberichte der Königlich Preußischen Akademie der Wissenschaften zu Berlin*, 633–639, 789–805.
2. Bernstein, S. (1912). Démonstration du théorème de Weierstrass fondée sur le calcul des probabilités. *Communications de la Société mathématique de Kharkow*, 13, 1–2.
3. Stone, M. H. (1948). The Generalized Weierstrass Approximation Theorem. *Mathematics Magazine*, 21(4), 167–184; 21(5), 237–254.
4. Ascoli, G. (1883–1884). Le curve limiti di una varietà data di curve. *Atti della R. Accademia dei Lincei, Memorie della Cl. Sci. Fis. Mat. Nat.*, 18, 521–586.
5. Arzelà, C. (1895). Sulle funzioni di linee. *Memorie della R. Accademia delle Scienze dell'Istituto di Bologna*, 5(5), 55–74.
6. Cauchy, A.-L. (1821). *Cours d'analyse de l'École royale polytechnique*. Paris.
7. Abel, N. H. (1826). Untersuchungen über die Reihe $1+\frac{m}{1}x+\frac{m(m-1)}{1\cdot2}x^2+\cdots$. *Journal für die reine und angewandte Mathematik*, 1, 311–339.
8. Seidel, P. L. (1847). Note über eine Eigenschaft der Reihen, welche discontinuirliche Functionen darstellen. *Abhandlungen der Bayerischen Akademie der Wissenschaften*, 5, 379–394.
9. Stokes, G. G. (1847). On the critical values of the sums of periodic series. *Transactions of the Cambridge Philosophical Society*, 8, 533–583.
10. Weierstrass, K. (1872). Über continuirliche Functionen eines reellen Arguments, die für keinen Werth des letzteren einen bestimmten Differentialquotienten besitzen. In *Mathematische Werke*, Bd. II, 71–74. Berlin: Mayer & Müller, 1895.
11. van der Waerden, B. L. (1930). Ein einfaches Beispiel einer nicht-differenzierbaren stetigen Funktion. *Mathematische Zeitschrift*, 32, 474–475.
12. Cantor, G. (1884). De la puissance des ensembles parfaits de points. *Acta Mathematica*, 4, 381–392.
