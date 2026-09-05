---
layout: post
title: "Endomorphism and Perron–Frobenius"
date: 2026-08-11
mathematicians: [Perron, Frobenius, Leontief, Hawkins, Simon]
---

## Endomorphism과 $GL(V)$

**Definition (Endomorphism, General Linear Group).** $V$에서 자기 자신으로 가는 linear map 전체 $$\operatorname{End}(V):=\mathcal{L}(V,V)$$를 $V$의 endomorphism이라 한다. 그중 invertible한 것 전체 $$GL(V):=\{\,T\in\operatorname{End}(V):T\text{ is invertible}\,\}$$를 $V$의 general linear group이라 한다. $GL(V)$는 합성을 연산으로 group을 이룬다(결합법칙은 자명하고, 항등원은 $\operatorname{id}$, $T\in GL(V)$의 역원은 $T^{-1}$).

**Definition ($GL_n(F)$).** 성분이 $F$에 속하는 invertible $n\times n$ 행렬 전체 $$GL_n(F):=\{\,A\in F^{n\times n}:A\text{ is invertible}\,\}$$도 행렬곱을 연산으로 group을 이루며, 이를 general linear group이라 한다.

**Proposition.** $\dim V=n$이면, 기저를 하나 고정한 행렬 표현 $T\mapsto[T]$가 $GL(V)\cong GL_n(F)$인 group isomorphism을 준다.

*Proof.* $T\mapsto[T]$는 이미 합성을 행렬곱으로 보내는 linear isomorphism $\mathcal{L}(V,V)\cong F^{n\times n}$이므로, $T$가 invertible인 것과 $[T]$가 invertible인 것이 동치임만 보이면 된다. $T$가 invertible이면 $[T][T^{-1}]=[T\circ T^{-1}]=[\operatorname{id}]=I$이라 $[T]$도 invertible이다. 역으로 $[T]$가 invertible이면 그 역행렬이 나타내는 linear map $S$가 $[S\circ T]=[S][T]=I=[\operatorname{id}]$를 만족해 $S\circ T=\operatorname{id}$이고 마찬가지로 $T\circ S=\operatorname{id}$이므로 $T$도 invertible이다. 이 대응이 전단사이고 합성$\leftrightarrow$곱을 보존하므로 group isomorphism이다. $\blacksquare$

determinant가 $1$인 원소들만 모으면 $GL$ 안의 subgroup이 된다.

**Definition (Special Linear Group).** $$SL_n(F):=\{\,A\in GL_n(F):\det A=1\,\}$$를, 유한차원 $V$에서는 $$SL(V):=\{\,T\in GL(V):\det T=1\,\}$$(Determinant 글의 Definition (Determinant of an Operator))를 special linear group이라 한다.

**Proposition.** $SL_n(F)$는 $GL_n(F)$의 subgroup이다(같은 논증으로 $SL(V)$도 $GL(V)$의 subgroup이다).

*Proof.* $\det I=1$이라 $I\in SL_n(F)$이다. $A,B\in SL_n(F)$이면 multiplicativity로 $\det(AB)=\det A\,\det B=1$이라 $AB\in SL_n(F)$이고, $\det(A^{-1})=1/\det A=1$이라 $A^{-1}\in SL_n(F)$이다. $\blacksquare$

**Example (shear는 언제나 $SL_2$).** 임의의 $t\in\mathbb{R}$에서 shear 행렬 $$\begin{pmatrix}1&t\\0&1\end{pmatrix}$$은 determinant가 $1\cdot1-t\cdot0=1$이라 항상 $SL_2(\mathbb{R})$에 속한다. 회전 행렬도 determinant가 $\cos^2\theta+\sin^2\theta=1$이라 $SL_2(\mathbb{R})$에 속하지만, $2$배로 늘리는 $2I$는 determinant가 $4$라 속하지 않는다. $SL_2(\mathbb{R})$은 넓이와 방향을 그대로 보존하는 선형변환들의 모임이다.

## Idempotent

Inner product space 글에서 이미 $P^2=P$를 만족하는 linear map $P:V\to V$를 projection이라 정의하고 $V=\operatorname{im}P\oplus\ker P$임을 보였다. inner product이 없는 일반적인 vector space에서는 이런 $T$를 idempotent라고도 부른다.

