---
layout: post
title: "함수의 극한과 연속성"
date: 2026-07-28
---

## 함수의 극한

**Definition (Limit of a Function).** Let $f$ be defined on a punctured neighborhood of $a$ (i.e., on some set containing points near $a$ other than possibly $a$ itself). $\lim_{x\to a} f(x) = L$ if for every $\varepsilon>0$ there exists $\delta>0$ such that $0<\vert x-a\vert<\delta$ implies $\vert f(x)-L\vert<\varepsilon$.

수열의 극한과 함수의 극한은 다음과 같이 연결된다.

**Proposition (Sequential Characterization).** $\lim_{x\to a} f(x) = L$ if and only if $f(x_n)\to L$ for every sequence $(x_n)$ with $x_n\ne a$ and $x_n\to a$.

*Proof.* ($\Rightarrow$) $\varepsilon>0$이 주어지면 $\delta>0$이 있어 $0<\vert x-a\vert<\delta \Rightarrow \vert f(x)-L\vert<\varepsilon$이다. $x_n\to a$, $x_n\ne a$이므로 어떤 $N$ 이후로 $0<\vert x_n-a\vert<\delta$가 되어 $\vert f(x_n)-L\vert<\varepsilon$이다. 따라서 $f(x_n)\to L$이다.

($\Leftarrow$) 대우를 보이자. $\lim_{x\to a}f(x)=L$이 아니라면, 어떤 $\varepsilon_0>0$이 있어 모든 $\delta>0$에 대해 $0<\vert x-a\vert<\delta$이면서 $\vert f(x)-L\vert\ge\varepsilon_0$인 $x$가 존재한다. $\delta=1/n$에 대해 이런 $x$를 $x_n$이라 잡으면 $0<\vert x_n-a\vert<1/n\to0$이므로 $x_n\to a$, $x_n\ne a$이지만 $\vert f(x_n)-L\vert\ge\varepsilon_0$이라 $f(x_n)\not\to L$이다. $\blacksquare$

**Proposition (극한의 사칙연산).** If $\lim_{x\to a}f(x)=L$ and $\lim_{x\to a}g(x)=M$, then $\lim_{x\to a}(f+g)(x)=L+M$ and $\lim_{x\to a}(fg)(x)=LM$; if moreover $M\ne0$, then $\lim_{x\to a}(f/g)(x)=L/M$.

*Proof.* $a$가 아니면서 $a$로 수렴하는 임의의 $(x_n)$에 대해 $f(x_n)\to L$, $g(x_n)\to M$이므로, 수열의 극한에 대한 사칙연산 법칙에 의해 $(f+g)(x_n)\to L+M$, $(fg)(x_n)\to LM$, ($M\ne0$이면) $(f/g)(x_n)\to L/M$이다. Sequential Characterization에 의해 원하는 결론을 얻는다. $\blacksquare$

**Definition (One-Sided Limits).** $\lim_{x\to a^+}f(x)=L$ if for every $\varepsilon>0$ there exists $\delta>0$ such that $a<x<a+\delta$ implies $\vert f(x)-L\vert<\varepsilon$. $\lim_{x\to a^-}f(x)=L$ is defined symmetrically, with $a-\delta<x<a$.

## 연속성

**Definition (Continuity).** $f$ is *continuous* at $a$ if $\lim_{x\to a}f(x) = f(a)$ (equivalently: for every $\varepsilon>0$ there exists $\delta>0$ such that $\vert x-a\vert<\delta$ implies $\vert f(x)-f(a)\vert<\varepsilon$). $f$ is continuous on a set $S$ if it is continuous at every point of $S$; at the endpoints of a closed interval $[a,b]$, continuity is judged using only the appropriate one-sided limit.

**Proposition (연속함수의 조합).** If $f,g$ are continuous at $a$, then $f+g$ and $fg$ are continuous at $a$, and $f/g$ is continuous at $a$ whenever $g(a)\ne0$. Moreover, if $f$ is continuous at $a$ and $g$ is continuous at $f(a)$, then the composition $g\circ f$ is continuous at $a$.

