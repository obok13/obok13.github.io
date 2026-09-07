---
layout: post
title: "Vector space"
date: 2026-08-05
mathematicians: [Peano, Grassmann, Steinitz, Hamel, Zorn, Cauchy, Blass, Tarski, Fréchet, Läuchli]
---

## 체와 벡터공간

**Definition (Abelian Group).** 집합 $G$와 연산 $+:G\times G\to G$가 다음을 만족하면 $(G,+)$를 abelian group이라 한다: 결합법칙 $(a+b)+c=a+(b+c)$가 성립하고, 항등원 $0\in G$가 존재해 모든 $a$에서 $a+0=a$이며, 각 $a\in G$마다 역원 $-a\in G$가 존재해 $a+(-a)=0$이고, 교환법칙 $a+b=b+a$가 성립한다.

**Definition (Field).** 집합 $F$와 두 연산 $+,\cdot$가 다음을 만족하면 $F$를 체(field)라 한다. $(F,+)$는 항등원 $0$을 갖는 abelian group이고, $$(F\setminus\{0\},\cdot)$$도 항등원 $1$을 갖는 abelian group이며, 분배법칙 $a(b+c)=ab+ac$가 성립한다.

예를 들어 $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$는 모두 체이다. finite field도 있다.

**Definition (Vector Space).** 체 $F$ 위의 벡터공간(vector space)은 집합 $V$와 덧셈 $V\times V\to V$, scalar multiplication $F\times V\to V$로 이루어지며, $(V,+)$가 abelian group이고 모든 $a,b\in F$와 $u,v\in V$에 대해
$$a(u+v)=au+av, \quad (a+b)v=av+bv, \quad (ab)v=a(bv), \quad 1v=v$$
를 만족한다. $V$의 원소를 벡터, $F$의 원소를 scalar라 한다.

정의에서 곧바로 $0v=0$, $a0=0$, $(-1)v=-v$가 나온다. 예컨대 $0v=(0+0)v=0v+0v$에서 양변에 $-0v$를 더하면 $0v=0$이다.

**Example (좌표공간 $F^n$).** $F^n$은 성분별 덧셈과 scalar multiplication으로 벡터공간이다. $\mathbb{R}^3$이 가장 익숙한 예다.

**Example (다항식공간).** 계수가 $F$에 속하는 다항식 전체 $F[x]$는 계수별 연산으로 벡터공간이다.

**Example (function space).** 집합 $X$ 위의 $F$값 함수 전체 $F^X$는 점별 덧셈·scalar multiplication으로 벡터공간이다. 연속함수나 수렴수열 같은 해석학의 주인공들이 모두 이 공간의 부분공간으로 그 안에 산다.

**Example (scalar field가 벡터공간을 바꾼다).** 같은 additive group이라도 scalar를 어느 체에서 가져오느냐에 따라 벡터공간의 성격이 달라진다. $\mathbb{C}$는 $\mathbb{R}$ 위의 벡터공간이자 $\mathbb{C}$ 위의 벡터공간이고, $\mathbb{R}$은 $\mathbb{Q}$ 위의 벡터공간인데, 뒤에서 보듯 세 경우의 차원은 각각 $2$, $1$, $\infty$로 완전히 다르다.

벡터공간을 이렇게 공리로 처음 세운 사람은 Peano로, 1888년 Grassmann의 1844년 《Ausdehnungslehre》[2]를 이어받아 오늘날과 같은 정의를 제시했다 [1].

## 부분공간

**Definition (Subspace).** $V$의 부분집합 $W$가 $0\in W$이고 임의의 $a,b\in F$, $u,v\in W$에 대해 $au+bv\in W$이면 $W$를 부분공간(subspace)이라 한다. 부분공간은 물려받은 연산으로 그 자체가 벡터공간이다.

**Example (원점을 지나는 평면).** $\mathbb{R}^3$에서 원점을 지나는 평면 $$\{(x,y,0):x,y\in\mathbb{R}\}$$은 부분공간이다. 원점을 지나는 직선도 마찬가지다.

**Example (차수 제한 다항식).** 차수가 $n$ 이하인 다항식 전체 $$\{p\in\mathbb{R}[x]:\deg p\le n\}$$은 $\mathbb{R}[x]$의 부분공간이다.

**Example (연속함수는 부분공간).** 닫힌구간 위 연속함수 전체 $C[a,b]$는 그 구간 위 모든 실함수 공간의 부분공간이다.