**Definition (Idempotent).** $T\in\operatorname{End}(V)$가 $T^2=T$를 만족하면 idempotent(또는 projection)라 한다.

**Proposition.** idempotent $T$에 대해 $\operatorname{im}T=\ker(\operatorname{id}-T)$이다.

*Proof.* $w=Tv\in\operatorname{im}T$이면 $(\operatorname{id}-T)w=Tv-T^2v=Tv-Tv=0$이라 $w\in\ker(\operatorname{id}-T)$이고, 역으로 $(\operatorname{id}-T)w=0$이면 $w=Tw\in\operatorname{im}T$이므로 $\operatorname{im}T=\ker(\operatorname{id}-T)$이다. $\blacksquare$

**Proposition.** $T$가 idempotent이면 $\operatorname{id}-T$도 idempotent다.

*Proof.* $(\operatorname{id}-T)^2=\operatorname{id}-2T+T^2=\operatorname{id}-2T+T=\operatorname{id}-T$이다. $\blacksquare$

**Theorem.** 유한차원에서 idempotent $T$는 diagonalizable이다.

*Proof.* 앞서 말한 direct sum $V=\operatorname{im}T\oplus\ker T$에서 $\operatorname{im}T$의 basis와 $\ker T$의 basis를 이어붙이면 $V$의 basis가 된다(직합과 기저 명제, Vector space 글). 이 basis에서 $T$는 $\operatorname{im}T$쪽 벡터를 그대로 두고($Tw=w$) $\ker T$쪽 벡터를 $0$으로 보내므로, 행렬은 대각성분이 $1$(그 개수는 $\dim\operatorname{im}T$) 또는 $0$(그 개수는 $\dim\ker T$)인 diagonal 행렬이다. $\blacksquare$

이는 Eigenvalue and diagonalization 글에서 본 "idempotent의 eigenvalue는 $0,1$뿐"이라는 사실을 완성한 것이다: eigenvalue가 그 두 값뿐일 뿐 아니라, 실제로 그 두 eigenspace만으로 공간 전체가 diagonalize된다.

**Example (좌표축 projection).** $\mathbb{R}^3$에서 $T(x,y,z)=(x,y,0)$은 $T^2=T$인 idempotent다. $\operatorname{im}T$는 $xy$평면, $\ker T$는 $z$축이고, 표준 basis 자체가 이미 이 direct sum에 맞춰 diagonal $\operatorname{diag}(1,1,0)$을 준다.

## Involution

**Definition (Involution).** $T\in\operatorname{End}(V)$가 $T^2=\operatorname{id}$를 만족하면 involution이라 한다.

**Proposition.** involution $T$는 invertible이고 $T^{-1}=T$이다. 표수가 $2$가 아닌 체 위에서는 $$V=\ker(T-\operatorname{id})\oplus\ker(T+\operatorname{id})$$이다.

*Proof.* $T\circ T=\operatorname{id}$가 그대로 $T^{-1}=T$를 준다. 임의의 $v$를 $$v=\frac{v+Tv}{2}+\frac{v-Tv}{2}$$로 쓰면(표수가 $2$가 아니라 $2$로 나눌 수 있다), $T\big(\frac{v+Tv}{2}\big)=\frac{Tv+T^2v}{2}=\frac{Tv+v}{2}$라 첫 항이 $\ker(T-\operatorname{id})$에 있고, $T\big(\frac{v-Tv}{2}\big)=\frac{Tv-v}{2}=-\frac{v-Tv}{2}$라 둘째 항이 $\ker(T+\operatorname{id})$에 있어 합이 $V$ 전체를 이룬다. $x$가 두 kernel에 모두 있으면 $Tx=x=-x$에서 $2x=0$인데 표수가 $2$가 아니므로 $x=0$이다. $\blacksquare$

**Example (반사).** $\mathbb{R}^2$에서 직선 $y=x$에 대한 반사 $T(x,y)=(y,x)$는 $T^2=\operatorname{id}$인 involution이다. $\ker(T-\operatorname{id})$는 그 직선 자신이고 $\ker(T+\operatorname{id})$는 그에 수직인 직선이다.

