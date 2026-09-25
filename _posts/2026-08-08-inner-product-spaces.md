---
layout: post
title: "Inner product space"
date: 2026-08-08
mathematicians: [Cauchy, Bunyakovsky, Schwarz, Gram, Schmidt, Legendre, Gauss, Hilbert, Pascual Jordan, von Neumann]
---

## inner product

먼저 실수 위에서 정의한다.

**Definition (Real Inner Product).** $\mathbb{R}$ 위의 vector space $V$에서 $\langle\cdot,\cdot\rangle:V\times V\to\mathbb{R}$가 다음을 만족하면 inner product이라 한다.

- (i) 대칭성 $\langle u,v\rangle=\langle v,u\rangle$.
- (ii) 첫 인수에 대한 선형성 $\langle\alpha u+\beta u',v\rangle=\alpha\langle u,v\rangle+\beta\langle u',v\rangle$.
- (iii) 양의 정부호성(positive-definiteness) $\langle v,v\rangle\ge0$이고 등호는 $v=0$일 때뿐.

대칭성과 (ii)를 합치면 둘째 인수에 대해서도 선형이다.

**Example (dot product).** $\mathbb{R}^n$에서 $\langle x,y\rangle:=x^{\mathsf T}y=\sum_{i=1}^n x_iy_i$가 표준 inner product이다. $\langle x,x\rangle=\sum x_i^2$이라 (iii)이 성립한다.

**Example (function space).** $C[a,b]$에서 $\langle f,g\rangle:=\int_a^b f(x)g(x)\,dx$도 inner product이다. $\langle f,f\rangle=\int_a^b f^2\ge0$이고, $f$가 연속이므로 이 적분이 $0$이면 $f\equiv0$이다. 유한차원이 아닌 vector space에도 inner product이 얹힌다는 것을 보여 주는 예다.

복소수 위에서는 켤레를 넣어야 length가 산다. $\mathbb{C}^n$에서 $\sum x_i^2$은 $x=(1,i)$에서 $1+i^2=0$이 되어 양의 정부호가 될 수 없기 때문이다.

**Definition (Complex Inner Product).** $\mathbb{C}$ 위의 vector space $V$에서 $\langle\cdot,\cdot\rangle:V\times V\to\mathbb{C}$가 다음을 만족하면 (Hermitian) inner product이라 한다.

- (i) 켤레대칭성 $\langle u,v\rangle=\overline{\langle v,u\rangle}$.
- (ii) 첫 인수 선형성.
- (iii) 양의 정부호성($\langle v,v\rangle$은 (i)에 의해 실수이며 $\ge0$, 등호는 $v=0$일 때뿐).

(i)과 (ii)에서 둘째 인수에는 켤레선형 $\langle u,\alpha v\rangle=\overline\alpha\langle u,v\rangle$이 따라 나오며, 이런 형식을 sesquilinear라 한다.

**Example (복소 표준 inner product).** $\mathbb{C}^n$에서 $\langle x,y\rangle:=\sum_{i=1}^n x_i\overline{y_i}=y^{\ast }x$가 표준 inner product이다. 여기서 $y^{\ast }:=\overline{y}^{\mathsf T}$는 conjugate transpose이고, $\langle x,x\rangle=\sum\vert x_i\vert^2\ge0$이다.

**Example (반례, Minkowski 형식).** $\mathbb{R}^2$에서 $B(x,y):=x_1y_1-x_2y_2$는 대칭이고 쌍선형이지만 inner product이 아니다. $B(v,v)=x_1^2-x_2^2$이 $v=(1,1)\ne0$에서 $0$이 되고 $v=(0,1)$에서는 음수가 되어 양의 정부호성이 깨지기 때문이다. 이 형식은 특수상대성의 시공간 기하에서 쓰인다.

완비성까지 갖춘 무한차원 inner product space는 Hilbert space라 부르며, Fourier 해석과 함수해석의 무대가 된다. 완비성은 위상적 성질이라 함수해석에서 따로 다루고, 이 글은 유한차원에 집중한다.

## Norm과 Cauchy–Schwarz inequality

길이라는 개념을 공리로 뽑아내면 다음과 같다.

**Definition (Norm).** $\mathbb{R}$ 또는 $\mathbb{C}$ 위의 vector space $V$에서 함수 $\lVert\cdot\rVert:V\to\mathbb{R}$가 다음을 만족하면 norm이라 하고, $(V,\lVert\cdot\rVert)$를 normed vector space라 한다.

- (i) 양의 정부호성: $\lVert v\rVert\ge0$이고 등호는 $v=0$일 때뿐.
- (ii) 절대 동차성: $\lVert cv\rVert=\vert c\vert\,\lVert v\rVert$.
- (iii) 삼각부등식: $\lVert u+v\rVert\le\lVert u\rVert+\lVert v\rVert$.

inner product은 곧바로 이런 norm 하나를 내놓는다.

