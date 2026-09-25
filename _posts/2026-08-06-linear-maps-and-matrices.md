---
layout: post
title: "Linear map"
date: 2026-08-06
mathematicians: [Cayley, Sylvester, Frobenius, Strang, Noether]
---

## 선형사상

**Definition (Linear Map).** 같은 체 $F$ 위의 벡터공간 $V,W$ 사이의 사상 $T:V\to W$가 모든 $a,b\in F$, $u,v\in V$에 대해
$$T(au+bv)=aT(u)+bT(v)$$
를 만족하면 $T$를 선형사상(linear map)이라 한다.

$a=b=0$을 넣으면 $T(0)=0$이 곧바로 나온다. 즉 선형사상은 원점을 원점으로 보낸다.

**Example (미분).** 다항식 공간 위의 미분 $D:\mathbb{R}[x]\to\mathbb{R}[x]$, $D(p)=p'$은 선형사상이다. $(ap+bq)'=ap'+bq'$이기 때문이다.

**Example (회전).** 평면의 원점 중심 $\theta$ 회전 $R_\theta:\mathbb{R}^2\to\mathbb{R}^2$은 선형사상이고, $R_\theta(x,y)=(x\cos\theta-y\sin\theta,\ x\sin\theta+y\cos\theta)$로 주어진다.

**Example (평가사상).** 한 점 $c$에서의 값매김 $$\operatorname{ev}_c:\mathbb{R}[x]\to\mathbb{R}$$, $p\mapsto p(c)$은 선형사상이다.

**Example (선형이 아닌 것: 평행이동).** $b\ne0$인 평행이동 $T(x)=x+b$는 $T(0)=b\ne0$이므로 선형사상이 아니다. 그래프가 원점을 지나는 직선이라도 그것이 원점을 안 지나면 선형이 아니다.

선형사상의 핵심 정보는 무엇이 $0$으로 가고(kernel) 무엇이 상으로 나타나는가(image)에 담겨 있다.

**Definition (Kernel, Image).** 선형사상 $T:V\to W$에 대해
$$\ker T := \{\,v\in V : T(v)=0\,\}, \qquad \operatorname{im}T := \{\,T(v) : v\in V\,\}$$
를 각각 $T$의 kernel과 image라 한다. $\ker T$는 $V$의 부분공간이고 $\operatorname{im}T$는 $W$의 부분공간이다.

**Proposition.** $T$가 단사(injective)인 것과 $$\ker T=\{0\}$$인 것은 동치다.

*Proof.* $T$가 단사이면 $T(v)=0=T(0)$에서 $v=0$이므로 $$\ker T=\{0\}$$이다. 역으로 $$\ker T=\{0\}$$이고 $T(u)=T(v)$이면 $T(u-v)=0$이라 $u-v\in\ker T$, 즉 $u=v$이다. $\blacksquare$

**Example (미분의 kernel과 image).** $D:\mathbb{R}[x]\to\mathbb{R}[x]$의 kernel은 미분이 $0$인 다항식, 곧 상수함수들이고, image는 $\mathbb{R}[x]$ 전체다(모든 다항식은 어떤 다항식의 도함수다). 상수를 $0$으로 뭉개는 만큼 정보가 줄어든다.

## Rank-Nullity 정리

**Definition (Rank, Nullity).** $\operatorname{rank}T:=\dim\operatorname{im}T$, $\operatorname{nullity}T:=\dim\ker T$라 한다.

**Theorem (Rank-Nullity).** $V$가 유한차원이고 $T:V\to W$가 선형사상이면
$$\dim V = \operatorname{rank}T + \operatorname{nullity}T.$$

*Proof.* $\ker T$의 기저 $$\{u_1,\dots,u_k\}$$를 잡고(따라서 $\operatorname{nullity}T=k$), 지난 글의 확장 정리로 이를 $V$의 기저 $$\{u_1,\dots,u_k,w_1,\dots,w_r\}$$로 늘린다. 그러면 $\dim V=k+r$이다. 이제 $$\{T(w_1),\dots,T(w_r)\}$$이 $\operatorname{im}T$의 기저임을 보이면 $\operatorname{rank}T=r$이 되어 증명이 끝난다.