**Example (원점을 지나지 않는 평면).** $$\{(x,y,1):x,y\in\mathbb{R}\}$$은 $0$을 포함하지 않으므로 부분공간이 아니다.

**Example (제1사분면).** $$\{(x,y):x\ge0,\ y\ge0\}$$은 덧셈에는 닫혀 있지만 $(-1)$배에 닫혀 있지 않으므로 부분공간이 아니다.

**Example (두 좌표축의 합집합).** $$\{(x,0):x\in\mathbb{R}\}\cup\{(0,y):y\in\mathbb{R}\}$$은 scalar multiplication에는 닫혀 있지만 $(1,0)+(0,1)=(1,1)$을 포함하지 않아 덧셈에 닫혀 있지 않으므로 부분공간이 아니다. 바로 앞의 제1사분면과 나란히 놓고 보면 덧셈과 scalar multiplication 두 닫힘 조건이 모두 필요함을 알 수 있다.

**Example (차수가 정확히 $n$인 다항식).** 이 모임은 $0$을 포함하지 않고 덧셈에도 닫히지 않으므로 부분공간이 아니다.

## 일차독립과 기저

**Definition (Span).** $S\subseteq V$에 대해 $S$의 유한 일차결합 전체
$$\operatorname{span}S := \{\,a_1v_1+\cdots+a_kv_k : k\ge0,\ a_i\in F,\ v_i\in S\,\}$$
를 $S$가 생성하는 부분공간이라 한다($k=0$인 빈 결합은 $0$). 이는 $S$를 포함하는 가장 작은 부분공간이다.

**Definition (Linear Independence).** $S\subseteq V$가 일차독립(linearly independent)이라는 것은, $S$의 서로 다른 유한개 $v_1,\dots,v_k$에 대해 $a_1v_1+\cdots+a_kv_k=0$이면 반드시 $a_1=\cdots=a_k=0$이라는 뜻이다. 그렇지 않으면 일차종속(linearly dependent)이라 한다.

**Definition (Basis).** $V$를 span하는 일차독립 집합 $B$를 $V$의 기저(basis)라 한다.

**Proposition.** $B$가 기저인 것과, 모든 $v\in V$가 $B$의 원소들의 유한 일차결합으로 유일하게 표현되는 것은 동치다.

*Proof.* span이라는 것이 표현의 존재이고, 두 표현 $v=\sum a_iv_i=\sum b_iv_i$의 차 $\sum(a_i-b_i)v_i=0$가 일차독립에 의해 $a_i=b_i$를 강제하는 것이 표현의 유일성이다. $\blacksquare$

**Example (표준기저).** $\mathbb{R}^3$의 표준기저는 $$\{(1,0,0),(0,1,0),(0,0,1)\}$$이다.

**Example (표준이 아닌 기저).** $$\{(1,1,0),(0,1,1),(1,0,1)\}$$도 $\mathbb{R}^3$의 기저다. 세 벡터가 일차독립이고 $\mathbb{R}^3$을 span하기 때문이다. 기저는 유일하지 않다.

**Example (다항식의 기저).** $\mathbb{R}[x]$에서 $$\{1,x,x^2,\dots\}$$은 기저이며, 이 기저가 무한집합이라는 데서 $\mathbb{R}[x]$가 무한차원임을 알 수 있다.

**Example (scalar field가 기저를 바꾼다).** $\mathbb{C}$를 $\mathbb{R}$ 위의 벡터공간으로 보면 $$\{1,i\}$$가 기저(차원 2)이지만, $\mathbb{C}$ 자신 위의 벡터공간으로 보면 $$\{1\}$$이 기저(차원 1)다.

**Example (종속이라 기저가 아님).** $\mathbb{R}^2$에서 $$\{(1,2),(2,4)\}$$는 $(2,4)=2(1,2)$이므로 일차종속이라 기저가 아니다. 벡터가 차원보다 많으면 반드시 종속이다(Exchange Lemma).

**Example (span하지 못해 기저가 아님).** $$\{(1,0)\}$$은 $\mathbb{R}^2$에서 일차독립이지만 $(0,1)$을 만들지 못해 $\mathbb{R}^2$를 span하지 않으므로 기저가 아니다. 벡터가 차원보다 적으면 결코 span할 수 없다.

## 기저의 존재