**Definition (Induced Norm).** $\lVert v\rVert:=\sqrt{\langle v,v\rangle}$.

**Theorem (Cauchy–Schwarz).** inner product space의 모든 $u,v$에 대해 $\vert\langle u,v\rangle\vert\le\lVert u\rVert\,\lVert v\rVert$이고, 등호는 $u,v$가 일차종속일 때에만 성립한다.

*Proof.* $v=0$이면 양변이 $0$이다. $v\ne0$일 때 $t:=\dfrac{\langle u,v\rangle}{\langle v,v\rangle}$라 두면, 양의 정부호성에서
$$0\le\langle u-tv,\;u-tv\rangle=\langle u,u\rangle-\overline t\langle u,v\rangle-t\langle v,u\rangle+t\overline t\langle v,v\rangle=\langle u,u\rangle-\frac{\vert\langle u,v\rangle\vert^2}{\langle v,v\rangle}$$
이다(마지막 등호는 $t$를 대입해 정리한 것이다). 곧 $\vert\langle u,v\rangle\vert^2\le\langle u,u\rangle\langle v,v\rangle$이고 제곱근을 취하면 inequality를 얻는다. 등호는 $\langle u-tv,u-tv\rangle=0$, 즉 $u=tv$일 때뿐이다. $\blacksquare$

**Corollary (triangle inequality).** $\lVert u+v\rVert\le\lVert u\rVert+\lVert v\rVert$.

*Proof.* $\lVert u+v\rVert^2=\lVert u\rVert^2+2\operatorname{Re}\langle u,v\rangle+\lVert v\rVert^2\le\lVert u\rVert^2+2\vert\langle u,v\rangle\vert+\lVert v\rVert^2\le(\lVert u\rVert+\lVert v\rVert)^2$이며, 가운데 inequality에 Cauchy–Schwarz를 썼다. $\blacksquare$

곧 induced norm은 실제로 norm이다: 양의 정부호성과 절대 동차성은 inner product의 정의에서 곧바로 나오고, 삼각부등식이 방금 얻은 이 Corollary다.

이 inequality는 조각조각 발견되었다. Cauchy가 1821년 유한합에 대해 세웠고 [1], Bunyakovsky가 1859년 적분 꼴로 [2], Schwarz가 1888년 일반적인 형태로 [3] 다시 얻어, 오늘날 Cauchy–Bunyakovsky–Schwarz inequality라고도 부른다.

실수 위의 inner product space에서는 Cauchy–Schwarz가 $\dfrac{\langle u,v\rangle}{\lVert u\rVert\,\lVert v\rVert}\in[-1,1]$을 보장하므로, 이 값을 $\cos\theta$로 두어 두 벡터 사이의 angle $\theta$를 정의할 수 있다.

모든 norm이 이렇게 inner product에서 나오는 것은 아니다. Induced norm은 다음 항등식을 하나 더 만족한다.

**Proposition (Parallelogram Law).** induced norm은 모든 $u,v$에서
$$\lVert u+v\rVert^2+\lVert u-v\rVert^2=2\lVert u\rVert^2+2\lVert v\rVert^2$$
를 만족한다.

*Proof.* $\lVert u+v\rVert^2=\lVert u\rVert^2+2\operatorname{Re}\langle u,v\rangle+\lVert v\rVert^2$이고 $\lVert u-v\rVert^2=\lVert u\rVert^2-2\operatorname{Re}\langle u,v\rangle+\lVert v\rVert^2$이므로 둘을 더하면 된다. $\blacksquare$

**Example (parallelogram law가 깨지는 norm).** $\mathbb{R}^2$ 위의 $$\lVert(x,y)\rVert_\infty:=\max(\vert x\vert,\vert y\vert)$$은 norm의 세 조건을 모두 만족하지만(직접 확인된다), $u=(1,0)$, $v=(0,1)$에서
$$\lVert u+v\rVert_\infty^2+\lVert u-v\rVert_\infty^2=1+1=2\ne4=2\lVert u\rVert_\infty^2+2\lVert v\rVert_\infty^2$$
이라 parallelogram law가 깨진다. 그러므로 이 norm은 어떤 inner product에서도 유도될 수 없다. 실은 거꾸로, parallelogram law를 만족하는 norm은 반드시 (극화항등식으로 복원되는) 어떤 inner product에서 유도된다는 것을 Pascual Jordan과 John von Neumann이 1935년에 보였다 [8].

## Orthogonality와 orthonormal 집합

angle이 $90^\circ$인 경우, 곧 inner product이 $0$인 경우가 특별하다.

**Definition (Orthogonality).** $\langle u,v\rangle=0$이면 $u$와 $v$가 orthogonal이라 하고 $u\perp v$로 쓴다.

**Proposition (Pythagoras).** $u\perp v$이면 $\lVert u+v\rVert^2=\lVert u\rVert^2+\lVert v\rVert^2$이다.

