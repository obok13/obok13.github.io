---
layout: post
title: "Vector space"
date: 2026-08-05
mathematicians: [Peano, Grassmann, Steinitz, Hamel, Zorn, Cauchy, Zermelo, Blass]
---

## 체와 벡터공간

**Definition (Field).** 집합 $F$와 두 연산 $+,\cdot$가 다음을 만족하면 $F$를 체(field)라 한다. $(F,+)$는 항등원 $0$을 갖는 abelian group이고, $$(F\setminus\{0\},\cdot)$$도 항등원 $1$을 갖는 abelian group이며, 분배법칙 $a(b+c)=ab+ac$가 성립한다.

예를 들어 $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$는 모두 체이다. 유한체도 있다.

**Definition (Vector Space).** 체 $F$ 위의 벡터공간(vector space)은 집합 $V$와 덧셈 $V\times V\to V$, 스칼라배 $F\times V\to V$로 이루어지며, $(V,+)$가 abelian group이고 모든 $a,b\in F$와 $u,v\in V$에 대해
$$a(u+v)=au+av, \quad (a+b)v=av+bv, \quad (ab)v=a(bv), \quad 1v=v$$
를 만족한다. $V$의 원소를 벡터, $F$의 원소를 스칼라라 한다.

정의에서 곧바로 $0v=0$, $a0=0$, $(-1)v=-v$가 나온다. 예컨대 $0v=(0+0)v=0v+0v$에서 양변에 $-0v$를 더하면 $0v=0$이다.

**Example.** $F^n$(성분별 연산), 한 집합 위의 $F$값 함수 전체, 다항식 공간 $F[x]$, 수열 공간이 모두 벡터공간이다. 특히 $\mathbb{C}$는 $\mathbb{R}$ 위의 벡터공간이자 $\mathbb{C}$ 위의 벡터공간이고, $\mathbb{R}$은 $\mathbb{Q}$ 위의 벡터공간이다. 마지막 것이 뒤에서 결정적인 역할을 한다.

벡터공간을 이렇게 공리로 처음 세운 사람은 Peano로, 1888년 Grassmann의 1844년 《Ausdehnungslehre》[2]를 이어받아 오늘날과 같은 정의를 제시했다 [1].

## 부분공간과 직합

**Definition (Subspace).** $V$의 부분집합 $W$가 $0\in W$이고 임의의 $a,b\in F$, $u,v\in W$에 대해 $au+bv\in W$이면 $W$를 부분공간(subspace)이라 한다. 부분공간은 물려받은 연산으로 그 자체가 벡터공간이다.

**Example (부분공간).** $\mathbb{R}^3$에서 원점을 지나는 직선 $$\{(t,2t,3t):t\in\mathbb{R}\}$$과 원점을 지나는 평면 $$\{(x,y,0):x,y\in\mathbb{R}\}$$은 부분공간이다. 함수 쪽에서는 닫힌구간 위 연속함수 전체 $C[a,b]$, 다항식 전체 $\mathbb{R}[x]$, 차수가 $n$ 이하인 다항식 전체 $$\{p\in\mathbb{R}[x]:\deg p\le n\}$$이 모두 부분공간이다.

**Example (원점을 지나지 않는 평면).** $$\{(x,y,1):x,y\in\mathbb{R}\}$$은 $0$을 포함하지 않으므로 부분공간이 아니다.

**Example (제1사분면).** $$\{(x,y):x\ge0,\ y\ge0\}$$은 덧셈에는 닫혀 있지만 $(-1)$배에 닫혀 있지 않으므로 부분공간이 아니다.

**Example (두 좌표축의 합집합).** $$\{(x,0):x\in\mathbb{R}\}\cup\{(0,y):y\in\mathbb{R}\}$$은 스칼라배에는 닫혀 있지만 $(1,0)+(0,1)=(1,1)$을 포함하지 않아 덧셈에 닫혀 있지 않으므로 부분공간이 아니다. 바로 앞의 제1사분면과 나란히 놓고 보면 덧셈과 스칼라배 두 닫힘 조건이 모두 필요함을 알 수 있다.