span: 임의의 $v=\sum a_iu_i+\sum b_jw_j$에 대해 $T(u_i)=0$이므로 $T(v)=\sum b_jT(w_j)$이다. 따라서 $T(w_j)$들이 $\operatorname{im}T$를 생성한다.

일차독립: $\sum c_jT(w_j)=0$이면 $T\big(\sum c_jw_j\big)=0$이라 $$\sum c_jw_j\in\ker T=\operatorname{span}\{u_i\}$$이다. 그러면 $\sum c_jw_j=\sum d_iu_i$인데, $$\{u_1,\dots,u_k,w_1,\dots,w_r\}$$이 일차독립이므로 모든 $c_j=0$이다. $\blacksquare$

**Example (미분에서의 rank-nullity).** 차수가 $n$ 이하인 다항식 공간 $P_n$($\dim=n+1$) 위의 미분 $D$를 보자. $\ker D$는 상수들이라 $\operatorname{nullity}D=1$이고, $\operatorname{im}D=P_{n-1}$이라 $\operatorname{rank}D=n$이다. 과연 $1+n=n+1=\dim P_n$이다.

**Corollary.** $\dim V=\dim W$인 유한차원 공간 사이의 선형사상 $T:V\to W$에서는 단사, 전사, 전단사가 모두 동치다.

*Proof.* $T$가 단사 $\iff\operatorname{nullity}T=0\iff\operatorname{rank}T=\dim V=\dim W\iff\operatorname{im}T=W\iff T$가 전사. $\blacksquare$

**Definition (Isomorphism).** 벡터공간 $V,W$ 사이의 linear map $T:V\to W$가 bijective(단사이며 전사)이면 isomorphism이라 하고, $V\cong W$로 쓴다.

## Quotient space

rank-nullity를 좌표 없이 다시 보는 방법이 있다. kernel을 통째로 $0$인 coset으로 뭉개면, 그 quotient space가 곧바로 image와 같아진다.

**Definition (Coset, Quotient Space).** $v\in V$에 대해 $$v+W:=\{\,v+w : w\in W\,\}$$를 $v$의 coset이라 한다. coset 전체를 $V/W$로 쓰고, 여기에 $$(v_1+W)+(v_2+W):=(v_1+v_2)+W,\qquad c\,(v+W):=(cv)+W$$로 연산을 준 것을 $W$에 의한 quotient space라 한다.

두 coset은 같거나 서로소다. 실제로 $v_1+W=v_2+W$인 것은 $v_1-v_2\in W$인 것과 동치다.

**Proposition (well-defined).** 위 두 연산은 대표원 선택에 무관하다.

*Proof.* $v_1+W=v_1'+W$, $v_2+W=v_2'+W$이면 $v_1-v_1',\,v_2-v_2'\in W$이라 $(v_1+v_2)-(v_1'+v_2')\in W$, 곧 $(v_1+v_2)+W=(v_1'+v_2')+W$이다. 스칼라곱도 $cv-cv'=c(v-v')\in W$라 같다. $\blacksquare$

$V/W$는 이 연산으로 vector space가 되고 영벡터는 $0+W=W$다.

**Example (trace로 몫공간 보기).** $V=F^{n\times n}$(모든 $n\times n$ 행렬), $$W=\{A\in F^{n\times n}:\operatorname{tr}A=0\}$$(trace가 $0$인 행렬 전체, $V$의 부분공간)이라 하자. 두 행렬 $A,B$가 같은 coset에 속하는 것과 $\operatorname{tr}A=\operatorname{tr}B$인 것은 동치이므로, coset $A+W$는 $\operatorname{tr}A$라는 숫자 하나로 완전히 결정된다.

**Theorem (Dimension).** $V$가 유한차원이면 $$\dim(V/W)=\dim V-\dim W.$$

*Proof.* $W$의 basis $w_1,\dots,w_k$를 $V$의 basis $w_1,\dots,w_k,u_1,\dots,u_r$로 확장한다($\dim V=k+r$). $u_1+W,\dots,u_r+W$가 $V/W$의 basis임을 보이면 된다. 임의의 $v=\sum a_iw_i+\sum b_ju_j$에서 $\sum a_iw_i\in W$이라 $v+W=\sum b_j(u_j+W)$이니 이들이 생성한다. 또 $\sum b_j(u_j+W)=W$이면 $\sum b_ju_j\in W$인데 $w_i,u_j$가 일차독립이라 모든 $b_j=0$이다. 따라서 $\dim(V/W)=r=\dim V-\dim W$이다. $\blacksquare$

