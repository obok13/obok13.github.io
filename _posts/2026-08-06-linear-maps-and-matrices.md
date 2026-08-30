---
layout: post
title: "Linear map"
date: 2026-08-06
mathematicians: [Cayley, Sylvester, Frobenius, Strang]
---

## 선형사상

**Definition (Linear Map).** 같은 체 $F$ 위의 벡터공간 $V,W$ 사이의 사상 $T:V\to W$가 모든 $a,b\in F$, $u,v\in V$에 대해
$$T(au+bv)=aT(u)+bT(v)$$
를 만족하면 $T$를 선형사상(linear map)이라 한다.

$a=b=0$을 넣으면 $T(0)=0$이 곧바로 나온다. 즉 선형사상은 원점을 원점으로 보낸다.

**Example (미분).** 다항식 공간 위의 미분 $D:\mathbb{R}[x]\to\mathbb{R}[x]$, $D(p)=p'$은 선형사상이다. $(ap+bq)'=ap'+bq'$이기 때문이다.

**Example (회전).** 평면의 원점 중심 $\theta$ 회전 $R_\theta:\mathbb{R}^2\to\mathbb{R}^2$은 선형사상이고, $R_\theta(x,y)=(x\cos\theta-y\sin\theta,\ x\sin\theta+y\cos\theta)$로 주어진다.

**Example (평가사상).** 한 점 $c$에서의 값매김 $\operatorname{ev}_c:\mathbb{R}[x]\to\mathbb{R}$, $p\mapsto p(c)$은 선형사상이다.

**Example (선형이 아닌 것: 평행이동).** $b\ne0$인 평행이동 $T(x)=x+b$는 $T(0)=b\ne0$이므로 선형사상이 아니다. 그래프가 원점을 지나는 직선이라도 그것이 원점을 안 지나면 선형이 아니다.

**Example (선형이 아닌 것: 노름).** $x\mapsto\lVert x\rVert$은 $\lVert 2x\rVert=2\lVert x\rVert$이지만 $\lVert x+y\rVert\ne\lVert x\rVert+\lVert y\rVert$이 일반적이라 선형사상이 아니다.

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

일차독립: $\sum c_jT(w_j)=0$이면 $T\big(\sum c_jw_j\big)=0$이라 $\sum c_jw_j\in\ker T=\operatorname{span}\{u_i\}$이다. 그러면 $\sum c_jw_j=\sum d_iu_i$인데, $$\{u_1,\dots,u_k,w_1,\dots,w_r\}$$이 일차독립이므로 모든 $c_j=0$이다. $\blacksquare$

**Example (미분에서의 rank-nullity).** 차수가 $n$ 이하인 다항식 공간 $P_n$($\dim=n+1$) 위의 미분 $D$를 보자. $\ker D$는 상수들이라 $\operatorname{nullity}D=1$이고, $\operatorname{im}D=P_{n-1}$이라 $\operatorname{rank}D=n$이다. 과연 $1+n=n+1=\dim P_n$이다.

**Corollary.** $\dim V=\dim W$인 유한차원 공간 사이의 선형사상 $T:V\to W$에서는 단사, 전사, 전단사가 모두 동치다.

*Proof.* $T$가 단사 $\iff\operatorname{nullity}T=0\iff\operatorname{rank}T=\dim V=\dim W\iff\operatorname{im}T=W\iff T$가 전사. $\blacksquare$

## 행렬 표현

행렬 표현은 유한차원 벡터공간 사이의 선형사상에 대한 이야기다. 이제부터 $V,W$가 유한차원이라 하고 $\dim V=n$, $\dim W=m$이라 하자. 기저를 고정하면 이런 선형사상은 행렬 하나로 완전히 번역된다. $V$의 기저 $$\mathcal{B}=\{v_1,\dots,v_n\}$$와 $W$의 기저 $$\mathcal{C}=\{w_1,\dots,w_m\}$$를 고정한다.

**Definition (Matrix of a Linear Map).** 각 $T(v_j)$를 $\mathcal{C}$로 전개해 $T(v_j)=\sum_{i=1}^m a_{ij}w_i$로 쓸 때, 계수들을 모은 $m\times n$ 행렬 $A=(a_{ij})$를 기저 $\mathcal{B},\mathcal{C}$에 대한 $T$의 행렬 표현이라 한다. 즉 $A$의 $j$번째 열은 $T(v_j)$의 $\mathcal{C}$-좌표다.

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