*Proof.* 앞부분은 극한의 사칙연산에서 $L=f(a)$, $M=g(a)$로 두면 바로 나온다. 합성함수 부분은 Sequential Characterization으로: $x_n\to a$이면 $f$의 연속성에 의해 $f(x_n)\to f(a)$이고, 이 수열에 다시 $g$의 연속성을 적용하면 $g(f(x_n))\to g(f(a))$이다. $\blacksquare$

## 중간값 정리

**Theorem (Intermediate Value Theorem).** Let $f:[a,b]\to\mathbb{R}$ be continuous, and let $y$ be a value between $f(a)$ and $f(b)$ (i.e., $f(a)<y<f(b)$ or $f(a)>y>f(b)$). Then there exists $c\in(a,b)$ such that $f(c)=y$.

*Proof.* $f(a)<y<f(b)$인 경우만 보면 충분하다 (반대 경우는 $-f$에 적용하면 된다). $$S:=\{x\in[a,b] : f(x)<y\}$$라 하자. $a\in S$이므로 $S\ne\emptyset$이고 $S$는 $b$로 위로 유계이므로, 실수의 완비성에 의해 $c:=\sup S$가 존재한다.

$f(c)<y$라 가정하자. $\varepsilon:=y-f(c)>0$에 대해 연속성으로부터 어떤 $\delta>0$이 있어 $\vert x-c\vert<\delta$이면 $f(x)<f(c)+\varepsilon=y$이다. $f(c)<y<f(b)$이므로 $c\ne b$, 즉 $c<b$이다. 따라서 $(c,\min(c+\delta,b))$에서 $x$를 하나 잡으면 $f(x)<y$이므로 $x\in S$인데 $x>c=\sup S$이므로 모순이다.

$f(c)>y$라 가정하자. $\varepsilon:=f(c)-y>0$에 대해 어떤 $\delta>0$이 있어 $\vert x-c\vert<\delta$이면 $f(x)>f(c)-\varepsilon=y$, 즉 $x\notin S$이다. $f(a)<y<f(c)$이므로 $c\ne a$, 즉 $c>a$이다. 따라서 $(\max(c-\delta,a),c]$의 모든 점이 $S$에 속하지 않으므로, $S$의 모든 원소는 $c-\delta$ 이하다. 이는 $c-\delta<c$가 $S$의 또다른 상계라는 뜻인데 $c=\sup S$(최소 상계)라는 사실에 모순이다.

따라서 $f(c)=y$이다. $f(a)<y=f(c)$이므로 $c\ne a$이고, $f(c)=y<f(b)$이므로 $c\ne b$이다. 즉 $c\in(a,b)$. $\blacksquare$

이 증명이 실수의 완비성(sup의 존재)을 직접 사용한다는 점을 눈여겨볼 만하다 — 유리수 위에서는 이 정리가 성립하지 않는다(예: $f(x)=x^2-2$는 $f(0)<0<f(2)$이지만 $f(c)=0$인 유리수 $c$는 없다).

이 정리를 처음 엄밀하게 증명한 사람은 Bolzano다 [1]. Cauchy도 1821년 *Cours d'analyse* 제2장에서 독립적으로 이 정리를 다뤘다 [2].

**Corollary.** Every odd-degree polynomial with real coefficients has at least one real root.

*Proof.* $p(x)=a_nx^n+\cdots+a_0$ ($n$은 홀수, $a_n\ne0$)이라 하자. $a_n>0$인 경우만 보면 충분하다 ($a_n<0$이면 $-p$에 적용). $p(x)=x^n\left(a_n+\dfrac{a_{n-1}}{x}+\cdots+\dfrac{a_0}{x^n}\right)$인데, $\vert x\vert\to\infty$일 때 괄호 안은 $a_n$으로 수렴하므로, 충분히 큰 $\vert x\vert$에서 괄호 안의 부호는 $a_n>0$과 같다. $n$이 홀수이므로 $x^n$의 부호는 $x$의 부호와 같으므로, 충분히 큰 $b>0$에서 $p(b)>0$이고 충분히 작은(즉 절댓값이 큰 음수) $a<0$에서 $p(a)<0$이다. $p$는 다항함수라 연속이므로, Intermediate Value Theorem에 의해 $p(c)=0$인 $c\in(a,b)$가 존재한다. $\blacksquare$