**Example (symmetric matrix를 diagonal matrix로 나눔).** $V=$ $3\times3$ symmetric matrix 전체($\dim V=6$), $W=$ diagonal matrix 전체($\dim W=3$, $V$의 부분공간)라 하자. Dimension 정리로 $\dim(V/W)=6-3=3$인데, 이는 symmetric matrix의 대각선 위쪽 세 성분($a_{12},a_{13},a_{23}$)의 자유도와 정확히 일치한다. 대각선분만 다른 두 symmetric matrix는 같은 coset에 속하기 때문이다.

coset으로 보내는 map이 quotient space의 뼈대다.

**Definition (Quotient Map).** $\pi:V\to V/W$, $\pi(v)=v+W$를 quotient map이라 한다. $\pi$는 surjective linear map이고 $\ker\pi=W$이다.

quotient는 "$W$를 $0$으로 만드는 map"을 가장 경제적으로 담는다.

**Theorem (Universal Property).** linear map $T:V\to U$가 $W\subseteq\ker T$를 만족하면, $T=\bar T\circ\pi$인 linear map $\bar T:V/W\to U$가 유일하게 존재한다.

*Proof.* $\bar T(v+W):=T(v)$로 정의한다. $v+W=v'+W$이면 $v-v'\in W\subseteq\ker T$라 $T(v)=T(v')$이니 well-defined이고, linear임은 연산의 정의에서 곧바로 나온다. $\bar T\circ\pi=T$는 정의 그대로이며, $\pi$가 surjective라 이 조건이 $\bar T$를 유일하게 정한다. $\blacksquare$

**Theorem (First Isomorphism).** linear map $T:V\to U$에 대해 $$V/\ker T\;\cong\;\operatorname{im}T.$$

*Proof.* universal property를 $W=\ker T$에 적용하면 $\bar T:V/\ker T\to U$가 나오고 그 상은 $\operatorname{im}T$다. $\bar T$는 injective다: $\bar T(v+\ker T)=0$이면 $T(v)=0$이라 $v\in\ker T$, 곧 $v+\ker T=\ker T$이다. 따라서 $V/\ker T\to\operatorname{im}T$가 isomorphism이다. $\blacksquare$

First Isomorphism은 $V$가 무한차원이어도 성립하므로 rank-nullity의 일반화라 할 수 있다. 실제로 $V$가 유한차원이어서 이 isomorphism에 차원을 셀 수 있으면 $\dim(V/\ker T)=\dim\operatorname{im}T$, 곧 $\dim V-\dim\ker T=\operatorname{rank}T$를 얻어 rank-nullity가 다시 나온다.

**Example (trace map).** $T=\operatorname{tr}:F^{n\times n}\to F$는 linear map이고 $$\ker T=\{A:\operatorname{tr}A=0\}$$은 앞서 본 $W$와 같다. $T$는 surjective다: 임의의 $c\in F$가 $(1,1)$ 성분만 $c$이고 나머지는 $0$인 행렬의 trace이기 때문이다. First Isomorphism은 $$F^{n\times n}/W\;\cong\;F$$를 주는데, 이는 앞에서 coset이 $\operatorname{tr}A$ 하나로 결정된다고 본 것을 정확히 다시 확인해준다.

두 subspace의 합과 교집합도 quotient로 비교할 수 있다.

**Theorem (Second Isomorphism).** subspace $U,W\subseteq V$에 대해 $$(U+W)/W\;\cong\;U/(U\cap W).$$

*Proof.* $\pi:V\to V/W$의 $U$로의 restriction $\pi\vert_U:U\to V/W$를 생각하자. 그 image는 $$\{\,u+W:u\in U\,\}=(U+W)/W$$이다($U+W$의 임의의 원소 $u+w$가 주는 coset이 $u+W$와 같기 때문이다). 또 kernel은 $$\{\,u\in U:u\in W\,\}=U\cap W$$이다. First Isomorphism Theorem을 $\pi\vert_U$에 적용하면 $$U/(U\cap W)=U/\ker(\pi\vert_U)\;\cong\;\operatorname{im}(\pi\vert_U)=(U+W)/W$$이다. $\blacksquare$

**Example (두 점에서의 소멸조건).** $V=P_2(\mathbb{R})$(차수 $2$ 이하 다항식, $\dim V=3$), $$U=\{p\in V:p(0)=0\}$$($\dim U=2$), $$W=\{p\in V:p(1)=0\}$$($\dim W=2$)라 하자. $$U\cap W=\{p\in V:p(0)=p(1)=0\}$$은 $x(x-1)$의 스칼라배뿐이라 $\dim(U\cap W)=1$이고, Grassmann's Dimension Formula로 $\dim(U+W)=2+2-1=3=\dim V$이니 $U+W=V$다. Second Isomorphism은 $$V/W\;\cong\;U/(U\cap W)$$를 주는데, 양쪽 모두 차원이 $3-2=2-1=1$로 일치한다.

quotient space와 isomorphism 정리를 대수 구조의 기본 도구로 끌어올린 것은 1920년대 Emmy Noether를 중심으로 한 추상대수학이며, 그 관점은 van der Waerden의 《Moderne Algebra》(1930)로 정리되어 널리 퍼졌다 [1].

## 행렬 표현

Finite dimensional vector space $V$의 basis를 $$\mathcal{B}=\{v_1,\dots,v_n\}$$, $W$의 basis를 $$\mathcal{C}=\{w_1,\dots,w_m\}$$라고 하자. $V$에서 $W$로 가는 linear map $T$는 각 $T(v_i)$만 결정하면 결정된다. 게다가 $T(v_i)$는 $w_j$의 선형 결합일 것이므로 $T$는 다음과 같이 $mn$개의 원소로 표현이 가능하다.

**Definition (Matrix of a Linear Map).** 각 $T(v_j)$를 $\mathcal{C}$로 전개해 $T(v_j)=\sum_{i=1}^m a_{ij}w_i$로 쓸 때, 계수들을 모은 $m\times n$ 행렬 $A=(a_{ij})$를 기저 $\mathcal{B},\mathcal{C}$에 대한 $T$의 행렬 표현이라 한다. 즉 $A$의 $j$번째 열은 $T(v_j)$의 $\mathcal{C}$-좌표다. 

$V$의 한 벡터를 $v=\sum_j\alpha_jv_j$라고 할 때 $T(v) = \sum_j \alpha_j T(v_j) = \sum_{i,j}\alpha_j a_{ij} w_i$이므로 각 $w_i$의 계수는 $\sum_ja_{ij}\alpha_j$가 된다. 여기서 핵심은 $a_{ij}$가 basis인 $w_i$에 대해서는 $i$-sum이지만 계수인 $\alpha_j$에 대해서는 $j$-sum이라는 것이다.

이 대응은 벡터공간 $\mathcal{L}(V,W)$(선형사상 전체)와 $m\times n$ 행렬 전체 사이의 동형사상이다. 특히 선형사상의 합성은 정확히 행렬의 곱이 된다.

**Theorem.** $T:V\to W$와 $S:W\to U$가 각각 행렬 $A$, $B$로 표현되면(가운데 기저를 공유), 합성 $S\circ T:V\to U$는 행렬 $BA$로 표현된다.

*Proof.* $T(v_j)=\sum_k a_{kj}w_k$이고 $S(w_k)=\sum_i b_{ik}u_i$이므로
$$S(T(v_j))=\sum_k a_{kj}S(w_k)=\sum_k a_{kj}\sum_i b_{ik}u_i=\sum_i\Big(\sum_k b_{ik}a_{kj}\Big)u_i$$
이고, $u_i$의 계수 $\sum_k b_{ik}a_{kj}$가 바로 곱행렬 $BA$의 $(i,j)$ 성분이다. $\blacksquare$

행렬 곱셈이 "행과 열을 훑어 곱해 더하는" 낯선 규칙으로 정의되는 이유가 여기 있다. 합성이 곱이 되도록 맞춘 것이다.

**Example (미분의 행렬).** $P_2$의 기저 $$\{1,x,x^2\}$$에서 $D(1)=0$, $D(x)=1$, $D(x^2)=2x$이므로 $D$의 행렬은
$$\begin{pmatrix} 0&1&0\\ 0&0&2\\ 0&0&0\end{pmatrix}$$
이다. 이 행렬을 두 번 곱하면 $D^2$(이계도함수)의 행렬이 되고, 세 번 곱하면 영행렬이 된다($P_2$에서 세 번 미분하면 $0$).

## 기저 변환과 similarity

Basis를 바꾸면 같은 벡터라도 좌표가 달라지고, 같은 linear map이라도 행렬 표현이 달라진다. 먼저 벡터의 좌표부터 보자. Vector space $V$의 두 basis를 $$\mathcal{B}=\{v_1,\dots,v_n\}$$, $$\mathcal{C}=\{u_1,\dots,u_n\}$$라 하자. 한 벡터 $v$를 두 basis로 전개하면 $$v=\sum_i\alpha_iv_i=\sum_j\beta_ju_j$$처럼 좌표 $\alpha=(\alpha_i)$와 $\beta=(\beta_j)$가 나온다. 둘을 잇기 위해 새 basis 벡터 $u_j$를 $\mathcal{B}$로 전개해 $u_j=\sum_iP_{ij}v_i$라 두자. 곧 $P$의 $j$번째 열은 $u_j$의 $\mathcal{B}$-좌표다. 그러면
$$v=\sum_j\beta_ju_j=\sum_j\beta_j\sum_iP_{ij}v_i=\sum_i\Big(\sum_jP_{ij}\beta_j\Big)v_i$$
이므로 $\alpha_i=\sum_jP_{ij}\beta_j$, 곧 $\alpha=P\beta$이다. 이 $P$를 basis 변환 행렬이라 한다.

거꾸로 $\beta$를 $\alpha$에서 얻으려면 $P$의 inverse가 필요하다. 정사각행렬의 inverse는 뒤 글에서 따로 다루지만, $P$는 두 basis의 좌표를 서로 옮기는 행렬이라 그 역과정이 분명히 있다. 그 inverse를 $P^{-1}$로 쓰면 $\beta=P^{-1}\alpha$이다.

이 좌표 변환을 linear map에 얹으면 행렬 표현의 변화가 나온다. 먼저 $T:V\to W$에서 정의역 basis만 $\mathcal{B}$에서 $\mathcal{C}$로 바꿔 보자(공역 basis는 그대로 두고, $\mathcal{B}$에서의 행렬 표현을 $A$라 한다). 어떤 벡터의 새 좌표가 $\beta$이면 옛 좌표는 $\alpha=P\beta$이고, 그 상의 좌표는 $A\alpha=AP\beta$이다. 곧 새 정의역 basis에서의 행렬 표현은 $AP$로, 좌표를 $P$로 옛 basis로 되돌린 뒤 $A$를 적용한 꼴이다.

이제 정의역과 공역이 같은 operator $T:V\to V$를 보자. 이때는 한 basis를 입력 쪽과 출력 쪽에 함께 쓰므로, basis를 $\mathcal{B}$에서 $\mathcal{C}$로 바꾸면 변환이 양쪽에서 일어난다. $\mathcal{B}$에서의 행렬 표현을 $A$라 하면, $\mathcal{C}$-좌표가 $\beta$인 벡터의 상은 $\mathcal{B}$-좌표로 $A\alpha=AP\beta$이고, 이를 다시 $\mathcal{C}$-좌표로 옮기면 $P^{-1}AP\beta$이다. 따라서 $\mathcal{C}$에서의 행렬 표현은
$$A'=P^{-1}AP$$
이다. 정의역 쪽 변화 $AP$에 공역 쪽 변화 $P^{-1}$가 하나 더 붙은 셈이다.

이렇게 같은 operator가 basis에 따라 갖는 두 행렬 표현의 관계를 similar라 한다.

**Definition (Similar).** 정사각행렬 $A,B$가 어떤 invertible $P$로 $B=P^{-1}AP$를 만족하면 $A$와 $B$가 similar하다고 한다. 곧 similar란 같은 선형사상을 서로 다른 기저에서 표현한 것이다.

**Example (기저를 바꾸면 단순해지는 operator).** 직선 $y=x$에 대한 반사 $T(x,y)=(y,x)$는 표준 basis에서 $$[T]=\begin{pmatrix}0&1\\1&0\end{pmatrix}$$이다. 그런데 반사축 방향과 그에 수직인 방향을 새 basis $$\mathcal{C}=\{(1,1),(1,-1)\}$$로 잡으면 $T(1,1)=(1,1)$, $T(1,-1)=(-1,1)=-(1,-1)$이라 이 basis에서는 $$[T]_\mathcal{C}=\begin{pmatrix}1&0\\0&-1\end{pmatrix}$$로 diagonal이 된다. 새 basis를 열로 세운 $$P=\begin{pmatrix}1&1\\1&-1\end{pmatrix}$$로 $P^{-1}[T]P$를 직접 계산해도 같은 diagonal이 나온다. 같은 반사가 basis에 따라 뒤섞인 행렬로도, 깔끔한 diagonal로도 나타난다. 이렇게 operator가 diagonal이 되는 basis를 찾는 것이 뒤 글들의 대각화다.

기저를 바꿔도 변하지 않는 양이 곧 선형사상 자체의 성질이다.

**Proposition (similarity invariant).** similar한 $A$와 $B=P^{-1}AP$는 rank가 같다.

*Proof.* $A$와 $B$가 같은 선형사상 $T$를 서로 다른 기저에서 표현한 것이라, 둘 다 $\dim\operatorname{im}T$와 같은 rank를 가진다. $\blacksquare$

rank뿐 아니라 determinant, trace, characteristic polynomial, 그리고 eigenvalue도 similar 행렬끼리 모두 같다. 이들은 좌표(기저) 선택과 무관한 선형사상 자체의 양이며, 각 개념을 세우는 뒤 글들에서 곧바로 확인된다.

## Direct sum of linear maps

**Definition (External Direct Sum, Direct Sum of Linear Maps).** 벡터공간 $V_1,V_2$에 대해 집합 $V_1\times V_2$에 성분별 연산 $$(v_1,v_2)+(v_1',v_2'):=(v_1+v_1',v_2+v_2'),\qquad c(v_1,v_2):=(cv_1,cv_2)$$을 주면 벡터공간이 되고, 이를 $V_1\oplus V_2$로도 쓴다($V_1,V_2$를 $$V_1\times\{0\}$$, $$\{0\}\times V_2$$로 동일시하면 앞 글에서 다룬 직합과 같은 뜻이 된다). linear map $T_1:V_1\to W_1$, $T_2:V_2\to W_2$에 대해 $$(T_1\oplus T_2)(v_1,v_2):=(T_1v_1,T_2v_2)$$로 정의한 $T_1\oplus T_2:V_1\oplus V_2\to W_1\oplus W_2$를 $T_1$과 $T_2$의 direct sum이라 한다.

**Proposition.** $V_1,V_2$의 기저를 이어붙인 것을 $V_1\oplus V_2$의 기저로, $W_1,W_2$의 기저를 이어붙인 것을 $W_1\oplus W_2$의 기저로 삼으면, $T_1\oplus T_2$의 행렬 표현은 $T_1,T_2$의 행렬 표현 $A_1,A_2$를 대각으로 놓은 block-diagonal 행렬 $$\begin{pmatrix}A_1&0\\0&A_2\end{pmatrix}$$이다.

*Proof.* $V_1$의 기저 벡터 $v_j$(합친 기저에서는 $(v_j,0)$)에 대해 $$(T_1\oplus T_2)(v_j,0)=(T_1v_j,0)$$이고, $T_1v_j$를 $W_1$의 기저로 전개한 계수가 $A_1$의 $j$번째 열이므로 이 값이 $W_2$쪽 성분은 $0$인 채로 합친 행렬의 $j$번째 열이 된다. $V_2$의 기저 벡터에서도 대칭적으로 $A_2$가 나오고 $W_1$쪽 성분은 $0$이다. 두 경우를 합치면 행렬이 정확히 block-diagonal이다. $\blacksquare$

**Example (회전과 반사의 direct sum).** $\mathbb{R}^2$의 $90^\circ$ 회전 $R$과 $\mathbb{R}$ 위의 반사 $S(x)=-x$에 대해, $R\oplus S:\mathbb{R}^2\oplus\mathbb{R}\to\mathbb{R}^2\oplus\mathbb{R}$의 행렬은 $$\begin{pmatrix}0&-1&0\\1&0&0\\0&0&-1\end{pmatrix}$$로, 왼쪽 위 $2\times2$ block이 회전, 오른쪽 아래 $1\times1$ block이 반사다.

## 열공간과 영공간

이제 처음부터 행렬로 주어진 경우, 곧 $A\in F^{m\times n}$이 정하는 선형사상 $x\mapsto Ax$ ($F^n\to F^m$)를 보자. 핵심은 $Ax$를 열의 조합으로 읽는 것이다. $A$의 열을 $a_1,\dots,a_n\in F^m$이라 하면
$$Ax = x_1a_1 + x_2a_2 + \cdots + x_na_n$$
이다. 즉 $Ax$는 언제나 $A$의 열들의 일차결합이고, 가중치가 바로 $x$의 성분이다.

**Definition (Column Space, Null Space).** $A\in F^{m\times n}$에 대해 열공간(column space)과 영공간(null space)을
$$C(A) := \{\,Ax : x\in F^n\,\} = \operatorname{span}\{a_1,\dots,a_n\}\subseteq F^m, \qquad N(A) := \{\,x\in F^n : Ax=0\,\}\subseteq F^n$$
으로 정의한다. 곧 $C(A)=\operatorname{im}A$는 열들이 생성하는 공간이고 $N(A)=\ker A$이다.

**Example (열공간과 영공간).** $$A=\begin{pmatrix}1&0&1\\0&1&1\end{pmatrix}$$의 열은 $(1,0),(0,1),(1,1)$이라 이미 $F^2$ 전체를 생성하므로 $C(A)=F^2$이고 $\operatorname{rank}A=2$이다. 영공간은 $Ax=0$, 즉 $x_1+x_3=0$과 $x_2+x_3=0$을 푸는 $x=t(-1,-1,1)$ 전체라 $\dim N(A)=1$이다. rank-nullity대로 $2+1=3=n$이다.

## Transpose와 행공간

행에 대해서도 같은 이야기를 하려면 행과 열을 맞바꾸는 연산이 필요하다.

**Definition (Transpose).** $A\in F^{m\times n}$의 transpose $A^{\mathsf T}\in F^{n\times m}$는 $$(A^{\mathsf T})_{ij}=A_{ji}$$로 정의한다. 즉 $A$의 행과 열을 맞바꾼 것이다. $(A^{\mathsf T})^{\mathsf T}=A$이고 $(AB)^{\mathsf T}=B^{\mathsf T}A^{\mathsf T}$이다.

$Ax$가 오른쪽에서 곱한 벡터로 열을 조합했듯, 행벡터 $y^{\mathsf T}$($y\in F^m$)를 왼쪽에서 곱하면 이번에는 행이 조합된다. $A$의 행을 $r_1,\dots,r_m\in F^n$이라 하면
$$y^{\mathsf T}A = y_1r_1 + y_2r_2 + \cdots + y_mr_m$$
이다. 즉 $y^{\mathsf T}A$가 훑는 공간이 곧 $A$의 행들의 일차결합 전체다.

**Definition (Row Space, Left Null Space).** $A$의 행들이 생성하는 공간 $$\{\,y^{\mathsf T}A : y\in F^m\,\}$$을 행공간(row space)이라 하며, 이는 $A^{\mathsf T}$의 열공간 $C(A^{\mathsf T})\subseteq F^n$과 같다. 그리고 left null space를 $$N(A^{\mathsf T})=\{\,y\in F^m : A^{\mathsf T}y=0\,\}\subseteq F^m$$으로 정의한다. $A^{\mathsf T}y=0$은 $y^{\mathsf T}A=0$, 곧 $y_1r_1+\cdots+y_mr_m=0$과 같으므로, left null space는 $y$가 $A$의 모든 열에 왼쪽에서 소멸하는 방향이자 행들 사이의 일차종속을 담는 공간이다.

이렇게 한 행렬 $A$에는 네 개의 부분공간이 딸린다. $F^n$ 안에는 행공간 $C(A^{\mathsf T})$와 영공간 $N(A)$가, $F^m$ 안에는 열공간 $C(A)$와 left null space $N(A^{\mathsf T})$가 있다.

**Example (네 부분공간).** $$A=\begin{pmatrix}1&2&3\\2&4&6\end{pmatrix}$$은 두 번째 행이 첫 번째 행의 두 배라 $\operatorname{rank}A=1$이다. 열공간 $$C(A)=\operatorname{span}\{(1,2)\}$$은 차원 $1$, 영공간 $N(A)$는 $x_1+2x_2+3x_3=0$을 푸는 평면이라 차원 $2$, 행공간 $$C(A^{\mathsf T})=\operatorname{span}\{(1,2,3)\}$$은 차원 $1$, left null space $$N(A^{\mathsf T})=\operatorname{span}\{(-2,1)\}$$은 차원 $1$이다.

## Fundamental Theorem of Linear Algebra

위 예에서 열공간과 행공간의 차원이 똑같이 $1$이었던 것은 우연이 아니다.

**Theorem (Row Rank = Column Rank).** 임의의 $A\in F^{m\times n}$에 대해 $\dim C(A)=\dim C(A^{\mathsf T})$이다. 이 공통 값을 $\operatorname{rank}A$라 한다.

*Proof.* $r=\dim C(A)$라 하고, $C(A)$의 기저를 열로 갖는 $m\times r$ 행렬 $C$를 만들자. $A$의 각 열이 이 기저의 일차결합이므로 그 계수들을 모으면 $A=CR$인 $r\times n$ 행렬 $R$이 존재한다. 그런데 $A=CR$은 $A$의 각 행이 $R$의 $r$개 행의 일차결합임을 뜻하므로, $A$의 행공간은 $R$의 행들로 생성되어 $\dim C(A^{\mathsf T})\le r=\dim C(A)$이다. 같은 논증을 $A^{\mathsf T}$에 적용하면 $\dim C(A)\le\dim C(A^{\mathsf T})$이므로 둘은 같다. $\blacksquare$

이제 네 부분공간의 차원이 모두 rank $r$ 하나로 정해진다.

**Theorem (Fundamental Theorem of Linear Algebra, 차원).** $A\in F^{m\times n}$의 rank를 $r$이라 하면
$$\dim C(A)=r,\quad \dim N(A)=n-r,\quad \dim C(A^{\mathsf T})=r,\quad \dim N(A^{\mathsf T})=m-r$$
이다.

*Proof.* $\dim C(A)=r$은 rank의 정의이고 $\dim C(A^{\mathsf T})=r$은 앞 정리다. 사상 $x\mapsto Ax$에 rank-nullity를 적용하면 $n=\operatorname{rank}A+\dim N(A)=r+\dim N(A)$이라 $\dim N(A)=n-r$이고, $A^{\mathsf T}$에 적용하면 $m=r+\dim N(A^{\mathsf T})$이라 $\dim N(A^{\mathsf T})=m-r$이다. $\blacksquare$

이것이 행렬 버전 Fundamental Theorem of Linear Algebra의 절반, 곧 차원에 관한 부분이다. 나머지 절반은 이 네 공간의 직교 관계로 나중에 다루게 된다. 이 네 부분공간과 정리의 이름은 Strang이 정리해 널리 퍼뜨렸다 [5].

행렬을 하나의 대수적 대상으로 보고 덧셈·곱셈을 부여한 것은 Cayley가 1858년 《A Memoir on the Theory of Matrices》에서 한 일이며 [2], "matrix"라는 이름은 그보다 앞서 Sylvester가 1850년에 붙였다 [3]. 행렬의 rank 개념은 Frobenius가 1878년에 명확히 세웠다 [4]. 이 글에서 본 대로 행렬은 결국 유한차원 선형사상을 좌표로 적어 놓은 표이고, 행렬 곱은 사상의 합성이다.

## 참고문헌

1. van der Waerden, B. L. (1930). *Moderne Algebra*. Berlin: Springer.
2. Cayley, A. (1858). A Memoir on the Theory of Matrices. *Philosophical Transactions of the Royal Society of London*, 148, 17–37.
3. Sylvester, J. J. (1850). Additions to the articles "On a New Class of Theorems" and "On Pascal's Theorem". *The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science*, 37, 363–370.
4. Frobenius, G. (1878). Über lineare Substitutionen und bilineare Formen. *Journal für die reine und angewandte Mathematik*, 84, 1–63.
5. Strang, G. (1993). The Fundamental Theorem of Linear Algebra. *The American Mathematical Monthly*, 100(9), 848–855.