**Theorem.** 표수가 $2$가 아닌 체 위의 유한차원에서 involution은 diagonalizable이다.

*Proof.* 위 direct sum $V=\ker(T-\operatorname{id})\oplus\ker(T+\operatorname{id})$에서 두 basis를 이어붙이면 $V$의 basis가 되고, 이 basis에서 $T$는 $\ker(T-\operatorname{id})$쪽을 그대로($1$배), $\ker(T+\operatorname{id})$쪽을 $-1$배로 보내므로 행렬이 대각성분이 $1$ 또는 $-1$인 diagonal 행렬이다. $\blacksquare$

## Nilpotent

**Definition (Nilpotent).** $T\in\operatorname{End}(V)$에 대해 어떤 양의 정수 $k$에서 $T^k=0$이면 $T$를 nilpotent라 하고, 그런 $k$ 중 가장 작은 것을 $T$의 nilpotency index라 한다.

**Proposition.** $$V\ne\{0\}$$이 유한차원이고 $T\ne0$이 nilpotent이면 $T$는 invertible이 아니다. 또 임의의 스칼라 $c\ne0$에서 $T-cI$는 invertible이다.

*Proof.* $T$가 invertible이면 $T^k$도 invertible인데 $T^k=0$은 $$V\ne\{0\}$$에서 invertible이 아니므로 모순이다. 이제 $c\ne0$이고 $(T-cI)v=0$, 곧 $Tv=cv$라 하면 반복해서 $T^kv=c^kv$인데 $T^k=0$이고 $c^k\ne0$이므로 $v=0$이다. 곧 $$\ker(T-cI)=\{0\}$$이라 $T-cI$는 injective이고, 유한차원에서 injective operator는 rank-nullity로 invertible이다. $\blacksquare$

곧 nilpotent operator의 eigenvalue는 $0$ 하나뿐이다(idempotent가 $0,1$뿐이었던 것과 대구를 이룬다).

**Example (미분 연산자).** 차수 $n$ 이하 다항식 공간 $P_n$ 위의 미분 $D$는 $D^{n+1}=0$이라 nilpotent이고, nilpotency index는 $n+1$이다.

nilpotency index는 하나의 벡터를 반복해 얻는 사슬의 길이로도 나타난다.

**Proposition (chain의 일차독립).** $N\ne0$이 nilpotent이고 nilpotency index가 $m$이면, $N^{m-1}x\ne0$인 $x$가 존재하고, 그런 $x$에 대해 $x,Nx,\dots,N^{m-1}x$는 linearly independent이다.

*Proof.* $m$이 최소이므로 $N^{m-1}\ne0$이라 $N^{m-1}x\ne0$인 $x$가 있다. $\sum_{i=0}^{m-1}c_iN^ix=0$이라 하자. 양변에 $N^{m-1}$을 적용하면 $i\ge1$인 항은 $N^{m-1+i}x=0$(지수가 $m$ 이상)으로 사라져 $c_0N^{m-1}x=0$만 남는데 $N^{m-1}x\ne0$이라 $c_0=0$이다. 남은 $\sum_{i=1}^{m-1}c_iN^ix=0$에 $N^{m-2}$를 적용하면 같은 방식으로 $c_1=0$을 얻고, 이를 반복하면 모든 $c_i=0$이다. $\blacksquare$

**Proposition.** 유한차원 $V$($\dim V=n$)의 nilpotent $N$은 $N^n=0$을 만족한다.

*Proof.* $N=0$이면 자명하다. $N\ne0$이고 nilpotency index가 $m$이면 위 Proposition으로 $x,Nx,\dots,N^{m-1}x$가 $m$개의 linearly independent한 벡터라 $m\le n$이고, 그러므로 $N^n=N^{n-m}N^m=0$이다. $\blacksquare$

nilpotent는 basis를 잘 고르면 대각선 위쪽에만 성분이 남는 행렬로도 나타난다(대각성분까지 포함해 $0$이라는 점에서 diagonalizable과는 정반대다).