**Corollary.** If $f:[a,b]\to[a,b]$ is continuous, then there exists $c\in[a,b]$ such that $f(c)=c$ (a *fixed point*).

*Proof.* $g(x):=f(x)-x$라 하면 $g$는 연속함수의 조합이므로 연속이다. $f(a)\in[a,b]$이므로 $g(a)=f(a)-a\ge0$이고, $f(b)\in[a,b]$이므로 $g(b)=f(b)-b\le0$이다. 둘 중 하나가 $0$이면 그 점이 고정점이다. 그렇지 않다면 $g(a)>0>g(b)$이므로, Intermediate Value Theorem에 의해 $g(c)=0$인 $c\in(a,b)$가 존재하고, 이는 $f(c)=c$란 뜻이다. $\blacksquare$

이 결과는 Brouwer Fixed Point Theorem의 $1$차원(구간) 버전이다. 일반적인 Brouwer의 정리는 임의의 유한차원에서 성립하지만, 그 증명은 대수적 위상수학(algebraic topology)의 도구가 필요할 만큼 훨씬 어렵다.

## 극값 정리

**Theorem (Extreme Value Theorem).** If $f:[a,b]\to\mathbb{R}$ is continuous, then $f$ attains a maximum and a minimum value on $[a,b]$ — i.e., there exist $c,d\in[a,b]$ such that $f(c)\le f(x)\le f(d)$ for all $x\in[a,b]$.

*Proof.* 먼저 $f$가 위로 유계임을 보이자. 그렇지 않다면 각 $n$에 대해 $f(x_n)>n$인 $x_n\in[a,b]$가 존재한다. $(x_n)$은 $[a,b]$에 속하는 유계수열이므로, 지난 글의 Bolzano–Weierstrass Theorem에 의해 수렴하는 부분수열 $x_{n_k}\to c$가 있고, $[a,b]$가 닫힌구간이므로 $c\in[a,b]$이다. $f$의 연속성에 의해 $f(x_{n_k})\to f(c)$인데, $f(x_{n_k})>n_k\to\infty$이므로 이는 유계인 수렴 수열이 될 수 없어 모순이다. 따라서 $f$는 위로 유계이고, 대칭적으로 아래로도 유계이다.

이제 $M:=\sup_{x\in[a,b]} f(x)$라 하자 (위로 유계인 공집합이 아닌 집합이므로 완비성에 의해 존재). $\sup$의 정의상 각 $n$에 대해 $f(x_n)>M-1/n$인 $x_n\in[a,b]$가 존재하는데, 항상 $f(x_n)\le M$이므로 $f(x_n)\to M$이다. Bolzano–Weierstrass에 의해 $x_{n_k}\to d\in[a,b]$인 부분수열이 있고, 연속성에 의해 $f(x_{n_k})\to f(d)$이다. 그런데 $f(x_{n_k})\to M$이기도 하므로 (수렴하는 수열의 부분수열은 같은 값으로 수렴) $f(d)=M$이다. 즉 $f$는 $d$에서 최댓값 $M$을 가진다. 최솟값도 $-f$에 같은 논증을 적용하면 얻는다. $\blacksquare$

이 정리는 Bolzano에 의해 1830년에 엄밀하게 증명되었고 한참 뒤인 1930년에 출판되었다 [3]. Weierstrass는 이를 일반적인 compact space로 확장한 형태를 1860년대에 증명했다고 알려져 있다.

## 균등연속성과 Lipschitz 연속성