두 vector space 사이의 linear map은 두 vector space의 basis를 어떻게 정하느냐에 따라서 다른 행렬로 나타난다. Basis $$\mathcal{B}=\{v_1,\dots,v_n\}$$에 대해서 벡터 $v$의 좌표벡터를 $$[v]_\mathcal{B}$$(곧 $$v=\sum_i([v]_\mathcal{B})_iv_i$$), $T$의 행렬 표현을 $$[T]_\mathcal{B}$$로 쓴다.

근데 $T$는 2개의 vector space의 basis 표현에 의존하잖아. 여기 다시 써줘.

**Definition (Change-of-Basis Matrix).** 새 기저 $$\mathcal{C}=\{c_1,\dots,c_n\}$$의 각 벡터를 $\mathcal{B}$-좌표로 적은 열들을 모은 행렬 $$P=\big(\,[c_1]_\mathcal{B}\ \cdots\ [c_n]_\mathcal{B}\,\big)$$을 $\mathcal{C}$에서 $\mathcal{B}$로의 change-of-basis 행렬이라 한다. $P$는 invertible이고, 모든 벡터에서 $$[v]_\mathcal{B}=P[v]_\mathcal{C}$$, 곧 $$[v]_\mathcal{C}=P^{-1}[v]_\mathcal{B}$$이다.

*Proof.* $$v=\sum_j([v]_\mathcal{C})_jc_j$$의 $\mathcal{B}$-좌표를 취하면 $$[v]_\mathcal{B}=\sum_j([v]_\mathcal{C})_j[c_j]_\mathcal{B}=P[v]_\mathcal{C}$$이다. $\mathcal{C}$가 기저라 $P$의 열이 일차독립, 곧 $P$가 invertible이다. $\blacksquare$

**Example (벡터의 좌표 변환).** $\mathbb{R}^2$에서 표준기저로 $v=(3,1)$인 벡터를 새 기저 $$\mathcal{C}=\{(1,1),(1,-1)\}$$로 보면, $v=2\,(1,1)+1\,(1,-1)$이라 $$[v]_\mathcal{C}=(2,1)$$이다. 같은 벡터가 기저에 따라 $(3,1)$로도 $(2,1)$로도 표현된다.

선형사상의 행렬은 좌표 변환을 앞뒤로 끼워 바뀐다.

**Theorem (기저 변환).** $T:V\to V$에 대해 $$[T]_\mathcal{C}=P^{-1}[T]_\mathcal{B}\,P$$이다.

*Proof.* $$[Tv]_\mathcal{C}=P^{-1}[Tv]_\mathcal{B}=P^{-1}[T]_\mathcal{B}[v]_\mathcal{B}=P^{-1}[T]_\mathcal{B}P[v]_\mathcal{C}$$가 모든 $v$에서 성립하므로 $$[T]_\mathcal{C}=P^{-1}[T]_\mathcal{B}P$$이다. $\blacksquare$

**Definition (Similar).** 정사각행렬 $A,B$가 어떤 invertible $P$로 $B=P^{-1}AP$를 만족하면 $A$와 $B$가 similar하다고 한다. 곧 similar란 같은 선형사상을 서로 다른 기저에서 표현한 것이다.

**Example (기저를 바꾸면 단순해지는 선형사상).** 직선 $y=x$에 대한 반사 $T(x,y)=(y,x)$는 표준기저에서 $$[T]=\begin{pmatrix}0&1\\1&0\end{pmatrix}$$이다. 그런데 반사축 방향과 그에 수직인 방향을 기저로 잡아 $$\mathcal{C}=\{(1,1),(1,-1)\}$$로 보면 $T(1,1)=(1,1)$, $T(1,-1)=(-1,1)=-(1,-1)$이라 $$[T]_\mathcal{C}=\begin{pmatrix}1&0\\0&-1\end{pmatrix}$$로 diagonal이 된다. 같은 반사가 기저에 따라 뒤섞인 행렬로도, 깔끔한 diagonal로도 나타난다. 이렇게 선형사상이 diagonal이 되는 기저를 찾는 것이 뒤 글들의 대각화다.

기저를 바꿔도 변하지 않는 양이 곧 선형사상 자체의 성질이다.

**Proposition (similarity invariant).** similar한 $A$와 $B=P^{-1}AP$는 rank가 같다.

*Proof.* $A$와 $B$가 같은 선형사상 $T$를 서로 다른 기저에서 표현한 것이라, 둘 다 $\dim\operatorname{im}T$와 같은 rank를 가진다. $\blacksquare$