**Theorem (유한생성 벡터공간의 기저 존재).** 유한개의 벡터로 span되는 벡터공간은 기저를 가진다.

*Proof.* $V$가 유한집합 $S$로 span된다고 하자. $S$의 원소 중 나머지의 결합으로 표현되는 것이 있으면 그 원소를 제거해도 남은 집합은 여전히 $V$를 span한다. 이 과정을 더 제거할 원소가 없을 때까지 반복하면(유한집합이라 유한 번에 끝난다), 남은 집합은 $V$를 span하면서 일차독립이므로 기저다. $\blacksquare$

이 논증은 $S$가 원래 주어진 생성집합이라는 사실과 무관하게 임의의 유한 span 집합에 그대로 적용되므로, 임의의 span 집합은 기저를 포함한다는 사실도 같은 증명으로 곧바로 따라온다.

**Theorem (기저로의 확장).** $V$가 유한개의 벡터로 span된다고 하자. 임의의 일차독립 집합은 기저로 확장할 수 있다.

*Proof.* 일차독립 집합에 span 밖의 벡터를 하나씩 계속 더해도 독립성이 유지된다. $V$가 유한 생성이므로 이 과정은 유한 번 만에 끝나고(전체를 span하는 순간 멈춘다), 그 결과는 기저다. $\blacksquare$

$V$가 유한개의 벡터로 span되지 않으면 이런 유한 절차가 끝나지 않는다. 여기서 선택 공리가 등장한다.

**Theorem (Basis Existence).** 모든 벡터공간은 기저를 가진다.

*Proof.* $V$의 일차독립 부분집합 전체를 포함관계로 정렬하자. 이 정렬에서 chain(전순서 부분집합) $\mathcal{C}$의 합집합 $U=\bigcup\mathcal{C}$는 다시 일차독립이다. $U$의 유한 부분집합이 일차종속이라면 그 유한개의 벡터가 chain의 어느 한 원소에 모두 들어가는데, 그 원소가 일차독립이라는 데 모순이기 때문이다. 따라서 모든 chain이 upper bound를 가지므로, 선택 공리 글에서 다룬 Zorn's Lemma에 의해 maximal 일차독립집합 $M$이 존재한다. 만약 $M$이 $V$를 span하지 않으면 $v\notin\operatorname{span}M$인 $v$가 있고 $$M\cup\{v\}$$가 여전히 일차독립이라 $M$의 maximality에 모순이다. 그러므로 $M$은 $V$를 span하는 일차독립 집합, 곧 기저다. $\blacksquare$

이 정리는 사실 선택 공리와 동치다. "모든 벡터공간이 기저를 가진다"는 명제에서 거꾸로 선택 공리를 이끌어낼 수 있음을 Blass가 1984년에 증명했다 [6]. 즉 일반적인 기저의 존재는 순수한 존재 정리일 뿐, 대개 구체적으로 적어낼 수 없다.

**Definition (Hamel Basis).** $\mathbb{R}$을 $\mathbb{Q}$ 위의 벡터공간으로 볼 때의 기저를 Hamel basis라 한다 [4]. 위 정리(즉 선택 공리)가 그 존재를 보장하지만, 명시적으로 나열하는 것은 불가능하다.

## Cauchy의 functional equation

Hamel basis의 존재는 해석학에 뜻밖의 그림자를 드리운다. Cauchy가 1821년에 다룬 다음 방정식이 그 무대다 [5].

**Definition.** 함수 $f:\mathbb{R}\to\mathbb{R}$가 모든 $x,y$에서 $f(x+y)=f(x)+f(y)$를 만족하면 additive라 한다.

**Proposition.** additive 함수 $f$는 $\mathbb{Q}$-선형이다. 즉 모든 $q\in\mathbb{Q}$, $x\in\mathbb{R}$에서 $f(qx)=qf(x)$이다. 특히 $f$가 한 점에서라도 연속이면 $f(x)=cx$ ($c=f(1)$) 꼴이다.

