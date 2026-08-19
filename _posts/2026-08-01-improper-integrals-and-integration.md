---
layout: post
title: "Improper Integral과 적분 계산"
date: 2026-08-01
mathematicians: [Cauchy, Liouville, Risch, Gauss, Hadamard, de la Vallée Poussin, Euler, Legendre, Fagnano, Abel, Jacobi, Weierstrass, Fresnel, Dirichlet]
---

## Improper integral

**Definition.** If $f$ is integrable on $[a,t]$ for every $t>a$, define

$$\int_a^\infty f := \lim_{t\to\infty} \int_a^t f$$

when this limit exists, in which case the improper integral *converges* (otherwise it *diverges*). ($\int_{-\infty}^b f$도 대칭적으로 정의된다.)

**Example.** $\displaystyle\int_1^\infty 1\,dx$는 수렴하지 않는다.

*Proof.* 상수함수의 적분은 (Darboux sum에서 바로 나오듯) 그 값에 구간 길이를 곱한 것이므로 $\int_1^t 1\,dx = t-1$인데, $t\to\infty$일 때 $\infty$로 발산한다. $\blacksquare$

**Example.** $\displaystyle\int_0^\infty e^{-x}\,dx = 1$.

*Proof.* $G(x):=-e^{-x}$라 하면 $G'(x)=e^{-x}$이므로, 미적분학의 기본정리, Part 2에 의해 $\int_0^t e^{-x}\,dx = G(t)-G(0) = 1-e^{-t}$이다. $t\to\infty$일 때 $e^{-t}\to0$이므로 $\int_0^\infty e^{-x}\,dx = 1$이다. $\blacksquare$

양쪽 끝이 모두 무한인 경우는 두 방향을 각각 독립적으로 처리해야 한다.

**Definition.** Let $f$ be integrable on $[s,t]$ for every $s<t$, and fix any $c\in\mathbb{R}$. If both $\int_{-\infty}^c f$ and $\int_c^\infty f$ converge, define

$$\int_{-\infty}^\infty f := \int_{-\infty}^c f + \int_c^\infty f.$$

유한 구간에서의 덧셈성에 의해 이 값은 $c$의 선택과 무관하다. 중요한 점은 두 극한이 *각각* 독립적으로 존재해야 한다는 것이다. 아래 예에서 보듯, 대칭적인 극한 $\lim_{R\to\infty}\int_{-R}^R f$ 하나만 존재하는 것으로는 부족하다.

**Example.** $\displaystyle\int_{-\infty}^\infty e^{-\vert x\vert}\,dx = 2$.

*Proof.* $x\ge0$에서 $e^{-\vert x\vert}=e^{-x}$이므로 위 예에 의해 $\int_0^\infty e^{-\vert x\vert}\,dx=1$이다. $x\le0$에서는 $e^{-\vert x\vert}=e^{x}$인데, 같은 방식으로 $\int_s^0 e^x\,dx = 1-e^s$이고 $s\to-\infty$일 때 $e^s\to0$이므로 $\int_{-\infty}^0 e^{-\vert x\vert}\,dx=1$이다. 두 극한이 모두 존재하므로 $\int_{-\infty}^\infty e^{-\vert x\vert}\,dx = 1+1=2$이다. $\blacksquare$

**Example.** $\displaystyle\int_{-\infty}^\infty x\,dx$는 수렴하지 않는다 (비록 $\displaystyle\lim_{R\to\infty}\int_{-R}^R x\,dx = 0$이지만).

*Proof.* $x$는 연속이므로 임의의 유한 구간에서 적분가능하고, ($\int_0^1 x^2\,dx$를 계산할 때와 같은 방식의 Darboux sum 계산으로) 일반적으로 $\int_a^b x\,dx = \dfrac{b^2-a^2}{2}$이다. 따라서 $\int_0^R x\,dx = R^2/2\to\infty$ ($R\to\infty$)이므로 $\int_0^\infty x\,dx$는 수렴하지 않고, 정의에 의해 $\int_{-\infty}^\infty x\,dx$도 수렴하지 않는다.

반면 $\int_{-R}^R x\,dx = \dfrac{R^2-R^2}{2}=0$이므로 $\displaystyle\lim_{R\to\infty}\int_{-R}^R x\,dx=0$은 존재한다. 이런 대칭적인 극한을 Cauchy principal value라 부르는데, 정의에서 요구하는 "두 극한이 각각 존재한다"는 것과는 다른, 더 약한 개념이다. $\blacksquare$

**Definition.** If $f$ is integrable on $[a+\varepsilon,b]$ for every $\varepsilon>0$ (but possibly unbounded near $a$), define