*Proof.* $\lVert u+v\rVert^2=\lVert u\rVert^2+2\operatorname{Re}\langle u,v\rangle+\lVert v\rVert^2$인데 $\langle u,v\rangle=0$이다. $\blacksquare$

length가 $1$이고 서로 orthogonal한 벡터들의 모임이 가장 다루기 좋다. 지표집합의 크기에 아무 제한도 두지 않고 정의한다.

**Definition (Orthonormal Set).** 임의의 지표집합 $I$에 대해 $\langle e_i,e_j\rangle=\delta_{ij}$ (곧 $i=j$면 $1$, 아니면 $0$)를 만족하는 벡터들의 모임 $$\{e_i\}_{i\in I}$$를 orthonormal 집합이라 한다.

**Proposition.** orthonormal set is linearly independent.

*Proof.* 유한개 $e_{i_1},\dots,e_{i_k}$에 대해 $\sum_l c_le_{i_l}=0$의 양변과 $e_{i_m}$의 inner product을 취하면 $\sum_l c_l\langle e_{i_l},e_{i_m}\rangle=c_m=0$이다. 모든 $m$에서 $c_m=0$이다. $\blacksquare$

**Example (회전한 basis).** $\mathbb{R}^2$에서 $$\Big\{\tfrac1{\sqrt2}(1,1),\ \tfrac1{\sqrt2}(1,-1)\Big\}$$은 orthonormal basis다. standard basis를 $45^\circ$ 돌린 것으로, 두 벡터의 length가 각각 $1$이고 inner product이 $\tfrac12(1\cdot1+1\cdot(-1))=0$이다.

**Example (Fourier).** 복소값 함수에 $\langle f,g\rangle:=\frac1{2\pi}\int_0^{2\pi}f(x)\overline{g(x)}\,dx$를 주면, $e_n(x):=e^{inx}$ ($n\in\mathbb{Z}$)들이
$$\langle e_m,e_n\rangle=\frac1{2\pi}\int_0^{2\pi}e^{i(m-n)x}\,dx=\delta_{mn}$$
을 만족해 가산 무한 orthonormal 집합을 이룬다. Fourier 급수가 함수를 이 $e_n$들로 펼치는 것으로, Fourier 해석에서 본격적으로 다룬다.

**Example (비가산 orthonormal 집합).** $\mathbb{R}$ 위의 함수들에 평균 inner product $\langle f,g\rangle:=\lim_{T\to\infty}\frac1{2T}\int_{-T}^{T}f(x)\overline{g(x)}\,dx$를 주자. 각 실수 $\lambda$마다 $e_\lambda(x):=e^{i\lambda x}$로 두면, $\lambda\ne\mu$일 때 $\frac1{2T}\int_{-T}^{T}e^{i(\lambda-\mu)x}\,dx=\frac{\sin((\lambda-\mu)T)}{(\lambda-\mu)T}\to0$이고 $\lambda=\mu$이면 값이 늘 $1$이라
$$\langle e_\lambda,e_\mu\rangle=\delta_{\lambda\mu}$$
이다. 곧 $$\{e_\lambda\}_{\lambda\in\mathbb{R}}$$가 비가산 orthonormal 집합이다.

## Gram–Schmidt와 QR decomposition

일차독립인 벡터들을 같은 공간을 생성하는 orthonormal 벡터들로 바꾸는 표준 절차가 있다.

**Theorem (Gram–Schmidt).** 일차독립인 벡터열 $v_1,v_2,\dots$ (유한이든 가산 무한이든)에 대해
$$u_j:=v_j-\sum_{i<j}\langle v_j,e_i\rangle e_i,\qquad e_j:=\frac{u_j}{\lVert u_j\rVert}$$
로 정의하면 $e_1,e_2,\dots$는 orthonormal이고, 모든 $j$에서 $$\operatorname{span}\{e_1,\dots,e_j\}=\operatorname{span}\{v_1,\dots,v_j\}$$이다.

*Proof.* $j$에 대한 귀납. $u_j$는 $v_j$에서 $$\operatorname{span}\{e_1,\dots,e_{j-1}\}=\operatorname{span}\{v_1,\dots,v_{j-1}\}$$ 위로의 orthogonal projection을 뺀 것이라, $v_1,\dots,v_j$의 일차독립성에서 $u_j\ne0$이고 $i<j$에 대해 $\langle u_j,e_i\rangle=\langle v_j,e_i\rangle-\langle v_j,e_i\rangle=0$이다. 정규화하면 orthonormal이 유지되고 span도 보존된다. $\blacksquare$

**Corollary.** 모든 유한차원 inner product space는 orthonormal basis를 갖는다.