*Proof.* $f(0)=f(0)+f(0)$에서 $f(0)=0$이고, 귀납법으로 $f(nx)=nf(x)$ ($n\ge1$), $f(-x)=-f(x)$를 얻는다. 또 $f(x)=f\!\left(n\cdot\tfrac{x}{n}\right)=nf\!\left(\tfrac{x}{n}\right)$이므로 $f(x/n)=f(x)/n$이고, 이 둘을 합치면 $q=m/n$에 대해 $f(qx)=qf(x)$이다. 이제 $f$가 어떤 한 점 $x_0$에서 연속이라 하자. 임의의 $h$에 대해 $f(x_0+h)-f(x_0)=f(h)$이므로($f$의 additivity), $h\to0$일 때 $x_0+h\to x_0$이고 $x_0$에서의 연속성으로 $f(x_0+h)\to f(x_0)$, 즉 $f(h)\to0$이다. 그러므로 $f$는 $0$에서 연속이고, 임의의 점 $a$에서도 $f(a+h)-f(a)=f(h)\to0$이므로 $f$는 사실 모든 점에서 연속이다. 이제 임의의 $x\in\mathbb{R}$에 대해 $x$로 수렴하는 유리수열 $q_k$를 잡으면 $f(q_k)=q_kf(1)$이고, 연속성으로 $k\to\infty$에서 $f(x)=xf(1)$이다. $\blacksquare$

연속 조건이 붙으면 이렇게 해가 직선 $f(x)=cx$로 고정된다. 그런데 아무 조건도 없으면 사정이 완전히 달라진다.

**Theorem (Hamel).** $f(x)=cx$ 꼴이 아닌 additive 함수가 존재한다. 그런 $f$는 어떤 점에서도 연속이 아니며, 그 그래프 $$\{(x,f(x)):x\in\mathbb{R}\}$$는 $\mathbb{R}^2$에서 조밀하다.

*Proof.* $\mathbb{R}$의 Hamel basis $H$를 하나 잡는다. 각 $H$의 원소 $h_i$에 대해서 $f$ 값을 자유롭게 정해도 $f\left(\sum q_ih_i\right):=\sum q_if(h_i)$가 항상 잘 정의된다. 따라서 $f(x)=cx$ 꼴이 아니어도 된다.

$f$가 $cx$ 꼴이 아니므로, 앞 Proposition의 대우에 의해 $f$는 어느 점에서도 연속일 수 없다(연속인 점이 하나라도 있었다면 $f(x)=cx$ 꼴이어야 한다). $\blacksquare$

사실 $f$가 measurable이기만 해도, 혹은 양의 measure를 갖는 어떤 집합에서 유계이기만 해도 $f(x)=cx$임이 알려져 있다(Fréchet, Sierpiński). 이 방향은 측도론이 필요하므로 뒤의 측도론 글로 미룬다.

비선형 additive 함수는 Vitali 집합이나 Banach–Tarski 분해처럼, 선택 공리가 낳지만 결코 손으로 그릴 수 없는 대상이다.

## 차원

기저의 크기가 표현 방식에 무관하게 정해진다는 것이 선형대수의 첫 번째 핵심이다. 그 열쇠가 Steinitz의 Exchange Lemma다 [3].

**Lemma (Steinitz Exchange).** $$\{v_1,\dots,v_m\}$$이 일차독립이고 $$\{w_1,\dots,w_n\}$$이 $V$를 span하면 $m\le n$이다.

*Proof.* $w$들이 span하므로 $v_1=\sum_{j=1}^n c_jw_j$인데, $v_1\ne0$(일차독립 집합은 $0$을 포함하지 않는다)이라 어떤 $c_j\ne0$이다. 번호를 바꿔 $c_1\ne0$이라 하면 $w_1$을 $v_1,w_2,\dots,w_n$의 결합으로 풀 수 있으므로 $$\{v_1,w_2,\dots,w_n\}$$도 $V$를 span한다. 이제 이미 $$\{v_1,\dots,v_k,w_{k+1},\dots,w_n\}$$이 span한다고 하자. $v_{k+1}$을 이 집합의 결합으로 쓰면, $w$들의 계수가 모두 $0$일 수는 없다(그렇다면 $$v_{k+1}\in\operatorname{span}\{v_1,\dots,v_k\}$$가 되어 $v$들의 일차독립에 모순). 그 $w$ 하나를 $v_{k+1}$로 교환하면 $$\{v_1,\dots,v_{k+1},w_{k+2},\dots,w_n\}$$이 다시 span한다. 만약 $m>n$이라면 $n$번의 교환 뒤 $w$가 모두 소진되어 $$\{v_1,\dots,v_n\}$$이 span하게 되고, 그러면 남은 $v_{n+1}$이 앞 $v$들의 결합이 되어 일차독립에 모순이다. 따라서 $m\le n$이다. $\blacksquare$