**Proposition (nilpotent와 strictly upper triangular).** 유한차원 $V$($\dim V=n$)의 nilpotent $N$에 대해, 어떤 basis $v_1,\dots,v_n$에서 $N$의 행렬은 strictly upper triangular이다(대각을 포함해 대각 아래 성분이 모두 $0$).

*Proof.* $\dim V$에 대한 귀납. $N=0$이면 임의의 basis에서 행렬이 $0$이라 자명하다. $N\ne0$이면 위 Proposition으로 invertible이 아니므로 $$\ker N\ne\{0\}$$이고, 따라서 $\dim\operatorname{im}N=n-\dim\ker N<n$이다. $U:=\operatorname{im}N$은 $N(U)=N(NV)=N^2V\subseteq NV=U$라 $N$이 $U$ 안으로 다시 들어가므로 $N\vert_U:U\to U$가 잘 정의되고, $(N\vert_U)^k=N^k\vert_U=0$(충분히 큰 $k$)이라 이 역시 nilpotent다. $\dim U<n$이므로 귀납 가정으로 $U$의 basis $u_1,\dots,u_r$($r=\dim U$)를 각 $i$에서 $Nu_i\in\operatorname{span}(u_1,\dots,u_{i-1})$이 되도록 잡을 수 있다. 이를 $V$의 basis $u_1,\dots,u_r,w_1,\dots,w_{n-r}$로 확장하면, 각 $w_j$에서 $Nw_j\in NV=U=\operatorname{span}(u_1,\dots,u_r)$이므로 $v_i:=u_i$($i\le r$), $v_{r+j}:=w_j$로 둔 basis에서 모든 $i$에 $Nv_i\in\operatorname{span}(v_1,\dots,v_{i-1})$이 성립한다. 이는 $[N]$의 $i$번째 열이 $i$번째 행부터 아래로 전부 $0$이라는 것, 곧 strictly upper triangular라는 뜻이다. $\blacksquare$

## Invariant subspace

$U:=\operatorname{im}N$이 다시 $N$ 안으로 들어간다는 위 증명의 관찰은 일반적인 현상이다.

**Definition (Invariant Subspace, Restriction).** subspace $W\subseteq V$가 $AW\subseteq W$를 만족하면 $A$-invariant라 하고, $W$ 위에서 $A$가 정하는 operator $A\vert_W$를 $A$의 $W$로의 restriction이라 한다.

$A$-invariant인 부분공간이 하나만 있어도 그 basis를 확장한 기저에서 행렬이 정리된 모양을 얻는다.

**Proposition (invariant subspace와 block-triangular).** $W\subseteq V$가 $A$-invariant이면, $W$의 basis를 $V$의 basis로 확장한 기저에서 $A$의 행렬은 $$\begin{pmatrix}B&C\\0&D\end{pmatrix}$$ 꼴(block upper triangular)이고, 왼쪽 위 block $B$가 $A\vert_W$의 행렬이다.

*Proof.* $W$의 basis $w_1,\dots,w_k$를 $V$의 basis $w_1,\dots,w_k,u_1,\dots,u_r$로 확장하자. $W$가 $A$-invariant이므로 각 $Aw_i\in W$이고, 따라서 이를 $V$의 이 기저로 전개할 때 $u_j$ 성분이 전혀 없다. 곧 행렬의 처음 $k$개 열은 아래쪽 $r$개 행이 모두 $0$이라 왼쪽 아래 block이 $0$인 block upper triangular 꼴이 되고, 왼쪽 위 $k\times k$ block은 각 $Aw_i$를 $w_1,\dots,w_k$만으로 전개한 계수, 곧 $A\vert_W$의 행렬 그 자체다. $\blacksquare$

공간이 여러 invariant subspace의 direct sum으로 쪼개지면 행렬이 block-diagonal이 된다.

**Lemma (invariant 분해와 block-diagonal).** $V=\bigoplus_jW_j$이고 각 $W_j$가 $A$-invariant이면, 이 분해에 맞춘 basis에서 $A$의 행렬은 대각 block이 $A\vert_{W_j}$인 block-diagonal이고, $p_A=\prod_j p_{A\vert_{W_j}}$이다(Eigenvalue and diagonalization 글의 characteristic polynomial $p_A(x)=\det(A-xI)$).