**Example (Gram–Schmidt).** $\mathbb{R}^3$에서 $v_1=(1,1,1)$, $v_2=(1,1,0)$, $v_3=(1,0,0)$에 적용하자. $e_1=\tfrac1{\sqrt3}(1,1,1)$이다. $\langle v_2,e_1\rangle=\tfrac2{\sqrt3}$이라 $u_2=(1,1,0)-\tfrac23(1,1,1)=\tfrac13(1,1,-2)$, $e_2=\tfrac1{\sqrt6}(1,1,-2)$이다. $\langle v_3,e_1\rangle=\tfrac1{\sqrt3}$, $\langle v_3,e_2\rangle=\tfrac1{\sqrt6}$이라 $u_3=(1,0,0)-\tfrac13(1,1,1)-\tfrac16(1,1,-2)=\tfrac12(1,-1,0)$, $e_3=\tfrac1{\sqrt2}(1,-1,0)$이다. 세 벡터가 orthonormal임이 확인된다.

이 절차를 행렬로 적으면 matrix decomposition이 된다. $v_j=\sum_{i\le j}\langle v_j,e_i\rangle e_i$이고 $\langle v_j,e_i\rangle=0$ ($i>j$)이므로, 계수들이 upper triangular로 쌓인다.

**Theorem (QR Decomposition).** 열이 일차독립인 $A\in\mathbb{R}^{m\times n}$은 $A=QR$로 decompose된다. 여기서 $Q\in\mathbb{R}^{m\times n}$은 열이 orthonormal($Q^{\mathsf T}Q=I_n$)이고, $R\in\mathbb{R}^{n\times n}$은 대각성분이 양수인 upper triangular 가역행렬이다. 구체적으로 $A$의 열 $v_1,\dots,v_n$에 Gram–Schmidt를 적용해 얻은 $e_1,\dots,e_n$을 $Q$의 열로 두고, $R_{ii}=\lVert u_i\rVert$, $R_{ij}=\langle v_j,e_i\rangle$ ($i<j$)로 둔다.

**Example (QR).** 열이 $v_1=(1,1,0)$, $v_2=(1,0,1)$인 $$A=\begin{pmatrix}1&1\\1&0\\0&1\end{pmatrix}$$을 보자. $e_1=\tfrac1{\sqrt2}(1,1,0)$이고, $\langle v_2,e_1\rangle=\tfrac1{\sqrt2}$이라 $u_2=(1,0,1)-\tfrac12(1,1,0)=\tfrac12(1,-1,2)$, $e_2=\tfrac1{\sqrt6}(1,-1,2)$이다. 따라서
$$Q=\begin{pmatrix}1/\sqrt2&1/\sqrt6\\1/\sqrt2&-1/\sqrt6\\0&2/\sqrt6\end{pmatrix},\qquad R=\begin{pmatrix}\sqrt2&1/\sqrt2\\0&\sqrt6/2\end{pmatrix}$$
이고 $A=QR$이다.

Finite linearly independent set에 대한 Gram-Schmidt만 다뤘지만, 같은 논리로 일반적인 countable linearly independent set에 대해서 Gram-Schmidt를 적용하여 orthonormal set을 얻을 수 있다. 이것이 basis가 되는지는 별개의 문제이며, 함수해석에서 다룬다.

이 orthogonalization 절차 자체는 Laplace와 Cauchy가 이미 썼지만, Gram이 1883년 least squares 맥락에서 [4], Schmidt가 1907년 적분방정식 연구에서 [5] 명확히 정식화하면서 두 사람의 이름이 붙었다.

## Orthogonal projection

**Definition (Projection).** linear map $P:V\to V$가 $P^2=P$를 만족하면 projection(또는 idempotent)이라 한다.

**Proposition.** projection $P$에 대해 $V=\operatorname{im}P\oplus\ker P$이다.

*Proof.* 임의의 $v\in V$는 $v=Pv+(v-Pv)$로 쓰이는데 $Pv\in\operatorname{im}P$이고, $P(v-Pv)=Pv-P^2v=Pv-Pv=0$이라 $v-Pv\in\ker P$이므로 $V=\operatorname{im}P+\ker P$이다. $w\in\operatorname{im}P\cap\ker P$이면 $w=Pu$인 $u$가 있어 $0=Pw=P^2u=Pu=w$이므로 $$\operatorname{im}P\cap\ker P=\{0\}$$이다. 따라서 $V=\operatorname{im}P\oplus\ker P$이다. $\blacksquare$

이 direct sum이 orthogonal이라는 보장은 없다. 여기에 inner product을 얹어 orthogonality까지 요구한 것이 orthogonal projection이다.

**Definition (Orthogonal Projection).** inner product space $V$에서 projection $P$가 모든 $v$에 대해 $v-Pv\perp Pv$를 만족하면 orthogonal projection이라 한다.

**Definition (Orthogonal Complement).** subspace $W\subseteq V$에 대해 $$W^{\perp}:=\{\,v\in V:\langle v,w\rangle=0\ \text{for all}\ w\in W\,\}$$을 $W$의 orthogonal complement라 한다. 이것도 $V$의 subspace이다.

**Proposition.** projection $P$가 orthogonal projection인 것은 $\ker P=(\operatorname{im}P)^{\perp}$인 것, 곧 $\operatorname{im}P$와 $\ker P$가 서로 orthogonal complement인 것과 동치다.