**Example (차수가 정확히 $n$인 다항식).** 이 모임은 $0$을 포함하지 않고 덧셈에도 닫히지 않으므로 부분공간이 아니다.

**Definition (Sum, Direct Sum).** 부분공간 $W_1,W_2$에 대해 그 합은
$$W_1+W_2 := \{\,w_1+w_2 : w_1\in W_1,\ w_2\in W_2\,\}$$
이고 이것도 부분공간이다. $$W_1\cap W_2=\{0\}$$이면 이 합을 직합(direct sum)이라 부르고 $W_1\oplus W_2$로 쓴다.

**Proposition.** $W_1+W_2$가 직합인 것과, 모든 원소가 $w_1+w_2$ ($w_i\in W_i$) 꼴로 유일하게 표현되는 것은 동치다.

*Proof.* 표현이 유일하지 않다면 $w_1+w_2=w_1'+w_2'$이면서 $(w_1,w_2)\ne(w_1',w_2')$인 경우가 있고, 이때 $x:=w_1-w_1'=w_2'-w_2$는 $W_1\cap W_2$에 속하는 영이 아닌 벡터다. 역으로 $$0\ne x\in W_1\cap W_2$$이면 $0=x+(-x)$가 $0=0+0$과 다른 표현이 된다. 따라서 표현의 유일성과 $$W_1\cap W_2=\{0\}$$은 동치다. $\blacksquare$

**Example (직합).** $\mathbb{R}^2$은 $x$축 $X=$ $$\{(a,0):a\in\mathbb{R}\}$$과 $y$축 $Y=$ $$\{(0,b):b\in\mathbb{R}\}$$의 직합이다. 모든 $(a,b)=(a,0)+(0,b)$가 유일하게 쪼개지기 때문이다. 함수 쪽의 예로, $\mathbb{R}$ 위의 모든 함수 $f$는
$$f(x)=\underbrace{\tfrac{f(x)+f(-x)}{2}}_{\text{even}}+\underbrace{\tfrac{f(x)-f(-x)}{2}}_{\text{odd}}$$
로 우함수와 기함수의 합으로 유일하게 쓰이므로, 함수공간은 우함수 부분공간과 기함수 부분공간의 직합이다.

**Example (직합이 아닌 합).** $\mathbb{R}^3$에서 $xy$평면 $P$와 $yz$평면 $Q$를 보면 $P+Q=\mathbb{R}^3$이지만 $P\cap Q$가 $y$축이라 직합이 아니다. 실제로 $(0,1,0)$이 $P$의 벡터로도 $Q$의 벡터로도 표현되어 유일성이 깨진다.

## 일차독립과 기저

**Definition (Span).** $S\subseteq V$에 대해 $S$의 유한 일차결합 전체
$$\operatorname{span}S := \{\,a_1v_1+\cdots+a_kv_k : k\ge0,\ a_i\in F,\ v_i\in S\,\}$$
를 $S$가 생성하는 부분공간이라 한다($k=0$인 빈 결합은 $0$). 이는 $S$를 포함하는 가장 작은 부분공간이다.

**Definition (Linear Independence).** $S\subseteq V$가 일차독립(linearly independent)이라는 것은, $S$의 서로 다른 유한개 $v_1,\dots,v_k$에 대해 $a_1v_1+\cdots+a_kv_k=0$이면 반드시 $a_1=\cdots=a_k=0$이라는 뜻이다. 그렇지 않으면 일차종속(linearly dependent)이라 한다.

**Definition (Basis).** $V$를 span하는 일차독립 집합 $B$를 $V$의 기저(basis)라 한다.

**Proposition.** $B$가 기저인 것과, 모든 $v\in V$가 $B$의 원소들의 유한 일차결합으로 유일하게 표현되는 것은 동치다.

*Proof.* span이라는 것이 표현의 존재이고, 두 표현 $v=\sum a_iv_i=\sum b_iv_i$의 차 $\sum(a_i-b_i)v_i=0$가 일차독립에 의해 $a_i=b_i$를 강제하는 것이 표현의 유일성이다. $\blacksquare$