$$\int_a^b f := \lim_{\varepsilon\to0^+} \int_{a+\varepsilon}^b f$$

when this limit exists. (함수가 $b$ 근방에서 유계가 아닌 경우, 그리고 양 끝 모두인 경우도 대칭적으로 정의된다.)

**Example.** $\displaystyle\int_0^1 \frac{dx}{\sqrt x} = 2$.

*Proof.* $G(x):=2\sqrt x$라 하면 $G'(x)=1/\sqrt x$이므로, 같은 방식으로 $\int_\varepsilon^1 x^{-1/2}\,dx = 2-2\sqrt\varepsilon$이다. $\varepsilon\to0^+$일 때 $2\sqrt\varepsilon\to0$이므로 $\int_0^1 x^{-1/2}\,dx=2$이다. $\blacksquare$

**Example.** $\displaystyle\int_0^1 \frac{dx}{x}$는 수렴하지 않는다.

*Proof.* $G(x):=\ln x$라 하면 $G'(x)=1/x$이므로 $\int_\varepsilon^1 x^{-1}\,dx = -\ln\varepsilon$이다. $\varepsilon\to0^+$일 때 $-\ln\varepsilon\to\infty$이므로 $\int_0^1 x^{-1}\,dx$는 수렴하지 않는다. $\blacksquare$

구간의 끝이 아니라 **중간**에 특이점이 있는 경우도 똑같은 방식으로 처리한다.

**Definition.** Let $c\in(a,b)$, and suppose $f$ is integrable on $[a,c-\varepsilon]$ and on $[c+\varepsilon,b]$ for every $\varepsilon>0$ (즉 $c$ 근방에서만 유계가 아닐 수 있다). If both $\int_a^c f$ and $\int_c^b f$ (각각 $c$에서 특이점을 갖는, 앞의 정의에 의한 improper integral로) converge, define

$$\int_a^b f := \int_a^c f + \int_c^b f.$$

양 끝이 모두 무한인 경우와 정확히 같은 구조다. 여기서도 두 극한이 각각 독립적으로 존재해야 하며, 대칭적인 극한 $\displaystyle\lim_{\varepsilon\to0^+}\left[\int_a^{c-\varepsilon}f + \int_{c+\varepsilon}^b f\right]$ 하나만 존재하는 것으로는 부족하다 (이 역시 Cauchy principal value라 부른다).

**Example.** $\displaystyle\int_{-1}^1 \frac{dx}{x^{2/3}} = 6$.

*Proof.* $x^{-2/3}$은 짝함수다. $(-x)^{2/3}=x^{2/3}$이므로 $(-x)^{-2/3}=x^{-2/3}$이다. $G(x):=3x^{1/3}$이라 하면 $x>0$에서 $G'(x)=x^{-2/3}$이므로, 앞의 (구간 끝 특이점에 대한) 정의에 의해

$$\int_0^1 x^{-2/3}\,dx = \lim_{\varepsilon\to0^+}\int_\varepsilon^1 x^{-2/3}\,dx = \lim_{\varepsilon\to0^+}\big(G(1)-G(\varepsilon)\big) = \lim_{\varepsilon\to0^+}\big(3-3\varepsilon^{1/3}\big) = 3$$

이다. $x^{-2/3}$이 짝함수이므로 (치환 $x\mapsto-x$에 의해) $\int_{-1}^0 x^{-2/3}\,dx$도 같은 값 $3$을 갖는다. 두 극한이 모두 존재하므로 $\int_{-1}^1 x^{-2/3}\,dx = 3+3=6$이다. $\blacksquare$

## 비교판정법

**Proposition (비교판정법, Comparison Test).** Suppose $0\le f\le g$ on $[a,\infty)$, both integrable on $[a,t]$ for every $t>a$. If $\int_a^\infty g$ converges, then $\int_a^\infty f$ converges, and $\int_a^\infty f\le\int_a^\infty g$.

*Proof.* $F(t):=\displaystyle\int_a^t f$라 하면, $t_1<t_2$에 대해 $F(t_2)-F(t_1)=\displaystyle\int_{t_1}^{t_2}f\ge0$ ($f\ge0$이므로)이라 $F$는 (단조)증가한다. 또한 단조성에 의해 $F(t)\le\displaystyle\int_a^t g$인데, $\displaystyle\int_a^t g$ 자체도 $t$에 대해 증가하며 $t\to\infty$일 때 $G:=\displaystyle\int_a^\infty g$로 수렴하므로 $F(t)\le G$ (모든 $t$에서). 즉 $F$는 증가하고 위로 유계다.