*Proof.* $w\in\operatorname{im}P$와 $z\in\ker P$에 대해 $v:=w+z$로 두면 $Pv=w$, $v-Pv=z$이므로, $v$가 $V$를 훑을 때 쌍 $(Pv,\,v-Pv)$는 $\operatorname{im}P\times\ker P$ 전체를 훑는다. 따라서 정의의 조건 "모든 $v$에서 $\langle v-Pv,Pv\rangle=0$"은 "모든 $w\in\operatorname{im}P$, $z\in\ker P$에서 $\langle z,w\rangle=0$", 곧 $\ker P\subseteq(\operatorname{im}P)^{\perp}$과 같다. 역방향 포함은 direct sum $V=\operatorname{im}P\oplus\ker P$에서 나온다. $u\in(\operatorname{im}P)^{\perp}$를 $u=w+z$ ($w\in\operatorname{im}P$, $z\in\ker P$)로 쓰면 $z\in\ker P\subseteq(\operatorname{im}P)^{\perp}$이라 $w=u-z$도 $(\operatorname{im}P)^{\perp}$에 있는데, $w\in\operatorname{im}P$이기도 하니 $\langle w,w\rangle=0$, 즉 $w=0$이고 $u=z\in\ker P$이다. 그러므로 $\ker P=(\operatorname{im}P)^{\perp}$이다. $\blacksquare$

이제 $v-Pv\in\ker P=(\operatorname{im}P)^{\perp}$이라, orthogonal projection의 residual은 상 $W=\operatorname{im}P$ 전체에 orthogonal이다. 여기서 best approximation이 곧바로 나온다.

**Theorem (Best Approximation).** orthogonal projection $P$와 그 상 $W=\operatorname{im}P$에 대해, $Pv$는 $W$의 원소 중 $v$에 가장 가까운 유일한 점이다. 곧 $w'\in W$, $w'\ne Pv$이면 $\lVert v-w'\rVert>\lVert v-Pv\rVert$이다.

*Proof.* $v-Pv\perp W$이고 $Pv-w'\in W$이라 둘이 orthogonal이다. Pythagoras에 의해
$$\lVert v-w'\rVert^2=\lVert(v-Pv)+(Pv-w')\rVert^2=\lVert v-Pv\rVert^2+\lVert Pv-w'\rVert^2>\lVert v-Pv\rVert^2$$
이며 등호는 $w'=Pv$일 때뿐이다. $\blacksquare$

Finite dimensional vector space에서는 projection이 orthogonal한 것과 symmetric한 것은 동치이다.

**Proposition (Symmetry criterion).** 정사각 실행렬 $P$($P^2=P$)가 orthogonal projection인 것은 $P^{\mathsf T}=P$와 동치다. 이때 상과 핵이 각각 $C(P)$, $N(P)$이고 $N(P)=C(P)^{\perp}$이다.

*Proof.* $P^{\mathsf T}=P$라 하자. $x\in C(P)$(그래서 $x=Pu$)와 $y\in N(P)$에 대해 $\langle x,y\rangle=\langle Pu,y\rangle=\langle u,P^{\mathsf T}y\rangle=\langle u,Py\rangle=0$이라 $C(P)\perp N(P)$, 곧 앞 Proposition에 의해 $P$는 orthogonal projection이다. 역으로 orthogonal projection이면 $\operatorname{im}P=C(P)$와 $\ker P=N(P)$가 orthogonal하고 $C(P)\oplus N(P)=\mathbb{R}^n$이라 $N(P)=C(P)^{\perp}$이다. 그러면 임의의 $u,v$에서 $u-Pu\in N(P)=C(P)^{\perp}$과 $Pv\in C(P)$로 $\langle u,Pv\rangle=\langle Pu,Pv\rangle$이고, 대칭적으로 $\langle Pu,v\rangle=\langle Pu,Pv\rangle$이라 $\langle Pu,v\rangle=\langle u,Pv\rangle$, 즉 $P^{\mathsf T}=P$이다. $\blacksquare$

여기까지는 orthogonal projection이 주어졌다고 할 때의 이야기다. 주어진 subspace $W$로의 orthogonal projection이 존재하는가는 별개의 문제이다. Finite dimensional vector space에서는 언제나 이런 orthogonal projection이 존재하며, 명시적으로 만들 수 있다. $W$의 orthonormal basis $e_1,\dots,e_r$에 대해
$$P_W(v):=\sum_{i=1}^{r}\langle v,e_i\rangle e_i$$
로 두면, 각 $e_j$에서 $\langle v-P_Wv,e_j\rangle=\langle v,e_j\rangle-\langle v,e_j\rangle=0$이라 $v-P_Wv\perp W=\operatorname{im}P_W$이고 $P_W^2=P_W$임이 바로 확인되어 $P_W$가 $W$ 위로의 orthogonal projection이다. $\mathbb{R}^n$에서 $e_i$를 열벡터로 보면 $\langle v,e_i\rangle e_i=(e_ie_i^{\mathsf T})v$이므로
$$P_W=\sum_{i=1}^{r}e_ie_i^{\mathsf T}=QQ^{\mathsf T}\qquad(Q=[\,e_1\ \cdots\ e_r\,])$$
로, rank-1 조각 $e_ie_i^{\mathsf T}$(각각 $e_i$ 방향 line 위로의 orthogonal projection)들의 합이다 (복소수에서는 $e_ie_i^{\ast }$, $QQ^{\ast }$). 이렇게 만든 $P_W$가 $\operatorname{im}P_W=W$, $\ker P_W=W^{\perp}$이라는 사실이 곧바로 공간의 분해를 준다.