*Proof.* 각 $W_j$의 basis를 이어 붙여 $V$의 basis로 삼는다. $W_j$가 $A$-invariant라 그 basis 벡터의 상이 다시 $W_j$ 안에 있으므로, 이 basis에서 $A$의 행렬은 대각 위치에 $A\vert_{W_j}$의 행렬을 놓고 다른 block 자리는 $0$인 block-diagonal이다. block-diagonal 행렬의 determinant는 각 block determinant의 곱이므로(Determinant 글의 Leibniz formula에서 서로 다른 block을 섞는 permutation은 그 자리 성분이 $0$이라 사라지고, 합이 block별로 갈라진다) $p_A=\det(A-xI)=\prod_j\det(A\vert_{W_j}-xI)=\prod_j p_{A\vert_{W_j}}$이다. $\blacksquare$

## Perron–Frobenius theorem

**Definition (Positive Matrix).** 모든 성분이 양수인 행렬을 $A>0$이라 쓴다. $x\ge0$은 모든 성분이 $\ge0$, $x>0$은 모든 성분이 $>0$을 뜻한다.

**Theorem (Perron).** $A\in\mathbb{R}^{n\times n}$이 $A>0$이면 다음이 성립한다. (i) $A$는 eigenvalue $\rho>0$과 그에 대한 eigenvector $v>0$을 가진다. (ii) $\rho$는 $A$의 spectral radius다: $A$의 임의의 eigenvalue $\lambda$에서 $\rho\ge\vert\lambda\vert$. (iii) $\vert\lambda\vert=\rho$인 $A$의 eigenvalue $\lambda$는 $\lambda=\rho$뿐이다(곧 $\rho$가 절댓값이 가장 큰 유일한 eigenvalue다). ($\rho$가 simple eigenvalue라는 것과 positive eigenvector가 스칼라배를 빼면 유일하다는 것까지도 성립하는데, 이는 증명하지 않고 참고문헌으로 넘긴다.)

*Proof.* $$\Delta:=\Big\{x\in\mathbb{R}^n:x\ge0,\ \sum_ix_i=1\Big\}$$(simplex)는 컴팩트다(Heine–Borel). $x\in\Delta$에 대해 $$f(x):=\min\{(Ax)_i/x_i : x_i>0\}$$로 정의하자($x\ne0$이라 이 min은 공집합이 아닌 유한집합 위에서 취해져 잘 정의된다).

$f$가 $\Delta$ 위에서 upper semicontinuous임을 보이자(Semicontinuity 글). $x^{(k)}\to x$라 하자. $f(x)$를 이루는 첨자를 $i_0$라 하면($x_{i_0}>0$이고 $$f(x)=\frac{(Ax)_{i_0}}{x_{i_0}}$$), $x^{(k)}_{i_0}\to x_{i_0}>0$이라 충분히 큰 $k$에서 $x^{(k)}_{i_0}>0$이고 $$f(x^{(k)})\le\frac{(Ax^{(k)})_{i_0}}{x^{(k)}_{i_0}}\longrightarrow\frac{(Ax)_{i_0}}{x_{i_0}}=f(x)$$이다(연속성, $x_{i_0}>0$이므로). 곧 $\limsup_kf(x^{(k)})\le f(x)$라 $f$는 upper semicontinuous다.

$f$는 위로 유계다: 임의의 $x\in\Delta$에서(pigeonhole로) 어떤 $i$가 $x_i\ge1/n$을 만족하고 $M:=\max_{a,b}A_{ab}$라 하면 $$\frac{(Ax)_i}{x_i}\le\frac{M\sum_jx_j}{1/n}=Mn$$이므로 $f(x)\le Mn$이다.

컴팩트 집합 위 upper semicontinuous 함수는 최댓값을 가지므로(Semicontinuity 글, EVT의 확장) $$\rho:=\max_\Delta f=f(v)$$인 $v\in\Delta$가 있다.