$L:=\sup_{t\ge a}F(t)$ ($\le G$, 완비성에 의해 존재)라 하자. $\varepsilon>0$이 주어지면 $\sup$의 정의에 의해 $F(t_0)>L-\varepsilon$인 $t_0$가 있고, $F$가 증가하므로 $t\ge t_0$인 모든 $t$에서 $L-\varepsilon<F(t_0)\le F(t)\le L$이다. 즉 $F(t)\to L$ ($t\to\infty$), 그래서 $\int_a^\infty f=L\le G=\int_a^\infty g$이다. $\blacksquare$

이 정리는 유계가 아닌 함수의 improper integral에 대해서도 ($\varepsilon\to0^+$ 극한으로) 대칭적으로 성립한다.

## 적분 판정법

**Theorem (Integral Test).** Let $f:[1,\infty)\to\mathbb{R}$ be non-negative and monotonically decreasing, and integrable on $[1,t]$ for every $t>1$. Then $\displaystyle\sum_{n=1}^\infty f(n)$ converges if and only if $\displaystyle\int_1^\infty f$ converges.

*Proof.* $f$가 감소하므로 $n\le x\le n+1$에서 $f(n+1)\le f(x)\le f(n)$이고, 이를 $[n,n+1]$ 위에서 적분하면(단조성) $f(n+1)\le\displaystyle\int_n^{n+1}f\le f(n)$이다. $n=1,\ldots,N-1$에 대해 더하면 (선형성)

$$\sum_{n=2}^{N} f(n) \;\le\; \int_1^N f \;\le\; \sum_{n=1}^{N-1} f(n).$$

$f\ge0$이므로 부분합 $\sum_{n=1}^N f(n)$과 $\int_1^t f$는 각각 $N$, $t$에 대해 단조증가한다. 위 부등식이 이 두 양을 위아래로 묶어두고 있으므로, 한쪽이 유계(=수렴)인 것과 다른 쪽이 유계(=수렴)인 것이 동치다. $\int_1^t f$가 $t$에 대해서도 단조증가하므로, $t\to\infty$일 때의 수렴은 정수 $t=N\to\infty$에서의 수렴과 같다(그 사이의 값들은 양 정수에서의 값 사이에 끼여 있으므로). $\blacksquare$

**Example.** $\displaystyle\int_1^\infty \frac{dx}{x^p}$는 $p>1$이면 수렴하고 $p\le1$이면 발산한다.

*Proof.* $p\ne1$이면 $\displaystyle\int_1^t x^{-p}\,dx = \dfrac{t^{1-p}-1}{1-p}$인데, $t\to\infty$일 때 $t^{1-p}$는 $1-p<0$ (즉 $p>1$)이면 $0$으로, $1-p>0$ (즉 $p<1$)이면 $\infty$로 간다. $p=1$이면 $\displaystyle\int_1^t x^{-1}dx=\ln t\to\infty$이다. 따라서 수렴하는 것은 $p>1$일 때뿐이고, 그 값은 $\dfrac{1}{p-1}$이다. $\blacksquare$

$p$-급수 $\sum 1/n^p$의 수렴 조건($p>1$)과 정확히 같은 경계에서 수렴·발산이 갈리는데, 이는 우연이 아니라 위 Integral Test를 $f(x)=1/x^p$에 적용하면 바로 나오는 사실이다.

## 절대수렴과 조건수렴

**Definition (절대수렴, Absolute Convergence).** $\int_a^\infty f$ is *absolutely convergent* if $\int_a^\infty \vert f\vert$ converges (if it converges but is not absolutely convergent, it is *conditionally convergent*).

**Proposition.** If $\int_a^\infty f$ is absolutely convergent, then it converges, and $\left\vert\int_a^\infty f\right\vert \le \int_a^\infty \vert f\vert$.

*Proof.* $p:=\max(f,0)$, $q:=\max(-f,0)$이라 하면 $f=p-q$, $\vert f\vert=p+q$이고 $0\le p,q\le\vert f\vert$이다. $\varphi(s):=\max(s,0)$은 연속이므로, 연속함수와 적분가능함수의 합성도 적분가능하다는 사실에 의해 $f$가 $[a,t]$에서 적분가능할 때마다 $p=\varphi\circ f$, $q=\varphi\circ(-f)$도 $[a,t]$에서 적분가능하다. $\int_a^\infty\vert f\vert$가 수렴한다고 가정했으므로, $0\le p,q\le\vert f\vert$에 위의 Comparison Test를 적용하면 $\int_a^\infty p$와 $\int_a^\infty q$가 모두 수렴한다. 따라서