**Theorem (차원의 불변성).** 벡터공간의 임의의 두 기저는 같은 cardinality를 가진다.

*Proof.* 두 기저 $B,C$ 중 하나, 이를테면 $B$가 유한(크기 $m$)이라 하자. $C$의 임의의 유한부분집합 $C_0$은 일차독립이고 $B$는 $V$를 span하므로 Steinitz Exchange로 $\vert C_0\vert\le m$이다. 이는 $C$의 모든 유한부분집합의 크기가 $m$ 이하라는 뜻이므로 $C$ 자신도 유한하고 $\vert C\vert\le m$이다(그렇지 않다면 $C$가 크기 $m+1$인 유한부분집합을 가져 모순). $B,C$의 역할을 바꾸면 같은 논증으로 $\vert B\vert\le\vert C\vert$도 얻어 $\vert B\vert=\vert C\vert$.

$B,C$가 모두 무한인 경우를 보자. $C$가 $V$를 span하므로 각 $b\in B$는 $C$의 어떤 유한부분집합 $C_b\subseteq C$의 결합으로 표현되고, $C$가 일차독립이므로 이 표현은 유일하다. $C' := \bigcup_{b\in B}C_b\subseteq C$라 두면, $B$가 $V$를 span하고 모든 $b\in B$가 $C'$의 결합이므로 $C'$도 $V$를 span한다. 그런데 어떤 $c\in C\setminus C'$가 있다면 $c$가 $$C'\subseteq C\setminus\{c\}$$의 결합으로 쓰이는 셈이라 $C$의 일차독립성에 모순이다. 따라서 $C'=C$, 즉 $C$는 무한집합 $B$로 인덱스된 유한집합들 $$\{C_b\}_{b\in B}$$의 합집합이다. 무한 cardinal $\kappa=\vert B\vert$에 대해 $\kappa\cdot\aleph_0=\kappa$이므로 $\vert C\vert\le\vert B\vert\cdot\aleph_0=\vert B\vert$. $B,C$의 역할을 바꾸면 같은 논증으로 $\vert B\vert\le\vert C\vert$도 얻어, Cantor–Schröder–Bernstein으로 $\vert B\vert=\vert C\vert$. $\blacksquare$

사실 위 증명에서 basis의 크기가 무한일 때는 증명에 선택공리가 쓰였다. "무한 cardinal $\kappa$에 대해 $\kappa\cdot\aleph_0=\kappa$" 부분이다. 선택공리가 이 명제의 충분조건이다. 참고로 필요충분조건은 이보다 더 강한 명제인 "모든 무한 cardinal의 제곱이 자기 자신과 같다"는 것이고 Tarski가 증명했다 [7]. 위 정리는 실제로 선택공리 없이는 성립하지 않을 수 있다. Läuchli는 선택공리가 완전히 실패하는 ZF의 한 모델에서, 서로 다른 cardinality의 두 기저를 가지는 벡터공간이 존재함을 보였다 [8].

**Definition (Dimension).** 이 공통의 cardinality를 $V$의 차원 $\dim V$라 한다. 이것이 유한이면 $V$를 유한차원, 아니면 무한차원이라 한다.

**Example ($\dim F^n=n$).** $F^n$의 표준기저가 $n$개이므로 $\dim F^n=n$이다.

**Example (무한차원).** $\mathbb{R}[x]$는 $1,x,x^2,\dots$가 일차독립이라 유한 기저를 가질 수 없으므로 무한차원이다.

## 부분공간의 합

**Definition (Sum).** 부분공간 $W_1,W_2$에 대해 그 합은
$$W_1+W_2 := \{\,w_1+w_2 : w_1\in W_1,\ w_2\in W_2\,\}$$
이고 이것도 부분공간이다.

두 부분공간의 합의 차원은 각 차원과 교집합의 차원으로 정해진다.