**Example (기저).** $\mathbb{R}^3$의 표준기저는 $$\{(1,0,0),(0,1,0),(0,0,1)\}$$이고, $$\{(1,1,0),(0,1,1),(1,0,1)\}$$도 기저다(세 벡터가 일차독립이고 $\mathbb{R}^3$을 span한다). 다항식 공간 $\mathbb{R}[x]$에서는 $$\{1,x,x^2,\dots\}$$이 기저이며, $$\{1,\,1+x,\,1+x+x^2,\dots\}$$도 기저다. $\mathbb{C}$를 $\mathbb{R}$ 위의 벡터공간으로 보면 $$\{1,i\}$$가 기저(차원 2)이지만, $\mathbb{C}$ 자신 위의 벡터공간으로 보면 $$\{1\}$$이 기저(차원 1)다. 같은 집합도 스칼라체를 무엇으로 잡느냐에 따라 기저와 차원이 달라진다.

**Example (기저가 아닌 것).** $\mathbb{R}^2$에서 $$\{(1,2),(2,4)\}$$는 $(2,4)=2(1,2)$로 일차종속이라 기저가 아니다. $$\{(1,0),(0,1),(1,1)\}$$은 $\mathbb{R}^2$를 span하지만 $(1,1)=(1,0)+(0,1)$로 종속이라(벡터가 차원보다 많다) 기저가 아니고, 거꾸로 $$\{(1,0)\}$$은 일차독립이지만 span하지 못해 기저가 아니다. 일반적으로 벡터가 차원보다 많으면 반드시 종속이고(교환 보조정리), 적으면 span할 수 없다.

## 차원

기저의 크기가 표현 방식에 무관하게 정해진다는 것이 선형대수의 첫 번째 핵심이다. 그 열쇠가 Steinitz의 교환 보조정리다 [3].

**Lemma (Steinitz Exchange).** $$\{v_1,\dots,v_m\}$$이 일차독립이고 $$\{w_1,\dots,w_n\}$$이 $V$를 span하면 $m\le n$이다.

*Proof.* $w$들이 span하므로 $v_1=\sum_{j=1}^n c_jw_j$인데, $v_1\ne0$(일차독립 집합은 $0$을 포함하지 않는다)이라 어떤 $c_j\ne0$이다. 번호를 바꿔 $c_1\ne0$이라 하면 $w_1$을 $v_1,w_2,\dots,w_n$의 결합으로 풀 수 있으므로 $$\{v_1,w_2,\dots,w_n\}$$도 $V$를 span한다. 이제 이미 $$\{v_1,\dots,v_k,w_{k+1},\dots,w_n\}$$이 span한다고 하자. $v_{k+1}$을 이 집합의 결합으로 쓰면, $w$들의 계수가 모두 $0$일 수는 없다(그렇다면 $v_{k+1}\in\operatorname{span}\{v_1,\dots,v_k\}$가 되어 $v$들의 일차독립에 모순). 그 $w$ 하나를 $v_{k+1}$로 교환하면 $$\{v_1,\dots,v_{k+1},w_{k+2},\dots,w_n\}$$이 다시 span한다. 만약 $m>n$이라면 $n$번의 교환 뒤 $w$가 모두 소진되어 $$\{v_1,\dots,v_n\}$$이 span하게 되고, 그러면 남은 $v_{n+1}$이 앞 $v$들의 결합이 되어 일차독립에 모순이다. 따라서 $m\le n$이다. $\blacksquare$

**Theorem.** 유한 기저를 가지는 벡터공간의 임의의 두 기저는 원소의 개수가 같다.

*Proof.* 기저 $B$(크기 $m$)와 $C$(크기 $n$)에 대해, $B$는 일차독립이고 $C$는 span하므로 교환 보조정리로 $m\le n$이고, 역할을 바꾸면 $n\le m$이다. 따라서 $m=n$이다. $\blacksquare$

**Definition (Dimension).** 이 공통의 개수를 $V$의 차원 $\dim V$라 한다. 유한 기저가 없으면 $V$를 무한차원이라 한다.

