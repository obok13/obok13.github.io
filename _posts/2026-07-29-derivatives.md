---
layout: post
title: "미분"
date: 2026-07-29
---

## 도함수

**Definition (Derivative).** Let $f$ be defined on an open interval containing $a$. $f$ is *differentiable* at $a$, with derivative

$$f'(a) := \lim_{h\to0} \frac{f(a+h)-f(a)}{h},$$

if this limit exists.

**Proposition.** If $f$ is differentiable at $a$, then $f$ is continuous at $a$.

*Proof.* $f(a+h)-f(a) = h\cdot\dfrac{f(a+h)-f(a)}{h}$인데, $h\to0$일 때 극한의 사칙연산에 의해 우변은 $0\cdot f'(a)=0$으로 수렴하므로 $f(a+h)\to f(a)$, 즉 $f$는 $a$에서 연속이다. $\blacksquare$

역은 성립하지 않는다.

**Example.** $f(x):=x\sin(1/x)$ ($x\ne0$), $f(0):=0$이라 하자. $\vert f(x)\vert\le\vert x\vert\to0$이므로 (Squeeze) $f$는 $0$에서 연속이다. 하지만

$$\frac{f(h)-f(0)}{h} = \sin(1/h)$$

는 $h\to0$일 때 극한이 없으므로, $f$는 $0$에서 미분 불가능하다.

**Proposition (미분의 사칙연산).** If $f,g$ are differentiable at $a$, then $f+g$ and $fg$ are differentiable at $a$, with $(f+g)'(a)=f'(a)+g'(a)$ and $(fg)'(a) = f'(a)g(a)+f(a)g'(a)$.

*Proof.* 합은 극한의 사칙연산에서 바로 나온다. 곱은

$$\frac{f(a+h)g(a+h)-f(a)g(a)}{h} = \frac{f(a+h)-f(a)}{h}\,g(a+h) + f(a)\,\frac{g(a+h)-g(a)}{h}$$

로 쪼갠 뒤(분자에 $-f(a)g(a+h)+f(a)g(a+h)$를 더하고 빼서 얻는다), $h\to0$이면 $g$가 $a$에서 연속이므로 $g(a+h)\to g(a)$이고, 나머지는 정의에 의해 $f'(a)$, $g'(a)$로 수렴하므로 극한의 사칙연산에 의해 전체는 $f'(a)g(a)+f(a)g'(a)$로 수렴한다. $\blacksquare$

**Theorem (Chain Rule).** If $f$ is differentiable at $a$ and $g$ is differentiable at $f(a)$, then $g\circ f$ is differentiable at $a$, with $(g\circ f)'(a) = g'(f(a))\cdot f'(a)$.

*Proof.* $y_0:=f(a)$라 하고, $g$의 정의역 위에서

$$\varphi(y) := \begin{cases} \dfrac{g(y)-g(y_0)}{y-y_0} & y\ne y_0 \\[4pt] g'(y_0) & y=y_0 \end{cases}$$

로 정의하자. $g$가 $y_0$에서 미분가능하므로 $\lim_{y\to y_0}\varphi(y)=g'(y_0)=\varphi(y_0)$, 즉 $\varphi$는 $y_0$에서 연속이다. 정의에서 바로, $y=y_0$인 경우까지 포함해 모든 $y$에 대해

$$g(y)-g(y_0) = \varphi(y)(y-y_0)$$

이 성립한다. $y=f(x)$를 대입하면 $g(f(x))-g(f(a)) = \varphi(f(x))\,(f(x)-f(a))$이고, $x\ne a$에서 양변을 $x-a$로 나누면

$$\frac{g(f(x))-g(f(a))}{x-a} = \varphi(f(x))\cdot\frac{f(x)-f(a)}{x-a}$$

이다. $x\to a$일 때 $f$가 $a$에서 연속이므로 $f(x)\to f(a)=y_0$이고, $\varphi$가 $y_0$에서 연속이므로 지난 글의 연속함수의 합성에 의해 $\varphi(f(x))\to\varphi(y_0)=g'(y_0)$이다. 또한 $\frac{f(x)-f(a)}{x-a}\to f'(a)$이므로, 극한의 사칙연산에 의해 우변 전체는 $g'(f(a))\cdot f'(a)$로 수렴한다. $\blacksquare$

## 극값