**Theorem (Grassmann's Dimension Formula).** 벡터공간의 유한차원 부분공간 $U,W$에 대해
$$\dim(U+W)=\dim U+\dim W-\dim(U\cap W).$$

*Proof.* $U\cap W$의 기저 $$\{x_1,\dots,x_k\}$$를 잡아, 이를 $U$의 기저 $$\{x_1,\dots,x_k,u_1,\dots,u_p\}$$와 $W$의 기저 $$\{x_1,\dots,x_k,w_1,\dots,w_q\}$$로 각각 확장한다(일차독립 집합의 기저 확장). 그러면 $$\{x_1,\dots,x_k,u_1,\dots,u_p,w_1,\dots,w_q\}$$가 $U+W$의 기저임을 보이면 되고, 이들이 $U+W$를 span하는 것은 분명하다. 일차독립을 보자. $\sum_i a_ix_i+\sum_j b_ju_j+\sum_l c_lw_l=0$이면 $\sum_l c_lw_l=-\sum_i a_ix_i-\sum_j b_ju_j\in U$인데 동시에 $W$에도 있으니 $U\cap W$에 속해 $\sum_l c_lw_l=\sum_i d_ix_i$로도 쓰인다. $W$의 기저에서 $w_l$과 $x_i$가 일차독립이라 모든 $c_l=0$이고, 남은 $\sum_i a_ix_i+\sum_j b_ju_j=0$에서 $U$의 기저가 일차독립이라 나머지 계수도 모두 $0$이다. 따라서 기저의 크기가 $k+p+q=(k+p)+(k+q)-k=\dim U+\dim W-\dim(U\cap W)$이다. $\blacksquare$

## 직합

**Definition (Direct Sum).** 부분공간 $W_1,W_2$의 합 $W_1+W_2$가 $$W_1\cap W_2=\{0\}$$을 만족하면 이 합을 직합(direct sum)이라 부르고 $W_1\oplus W_2$로 쓴다.

**Proposition.** $W_1+W_2$가 직합인 것과, 모든 원소가 $w_1+w_2$ ($w_i\in W_i$) 꼴로 유일하게 표현되는 것은 동치다.

*Proof.* 표현이 유일하지 않다면 $w_1+w_2=w_1'+w_2'$이면서 $(w_1,w_2)\ne(w_1',w_2')$인 경우가 있고, 이때 $x:=w_1-w_1'=w_2'-w_2$는 $W_1\cap W_2$에 속하는 영이 아닌 벡터다. 역으로 $$0\ne x\in W_1\cap W_2$$이면 $0=x+(-x)$가 $0=0+0$과 다른 표현이 된다. 따라서 표현의 유일성과 $$W_1\cap W_2=\{0\}$$은 동치다. $\blacksquare$

**Example (평면의 직합).** $\mathbb{R}^2$은 $x$축 $$\{(a,0):a\in\mathbb{R}\}$$과 $y$축 $$\{(0,b):b\in\mathbb{R}\}$$의 직합이다. 모든 $(a,b)=(a,0)+(0,b)$가 유일하게 쪼개지기 때문이다.

**Example (우함수와 기함수).** $\mathbb{R}$ 위의 모든 함수 $f$는
$$f(x)=\underbrace{\tfrac{f(x)+f(-x)}{2}}_{\text{even}}+\underbrace{\tfrac{f(x)-f(-x)}{2}}_{\text{odd}}$$
로 우함수와 기함수의 합으로 유일하게 쓰인다. 따라서 function space는 우함수 부분공간과 기함수 부분공간의 직합이다. 이 분해는 연속함수에 그대로 제한되어 $C(\mathbb{R})$도 연속 우함수와 연속 기함수의 직합이 된다.

**Example (연속함수의 직합).** $C[a,b]$는 상수함수들의 부분공간과 적분이 $0$인 연속함수들의 부분공간 $$\{g\in C[a,b]:\textstyle\int_a^b g=0\}$$의 직합이다. 임의의 $f$를 그 평균 $c=\frac{1}{b-a}\int_a^b f$와 나머지 $f-c$로 쪼개면 $\int_a^b(f-c)=0$이라 $f-c$가 뒤 부분공간에 속하고, 상수이면서 적분이 $0$인 함수는 $0$뿐이라 이 분해가 유일하다.

**Example (직합이 아닌 합).** $\mathbb{R}^3$에서 $xy$평면 $P$와 $yz$평면 $Q$를 보면 $P+Q=\mathbb{R}^3$이지만 $P\cap Q$가 $y$축이라 직합이 아니다. 실제로 $(0,1,0)$이 $P$의 벡터로도 $Q$의 벡터로도 표현되어 유일성이 깨진다.

직합은 두 개뿐 아니라 임의의(무한이어도 되는) 개수의 부분공간으로도 일반화된다.

**Definition (일반화된 직합).** 부분공간들의 모임 $$\{W_i\}_{i\in I}$$(index 집합 $I$는 무한이어도 된다)에 대해, 유한개의 $i$에서만 $w_i\ne0$인 합 $\sum_{i\in I}w_i$ ($w_i\in W_i$) 전체를 그 합이라 한다. 이 합에서 $0$의 표현이 (모든 $w_i=0$이라는) 자명한 것뿐이면, 곧
$$\sum_{i\in I}w_i=0\ (w_i\in W_i,\text{ 유한개 제외 }0)\ \Longrightarrow\ \text{모든 }i\text{에서 }w_i=0$$
이면 이 합을 직합이라 하고 $\bigoplus_{i\in I}W_i$로 쓴다. $$I=\{1,2\}$$인 경우가 앞서 본 정의다.

**Example (다항식공간의 무한 직합).** $\mathbb{R}[x]=\bigoplus_{n=0}^{\infty}\mathbb{R}x^n$이다. 여기서 $$\mathbb{R}x^n:=\{cx^n:c\in\mathbb{R}\}$$은 $1$차원 부분공간이고, 모든 다항식이 (유한개의 $0$이 아닌 계수를 가진) 이 monomial들의 결합으로 유일하게 쓰인다는 사실이 정확히 직합의 조건이다.

**Example (지수함수들의 uncountable 직합).** index 집합 $I$가 countable일 필요는 없다. $\mathbb{C}$ 위의 벡터공간 $\mathbb{C}^{\mathbb{R}}$($\mathbb{R}$에서 $\mathbb{C}$로 가는 모든 함수)에서, 서로 다른 $\lambda\in\mathbb{R}$마다 $e_\lambda(x):=e^{i\lambda x}$로 정의된 함수는 언제나 일차독립이다. 실제로 서로 다른 $\lambda_1,\dots,\lambda_n$과 $\sum_{k=1}^nc_ke_{\lambda_k}=0$(모든 $x$에서)이 주어졌을 때, 미분연산자 $D=\frac{d}{dx}$가 $De_{\lambda_k}=i\lambda_ke_{\lambda_k}$를 만족한다는 데 주목하면, $\prod_{j\ne i}(D-i\lambda_jI)$를 양변에 적용할 때 $k\ne i$인 항은 인수 $(D-i\lambda_kI)$에 의해 사라지고 $k=i$인 항만 남아
$$c_i\prod_{j\ne i}(i\lambda_i-i\lambda_j)\,e_{\lambda_i}=0$$
이 된다. $e_{\lambda_i}$는 어디서도 $0$이 아니고 $\lambda_i$들이 서로 다르니 저 곱도 $0$이 아니므로 $c_i=0$이다. 따라서 $$W_\lambda:=\mathbb{C}e_\lambda\quad(\lambda\in\mathbb{R})$$들의 합 $\sum_{\lambda\in\mathbb{R}}W_\lambda$는 uncountable index 집합 $\mathbb{R}$ 위의 직합 $\bigoplus_{\lambda\in\mathbb{R}}W_\lambda$이고, 그 원소인 유한 결합 $\sum_kc_ke^{i\lambda_kx}$들이 바로 Fourier 해석에서 나타나는 generalized trigonometric polynomial의 공간이다.

**Corollary.** 합이 직합이면 $\dim(U\oplus W)=\dim U+\dim W$.

이 차원 등식은 실은 두 기저를 그냥 이어붙인 것이 기저가 된다는 더 구체적인 사실에서 나온다.

**Proposition (직합과 기저).** 부분공간 $U,W\subseteq V$의 기저가 각각 $u_1,\dots,u_p$, $w_1,\dots,w_q$일 때, $V=U\oplus W$인 것과 $u_1,\dots,u_p,w_1,\dots,w_q$가 $V$의 기저인 것은 동치다.

*Proof.* ($\Rightarrow$) $V=U\oplus W$이면 임의의 $v\in V$가 $v=u+w$ ($u\in U$, $w\in W$)로 유일하게 쪼개지고, $u,w$를 각자의 기저로 전개하면 $v$가 합친 벡터들의 결합이 되어 이들이 $V$를 span한다. 일차독립을 보자. $\sum_ia_iu_i+\sum_jb_jw_j=0$이면 $$\sum_ia_iu_i=-\sum_jb_jw_j\in U\cap W=\{0\}$$이라 $\sum_ia_iu_i=0$, $\sum_jb_jw_j=0$이고, 각 기저의 일차독립성으로 모든 계수가 $0$이다.

($\Leftarrow$) 합친 것이 $V$의 기저라 하자. 임의의 $v\in V$를 이 기저로 전개해 $U$쪽 항의 합을 $u$, $W$쪽 항의 합을 $w$라 두면 $v=u+w$이니 $V=U+W$이다. 또 $x\in U\cap W$, $x\ne0$이면 $x$를 $U$의 기저로 쓴 결합과 $W$의 기저로 쓴 결합의 차가 합친 기저의 자명하지 않은 일차종속 관계를 주어 모순이므로 $$U\cap W=\{0\}$$이다. 따라서 $V=U\oplus W$이다. $\blacksquare$

이 논증은 기저가 무한집합이어도 그대로 성립한다(어느 쪽이든 결합은 언제나 유한 합이기 때문이다).

## Complement

직합의 두 조각 중 하나를 고정해도, 나머지 하나는 유일하지 않을 뿐 존재는 항상 보장된다.

**Definition (Complement).** subspace $W\subseteq V$에 대해 $V=W\oplus U$를 만족하는 subspace $U$를 $W$의 complement라 한다.

**Example (직선의 여러 complement).** $\mathbb{R}^2$에서 $x$축 $$W=\{(a,0):a\in\mathbb{R}\}$$의 complement로 $y$축뿐 아니라 원점을 지나는 $W$가 아닌 임의의 직선을 잡을 수 있다. 예컨대 $$U=\{(a,a):a\in\mathbb{R}\}$$도 $$W\cap U=\{0\}$$, $W+U=\mathbb{R}^2$를 만족해 $W$의 complement다. Complement는 존재하지만 이렇게 유일하지 않다.

**Theorem (Complement의 존재).** 모든 subspace $W\subseteq V$는 complement를 가진다.

*Proof.* $W$도 벡터공간이므로 Basis Existence로 기저 $B_W$를 가진다. $B_W$를 포함하는 $V$의 일차독립 부분집합 전체를 포함관계로 정렬하면, 위 Basis Existence 증명과 똑같이(chain의 합집합도 일차독립이라 Zorn's Lemma가 적용된다) $B_W$를 포함하는 maximal 일차독립집합 $B$가 있고, 그 maximality가 $B$가 $V$를 span함을 보장하므로 $B$는 $B_W\subseteq B$인 $V$의 기저다. $$U:=\operatorname{span}(B\setminus B_W)$$로 두면 $B$가 $B_W$와 $B\setminus B_W$로 쪼개진 $V$의 기저이므로, 앞 "직합과 기저" Proposition의 ($\Leftarrow$) 방향으로 $V=W\oplus U$이다. $\blacksquare$

**Example (복소수를 실수부와 순허수부로).** $\mathbb{C}$를 $\mathbb{R}$ 위의 벡터공간으로 보면, 실수축 $\mathbb{R}\subseteq\mathbb{C}$의 complement로 순허수축 $i\mathbb{R}$을 잡을 수 있다. $z=\operatorname{Re}z+i\operatorname{Im}z$가 바로 이 direct sum에 대응하는 분해다.

## 참고문헌

1. Peano, G. (1888). *Calcolo geometrico secondo l'Ausdehnungslehre di H. Grassmann*. Torino: Bocca.
2. Grassmann, H. (1844). *Die lineale Ausdehnungslehre, ein neuer Zweig der Mathematik*. Leipzig: Otto Wigand.
3. Steinitz, E. (1910). Algebraische Theorie der Körper. *Journal für die reine und angewandte Mathematik*, 137, 167–309.
4. Hamel, G. (1905). Eine Basis aller Zahlen und die unstetigen Lösungen der Funktionalgleichung $f(x+y)=f(x)+f(y)$. *Mathematische Annalen*, 60, 459–462.
5. Cauchy, A.-L. (1821). *Cours d'analyse de l'École royale polytechnique*. Paris.
6. Blass, A. (1984). Existence of bases implies the axiom of choice. In *Axiomatic Set Theory*, Contemporary Mathematics 31, 31–33. American Mathematical Society.
7. Tarski, A. (1924). Sur quelques théorèmes qui équivalent à l'axiome du choix. *Fundamenta Mathematicae*, 5, 147–154.
8. Läuchli, H. (1962). Auswahlaxiom in der Algebra. *Commentarii Mathematici Helvetici*, 37, 1–18.