**Example.** $\dim F^n=n$(표준기저), $\dim_{\mathbb{R}}\mathbb{C}=2$, $\dim_{\mathbb{C}}\mathbb{C}=1$이다. 다항식 공간 $F[x]$는 $1,x,x^2,\dots$가 일차독립이라 무한차원이다. 무한차원에서도 임의의 두 기저는 같은 cardinality를 가지지만, 그 증명은 무한 cardinal 산술이 필요하므로 여기서는 넘어간다.

## 기저의 존재

**Theorem.** 유한개의 벡터로 span되는 벡터공간은 기저를 가진다. 더욱이 임의의 일차독립 집합은 기저로 확장할 수 있고, 임의의 span 집합은 기저를 포함한다.

*Proof.* 유한 span 집합에서 다른 원소들의 결합으로 표현되는 벡터를 하나씩 제거해도 span은 유지되고, 더 제거할 수 없게 되면 남은 집합은 일차독립이라 기저다. 확장의 경우, 일차독립 집합에 span 밖의 벡터를 계속 더하면 독립성이 유지되고, 유한 생성이면 이 과정이 유한 번에 끝나 기저에 도달한다. $\blacksquare$

무한차원에서는 이런 유한 절차가 끝나지 않는다. 여기서 선택 공리가 등장한다.

**Theorem (Basis Existence).** 모든 벡터공간은 기저를 가진다.

*Proof.* $V$의 일차독립 부분집합 전체를 포함관계로 정렬하자. 이 정렬에서 사슬(전순서 부분집합) $\mathcal{C}$의 합집합 $U=\bigcup\mathcal{C}$는 다시 일차독립이다. $U$의 유한 부분집합이 일차종속이라면 그 유한개의 벡터가 사슬의 어느 한 원소에 모두 들어가는데, 그 원소가 일차독립이라는 데 모순이기 때문이다. 따라서 모든 사슬이 상계를 가지므로, 선택 공리 글에서 다룬 Zorn's Lemma에 의해 극대 일차독립집합 $M$이 존재한다. 만약 $M$이 $V$를 span하지 않으면 $v\notin\operatorname{span}M$인 $v$가 있고 $$M\cup\{v\}$$가 여전히 일차독립이라 $M$의 극대성에 모순이다. 그러므로 $M$은 $V$를 span하는 일차독립 집합, 곧 기저다. $\blacksquare$

이 정리는 사실 선택 공리와 동치다. "모든 벡터공간이 기저를 가진다"는 명제에서 거꾸로 선택 공리를 이끌어낼 수 있음을 Blass가 1984년에 증명했다 [6]. 즉 무한차원 기저의 존재는 순수한 존재 정리일 뿐, 대개 구체적으로 적어낼 수 없다.

**Definition (Hamel Basis).** $\mathbb{R}$을 $\mathbb{Q}$ 위의 벡터공간으로 볼 때의 기저를 Hamel basis라 한다 [4]. 위 정리(즉 선택 공리)가 그 존재를 보장하지만, 명시적으로 나열하는 것은 불가능하다.

## Cauchy의 함수방정식

Hamel basis의 존재는 해석학에 뜻밖의 그림자를 드리운다. Cauchy가 1821년에 다룬 다음 방정식이 그 무대다 [5].

**Definition.** 함수 $f:\mathbb{R}\to\mathbb{R}$가 모든 $x,y$에서 $f(x+y)=f(x)+f(y)$를 만족하면 additive라 한다.

**Proposition.** additive 함수 $f$는 $\mathbb{Q}$-선형이다. 즉 모든 $q\in\mathbb{Q}$, $x\in\mathbb{R}$에서 $f(qx)=qf(x)$이다. 특히 $f$가 한 점에서라도 연속이면 $f(x)=cx$ ($c=f(1)$) 꼴이다.