**Theorem (orthogonal decomposition).** 유한차원 inner product space $V$의 subspace $W$에 대해 $V=W\oplus W^{\perp}$이다.

*Proof.* 방금 만든 $P_W$가 $\operatorname{im}P_W=W$, $\ker P_W=W^{\perp}$이므로($P_Wv=0$은 모든 $e_i$에 대해 $\langle v,e_i\rangle=0$, 곧 $v\in W^{\perp}$과 동치다), 앞 Proposition의 $V=\operatorname{im}P_W\oplus\ker P_W$가 곧 $V=W\oplus W^{\perp}$이다. $\blacksquare$

이 direct sum은 $$W\cap W^{\perp}=\{0\}$$을 만족하므로, vector space 글의 Grassmann dimension formula에서 $\dim W+\dim W^{\perp}=\dim V$이다. 또 orthogonal complement를 두 번 취하면 제자리로 돌아온다.

**Corollary.** 유한차원에서 $(W^{\perp})^{\perp}=W$이다.

*Proof.* $W\subseteq(W^{\perp})^{\perp}$은 정의에서 바로 나온다. 역으로 $v\in(W^{\perp})^{\perp}$를 위 정리로 $v=w+z$ ($w\in W$, $z\in W^{\perp}$)로 쪼개면, $\langle v,z\rangle=0$($v\in(W^{\perp})^{\perp}$이고 $z\in W^{\perp}$)이고 $\langle w,z\rangle=0$이라 $\langle z,z\rangle=\langle v-w,z\rangle=0$, 곧 $z=0$이고 $v=w\in W$이다. $\blacksquare$

**Theorem ($C(A)$ 위로의 orthogonal projection).** $A\in\mathbb{R}^{m\times n}$이 full column rank이면 $P=A(A^{\mathsf T}A)^{-1}A^{\mathsf T}$가 $C(A)$ 위로의 orthogonal projection이다.

*Proof.* Gaussian elimination 글의 $$N(A^{\mathsf T}A)=N(A)=\{0\}$$에 의해 $A^{\mathsf T}A$가 가역이라 $P$가 정의된다. $P^2=A(A^{\mathsf T}A)^{-1}(A^{\mathsf T}A)(A^{\mathsf T}A)^{-1}A^{\mathsf T}=A(A^{\mathsf T}A)^{-1}A^{\mathsf T}=P$이고, $A^{\mathsf T}A$가 대칭이라 $P^{\mathsf T}=A(A^{\mathsf T}A)^{-1}A^{\mathsf T}=P$이다. 위 Proposition에 의해 $P$는 $C(P)$ 위로의 orthogonal projection인데, $x=Ay\in C(A)$면 $Px=A(A^{\mathsf T}A)^{-1}A^{\mathsf T}Ay=Ay=x$이고 $C(P)\subseteq C(A)$는 분명하므로 $C(P)=C(A)$이다. $\blacksquare$

특히 $A$의 열이 이미 orthonormal이면 $A^{\mathsf T}A=I$라 $P=AA^{\mathsf T}$로 줄고, 이는 열을 $e_1,\dots,e_r$로 본 앞의 $QQ^{\mathsf T}=\sum_i e_ie_i^{\mathsf T}$와 정확히 같다.

가장 간단한 $n=1$이 line 위로의 orthogonal projection이다.

**Example (line 위로의 orthogonal projection).** $a\ne0$이 생성하는 line 위로의 orthogonal projection은 위 정리에서 $A=a$(열 하나)로 두어 $P=\dfrac{aa^{\mathsf T}}{a^{\mathsf T}a}$, 곧 $\operatorname{proj}(v)=\dfrac{\langle v,a\rangle}{\langle a,a\rangle}\,a$이다. 이는 $a/\lVert a\rVert$를 orthonormal basis로 하는 위 orthogonal projection 공식과도 일치한다.

**Theorem (Fundamental Theorem of Linear Algebra, orthogonality).** $A\in\mathbb{R}^{m\times n}$에 대해 $\mathbb{R}^n$ 안에서 $N(A)=C(A^{\mathsf T})^{\perp}$이고, $\mathbb{R}^m$ 안에서 $N(A^{\mathsf T})=C(A)^{\perp}$이다. 따라서
$$\mathbb{R}^n=C(A^{\mathsf T})\oplus N(A),\qquad \mathbb{R}^m=C(A)\oplus N(A^{\mathsf T})$$
이 각각 orthogonal decomposition다.