$Av=\rho v$임을 보이자. $f$의 정의에서 $v_i>0$인 모든 $i$에서 $$(Av)_i\ge\rho v_i$$이고, $v_i=0$인 $i$에서는 $A>0$과 $v\ge0,v\ne0$이라 $$(Av)_i>0=\rho v_i$$이므로, 어느 경우든 $Av\ge\rho v$(성분별)이다. $Av\ne\rho v$라면 $w:=Av-\rho v\ge0$, $w\ne0$이라 $Aw>0$(성분별)이고, $u:=Av>0$(성분별)에 대해 $$Au-\rho u=A(Av-\rho v)=Aw>0$$이라 모든 $i$에서 $$\frac{(Au)_i}{u_i}>\rho$$($u_i>0$이라 나눌 수 있다), 곧 $f(u)>\rho$다. $f$는 양의 배율에 무관하므로($f(cx)=f(x)$, $c>0$) $u/\lVert u\rVert_1\in\Delta$에서도 $f(u/\lVert u\rVert_1)=f(u)>\rho$인데, 이는 $\rho=\max_\Delta f$에 모순이다. 그러므로 $Av=\rho v$다. $\rho>0$이고 $Av=\rho v>0$이므로 $v>0$이다. (i)가 증명되었다.

(ii) $Az=\lambda z$($z\ne0$, 일반적으로 복소수)이라 하자. 각 성분에서 삼각부등식으로 $$\vert\lambda\vert\,\vert z_i\vert=\Big\vert\sum_jA_{ij}z_j\Big\vert\le\sum_jA_{ij}\vert z_j\vert=(A\vert z\vert)_i$$이므로 $A\vert z\vert\ge\vert\lambda\vert\,\vert z\vert$(성분별)이고, 곧 $f(\vert z\vert/\lVert z\rVert_1)\ge\vert\lambda\vert$다. $\rho=\max_\Delta f\ge f(\vert z\vert/\lVert z\rVert_1)\ge\vert\lambda\vert$이다.

(iii) $\vert\lambda\vert=\rho$라 하자. (ii)에서 $A\vert z\vert\ge\rho\vert z\vert$인데 $f(\vert z\vert/\lVert z\rVert_1)\ge\rho=\max_\Delta f$이므로 등호, 곧 $f(\vert z\vert/\lVert z\rVert_1)=\rho$다. (i)에서 쓴 "otherwise" 논증(그 논증은 $f$가 $\rho$에서 최댓값을 가지는 임의의 점에 그대로 적용된다)을 $\vert z\vert/\lVert z\rVert_1$에 적용하면 $A\vert z\vert=\rho\vert z\vert$까지 나온다(등호). 그러면 모든 $i$에서 $$\vert\lambda\vert\,\vert z_i\vert=\rho\vert z_i\vert=(A\vert z\vert)_i=\sum_jA_{ij}\vert z_j\vert=\Big\vert\sum_jA_{ij}z_j\Big\vert$$로 삼각부등식이 등호가 되고, $A_{ij}>0$이 모든 $j$에서 성립하므로(등호 조건) $z_1,\dots,z_n$은 모두 같은 복소수 argument를 가진다: 어떤 $\theta$에서 $z=e^{i\theta}\vert z\vert$다. $Az=\lambda z$에 대입하면 $A\vert z\vert=\lambda\vert z\vert$인데 이미 $A\vert z\vert=\rho\vert z\vert$이고 $\vert z\vert\ne0$이므로 $\lambda=\rho$다. $\blacksquare$

**Example.** $$A=\begin{pmatrix}2&1\\1&2\end{pmatrix}$$(모든 성분이 양수)는 Eigenvalue and diagonalization 글에서 이미 다룬 행렬로, eigenvalue $1,3$과 eigenvector $(1,-1),(1,1)$을 가진다. Perron root는 절댓값이 더 큰 $\rho=3$이고, 그 eigenvector $(1,1)$은 실제로 모든 성분이 양수다.

Oskar Perron이 1907년 양의 성분을 가진 행렬에서 이 정리를 증명했고 [1], Georg Frobenius가 1912년 (양수 대신 음이 아니고 "irreducible"인 조건까지 완화해) 일반화했다 [2]. irreducible nonnegative matrix까지 다루는 완전한 Frobenius의 정리는 그 조건을 서술하는 graph 이론적 언어가 필요해 이 글에서는 다루지 않는다.