rank뿐 아니라 determinant, trace, characteristic polynomial, 그리고 eigenvalue도 similar 행렬끼리 모두 같다. 이들은 좌표(기저) 선택과 무관한 선형사상 자체의 양이며, 각 개념을 세우는 뒤 글들에서 곧바로 확인된다.

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

**Example (네 부분공간).** $$A=\begin{pmatrix}1&2&3\\2&4&6\end{pmatrix}$$은 두 번째 행이 첫 번째 행의 두 배라 $\operatorname{rank}A=1$이다. 열공간 $C(A)=\operatorname{span}\{(1,2)\}$은 차원 $1$, 영공간 $N(A)$는 $x_1+2x_2+3x_3=0$을 푸는 평면이라 차원 $2$, 행공간 $C(A^{\mathsf T})=\operatorname{span}\{(1,2,3)\}$은 차원 $1$, left null space $N(A^{\mathsf T})=\operatorname{span}\{(-2,1)\}$은 차원 $1$이다.

## Fundamental Theorem of Linear Algebra

위 예에서 열공간과 행공간의 차원이 똑같이 $1$이었던 것은 우연이 아니다.

**Theorem (Row Rank = Column Rank).** 임의의 $A\in F^{m\times n}$에 대해 $\dim C(A)=\dim C(A^{\mathsf T})$이다. 이 공통 값을 $\operatorname{rank}A$라 한다.

*Proof.* $r=\dim C(A)$라 하고, $C(A)$의 기저를 열로 갖는 $m\times r$ 행렬 $C$를 만들자. $A$의 각 열이 이 기저의 일차결합이므로 그 계수들을 모으면 $A=CR$인 $r\times n$ 행렬 $R$이 존재한다. 그런데 $A=CR$은 $A$의 각 행이 $R$의 $r$개 행의 일차결합임을 뜻하므로, $A$의 행공간은 $R$의 행들로 생성되어 $\dim C(A^{\mathsf T})\le r=\dim C(A)$이다. 같은 논증을 $A^{\mathsf T}$에 적용하면 $\dim C(A)\le\dim C(A^{\mathsf T})$이므로 둘은 같다. $\blacksquare$

이제 네 부분공간의 차원이 모두 rank $r$ 하나로 정해진다.

**Theorem (Fundamental Theorem of Linear Algebra, 차원).** $A\in F^{m\times n}$의 rank를 $r$이라 하면
$$\dim C(A)=r,\quad \dim N(A)=n-r,\quad \dim C(A^{\mathsf T})=r,\quad \dim N(A^{\mathsf T})=m-r$$
이다.

*Proof.* $\dim C(A)=r$은 rank의 정의이고 $\dim C(A^{\mathsf T})=r$은 앞 정리다. 사상 $x\mapsto Ax$에 rank-nullity를 적용하면 $n=\operatorname{rank}A+\dim N(A)=r+\dim N(A)$이라 $\dim N(A)=n-r$이고, $A^{\mathsf T}$에 적용하면 $m=r+\dim N(A^{\mathsf T})$이라 $\dim N(A^{\mathsf T})=m-r$이다. $\blacksquare$

이것이 행렬 버전 Fundamental Theorem of Linear Algebra의 절반, 곧 차원에 관한 부분이다. 나머지 절반은 이 네 공간의 직교 관계로 나중에 다루게 된다. 이 네 부분공간과 정리의 이름은 Strang이 정리해 널리 퍼뜨렸다 [4].

행렬을 하나의 대수적 대상으로 보고 덧셈·곱셈을 부여한 것은 Cayley가 1858년 《A Memoir on the Theory of Matrices》에서 한 일이며 [1], "matrix"라는 이름은 그보다 앞서 Sylvester가 1850년에 붙였다 [2]. 행렬의 rank 개념은 Frobenius가 1878년에 명확히 세웠다 [3]. 이 글에서 본 대로 행렬은 결국 유한차원 선형사상을 좌표로 적어 놓은 표이고, 행렬 곱은 사상의 합성이다.

## 참고문헌

1. Cayley, A. (1858). A Memoir on the Theory of Matrices. *Philosophical Transactions of the Royal Society of London*, 148, 17–37.
2. Sylvester, J. J. (1850). Additions to the articles "On a New Class of Theorems" and "On Pascal's Theorem". *The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science*, 37, 363–370.
3. Frobenius, G. (1878). Über lineare Substitutionen und bilineare Formen. *Journal für die reine und angewandte Mathematik*, 84, 1–63.
4. Strang, G. (1993). The Fundamental Theorem of Linear Algebra. *The American Mathematical Monthly*, 100(9), 848–855.