**Definition (Uniform Continuity).** $f$ is *uniformly continuous* on $S$ if for every $\varepsilon>0$ there exists $\delta>0$ such that for all $x,y\in S$, $\vert x-y\vert<\delta$ implies $\vert f(x)-f(y)\vert<\varepsilon$.

보통의 연속성과 다른 점은 $\delta$가 있는 위치다 — 연속성의 정의에서는 $\delta$가 $\varepsilon$뿐 아니라 점 $a$에도 의존해도 되지만, 균등연속성에서는 $S$ 전체에서 통하는 $\delta$ 하나를 $\varepsilon$만 보고 잡아야 한다. 정의에서 바로, 균등연속이면 (각 점에서) 연속이다.

역은 성립하지 않는다. $f(x)=x^2$은 $\mathbb{R}$에서 연속이지만 균등연속은 아니다 — $\varepsilon_0=1$을 고정하면, 임의의 $\delta>0$에 대해 $x:=1/\delta$, $y:=x+\delta/2$로 두면 $\vert x-y\vert=\delta/2<\delta$이지만

$$f(y)-f(x) = (y-x)(y+x) = \frac{\delta}{2}\left(\frac2\delta+\frac\delta2\right) = 1+\frac{\delta^2}4 > 1$$

이라, 어떤 $\delta$를 잡아도 $\varepsilon_0=1$에 대한 균등연속성의 조건을 깨는 $x,y$가 있다.

그런데 닫힌유계구간 위에서는 이 간극이 사라진다.

**Theorem (Heine–Cantor Theorem [4]).** If $f:[a,b]\to\mathbb{R}$ is continuous, then $f$ is uniformly continuous on $[a,b]$.

*Proof.* 그렇지 않다고 가정하면, 어떤 $\varepsilon_0>0$이 있어 각 $n$에 대해 $\vert x_n-y_n\vert<1/n$이지만 $\vert f(x_n)-f(y_n)\vert\ge\varepsilon_0$인 $x_n,y_n\in[a,b]$가 존재한다. Bolzano–Weierstrass에 의해 $(x_n)$은 수렴하는 부분수열 $x_{n_k}\to c\in[a,b]$를 가지는데, $\vert y_{n_k}-c\vert \le \vert y_{n_k}-x_{n_k}\vert+\vert x_{n_k}-c\vert \to 0$이므로 $y_{n_k}\to c$이기도 하다. $f$의 연속성에 의해 $f(x_{n_k})\to f(c)$, $f(y_{n_k})\to f(c)$이므로 $\vert f(x_{n_k})-f(y_{n_k})\vert\to0$인데, 이는 모든 $k$에서 $\vert f(x_{n_k})-f(y_{n_k})\vert\ge\varepsilon_0$이라는 사실에 모순이다. $\blacksquare$

균등연속성보다도 더 강한 조건이 하나 더 있다.

**Definition (Lipschitz Continuity [5]).** $f$ is *Lipschitz continuous* on $S$ if there exists $K\ge0$ such that $\vert f(x)-f(y)\vert \le K\vert x-y\vert$ for all $x,y\in S$.

이런 $K$ 중 가장 작은 값

$$K_f := \sup_{\substack{x,y\in S \\ x\ne y}} \frac{\vert f(x)-f(y)\vert}{\vert x-y\vert}$$

을 $f$의 *Lipschitz constant*라 부른다. 이 sup이 유한하다는 것 자체가 $f$가 Lipschitz 연속이라는 것과 동치이고, 그 경우 $K_f$ 자신도 정의를 만족하는 $K$가 된다 (즉 최소상계이자 동시에 실제로 달성 가능한 값).

**Proposition.** If $f$ is Lipschitz continuous on $S$, then $f$ is uniformly continuous on $S$.

*Proof.* $K=0$이면 $f$는 상수함수라 자명하다. $K>0$이면, $\varepsilon>0$에 대해 $\delta:=\varepsilon/K$로 두면 $\vert x-y\vert<\delta$일 때 $\vert f(x)-f(y)\vert \le K\vert x-y\vert < K\delta=\varepsilon$이다. 이 $\delta$는 점의 위치와 무관하므로 균등연속성의 정의를 만족한다. $\blacksquare$