$$\int_a^\infty f = \lim_{t\to\infty}\int_a^t f = \lim_{t\to\infty}\left(\int_a^t p-\int_a^t q\right) = \int_a^\infty p - \int_a^\infty q$$

도 수렴한다. 또한 모든 유한한 $t$에서 (지난 적분 글에서 본) $\left\vert\int_a^t f\right\vert\le\int_a^t\vert f\vert$인데, 양변이 $t\to\infty$일 때 극한을 가지므로 부등식이 극한에서도 유지되어 $\left\vert\int_a^\infty f\right\vert\le\int_a^\infty\vert f\vert$이다. $\blacksquare$

**Example.** $\displaystyle\int_1^\infty \frac{\cos x}{x^2}\,dx$는 절대수렴한다.

*Proof.* $\left\vert\dfrac{\cos x}{x^2}\right\vert\le\dfrac1{x^2}$이고, $G(x):=-1/x$가 $x^{-2}$의 부정적분이므로 미적분학의 기본정리, Part 2에 의해 $\int_1^t x^{-2}\,dx=1-1/t\to1$이라 $\int_1^\infty x^{-2}\,dx$가 수렴한다. 위의 Comparison Test에 의해 $\displaystyle\int_1^\infty\left\vert\frac{\cos x}{x^2}\right\vert\,dx$가 수렴하므로, $\int_1^\infty \cos x/x^2\,dx$는 절대수렴한다. $\blacksquare$

역은 성립하지 않는다. 수렴하지만 절대수렴하지는 않는(조건수렴하는) improper integral이 있다.

**Example.** $\displaystyle\int_0^\infty \frac{\sin x}{x}\,dx$는 수렴하지만 절대수렴하지 않는다. ($x=0$에서 $\sin x/x\to1$이므로 $[0,1]$ 위의 적분은 그냥 연속함수의 보통 적분이고, 핵심 부분은 $[1,\infty)$뿐이다.)

*Proof (수렴).* $(fg)'=f'g+fg'$이므로 (Integration by Parts, $$\int_a^b fg' = [fg]_a^b - \int_a^b f'g$$를 쓰면) $f(x):=1/x$, $g(x):=-\cos x$로 $[1,t]$에서

$$\int_1^t \frac{\sin x}{x}\,dx = \left[-\frac{\cos x}{x}\right]_1^t - \int_1^t \frac{\cos x}{x^2}\,dx = \cos1-\frac{\cos t}{t}-\int_1^t\frac{\cos x}{x^2}\,dx$$

이다. $t\to\infty$일 때 $\cos t/t\to0$이고, 위 예와 앞의 Proposition에 의해 $\int_1^\infty \cos x/x^2\,dx$가 수렴한다. 따라서 우변이 $t\to\infty$에서 극한을 가지므로 $\int_1^\infty \sin x/x\,dx$가 수렴한다.

*Proof (절대수렴하지 않음).* $\vert\sin x\vert$는 주기 $\pi$를 가지므로($\sin(x+\pi)=-\sin x$) $\int_{n\pi}^{(n+1)\pi}\vert\sin x\vert\,dx=\int_0^\pi\sin t\,dt=2$가 모든 정수 $n\ge1$에서 성립한다. $[n\pi,(n+1)\pi]$에서는 $x\le(n+1)\pi$이므로

$$\int_{n\pi}^{(n+1)\pi}\frac{\vert\sin x\vert}{x}\,dx \ge \frac{1}{(n+1)\pi}\int_{n\pi}^{(n+1)\pi}\vert\sin x\vert\,dx = \frac{2}{(n+1)\pi}$$

이고, $n=1,\ldots,N-1$에 대해 더하면

$$\int_\pi^{N\pi}\frac{\vert\sin x\vert}{x}\,dx \ge \frac2\pi\sum_{n=1}^{N-1}\frac1{n+1} = \frac2\pi\sum_{k=2}^N \frac1k$$

인데, 우변은 지난 급수 글에서 본 조화급수의 부분합(첫 항 제외)이라 $N\to\infty$일 때 $\infty$로 간다. 따라서 $\int_1^\infty\vert\sin x/x\vert\,dx$는 발산한다. $\blacksquare$

## 부정적분 계산

**Example.** For $x>0$, $\displaystyle\int_1^x \ln t\,dt = x\ln x-x+1$.

*Proof.* Integration by Parts를 $f(t):=\ln t$, $g(t):=t$ (즉 $g'(t)=1$, $f'(t)=1/t$)로 $[1,x]$에서 적용하면