**Definition (Local Maximum, Local Minimum).** $f$ has a *local maximum* at $c$ if there exists $\delta>0$ such that $f(x)\le f(c)$ for every $x$ in the domain of $f$ with $\vert x-c\vert<\delta$. *Local minimum* is defined symmetrically (with $f(x)\ge f(c)$). A *local extremum* is a local maximum or a local minimum.

**Theorem (Fermat).** If $f$ has a local extremum at an interior point $c$ of its domain, and $f$ is differentiable at $c$, then $f'(c)=0$.

*Proof.* $f$가 $c$에서 local maximum을 가지는 경우만 보면 충분하다 (minimum이면 $-f$에 적용). $c$가 내부점이므로, 충분히 작은 $\delta>0$에 대해 $(c-\delta,c+\delta)$가 정의역에 포함되고 이 구간에서 $f(x)\le f(c)$이다. $0<h<\delta$이면 $\dfrac{f(c+h)-f(c)}{h}\le0$ (분자 $\le0$, 분모 $>0$)이므로, $h\to0^+$로 보내면 $f'(c)\le0$이다. $-\delta<h<0$이면 $\dfrac{f(c+h)-f(c)}{h}\ge0$ (분자 $\le0$, 분모 $<0$)이므로, $h\to0^-$로 보내면 $f'(c)\ge0$이다. $f'(c)$가 (양쪽 극한이 일치하는) 하나의 값으로 존재하므로 $f'(c)=0$이다. $\blacksquare$

Fermat가 이 정리를 증명할 당시에 미분이나 극한의 개념은 없었으나, 아이디어는 비슷하다 [1].

## Rolle's Theorem

**Theorem (Rolle).** Let $f:[a,b]\to\mathbb{R}$ be continuous on $[a,b]$ and differentiable on $(a,b)$, with $f(a)=f(b)$. Then there exists $c\in(a,b)$ such that $f'(c)=0$.

*Proof.* Extreme Value Theorem에 의해 $f$는 $[a,b]$에서 최댓값과 최솟값을 가진다. 만약 이 최댓값과 최솟값이 (같은 값이든 다른 값이든) 둘 다 끝점 $$\{a,b\}$$에서만 달성된다면, $f(a)=f(b)$이므로 사실 최댓값과 최솟값이 서로 같은 값이 되어 $f$는 $[a,b]$에서 상수함수이고, 이 경우 임의의 $c\in(a,b)$에서 $f'(c)=0$이다. 그렇지 않다면 최댓값이나 최솟값 중 하나가 어떤 내부점 $c\in(a,b)$에서 달성되는데, 이는 $f$가 $c$에서 (내부점에서의) local extremum을 가진다는 뜻이므로, Fermat's Theorem에 의해 $f'(c)=0$이다. $\blacksquare$

이 정리는 Michel Rolle이 미분과 무관하게 다항방정식에 대해서만 순수하게 대수적으로 증명했으나 [2], 후대에 일반적인 미분가능 함수로 확장되었다.

## Mean Value Theorem

**Theorem (Mean Value Theorem).** Let $f:[a,b]\to\mathbb{R}$ be continuous on $[a,b]$ and differentiable on $(a,b)$. Then there exists $c\in(a,b)$ such that

$$f'(c) = \frac{f(b)-f(a)}{b-a}.$$

*Proof.* $g(x):=f(x)-f(a)-\dfrac{f(b)-f(a)}{b-a}(x-a)$라 하자. $g$는 연속함수·미분가능함수의 조합이므로 $[a,b]$에서 연속이고 $(a,b)$에서 미분가능하다. $g(a)=0$이고 $g(b)=f(b)-f(a)-(f(b)-f(a))=0$이므로 $g(a)=g(b)$이다. Rolle's Theorem에 의해 $g'(c)=0$인 $c\in(a,b)$가 존재하는데, $g'(x)=f'(x)-\dfrac{f(b)-f(a)}{b-a}$이므로 $f'(c)=\dfrac{f(b)-f(a)}{b-a}$이다. $\blacksquare$

기하학적으로는, 두 끝점을 잇는 할선(secant line)과 평행한 접선이 그래프 위 어딘가에 있다는 뜻이다. Rolle's Theorem은 정확히 그 할선의 기울기가 $0$인 특수한 경우다.

Mean Value Theorem은 일반적인 형태로는 Lagrange가 처음 다뤘고 [3] 오늘날처럼 엄밀한 증명은 Cauchy가 제시했다 [4].