역시 역은 성립하지 않는다. $f(x)=\sqrt{x}$는 $[0,1]$에서 (닫힌유계구간 위의 연속함수이므로 Heine–Cantor Theorem에 의해) 균등연속이지만, Lipschitz 연속은 아니다. 만약 어떤 $K$에 대해 모든 $x\in[0,1]$에서 $\sqrt{x}=\vert\sqrt x-\sqrt0\vert\le K\vert x-0\vert=Kx$가 성립한다면, 양변을 $\sqrt x>0$으로 나눠 $1\le K\sqrt x$, 즉 모든 $x>0$에 대해 $x\ge 1/K^2$이어야 하는데, $x:=1/(4K^2)<1/K^2$을 대입하면 모순이다. 따라서 그런 $K$는 존재하지 않는다.

## 단조함수의 불연속점

단조함수는 일반적인 함수보다 불연속점이 훨씬 제한적이다. 그 이유는 단조함수의 한쪽 극한이 언제나 존재하기 때문이다.

**Proposition.** Let $f:(a,b)\to\mathbb{R}$ be monotonically increasing. Then for every $x\in(a,b)$, the one-sided limits $f(x^-):=\lim_{t\to x^-}f(t)$ and $f(x^+):=\lim_{t\to x^+}f(t)$ both exist, and $f(x^-) \le f(x) \le f(x^+)$.

*Proof.* $$\{f(t):t<x\}$$는 $f(x)$로 위로 유계이므로 완비성에 의해 $L:=\sup_{t<x}f(t)$가 존재하고 $L\le f(x)$이다. $\varepsilon>0$이 주어지면 $\sup$의 정의에 의해 어떤 $t_0<x$가 있어 $f(t_0)>L-\varepsilon$이고, $t_0<t<x$인 모든 $t$에 대해 단조성에 의해 $L-\varepsilon<f(t_0)\le f(t)\le L$이므로 $f(t)\to L$ ($t\to x^-$), 즉 $f(x^-)=L\le f(x)$이다. 오른쪽 극한도 $\inf_{t>x}f(t)$에 대해 대칭적인 논증으로 $f(x)\le f(x^+)$를 얻는다. $\blacksquare$

특히 $f$가 $x$에서 연속인 것과 $f(x^-)=f(x)=f(x^+)$인 것은 동치이므로, $x$가 불연속점이면 반드시 $f(x^-)<f(x^+)$(진짜 "jump")이다.

**Theorem. [6,8]** If $f:(a,b)\to\mathbb{R}$ is monotonic, then the set of points of $(a,b)$ at which $f$ is discontinuous is countable.

*Proof.* $f$가 증가하는 경우만 보면 충분하다 (감소하면 $-f$에 적용하면 된다). $x$가 불연속점이면 $$I_x:=(f(x^-),f(x^+))$$는 공집합이 아닌 열린구간이다. $x<y$가 둘 다 불연속점이라 하자. $(x,y)$의 아무 점 $t$에 대해서나 단조성에 의해 $f(x^+)=\inf_{s>x}f(s)\le f(t) \le \sup_{s<y}f(s)=f(y^-)$이므로 $f(x^+)\le f(y^-)$, 즉 $I_x$와 $I_y$는 서로 겹치지 않는다.

$\mathbb{Q}$는 $\mathbb{R}$에서 조밀하므로 각 $I_x$는 유리수를 적어도 하나 포함하는데, 서로 다른 불연속점의 $I_x$들이 겹치지 않으므로 이렇게 고른 유리수들도 서로 다르다. 즉 불연속점들의 집합에서 $\mathbb{Q}$로 가는 단사함수가 존재하므로, 이 집합은 가산(countable)이다. $\blacksquare$

## 반연속성