$$\int_1^x \ln t\cdot1\,dt = \big[t\ln t\big]_1^x - \int_1^x \frac1t\cdot t\,dt = x\ln x - 1\cdot\ln1 - \int_1^x 1\,dt = x\ln x-(x-1) = x\ln x-x+1$$

이다. $\blacksquare$

**Example.** For $x\in(-1,1)$, $\displaystyle\int_0^x \frac{dt}{\sqrt{1-t^2}} = \arcsin x$.

*Proof.* $g(\theta):=\sin\theta$ ($\theta\in(-\pi/2,\pi/2)$에서 $C^1$이고 $g'(\theta)=\cos\theta$, 치역은 $(-1,1)$)라 하고 $f(t):=\dfrac{1}{\sqrt{1-t^2}}$라 하자. $\theta\in(-\pi/2,\pi/2)$에서 $\cos\theta>0$이므로 $\sqrt{1-\sin^2\theta}=\cos\theta$이고,

$$f(g(\theta))g'(\theta) = \frac{\cos\theta}{\sqrt{1-\sin^2\theta}} = \frac{\cos\theta}{\cos\theta} = 1.$$

Substitution Rule에서 구간을 $[0,\arcsin x]$로 두면 ($g(0)=0$, $g(\arcsin x)=x$)

$$\int_0^x \frac{dt}{\sqrt{1-t^2}} = \int_{g(0)}^{g(\arcsin x)} f(t)\,dt = \int_0^{\arcsin x} f(g(\theta))g'(\theta)\,d\theta = \int_0^{\arcsin x} 1\,d\theta = \arcsin x$$

이다. $\blacksquare$

**Example.** $\displaystyle\int_0^x \frac{dt}{1+t^2} = \arctan x$.

*Proof.* $g(\theta):=\tan\theta$ ($\theta\in(-\pi/2,\pi/2)$에서 $C^1$이고 $g'(\theta)=\sec^2\theta=1+\tan^2\theta$, 치역은 $\mathbb{R}$ 전체)라 하고 $f(t):=\dfrac{1}{1+t^2}$라 하면

$$f(g(\theta))g'(\theta) = \frac{1+\tan^2\theta}{1+\tan^2\theta} = 1$$

이므로, Substitution Rule에서 구간을 $[0,\arctan x]$로 두면 ($g(0)=0$, $g(\arctan x)=x$)

$$\int_0^x \frac{dt}{1+t^2} = \int_0^{\arctan x} 1\,d\theta = \arctan x$$

이다. $\blacksquare$

조금 색다른 예로, $\sec x$의 부정적분은 그것을 찾아내는 과정 자체가 꽤 기교적인 것으로 유명하다.

**Example.** For $x\in(-\pi/2,\pi/2)$, $\displaystyle\int_0^x \sec\theta\,d\theta = \ln(\sec x+\tan x)$.

*Proof.* $u(\theta):=\sec\theta+\tan\theta$라 하면, $(-\pi/2,\pi/2)$에서 $u(\theta)=\dfrac{1+\sin\theta}{\cos\theta}>0$이므로($\cos\theta>0$이고 $1+\sin\theta>0$) $\ln u(\theta)$가 정의된다. 분자·분모에 $u(\theta)$를 곱하면

$$\sec\theta = \sec\theta\cdot\frac{\sec\theta+\tan\theta}{\sec\theta+\tan\theta} = \frac{\sec^2\theta+\sec\theta\tan\theta}{u(\theta)} = \frac{u'(\theta)}{u(\theta)}$$

인데(분자가 정확히 $u'(\theta)=\sec\theta\tan\theta+\sec^2\theta$와 일치한다), 이는 $\dfrac{d}{d\theta}\ln u(\theta) = \sec\theta$라는 말이므로 $\ln u$는 $\sec\theta$의 한 부정적분이다. 미적분학의 기본정리, Part 2에 의해

$$\int_0^x \sec\theta\,d\theta = \ln u(x) - \ln u(0) = \ln(\sec x+\tan x) - \ln(1+0) = \ln(\sec x+\tan x)$$

이다. $\blacksquare$

## 초등함수로 표현되지 않는 적분

미분은 초등함수를 초등함수로 보내지만, 적분은 그렇지 않다. 초등함수의 부정적분이 초등함수가 아닌 경우가 매우 많은데, 먼저 초등함수가 무엇인지부터 정확히 해두자.

**Definition (Elementary Function).** An *elementary function* is one built from polynomials, the exponential and logarithmic functions, and the trigonometric functions with their inverses, by finitely many arithmetic operations and compositions.

어떤 초등함수의 부정적분이 다시 초등함수인지 아닌지는 Joseph Liouville가 세운 정밀한 판정 기준으로 가릴 수 있고 [1], Robert Risch가 이를 기계적으로 판정하는 알고리즘으로 발전시켰다 [2]. 아래에 소개하는 함수들은 모두 그 부정적분이 초등함수가 아니며, 자주 등장하는 만큼 고유한 이름이 붙어 있다.

**Definition (Error Function).** $\displaystyle\operatorname{erf}(x):=\frac{2}{\sqrt\pi}\int_0^x e^{-t^2}\,dt.$

$e^{-x^2}$의 부정적분이 초등함수가 아니라서 이렇게 따로 이름을 붙였으며, 확률의 정규분포에서 핵심적으로 쓰인다.

**Definition (Sine Integral).** $\displaystyle\operatorname{Si}(x):=\int_0^x \frac{\sin t}{t}\,dt.$

**Definition (Fresnel Integrals).** $\displaystyle S(x):=\int_0^x \sin(t^2)\,dt, \qquad C(x):=\int_0^x \cos(t^2)\,dt.$

광학의 회절 이론에서 나온다. 진폭은 줄지 않는데도 $t^2$ 때문에 진동이 점점 빨라져, $\int_0^\infty \sin(x^2)\,dx=\int_0^\infty \cos(x^2)\,dx=\frac{1}{2}\sqrt{\frac{\pi}{2}}$로 (절대수렴은 아니지만) 수렴한다.

**Definition (Logarithmic Integral).** $\displaystyle\operatorname{li}(x):=\int_0^x \frac{dt}{\ln t}$ (여기서 $t=1$의 특이점은 principal value로 처리한다).

$\dfrac{1}{\ln x}$의 부정적분인 이 함수는 다음 정리를 통해 정수론의 심장부에 닿는다.

**Theorem (Prime Number Theorem).** Let $\pi(x)$ denote the number of primes not exceeding $x$. Then $\pi(x)\sim\operatorname{li}(x)$ as $x\to\infty$, that is, $\pi(x)/\operatorname{li}(x)\to1$ (equivalently, $\pi(x)\sim x/\ln x$).

Carl Friedrich Gauss가 소수의 분포를 $\operatorname{li}(x)$로 근사할 수 있으리라 추측했고 [3], Jacques Hadamard와 Charles-Jean de la Vallée Poussin이 1896년에 독립적으로 증명했다 [4, 5]. 초등적으로 적분되지 않는 함수가 소수의 개수라는 전혀 다른 문제의 답을 준다는 점이 인상적이다.

역사적으로 가장 유명한 예는 elliptic integral이다.

**Definition (Elliptic Integral).** An *elliptic integral* is an integral of the form $\int R\big(t,\sqrt{P(t)}\big)\,dt$, where $R$ is a rational function and $P$ is a cubic or quartic polynomial with no repeated root. Apart from degenerate cases such integrals are not elementary.

이름은 타원에서 나왔다. 타원 $x=a\cos\theta$, $y=b\sin\theta$의 넓이는 $\pi ab$로 쉽게 구하지만, 둘레의 길이 $\int\sqrt{a^2\sin^2\theta+b^2\cos^2\theta}\,d\theta$는 위 꼴의 elliptic integral이라 초등함수로 나오지 않는다. 특히 lemniscate(방정식 $(x^2+y^2)^2=x^2-y^2$)의 호의 길이에서 나오는 $\displaystyle\varphi(x):=\int_0^x \frac{dt}{\sqrt{1-t^4}}$ (즉 $P(t)=1-t^4$)가 역사적으로 결정적인 역할을 했다.

Giulio Fagnano는 이 적분에서 놀라운 규칙을 발견했다. 원에서 $\int_0^r\frac{dt}{\sqrt{1-t^2}}=\arcsin r$이 배각 공식 $2\arcsin r=\arcsin\!\big(2r\sqrt{1-r^2}\big)$을 만족하듯, $\varphi$도 배각 공식을 갖는다는 것이다 [6]. 이를 눈여겨본 Leonhard Euler는 그것이 훨씬 일반적인 덧셈정리의 특수한 경우임을 간파했다.

**Theorem (Euler's Addition Theorem).** For $\displaystyle\varphi(x):=\int_0^x \frac{dt}{\sqrt{1-t^4}}$, one has $\varphi(x)+\varphi(y)=\varphi(z)$ where

$$z=\frac{x\sqrt{1-y^4}+y\sqrt{1-x^4}}{1+x^2 y^2}.$$

원의 $\arcsin x+\arcsin y=\arcsin\!\big(x\sqrt{1-y^2}+y\sqrt{1-x^2}\big)$과 정확히 같은 꼴로, 두 적분의 합이 상한을 $x,y$의 **대수적** 함수로 갖는 하나의 적분으로 묶인다. $x=y$로 두면 Fagnano가 먼저 발견했던 배각 공식 $z=\frac{2x\sqrt{1-x^4}}{1+x^4}$이 된다. Euler는 이를 분모에 일반적인 4차식의 제곱근이 오는 elliptic integral로까지 확장했다 [7].

Adrien-Marie Legendre는 40년 넘게 매달려 모든 elliptic integral을 세 가지 표준형으로 환원하고 방대한 수치표를 만들었다 [8]. 하지만 적분을 상한의 함수로 본 $\varphi(x)$는 초등함수도 아니고, 이 형태 그대로는 덧셈정리 말고는 뚜렷한 구조가 잘 드러나지 않았다.

돌파구는 관점을 뒤집는 데서 나왔다. 원에서 $\arcsin$의 역함수가 다루기 좋은 $\sin$이었듯, elliptic integral도 그 **역함수**를 보자는 것이다. 그 역함수를 복소평면 전체로 확장하면 다음 성질을 갖는다.

**Definition (Elliptic Function).** A meromorphic function $f$ on $\mathbb{C}$ is *elliptic* (doubly periodic) if there exist $\omega_1,\omega_2\in\mathbb{C}$, linearly independent over $\mathbb{R}$, such that $f(z+\omega_1)=f(z+\omega_2)=f(z)$ for all $z$.

$\sin$은 주기가 $2\pi$ 하나뿐이지만 elliptic function은 서로 독립인 두 주기를 가져, 함숫값이 복소평면을 $\omega_1,\omega_2$가 만드는 평행사변형 격자를 따라 반복된다. 실변수 함수는 상수가 아닌 한 이런 두 주기를 가질 수 없으니, 이중주기성은 적분의 역함수를 복소수까지 밀어붙였을 때 비로소 드러나는 성질이다. 1827년과 1829년 사이 Niels Henrik Abel과 Carl Gustav Jacob Jacobi가 거의 동시에 이 아이디어를 밀어붙여 elliptic function 이론을 열었다 [9][10]. 가난 속에 스물여섯으로 요절한 Abel과 그와 우선권을 다투던 Jacobi가 불과 몇 달 사이로 결과를 쏟아낸 이 경쟁은 수학사의 유명한 장면이다 (사실 Gauss는 이미 수십 년 전 개인 노트에 같은 것을 적어두고도 발표하지 않았다).

이 이론의 대표 함수가 Karl Weierstrass의 $\wp$-함수다.

**Definition (Weierstrass $\wp$-function).** For a lattice consisting of the points $\omega=m\omega_1+n\omega_2$ ($m,n\in\mathbb{Z}$),

$$\wp(z):=\frac{1}{z^2}+\sum_{\omega\ne0}\left(\frac{1}{(z-\omega)^2}-\frac{1}{\omega^2}\right),$$

the sum ranging over the nonzero lattice points.

이는 각 격자점에서 이차 pole을 갖는 elliptic function이며, 다음을 만족한다.

**Theorem.** $\wp$ satisfies the differential equation $(\wp')^2=4\wp^3-g_2\wp-g_3$ for constants $g_2,g_3$ determined by the lattice. Consequently $\displaystyle z=\int_{\wp(z)}^{\infty}\frac{dt}{\sqrt{4t^3-g_2 t-g_3}}$, so that $\wp$ is the inverse of this elliptic integral.

$y=\sin z$가 $(y')^2=1-y^2$을 만족해 $\arcsin y=\int_0^y\frac{dt}{\sqrt{1-t^2}}$를 뒤집은 것과 똑같은 구조로, $\sin$에서 원 $\sqrt{1-t^2}$이 놓이던 자리에 삼차곡선 $\sqrt{4t^3-g_2 t-g_3}$이 들어간 셈이다. 초등함수로 표현되지 않는 적분 하나가 완전히 새로운 함수의 세계로 가는 문이었던 것이다.

## 정적분 계산

아래 적분들의 값을 얻으려면 복소해석의 residue, 매개변수 미분, Fourier 해석 같은 더 깊은 도구가 필요하므로 증명은 생략한다.

**Theorem (Gaussian Integral).** $\displaystyle\int_{-\infty}^\infty e^{-x^2}\,dx = \sqrt\pi$.

*Proof (수렴).* $e^{-x^2}$은 연속이라 $[-1,1]$에서의 적분은 유한하다. $x\ge1$에서는 $x^2\ge x$이므로 $0<e^{-x^2}\le e^{-x}$인데, $\int_1^\infty e^{-x}\,dx=e^{-1}$이 수렴하므로 Comparison Test에 의해 $\int_1^\infty e^{-x^2}\,dx$가 수렴한다. $e^{-x^2}$이 짝함수이므로 $\int_{-\infty}^{-1}$ 쪽도 마찬가지이고, 따라서 $\int_{-\infty}^\infty e^{-x^2}\,dx$가 수렴한다. $\blacksquare$

값이 $\sqrt\pi$라는 것은 지금까지의 일변수 도구만으로는 얻기 어렵다. 적분을 제곱해 이중적분으로 올린 뒤 극좌표로 바꾸는 유명한 방법이 있는데, 이는 다변수 적분을 다루는 다른 글에서 계산하기로 하고 여기서는 결과만 쓴다. Gaussian integral은 확률론의 정규분포, 통계역학, Fourier 해석 등 곳곳에서 나타난다.

**Theorem.** For $n>1$, $\displaystyle\int_0^\infty \frac{dx}{1+x^n} = \frac{\pi/n}{\sin(\pi/n)}$.

수렴은 $x\ge1$에서 $\frac{1}{1+x^n}\le x^{-n}$과 Comparison Test로 바로 나온다. 앞의 arctan 계산에서 $x\to\infty$로 보내면 $\int_0^\infty \frac{dx}{1+x^2}=\dfrac{\pi}{2}$인데, 위 공식에 $n=2$를 넣은 $\dfrac{\pi/2}{\sin(\pi/2)}=\dfrac{\pi}{2}$와 정확히 일치한다.

**Theorem (Dirichlet Integral).** $\displaystyle\int_0^\infty \frac{\sin x}{x}\,dx = \frac{\pi}{2}$.

앞에서 이 적분이 조건수렴함은 이미 보였고, 그 값이 정확히 $\pi/2$이다. Fourier 해석과 신호 처리 곳곳에서 나타난다.

**Theorem.** $\displaystyle\int_0^{\pi/2} \ln(\sin x)\,dx = -\frac{\pi}{2}\ln 2$.

$x=0$에서 $\ln\sin x\to-\infty$인 특이점이 있지만 적분은 수렴하며, 값이 놀랍도록 단순하다.

**Theorem.** $\displaystyle\int_0^\infty \frac{x}{e^x-1}\,dx = \frac{\pi^2}{6}$.

지난 급수 글에서 본 Basel 문제의 값 $\zeta(2)=\pi^2/6$이 여기서도 나온다. 지수를 $x^3$으로 바꾼 $\int_0^\infty \frac{x^3}{e^x-1}\,dx=\dfrac{\pi^4}{15}$은 흑체 복사의 Stefan–Boltzmann 법칙(복사 에너지가 온도의 네제곱에 비례한다)의 바탕이 되는 적분이다.

## 참고문헌

1. Liouville, J. (1835). Mémoire sur l'intégration d'une classe de fonctions transcendantes. *Journal für die reine und angewandte Mathematik*, 13, 93–118.
2. Risch, R. H. (1969). The problem of integration in finite terms. *Transactions of the American Mathematical Society*, 139, 167–189.
3. Gauss, C. F. (1863). Brief an J. F. Encke (24. Dezember 1849). In *Werke*, Band 2 (pp. 444–447). Göttingen: Königliche Gesellschaft der Wissenschaften.
4. Hadamard, J. (1896). Sur la distribution des zéros de la fonction $\zeta(s)$ et ses conséquences arithmétiques. *Bulletin de la Société Mathématique de France*, 24, 199–220.
5. de la Vallée Poussin, C.-J. (1896). Recherches analytiques sur la théorie des nombres premiers. *Annales de la Société Scientifique de Bruxelles*, 20, 183–256.
6. Fagnano dei Toschi, G. C. (1750). *Produzioni matematiche* (2 vols.). Pesaro: Gavelli.
7. Euler, L. (1761). Observationes de comparatione arcuum curvarum irrectificabilium. *Novi Commentarii Academiae Scientiarum Petropolitanae*, 6, 58–84.
8. Legendre, A.-M. (1825–1828). *Traité des fonctions elliptiques et des intégrales eulériennes* (3 vols.). Paris: Huzard-Courcier.
9. Abel, N. H. (1827–1828). Recherches sur les fonctions elliptiques. *Journal für die reine und angewandte Mathematik*, 2, 101–181; 3, 160–190.
10. Jacobi, C. G. J. (1829). *Fundamenta nova theoriae functionum ellipticarum*. Königsberg: Borntraeger.