*Proof.* $A$의 행을 $r_1,\dots,r_m$이라 하면 $Ax=0$은 모든 $i$에서 $r_i\cdot x=0$, 곧 $x$가 모든 행에 orthogonal한 것과 같다. 행들이 $C(A^{\mathsf T})$를 생성하므로 이는 $x\in C(A^{\mathsf T})^{\perp}$과 동치다. 따라서 $N(A)=C(A^{\mathsf T})^{\perp}$이다. 같은 논증을 $A^{\mathsf T}$에 적용하면 $N(A^{\mathsf T})=C(A)^{\perp}$이다. 두 orthogonal decomposition은 위 정리를 $W=C(A^{\mathsf T})$와 $W=C(A)$에 적용한 것이다. $\blacksquare$

행공간과 영공간이 $\mathbb{R}^n$을 서로 orthogonal하게 가르고, 열공간과 left null space가 $\mathbb{R}^m$을 서로 orthogonal하게 가른다. 차원($r$과 $n-r$, $r$과 $m-r$)에 이어 angle까지 채워지면서 Fundamental Theorem of Linear Algebra가 완성된다.

지금까지는 유한차원을 가정했다. 무한차원에서는 subspace $W$로의 orthogonal projection이 존재하지 않을 수 있고, $W$에 대한 orthogonal decomposition도 성립하지 않을 수 있다.

**Example (projection이 없는 경우).** $\ell^2$의 닫히지 않은 subspace $c_{00}$과 $v=(1,\tfrac12,\tfrac13,\dots)\in\ell^2$을 보자. $v$의 앞 $N$항만 남긴 truncation $w_N\in c_{00}$은 $\lVert v-w_N\rVert^2=\sum_{n>N}1/n^2\to0$이라 $c_{00}$까지의 distance의 하한은 $0$이다. 하지만 $v\notin c_{00}$이므로 이 하한을 실제로 이루는 $w\in c_{00}$은 없다. 곧 $c_{00}$ 안에 $v$의 best approximation이 없고, 따라서 $c_{00}$ 위로의 orthogonal projection도 존재하지 않는다.

**Example (분해가 무너지는 경우).** 같은 $c_{00}$은 $\ell^2$에서 dense하기 때문에 $$c_{00}^{\perp}=\{0\}$$이다. 따라서 $c_{00}\oplus c_{00}^{\perp}=c_{00}\subsetneq\ell^2$로, orthogonal decomposition이 성립하지 않는다.

## Least square solution

공학에서 $Ax=b$를 풀 일이 많고 사실 $b \notin C(A)$인 경우가 많다. 즉, 해가 없는 경우가 많다. 대신 $\lVert Ax-b\rVert$를 가장 작게 만드는 해인 least square solution $\hat x$을 구하게 된다.

**Theorem (Normal Equations).** $A^{\mathsf T}A\hat x=A^{\mathsf T}b$를 푸는 $\hat x$는 항상 존재하며 이 해가 least square solution이 된다. 더 나아가서 $A$가 full column rank이면 normal equation의 해는 $\hat x=(A^{\mathsf T}A)^{-1}A^{\mathsf T}b$로 유일하다.

*Proof.* 먼저 normal equation이 항상 풀린다는 것부터 본다. $A^{\mathsf T}b$가 언제나 $C(A^{\mathsf T}A)$에 들어 있으면 되는데, 실제로
$$C(A^{\mathsf T}A)=C((A^{\mathsf T}A)^{\mathsf T})=N(A^{\mathsf T}A)^{\perp}=N(A)^{\perp}=C(A^{\mathsf T})$$
이다 (차례로 $A^{\mathsf T}A$의 대칭성, FTLA의 orthogonality 관계 $C(M^{\mathsf T})=N(M)^{\perp}$, Gaussian elimination 글의 $N(A^{\mathsf T}A)=N(A)$, 다시 FTLA를 썼다). $A^{\mathsf T}b\in C(A^{\mathsf T})=C(A^{\mathsf T}A)$이므로 해가 존재한다. 그 해 $\hat x$가 least square solution인 것은 residual이 $C(A)$에 orthogonal이라는 것과 같은데,
$$(A\hat x-b)\perp C(A)\iff (A\hat x-b)\in N(A^{\mathsf T})\iff A^{\mathsf T}(A\hat x-b)=0\iff A^{\mathsf T}A\hat x=A^{\mathsf T}b$$
이므로 best approximation 정리가 말하는 "$A\hat x$가 $b$의 $C(A)$ 위 orthogonal projection"이라는 조건이 곧 normal equation이다. 끝으로 $A$가 full column rank이면 $$N(A^{\mathsf T}A)=N(A)=\{0\}$$이라 $(A^{\mathsf T}A)^{-1}$가 존재해 $\hat x=(A^{\mathsf T}A)^{-1}A^{\mathsf T}b$로 유일하다. $\blacksquare$