연속성보다 약한 반연속성이라는 개념도 있다 [7]. 이를 정의하려면 $\limsup$, $\liminf$ 개념을 함수에도 옮겨와야 한다.

**Definition ($\limsup$, $\liminf$ of a Function).** Let $f$ be defined on a punctured neighborhood of $a$. Then

$$\limsup_{x\to a} f(x) := \inf_{\delta>0}\Big(\sup_{0<\vert x-a\vert<\delta} f(x)\Big), \qquad \liminf_{x\to a} f(x) := \sup_{\delta>0}\Big(\inf_{0<\vert x-a\vert<\delta} f(x)\Big),$$

**Proposition.** $\liminf_{x\to a}f(x)\le\limsup_{x\to a}f(x)$

**Proposition.** $\lim_{x\to a}f(x)=L$ iff $\limsup_{x\to a}f(x)=\liminf_{x\to a}f(x)=L$.

**Definition (Upper/Lower Semicontinuity).** $f:S\to\mathbb{R}$ is *upper semicontinuous* (USC) at $a\in S$ if $\limsup_{x\to a} f(x) \le f(a)$. $f$ is *lower semicontinuous* (LSC) at $a$ if $\liminf_{x\to a} f(x) \ge f(a)$. $f$ is USC (or LSC) on $S$ if it is so at every point of $S$.

**Proposition.** $f$ is USC at $a$ iff for all $\varepsilon > 0$, there exists $\delta > 0$ such that $\vert x-a\vert < \delta$ $\Rightarrow$ $f(x) < f(a) + \varepsilon$.

LSC에 대해 비슷한 명제가 성립한다.

**Proposition.** $f$ is continuous at $a$ if and only if $f$ is both upper and lower semicontinuous at $a$.

*Proof.* 항상 $\liminf_{x\to a}f(x)\le\limsup_{x\to a}f(x)$이다. $f$가 USC이면 $\limsup\le f(a)$이고 LSC이면 $\liminf\ge f(a)$이므로, 둘 다 성립하면 $f(a)\le\liminf\le\limsup\le f(a)$가 되어 $\liminf=\limsup=f(a)$, 즉 $f$는 $a$에서 연속이다. 역으로 $f$가 연속이면 $\limsup=\liminf=f(a)$이므로 두 조건이 모두 성립한다. $\blacksquare$

반연속성을 생각해보는 이유는 아래 2가지이다.

**첫째, Extreme Value Theorem은 사실 연속성 전체가 필요한 게 아니다.**

**Theorem.** If $f:[a,b]\to\mathbb{R}$ is upper semicontinuous, then $f$ attains a maximum on $[a,b]$ — i.e., there exists $d\in[a,b]$ such that $f(x)\le f(d)$ for all $x\in[a,b]$.

*Proof.* 먼저 $f$가 위로 유계임을 보이자. 그렇지 않다면 각 $n$에 대해 $f(x_n)>n$인 $x_n\in[a,b]$가 존재한다. Bolzano–Weierstrass에 의해 수렴하는 부분수열 $x_{n_k}\to c\in[a,b]$가 있다. $f$가 $c$에서 USC이므로, $\varepsilon=1$에 대해 어떤 $\delta>0$이 있어 $\vert x-c\vert<\delta$이면 $f(x)<f(c)+1$인데, 충분히 큰 $k$에서는 $\vert x_{n_k}-c\vert<\delta$가 되어 $f(x_{n_k})<f(c)+1$이어야 한다. 그런데 $f(x_{n_k})>n_k\to\infty$이므로 모순이다.