**Corollary.** If $f'(x)=0$ for every $x$ in an interval $I$, then $f$ is constant on $I$.

*Proof.* $x<y$인 임의의 $x,y\in I$에 대해 $[x,y]$에 Mean Value Theorem을 적용하면 $f(y)-f(x)=f'(c)(y-x)=0$인 $c$가 존재하므로 $f(x)=f(y)$이다. $\blacksquare$

**Corollary.** If $f'(x)>0$ (respectively $f'(x)<0$) for every $x$ in an interval $I$, then $f$ is strictly increasing (respectively strictly decreasing) on $I$.

*Proof.* $x<y\in I$에 대해 Mean Value Theorem으로 $f(y)-f(x)=f'(c)(y-x)$인 $c\in(x,y)$를 얻는데, $f'(c)>0$이고 $y-x>0$이므로 $f(y)-f(x)>0$이다. 감소하는 경우도 대칭적이다. $\blacksquare$

## 도함수 판정법

앞서 본 Fermat's Theorem은 극값의 필요조건이다. 즉, $f'(c)=0$이라고 해서 $c$가 실제로 극값인 것은 아니다. $f(x)=x^3$은 $f'(0)=0$이지만 0에서 극값을 가지지 않는다. 실제로 극값인지 판정하기 위해서 도함수를 좀 더 폭넓게 사용하면 된다.

**Proposition (제1차 도함수 판정법, First Derivative Test).** Suppose $f$ is differentiable on $$(c-\delta,c+\delta)\setminus\{c\}$$ and continuous at $c$. If $f'(x)>0$ for $x\in(c-\delta,c)$ and $f'(x)<0$ for $x\in(c,c+\delta)$, then $f$ has a local maximum at $c$. (Symmetrically, $f'<0$ then $f'>0$ gives a local minimum.)

*Proof.* 앞의 Corollary에 의해 $f$는 $(c-\delta,c]$에서 증가하고 $[c,c+\delta)$에서 감소하므로, 이 구간 전체에서 $f(x)\le f(c)$이다. $\blacksquare$

**Proposition (제2차 도함수 판정법, Second Derivative Test).** Suppose $f'(c)=0$ and $f''(c)$ exists. If $f''(c)>0$, then $f$ has a local minimum at $c$; if $f''(c)<0$, a local maximum.