만약 $A$가 full column rank가 아닌 경우에는 해가 여러 개일 수 있다. 이 경우에는 length가 제일 짧은 minimum length solution을 찾는 방법을 뒤에서 또 다루게 된다.

$A$가 full column rank일 때 $b$의 $C(A)$ 위로의 orthogonal projection은 $A\hat x=A(A^{\mathsf T}A)^{-1}A^{\mathsf T}b$가 된다. 이는 위에서 $A(A^{\mathsf T}A)^{-1}A^{\mathsf T}$가 $C(A)$ 위로의 orthogonal projection이라는 사실과 일맥상통한다.


**Example (line 맞추기).** 점 $(1,1),(2,2),(3,2)$에 line $y=c+dx$를 least squares로 맞추자. $$A=\begin{pmatrix}1&1\\1&2\\1&3\end{pmatrix}$$, $b=(1,2,2)$로 두면 $$A^{\mathsf T}A=\begin{pmatrix}3&6\\6&14\end{pmatrix}$$, $A^{\mathsf T}b=(5,11)$이라 normal equations는 $3c+6d=5$, $6c+14d=11$이다. 풀면 $c=\tfrac23$, $d=\tfrac12$로, 최선의 line은 $y=\tfrac23+\tfrac12x$이다.

**Example (다항식으로 $\sin$ 근사).** least squares는 function space에서도 똑같이 작동한다. $C[-\pi,\pi]$에 $\langle f,g\rangle=\int_{-\pi}^{\pi}fg\,dx$를 주고, $1$과 $x$가 생성하는 $1$차 다항식 공간 $W$ 위에서 $\sin x$에 가장 가까운 원소를 찾자. $\int_{-\pi}^{\pi}1\cdot x\,dx=0$이라 $1\perp x$이므로 orthogonal projection은 두 axis에 각각 project한 것의 합이다. $\langle\sin x,1\rangle=\int_{-\pi}^{\pi}\sin x\,dx=0$, $\langle\sin x,x\rangle=\int_{-\pi}^{\pi}x\sin x\,dx=2\pi$, $\langle x,x\rangle=\int_{-\pi}^{\pi}x^2\,dx=\tfrac{2\pi^3}{3}$이므로
$$\operatorname{proj}_W(\sin x)=\frac{\langle\sin x,1\rangle}{\langle 1,1\rangle}\cdot 1+\frac{\langle\sin x,x\rangle}{\langle x,x\rangle}\,x=\frac{3}{\pi^2}\,x$$
이다. 곧 $[-\pi,\pi]$ 위에서 제곱적분 오차 $\int_{-\pi}^{\pi}(\sin x-p(x))^2\,dx$를 가장 작게 하는 $1$차 다항식 $p$는 $\tfrac{3}{\pi^2}x$다. origin 근처만 맞추는 Taylor의 $\sin x\approx x$와 달리, 이 근사는 구간 전체에서 평균제곱으로 최선이다.

이 방법은 Adrien-Marie Legendre가 1805년 혜성 궤도 계산에서 처음 출판했다 [6]. Carl Friedrich Gauss는 1809년 저서에서 자신이 1795년부터 써 왔다고 밝히며 least squares를 normal distribution과 연결했는데 [7], 두 사람 사이의 우선권 논쟁은 수학사의 유명한 장면이다.



## 참고문헌

1. Cauchy, A.-L. (1821). *Cours d'analyse de l'École Royale Polytechnique. Première partie: Analyse algébrique*. Paris: Debure. (Note II.)
2. Bunyakovsky, V. (1859). Sur quelques inégalités concernant les intégrales ordinaires et les intégrales aux différences finies. *Mémoires de l'Académie impériale des sciences de St.-Pétersbourg (7e série)*, 1(9).
3. Schwarz, H. A. (1888). Über ein die Flächen kleinsten Flächeninhalts betreffendes Problem der Variationsrechnung. *Acta Societatis Scientiarum Fennicae*, 15, 315–362.
4. Gram, J. P. (1883). Ueber die Entwickelung reeller Functionen in Reihen mittelst der Methode der kleinsten Quadrate. *Journal für die reine und angewandte Mathematik*, 94, 41–73.
5. Schmidt, E. (1907). Zur Theorie der linearen und nichtlinearen Integralgleichungen. I. *Mathematische Annalen*, 63, 433–476.
6. Legendre, A.-M. (1805). *Nouvelles méthodes pour la détermination des orbites des comètes*. Paris: Firmin Didot.
7. Gauss, C. F. (1809). *Theoria motus corporum coelestium in sectionibus conicis solem ambientium*. Hamburg: Perthes & Besser.
8. Jordan, P., & von Neumann, J. (1935). On Inner Products in Linear, Metric Spaces. *Annals of Mathematics*, 36(3), 719–723.