이제 $M:=\sup_{[a,b]}f$ (유한, 위 단계에 의해)라 하고, $f(x_n)>M-1/n$인 $x_n\in[a,b]$를 잡자. Bolzano–Weierstrass에 의해 $x_{n_k}\to d\in[a,b]$인 부분수열이 있다. $f(d)<M$이라 가정하면, $\varepsilon:=(M-f(d))/2>0$에 대해 USC로부터 어떤 $\delta>0$이 있어 $\vert x-d\vert<\delta$이면 $f(x)<f(d)+\varepsilon=(f(d)+M)/2<M$이다. 충분히 큰 $k$에서는 $\vert x_{n_k}-d\vert<\delta$이면서 동시에 $f(x_{n_k})>M-1/n_k>(f(d)+M)/2$가 되는데, 이는 방금 얻은 $f(x_{n_k})<(f(d)+M)/2$와 모순된다. 따라서 $f(d)=M$이다. $\blacksquare$

대칭적으로, lower semicontinuous 함수는 $[a,b]$에서 최솟값을 가진다 — 즉 Extreme Value Theorem의 최댓값 쪽은 USC만으로, 최솟값 쪽은 LSC만으로 충분하다. 예컨대 세금 구간처럼 특정 임계값에서 값이 위로 튀어 오르는(하지만 그 외에는 연속인) 함수는 완전히 연속은 아니어도 USC이기만 하면 최댓값의 존재가 여전히 보장된다.

**둘째, 반연속성은 sup·inf를 취해도 깨지지 않는다.** 연속함수들의 모임에서 sup(또는 inf)을 취하면 일반적으로 연속성은 사라지지만, 반연속성은 살아남는다.

**Proposition.** Let $$\{f_i\}_{i\in I}$$ be a family of lower semicontinuous functions on $S$. Then $f(x):=\sup_{i\in I}f_i(x)$ is lower semicontinuous on $S$.

*Proof.* $a\in S$, $\varepsilon>0$이라 하자 ($f(a)$가 유한한 경우만 보면 충분하다). $f(a)=\sup_i f_i(a)$이므로 어떤 $i_0$이 있어 $f_{i_0}(a)>f(a)-\varepsilon$이다. $f_{i_0}$이 $a$에서 LSC이므로, $\varepsilon':=f_{i_0}(a)-(f(a)-\varepsilon)>0$에 대해 어떤 $\delta>0$이 있어 $\vert x-a\vert<\delta$이면 $f_{i_0}(x)>f_{i_0}(a)-\varepsilon'=f(a)-\varepsilon$이다. 이런 $x$에 대해 $f(x)=\sup_i f_i(x)\ge f_{i_0}(x)>f(a)-\varepsilon$이므로, $f$는 $a$에서 LSC이다. $\blacksquare$

대칭적으로, USC 함수들의 inf도 USC이다.

## 참고문헌

1. Bolzano, B. (1817). *Rein analytischer Beweis des Lehrsatzes, dass zwischen je zwey Werthen, die ein entgegengesetztes Resultat gewähren, wenigstens eine reelle Wurzel der Gleichung liege*. Prague. (English translation: Russ, S. B. (1980). A translation of Bolzano's paper on the intermediate value theorem. *Historia Mathematica*, 7(2), 156–185.)
2. Cauchy, A.-L. (1821). *Cours d'analyse de l'École royale polytechnique; I.re Partie. Analyse algébrique*. Chapitre II. Paris: Imprimerie Royale.
3. Rusnock, P., & Kerr-Lawson, A. (2005). Bolzano and Uniform Continuity. *Historia Mathematica*, 32(3), 303–311.
4. Heine, E. (1872). Die Elemente der Functionenlehre. *Journal für die reine und angewandte Mathematik*, 74, 172–188.
5. Lipschitz, R. (1868–69). Disamina della possibilità d'integrare completamente un dato sistema di equazioni differenziali ordinarie. *Annali di Matematica Pura ed Applicata*, 2, 288–302.
6. Froda, A. (1929). *Sur la distribution des propriétés de voisinage des fonctions de variables réelles* (박사논문, Paris).
7. Baire, R. (1899). Sur les fonctions de variables réelles. *Annali di Matematica Pura ed Applicata*, 3, 1–123.
8. Darboux, G. (1875). Mémoire sur les fonctions discontinues. *Annales scientifiques de l'École Normale Supérieure*, 2e série, 4, 57–112.