**Theorem (Neumann series, Leontief 조건).** $A\ge0$(모든 성분이 $\ge0$)인 정사각행렬에 대해, $(I-A)^{-1}$이 존재하고 모든 성분이 $\ge0$인 것은 $A$의 spectral radius $\rho(A)<1$인 것과 동치다. 이때 $$(I-A)^{-1}=\sum_{k=0}^\infty A^k$$(성분별로 수렴)이다.

*Proof.* ($\Leftarrow$) $\rho(A)<1$이라 하자. $A$의 모든 eigenvalue $\lambda$가 $\vert\lambda\vert\le\rho(A)<1$이라 $1$은 eigenvalue가 아니므로 $\det(I-A)=\prod_i(1-\lambda_i)\ne0$, 곧 $I-A$는 invertible이다.

부분합 $S_N:=\sum_{k=0}^NA^k\ge0$(성분별, $A\ge0$의 거듭제곱과 합이므로)을 보자. Perron eigenvector $v>0$($Av=\rho v$, $\rho=\rho(A)<1$)을 쓰면 $$S_Nv=\sum_{k=0}^NA^kv=\Big(\sum_{k=0}^N\rho^k\Big)v\le\frac{v}{1-\rho}$$이다(실수 등비급수, $\rho<1$). $v>0$이고 $S_N\ge0$이므로 각 성분에서 $$(S_N)_{ij}v_j\le\sum_k(S_N)_{ik}v_k=(S_Nv)_i\le\frac{v_i}{1-\rho},$$ 곧 $$(S_N)_{ij}\le\frac{v_i}{(1-\rho)v_j}$$로 $N$에 무관하게 유계다. $S_N$의 각 성분은 $N$에 대해 단조증가($A^k\ge0$이라 더할수록 커진다)하고 유계이므로 수렴한다(단조수렴정리, 수열의 극한 글). $S_N\to S\ge0$이라 하면 $A^{N+1}=S_{N+1}-S_N\to S-S=0$이고, $(I-A)S_N=I-A^{N+1}\to I$이므로 $(I-A)S=I$다. $I-A$가 이미 invertible이므로 $S=(I-A)^{-1}\ge0$이다.

($\Rightarrow$) $(I-A)^{-1}=:B\ge0$이 존재한다고 하자. Perron eigenvector $v>0$에서 $(I-A)v=(1-\rho)v$이므로 양변에 $B$를 곱하면 $v=(1-\rho)Bv$다. $Bv\ge0$(성분별)인데 $v>0$이라 $$(1-\rho)(Bv)_i=v_i>0$$이 모든 $i$에서 성립해야 하므로 $$(Bv)_i>0$$이고(그렇지 않으면 $v_i\le0$이 되어 모순) $1-\rho$는 모든 $i$에서 같은 부호(양수)여야 한다. 곧 $\rho<1$이다. $\blacksquare$

이는 경제학의 Leontief input-output model에서 그대로 쓰인다: $A$를 산업 간 투입-산출 계수행렬이라 하면, 경제가 유한한 생산으로 모든 수요를 충족시킬 수 있는 것("productive"한 경제)과 $\rho(A)<1$이 동치다. Wassily Leontief가 1936년 이 모형을 도입했고 [3], Hawkins와 Simon이 1949년 이 조건(Hawkins–Simon condition이라 불린다)을 정리했다 [4].

## 참고문헌

1. Perron, O. (1907). Zur Theorie der Matrices. *Mathematische Annalen*, 64, 248–263.
2. Frobenius, G. (1912). Über Matrizen aus nicht negativen Elementen. *Sitzungsberichte der Königlich Preussischen Akademie der Wissenschaften*, 456–477.
3. Leontief, W. (1936). Quantitative Input and Output Relations in the Economic Systems of the United States. *The Review of Economic Statistics*, 18(3), 105–125.
4. Hawkins, D., & Simon, H. A. (1949). Note: Some Conditions of Macroeconomic Stability. *Econometrica*, 17(3), 245–248.