*Proof.* $f(0)=f(0)+f(0)$에서 $f(0)=0$이고, 귀납법으로 $f(nx)=nf(x)$ ($n\ge1$), $f(-x)=-f(x)$를 얻는다. 또 $f(x)=f\!\left(n\cdot\tfrac{x}{n}\right)=nf\!\left(\tfrac{x}{n}\right)$이므로 $f(x/n)=f(x)/n$이고, 이 둘을 합치면 $q=m/n$에 대해 $f(qx)=qf(x)$이다. 이제 $f$가 연속이라 하자. 임의의 $x\in\mathbb{R}$에 대해 $x$로 수렴하는 유리수열 $q_k$를 잡으면 $f(q_k)=q_kf(1)$이고, 연속성으로 $k\to\infty$에서 $f(x)=xf(1)$이다. $\blacksquare$

연속 조건이 붙으면 이렇게 해가 직선 $f(x)=cx$로 고정된다. 그런데 아무 조건도 없으면 사정이 완전히 달라진다.

**Theorem (Hamel).** $f(x)=cx$ 꼴이 아닌 additive 함수가 존재한다. 그런 $f$는 어떤 점에서도 연속이 아니며, 그 그래프 $$\{(x,f(x)):x\in\mathbb{R}\}$$는 $\mathbb{R}^2$에서 조밀하다.

*Proof.* $\mathbb{R}$의 Hamel basis $H$를 하나 잡는다. 각 $x\in\mathbb{R}$은 $H$의 원소들의 유한 유리계수 결합으로 유일하게 쓰이므로, $H$ 위에서 $f$의 값을 임의로 정하면 $\mathbb{Q}$-선형으로 유일하게 확장되고 이 $f$는 additive다. 이때 서로 다른 $h_1,h_2\in H$에서 $f(h_1)/h_1\ne f(h_2)/h_2$가 되도록 값을 정하자. 만약 모든 $x$에서 $f(x)=cx$라면 특히 모든 $h\in H$에서 $f(h)/h=c$로 일정해야 하므로 모순이다. 따라서 $f$는 $cx$ 꼴이 아니다.

이제 $f$가 $\mathbb{Q}$-선형이지만 어떤 직선 $y=cx$에도 담기지 않으므로, 그래프 $G=\{(x,f(x))\}$는 $\mathbb{R}^2$의 $\mathbb{Q}$-부분공간이면서 한 직선에 들어가지 않는다. 그런 $\mathbb{Q}$-부분공간은 일차독립인 두 벡터 $(x_1,f(x_1))$, $(x_2,f(x_2))$를 포함하고, 그 유리계수 결합 전체가 이미 $\mathbb{R}^2$에서 조밀하다. 조밀한 그래프를 가진 함수는 어느 점에서도 연속일 수 없다(연속이면 그래프가 국소적으로 곡선 근방에 갇혀 조밀할 수 없다). $\blacksquare$

사실 $f$가 measurable이기만 해도, 혹은 양의 measure를 갖는 어떤 집합에서 유계이기만 해도 $f(x)=cx$임이 알려져 있다(Fréchet, Sierpiński). 이 방향은 측도론이 필요하므로 뒤의 측도론 글로 미룬다.

비선형 additive 함수는 Vitali 집합이나 Banach–Tarski 분해처럼, 선택 공리가 낳지만 결코 손으로 그릴 수 없는 대상이다.

## 참고문헌

1. Peano, G. (1888). *Calcolo geometrico secondo l'Ausdehnungslehre di H. Grassmann*. Torino: Bocca.
2. Grassmann, H. (1844). *Die lineale Ausdehnungslehre, ein neuer Zweig der Mathematik*. Leipzig: Otto Wigand.
3. Steinitz, E. (1910). Algebraische Theorie der Körper. *Journal für die reine und angewandte Mathematik*, 137, 167–309.
4. Hamel, G. (1905). Eine Basis aller Zahlen und die unstetigen Lösungen der Funktionalgleichung $f(x+y)=f(x)+f(y)$. *Mathematische Annalen*, 60, 459–462.
5. Cauchy, A.-L. (1821). *Cours d'analyse de l'École royale polytechnique*. Paris.
6. Blass, A. (1984). Existence of bases implies the axiom of choice. In *Axiomatic Set Theory*, Contemporary Mathematics 31, 31–33. American Mathematical Society.