*Proof.* $f''(c)>0$인 경우만 보이면 충분하다 (부호가 반대면 $-f$에 적용). $f''(c) = \lim_{h\to0}\dfrac{f'(c+h)-f'(c)}{h} = \lim_{h\to0}\dfrac{f'(c+h)}{h}$ ($f'(c)=0$이므로)인데, 이 극한이 $f''(c)>0$이므로, $\varepsilon:=f''(c)/2>0$에 대해 어떤 $\eta>0$이 있어 $0<\vert h\vert<\eta$이면 $\dfrac{f'(c+h)}{h} > f''(c)-\varepsilon = \varepsilon$이다. $0<h<\eta$이면 이로부터 $f'(c+h) > \varepsilon h>0$이고, $-\eta<h<0$이면 (부등식의 양변에 음수 $h$를 곱하며 부등호가 뒤집혀) $f'(c+h) < \varepsilon h<0$이다. 즉 $f'$은 $c$ 바로 왼쪽에서 음수, 바로 오른쪽에서 양수이므로, 제1차 도함수 판정법에 의해 $f$는 $c$에서 local minimum을 가진다. $\blacksquare$

이 증명이 $f''$가 $c$ 근방에서 연속이라고 가정하지 않고 $f''(c)$의 존재만으로 끝난다는 점을 눈여겨볼 만하다 — $f''$가 $c$에서만 저 값을 가지고 다른 곳에서는 어떻게 행동하는지 전혀 몰라도 판정법이 성립한다.

## Cauchy's Mean Value Theorem

Mean Value Theorem을 두 함수의 비율로 일반화하면 다음을 얻는다.

**Theorem (Cauchy's Mean Value Theorem).** Let $f,g:[a,b]\to\mathbb{R}$ be continuous on $[a,b]$ and differentiable on $(a,b)$, with $g'(x)\ne0$ for every $x\in(a,b)$. Then $g(a)\ne g(b)$, and there exists $c\in(a,b)$ such that

$$\frac{f(b)-f(a)}{g(b)-g(a)} = \frac{f'(c)}{g'(c)}.$$

*Proof.* $g(a)=g(b)$라면 Rolle's Theorem에 의해 $g'(x)=0$인 $x\in(a,b)$가 존재해 가정에 모순이므로 $g(a)\ne g(b)$이다. $h(x):=(f(x)-f(a))(g(b)-g(a)) - (g(x)-g(a))(f(b)-f(a))$라 하면 $h(a)=0$이고 $h(b)=(f(b)-f(a))(g(b)-g(a))-(g(b)-g(a))(f(b)-f(a))=0$이므로 $h(a)=h(b)$이다. Rolle's Theorem에 의해 $h'(c)=0$인 $c\in(a,b)$가 존재하는데, $h'(x)=f'(x)(g(b)-g(a))-g'(x)(f(b)-f(a))$이므로 $f'(c)(g(b)-g(a))=g'(c)(f(b)-f(a))$이다. $g'(c)\ne0$이고 $g(b)\ne g(a)$이므로 양변을 $g'(c)(g(b)-g(a))$로 나누면 원하는 식을 얻는다. $\blacksquare$

$g(x)=x$로 두면 $g'(x)=1\ne0$, $g(b)-g(a)=b-a$가 되어 곧바로 (일반) Mean Value Theorem이 나오므로, 이 정리는 정확히 그 일반화다.

이 정리는 실제로 Cauchy가 Mean Value Theorem의 엄밀한 증명을 실었던 저서에 함께 실려 있다 [4].

## L'Hôpital's Rule

**Theorem (L'Hôpital's Rule).** Let $-\infty\le a<b\le+\infty$, and let $f,g$ be differentiable on $(a,b)$ with $g'(x)\ne0$ for every $x\in(a,b)$. Suppose $\lim_{x\to a^+}\dfrac{f'(x)}{g'(x)}=A$ exists, where $A\in\overline{\mathbb{R}}$. If either (i) $\displaystyle\lim_{x\to a^+}f(x)=\lim_{x\to a^+}g(x)=0$, or (ii) $\displaystyle\lim_{x\to a^+}g(x)=+\infty$, then $\displaystyle\lim_{x\to a^+}\frac{f(x)}{g(x)}=A$.

*Proof.* $a$가 유한하고 $A$도 유한한 경우만 보이자 ($a=-\infty$인 경우는 $x\mapsto1/x$ 치환으로 이 경우로 환원되고, $A=\pm\infty$인 경우는 아래 논증에서 부등식 $A-\varepsilon<\cdots<A+\varepsilon$을 $M<\cdots$ 또는 $\cdots<M$ 꼴의 한쪽 부등식만으로 바꿔 같은 방식으로 처리되므로, 본질적인 어려움은 이 경우에 있다).

먼저 $g$가 $(a,b)$에서 단사(injective)임을 보이자. 그렇지 않다면 $g(x_1)=g(x_2)$인 $x_1<x_2\in(a,b)$가 있을 것인데, Rolle's Theorem에 의해 그 사이 어딘가에서 $g'=0$이 되어 가정에 모순이다.

$\varepsilon>0$이 주어지면, 가정에 의해 어떤 $c\in(a,b)$가 있어 $a<x<c$이면 $A-\varepsilon<\dfrac{f'(x)}{g'(x)}<A+\varepsilon$이다. $g$가 단사이므로 $a<x<y<c$에 대해 $g(x)\ne g(y)$이고, Cauchy's Mean Value Theorem을 $[x,y]$에 적용하면

$$A-\varepsilon < \frac{f(x)-f(y)}{g(x)-g(y)} < A+\varepsilon \tag{$*$}$$

이 성립한다.

**(i)의 경우.** $y\in(a,c)$를 하나 고정하자 ($g(y)=0$이면 $g$가 단사이므로 그런 $y$는 많아야 하나뿐이니, 그 점만 피해서 고정한다). $(*)$에서 $x\to a^+$로 보내면 $f(x)\to0$, $g(x)\to0$이므로

$$A-\varepsilon \le \frac{f(y)}{g(y)} \le A+\varepsilon.$$

이것이 (그 예외적인 점을 제외한) 모든 $y\in(a,c)$에서 성립하고, $\varepsilon$이 임의였으므로 $\displaystyle\lim_{y\to a^+}\frac{f(y)}{g(y)}=A$이다.

**(ii)의 경우.** $g'\ne0$이므로 Intermediate Value Theorem에 의해 $g'$은 $(a,b)$에서 부호가 일정한데, $x\to a^+$일 때(즉 $x$가 $a$에 가까워질수록) $g(x)\to+\infty$이려면 그 부호가 음이어야 하므로 $g$는 $(a,b)$에서 (엄밀히) 감소한다. $c_1\in(a,c)$를 ($g(c_1)>0$이 되도록, $g\to+\infty$이니 가능하다) 하나 고정하면, $g$가 감소하므로 $a<x<c_1$인 모든 $x$에서 $g(x)>g(c_1)>0$이다. $(*)$에서 $y:=c_1$로 두면

$$A-\varepsilon < \frac{f(x)-f(c_1)}{g(x)-g(c_1)} < A+\varepsilon$$

인데, $g(x)-g(c_1)>0$이므로 부등식의 양변에 곱해도 방향이 유지되어

$$(A-\varepsilon)\big(g(x)-g(c_1)\big) < f(x)-f(c_1) < (A+\varepsilon)\big(g(x)-g(c_1)\big)$$

이고, 양변을 $g(x)>0$으로 나누면

$$(A-\varepsilon)\left(1-\frac{g(c_1)}{g(x)}\right)+\frac{f(c_1)}{g(x)} < \frac{f(x)}{g(x)} < (A+\varepsilon)\left(1-\frac{g(c_1)}{g(x)}\right)+\frac{f(c_1)}{g(x)}$$

를 얻는다. $x\to a^+$이면 $g(x)\to+\infty$이므로 $\dfrac{g(c_1)}{g(x)}\to0$, $\dfrac{f(c_1)}{g(x)}\to0$ ($f(c_1),g(c_1)$은 고정된 값)이 되어, 좌변은 $A-\varepsilon$으로, 우변은 $A+\varepsilon$으로 수렴한다. 따라서 어떤 $c_2\in(a,c_1)$이 있어 $a<x<c_2$이면 좌변은 $A-2\varepsilon$보다 크고 우변은 $A+2\varepsilon$보다 작으므로, $\left\vert\dfrac{f(x)}{g(x)}-A\right\vert<2\varepsilon$이다. $\varepsilon$이 임의였으므로 $\displaystyle\lim_{x\to a^+}\frac{f(x)}{g(x)}=A$이다. $\blacksquare$

$a$가 유한한 실수이고 (i)의 조건($f,g\to0$)으로 국한하면, 이것이 바로 전통적으로 알려진 $0/0$ 꼴의 L'Hôpital's Rule이다. $x\to b^-$인 경우나 $g(x)\to-\infty$인 경우도 (부등식의 방향이나 치환을 적절히 바꾸면) 대칭적으로 성립한다 — Rudin의 책에서도 정확히 이 경우들을 "analogous"라는 말로 남겨둔다.

L'Hôpital's Rule은 사실 Johann Bernoulli에 의해 발견되었다. 이 정리가 l'Hôpital's Rule로 알려진 이유는 l'Hôpital이 1694년 Bernoulli와 계약을 맺어, Bernoulli의 수학적 발견들을 독점적으로 넘겨받아 자신의 이름으로 출판할 권리를 얻었기 때문이라고 추측이 되었다 [5]. 그러다가 Paul Schafheitlin이 1924년 Johann Bernoulli의 조카 Nicolaus (I) Bernoulli가 1705년경 그 강의 내용을 옮겨 적은 사본을 공개했고, 그 내용이 l'Hôpital의 책과 거의 그대로 일치해 추측이 뒷받침됐다 [6].

## 참고문헌

1. Fermat, P. de (written c. 1636, published 1679). *Methodus ad disquirendam maximam et minimam*. In *Varia Opera Mathematica*. Toulouse.
2. Rolle, M. (1691). *Démonstration d'une méthode pour résoudre les égalitéz de tous les degréz*. Paris.
3. Lagrange, J.-L. (1797). *Théorie des fonctions analytiques*. Paris.
4. Cauchy, A.-L. (1823). *Résumé des leçons données à l'École royale polytechnique sur le calcul infinitésimal*. Paris.
5. Truesdell, C. (1958). The New Bernoulli Edition. *Isis*, 49(1), 54–62.
6. Schafheitlin, P. (Ed. & Trans.) (1924). *Die Differentialrechnung von Johann Bernoulli aus dem Jahre 1691/92*. Ostwalds Klassiker der exakten Wissenschaften, Nr. 211. Leipzig: Akademische Verlagsgesellschaft.
