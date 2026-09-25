---
layout: post
title: "Singular value decomposition"
date: 2026-08-16
mathematicians: [Beltrami, Jordan, Autonne, Moore, Penrose, Eckart, Young, Mirsky, Weyl]
---

## SVD와 polar decomposition

SVD는 Eugenio Beltrami가 1873년 [1], Camille Jordan이 1874년 [2] 각자 독립적으로 실수 정사각행렬에 대해 증명했다. 복소수·직사각 행렬까지 다루는 polar decomposition은 Léon Autonne이 1902년 완성했다 [3].

**Theorem (Singular Value Decomposition).** $T:V\to W$가 유한차원 inner product space 사이의 linear map($\dim V=n$, $\dim W=m$)이면, $V$의 orthonormal basis $v_1,\dots,v_n$과 $W$의 orthonormal basis $u_1,\dots,u_m$, 그리고 $$\sigma_1\ge\dots\ge\sigma_r>0$$($r=\operatorname{rank}T$)이 존재해 $$Tv_i=\sigma_iu_i\ (i\le r),\qquad Tv_i=0\ (i>r)$$이다. 행렬로는 $A=U\Sigma V^\ast $($U,V$는 unitary, $\Sigma$는 대각성분이 $\sigma_1,\dots,\sigma_r,0,\dots,0$인, 일반적으로 정사각이 아닌 대각행렬)이다.

*Proof.* $T^\ast T:V\to V$는 $(T^\ast T)^\ast =T^\ast T^{\ast \ast }=T^\ast T$라 self-adjoint이고, $\langle T^\ast Tv,v\rangle=\langle Tv,Tv\rangle=\lVert Tv\rVert^2\ge0$이라 positive semidefinite다. spectral theorem으로 orthonormal eigenbasis $v_1,\dots,v_n$과 eigenvalue $\lambda_1\ge\dots\ge\lambda_n\ge0$을 잡고 $\sigma_i:=\sqrt{\lambda_i}$로 두자. $$T^*Tv=0\iff\lVert Tv\rVert^2=\langle T^*Tv,v\rangle=0\iff Tv=0$$이라 $\ker(T^\ast T)=\ker T$이고, 따라서 $\operatorname{rank}(T^\ast T)=\operatorname{rank}T=r$, 곧 $\lambda_i>0$인 것은 정확히 $i\le r$일 때다.

$i\le r$에서 $u_i:=Tv_i/\sigma_i$로 두면 $$\langle u_i,u_j\rangle=\frac{\langle Tv_i,Tv_j\rangle}{\sigma_i\sigma_j}=\frac{\langle T^*Tv_i,v_j\rangle}{\sigma_i\sigma_j}=\frac{\lambda_i\langle v_i,v_j\rangle}{\sigma_i\sigma_j}=\delta_{ij}$$($\sigma_i^2=\lambda_i$를 썼다)이라 $u_1,\dots,u_r$은 orthonormal이다. 이를 $W$의 orthonormal basis $u_1,\dots,u_m$으로 확장한다(Gram–Schmidt). $i>r$에서는 $\lambda_i=0$이라 (단위벡터 $v_i$에서) $$\lVert Tv_i\rVert^2=\langle T^*Tv_i,v_i\rangle=\lambda_i=0,$$ 곧 $Tv_i=0$이다. $\blacksquare$

**Definition (Singular Value).** $\sigma_1\ge\dots\ge\sigma_r>0$을 $T$의 singular value라 한다(나머지는 $0$으로 채운다).

**Remark (4개의 fundamental subspace).** 위 증명에서 $u_1,\dots,u_r$은 $Tv_1,\dots,Tv_r$을 정규화한 것이므로 $\operatorname{im}T$의 orthonormal basis이고, $v_1,\dots,v_r$은 $\ker(T^\ast T)=\ker T$의 orthogonal complement, 곧 $(\ker T)^\perp$의 orthonormal basis다. 나머지 $v_{r+1},\dots,v_n$과 $u_{r+1},\dots,u_m$은 각각 $\ker T$, $(\operatorname{im}T)^\perp$의 orthonormal basis이다. $\ker T^\ast=(\operatorname{im}T)^\perp$, $\operatorname{im}T^\ast=(\ker T)^\perp$이므로, $V=[v_1\cdots v_n]$과 $U=[u_1\cdots u_m]$의 열들이 $T$의 4개의 fundamental subspace 각각의 orthonormal basis를 동시에 준다: $$v_1,\dots,v_r:\operatorname{im}T^\ast,\qquad v_{r+1},\dots,v_n:\ker T,\qquad u_1,\dots,u_r:\operatorname{im}T,\qquad u_{r+1},\dots,u_m:\ker T^\ast.$$

**Corollary (SVD의 합 표현).** 위 SVD에서 $$T=\sum_{i=1}^r\sigma_iu_iv_i^\ast$$이다.

*Proof.* 임의의 $x\in V$를 orthonormal basis $v_1,\dots,v_n$으로 전개하면 $x=\sum_j\langle x,v_j\rangle v_j$이므로 $$Tx=\sum_j\langle x,v_j\rangle Tv_j=\sum_{i\le r}\langle x,v_j\rangle\sigma_iu_i=\Big(\sum_{i\le r}\sigma_iu_iv_i^\ast\Big)x$$이다(마지막 등호는 $v_i^\ast(x)=\langle x,v_i\rangle$라는 정의 그대로). $\blacksquare$

이는 spectral decomposition $T=\sum_i\lambda_iv_iv_i^\ast$와 같은 모양이지만 SVD에서는 정의역, 치역의 basis $v_i,u_i$가 서로 다르고 행렬이 정사각 혹은 normal이라는 조건이 필요 없으므로 더 일반적이다. 실제로 만약 $T$가 normal일 때 SVD는 spectral decomposition과 거의 유사하다.

**Corollary (SVD와 spectral decomposition의 관계).**
- $T$가 normal이면 singular value는 eigenvalue의 절댓값이다: $\sigma_i=\vert\lambda_i\vert$이고, $\lambda_i\ne0$인 곳에서는 $u_i=e^{i\theta_i}v_i$($\lambda_i=\vert\lambda_i\vert e^{i\theta_i}$)로 잡을 수 있다.
- $T$가 self-adjoint이면 $\lambda_i\in\mathbb{R}$이라 $\lambda_i\ge0$인 곳에서는 $u_i=v_i$, $\lambda_i<0$인 곳에서는 $u_i=-v_i$가 된다.
- $T$가 positive semidefinite이면 SVD는 spectral decomposition과 정확히 같다($\sigma_i=\lambda_i$, $u_i=v_i$).

*Proof.* $T$가 normal이면 (복소수) spectral theorem으로 $T=UDU^\ast$($U$ unitary, $D=\operatorname{diag}(\lambda_1,\dots,\lambda_n)$, $U$의 열이 eigenvector $v_i$)로 대각화되고, $$T^\ast T=UD^\ast DU^\ast=U\operatorname{diag}(\vert\lambda_1\vert^2,\dots,\vert\lambda_n\vert^2)U^\ast$$이므로 $T^\ast T$의 eigenbasis가 정확히 $T$의 eigenbasis $v_i$와 일치하고 eigenvalue는 $\vert\lambda_i\vert^2$다. 곧 $\sigma_i=\vert\lambda_i\vert$이며, $\lambda_i\ne0$인 곳에서 $u_i:=Tv_i/\sigma_i=\lambda_iv_i/\vert\lambda_i\vert=e^{i\theta_i}v_i$다. $T$가 self-adjoint이면 $\lambda_i\in\mathbb{R}$이라 $e^{i\theta_i}=\operatorname{sign}(\lambda_i)=\pm1$로 줄어든다. $\blacksquare$

**Example (rank $1$ 행렬의 SVD).** $$A=\begin{pmatrix}1&1\\1&1\end{pmatrix}$$을 보자. $$A^{\mathsf T}A=\begin{pmatrix}2&2\\2&2\end{pmatrix}$$의 eigenvalue는 $4,0$이고 eigenvector는 각각 $\frac1{\sqrt2}(1,1),\frac1{\sqrt2}(1,-1)$이다. 곧 $\sigma_1=2$, $v_1=\frac1{\sqrt2}(1,1)$이고 $$u_1=\frac{Av_1}{\sigma_1}=\frac1{2}\cdot\frac1{\sqrt2}\begin{pmatrix}2\\2\end{pmatrix}=\frac1{\sqrt2}\begin{pmatrix}1\\1\end{pmatrix}$$이다. $\operatorname{rank}A=1$이라 $\sigma_2=0$이고, $$A=\sigma_1u_1v_1^{\mathsf T}=2\cdot\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix}$$로 확인된다.

**Example (rank $2$, $3\times2$ 행렬의 SVD).** $$A=\begin{pmatrix}1&0\\1&1\\0&1\end{pmatrix}$$을 보자. $$A^{\mathsf T}A=\begin{pmatrix}2&1\\1&2\end{pmatrix}$$은 [Eigenvalue and diagonalization]({% post_url 2026-08-10-eigenvalue-and-diagonalization %})에서 다룬 행렬로, eigenvalue $3,1$과 eigenvector $\frac1{\sqrt2}(1,1),\frac1{\sqrt2}(1,-1)$을 가진다. 곧 $\sigma_1=\sqrt3$, $\sigma_2=1$이고 $$v_1=\frac1{\sqrt2}\binom11,\quad v_2=\frac1{\sqrt2}\binom1{-1},\qquad u_1=\frac{Av_1}{\sigma_1}=\frac1{\sqrt6}\begin{pmatrix}1\\2\\1\end{pmatrix},\quad u_2=\frac{Av_2}{\sigma_2}=\frac1{\sqrt2}\begin{pmatrix}1\\0\\-1\end{pmatrix}$$이다. $\operatorname{rank}A=2<m=3$이라 $W=\mathbb{R}^3$의 orthonormal basis를 완성하려면 $u_1,u_2$에 orthogonal한 $$u_3=\frac1{\sqrt3}\begin{pmatrix}1\\-1\\1\end{pmatrix}$$를 (Gram–Schmidt로) 하나 더 골라야 한다. $A$의 두 열이 일차독립이라 $$\ker A=\{0\}$$이므로, $V=\mathbb{R}^2$ 쪽에는 $0$인 singular value가 없다.

**Remark (singular value는 유일하지만 singular vector는 아니다).** $\sigma_1,\dots,\sigma_r$은 $T^\ast T$의 (음이 아닌) eigenvalue이므로 $T$에 의해 완전히 결정되어 유일하다. 그러나 $v_i,u_i$는 그렇지 않다. eigenvalue $\lambda_i$의 eigenspace가 $2$차원 이상이면 그 안에서 orthonormal basis를 고르는 방법이 여럿이고, $\lambda_i$가 단순해도 $v_i\mapsto-v_i$(복소수에서는 $v_i\mapsto e^{i\theta}v_i$)와 $u_i\mapsto-u_i$($e^{i\theta}u_i$)를 같이 하면 $\sigma_iu_iv_i^{\mathsf T}$는 바뀌지 않으면서 $v_i,u_i$ 각각은 다른 선택이 된다.

**Example (같은 행렬의 서로 다른 두 SVD).** [Adjoint operator and the spectral theorem]({% post_url 2026-08-14-adjoint-operator-and-spectral-theorem %})에서 normal이지만 self-adjoint도 unitary도 아닌 예로 든 $$A=\begin{pmatrix}1&-1\\1&1\end{pmatrix}$$을 다시 보자. $A^{\mathsf T}A=2I$라 singular value가 $\sigma_1=\sigma_2=\sqrt2$로 중복되므로(eigenspace가 $\mathbb{R}^2$ 전체), $V=\mathbb{R}^2$의 **어떤** orthonormal basis를 $v_1,v_2$로 잡아도 SVD가 된다.

표준 basis $v_1=(1,0)$, $v_2=(0,1)$을 고르면 $$u_1=\frac{Av_1}{\sqrt2}=\frac1{\sqrt2}\binom11,\qquad u_2=\frac{Av_2}{\sqrt2}=\frac1{\sqrt2}\binom{-1}1$$이고, $U_1:=[u_1\ u_2]$, $\Sigma:=\sqrt2I$, $V_1:=[v_1\ v_2]=I$로 두면 $$A=U_1\Sigma V_1^{\mathsf T}=\frac1{\sqrt2}\begin{pmatrix}1&-1\\1&1\end{pmatrix}\begin{pmatrix}\sqrt2&0\\0&\sqrt2\end{pmatrix}=\begin{pmatrix}1&-1\\1&1\end{pmatrix}$$이다.

반면 $45^\circ$ 돌린 basis $v_1'=\frac1{\sqrt2}(1,1)$, $v_2'=\frac1{\sqrt2}(1,-1)$을 고르면 $$u_1'=\frac{Av_1'}{\sqrt2}=\binom01,\qquad u_2'=\frac{Av_2'}{\sqrt2}=\binom10$$이고, $U_2:=[u_1'\ u_2']$, $V_2:=[v_1'\ v_2']$로 두면 $$A=U_2\Sigma V_2^{\mathsf T}=\begin{pmatrix}0&1\\1&0\end{pmatrix}\begin{pmatrix}\sqrt2&0\\0&\sqrt2\end{pmatrix}\cdot\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}=\begin{pmatrix}1&-1\\1&1\end{pmatrix}$$이다. $U_1\ne U_2$, $V_1\ne V_2$인데도 둘 다 같은 $A$를 준다. 단순히 부호만 뒤집는 게 아니라 $U,V$ 전체가 서로 다른 orthogonal 행렬로 바뀌는, 훨씬 극단적인 비유일성을 보여준다.

**Theorem, Definition (Polar Decomposition).** $T:V\to V$(정사각)이면 unitary $U$와 positive semidefinite self-adjoint $P$가 존재해 $$T=UP$$이다. $P$는 언제나 유일하게 $P=\sqrt{T^\ast T}$로 정해진다. Furthermore, $T$가 invertible이면 $U$도 유일하게 정해지고 $P$는 positive definite이다.

*Proof.* $T$의 SVD $T=U_0\Sigma V_0^\ast$(정사각이라 $U_0,\Sigma,V_0$ 모두 $n\times n$)에서 $$U:=U_0V_0^\ast,\qquad P:=V_0\Sigma V_0^\ast$$로 두자. $U$는 unitary끼리의 곱이라 unitary이고, $\Sigma$가 음이 아닌 실수 대각이라 $P$는 그 congruence, 곧 positive semidefinite self-adjoint다(eigenvalue가 $\Sigma$의 대각성분과 같다). $$UP=U_0V_0^\ast V_0\Sigma V_0^\ast=U_0\Sigma V_0^\ast=T$$이므로 존재성이 나온다.

유일성. $T=UP$이면 $$T^\ast T=P^\ast U^\ast UP=P^2$$이므로 $P$는 $T^\ast T$(positive semidefinite)의 유일한 positive semidefinite square root, 곧 $P=\sqrt{T^\ast T}$다([Bilinear forms, quadratic forms, and positive operators]({% post_url 2026-08-15-bilinear-quadratic-forms-and-positive-operators %})의 Theorem과 그 Remark의 semidefinite 버전). SVD 증명과 같은 논증($\langle T^\ast Tv,v\rangle=\lVert Tv\rVert^2$)으로 $\ker(T^\ast T)=\ker T$이고, $P$가 대각화가능이라 $\ker P=\ker P^2=\ker(T^\ast T)$이므로 $$\ker P=\ker T$$이다. 곧 $P$가 invertible인 것(곧 positive definite인 것)은 $T$가 invertible인 것과 동치이고, 이때는 $T=UP$의 양쪽에 우측에서 $P^{-1}$을 곱해 $U=TP^{-1}$로 유일하게 정해진다. $T$(따라서 $P$)가 invertible이 아니면 $\ker T=\ker P$ 위에서 $U$가 이 부분공간을 어디로 보내는지는 $T=UP$만으로는 정해지지 않고 전체가 unitary가 되도록만 하면 되므로, $U$는 유일하지 않다. $\blacksquare$

**Remark (복소수의 polar decomposition).** $n=1$(곧 $V=\mathbb{C}$)이면 $T$는 스칼라 $z$이고, $z\ne0$일 때 $$P=\sqrt{z^\ast z}=\vert z\vert,\qquad U=z/\vert z\vert$$이다($\vert U\vert=1$). 곧 $T=UP$, 곧 $z=\vert z\vert\cdot(z/\vert z\vert)$는 정확히 복소수의 극형식 $z=\vert z\vert e^{i\theta}$이고, "polar decomposition"이라는 이름이 여기서 온다.

**Remark (반대 순서의 polar decomposition).** $P':=UPU^\ast$로 두면 $P'$도 positive semidefinite self-adjoint이고(eigenvalue는 $P$와 같은 $\sigma_i$, eigenvector는 $v_i$ 대신 $u_i=Uv_i$), $$P'U=UPU^\ast U=UP=T$$이므로 $T=P'U$로도 쓸 수 있다(일반적으로 $P'\ne P$).

$T$가 invertible(정사각이니 $r=n=m$)이면, $T$는 unit sphere를 타원체로 변환하는 operator로 해석할 수 있다. $x=\sum_ic_iv_i$($\sum_ic_i^2=1$)의 image는 $Tx=\sum_i\sigma_ic_iu_i$이므로 $Tx$ 전체는 반지름이 $\sigma_i$이고 축의 방향이 $u_i$인 타원체를 이룬다. $v_1,\dots,v_n$이 orthonormal이었던 것을 unitary $U$가 그대로 보존해 $u_1,\dots,u_n$도 orthonormal이기 때문에, 이 image는 아무렇게나 기울어진 quadric이 아니라 서로 수직인 축을 가진 진짜 타원체가 된다. 일반적으로 invertible linear map이 unit sphere를 타원체로 보내는 이유와 그 구체적인 모양이 바로 이렇게 SVD/polar decomposition으로 드러난다.

일반적인 polar decomposition $T=UP$로 보면 먼저 $P$가 $v_i$축의 방향은 그대로 둔 채 길이만 $\sigma_i$배로 조절하고, 그 다음 $U$가 그 타원체의 축 방향을 $v_i$에서 $u_i$로 바꾼다. $T=P'U$ 쪽으로 보면 순서가 반대다: 먼저 $U$가 축의 방향을 $v_i$에서 $u_i$로 바꾸고, 그 다음 $P'$가 그 축을 따라 길이를 $\sigma_i$배로 조절한다.

$T$가 positive definite면 $U=I$(따라서 $P=P'=T$)이므로 축의 방향은 전혀 바뀌지 않고 길이만 $\sigma_i$배로 조절된다.

## Matrix norm

**Definition (Frobenius norm, Operator norm).** $$\lVert A\rVert_F:=\sqrt{\operatorname{tr}(A^*A)},\qquad\lVert A\rVert_{op}:=\max_{\lVert x\rVert=1}\lVert Ax\rVert$$

참고로 $\lVert A\rVert_{op}$의 존재성은 extreme value theorem으로 보장된다. $\lVert A\rVert_F$는 [Dual space and Riesz representation]({% post_url 2026-08-13-dual-space-and-riesz-representation %})에서 등장한 행렬의 inner product $\langle A,B\rangle=\operatorname{tr}(B^\ast A)$가 주는 norm이다.

**Proposition.** $$\lVert A\rVert_{op}=\sigma_1,\qquad\lVert A\rVert_F=\Big(\sum_{i=1}^r\sigma_i^2\Big)^{1/2}$$($\sigma_i$는 $A$의 singular value).

*Proof.* $A$의 SVD로 $\lVert x\rVert=1$을 $x=\sum_ic_iv_i$($\sum_i\vert c_i\vert^2=1$)라 쓰면 $$\lVert Ax\rVert^2=\Big\lVert\sum_i\sigma_ic_iu_i\Big\rVert^2=\sum_i\sigma_i^2\vert c_i\vert^2\le\sigma_1^2\sum_i\vert c_i\vert^2=\sigma_1^2$$이고 등호는 $x=v_1$에서 성립하므로 $\lVert A\rVert_{op}=\sigma_1$이다. Frobenius는 $$\lVert A\rVert_F^2=\operatorname{tr}(A^*A)=\sum_i\lambda_i(A^*A)=\sum_i\sigma_i^2$$이다(trace는 eigenvalue의 합, [Eigenvalue and diagonalization]({% post_url 2026-08-10-eigenvalue-and-diagonalization %})). $\blacksquare$

**Definition (Submultiplicative).** norm $\lVert\cdot\rVert$가 $\lVert AB\rVert\le\lVert A\rVert\lVert B\rVert$를 만족하면 submultiplicative라 한다.

**Proposition.** operator norm과 Frobenius norm은 모두 submultiplicative다.

*Proof.* operator norm: $\lVert x\rVert=1$에서 $\lVert ABx\rVert\le\lVert A\rVert_{op}\lVert Bx\rVert\le\lVert A\rVert_{op}\lVert B\rVert_{op}$이므로 $\max$를 취하면 나온다. Frobenius norm: Cauchy–Schwarz([Inner product space]({% post_url 2026-08-08-inner-product-spaces %}))로 $$\lVert AB\rVert_F^2=\sum_{i,k}\Big\vert\sum_jA_{ij}B_{jk}\Big\vert^2\le\sum_{i,k}\Big(\sum_j\vert A_{ij}\vert^2\Big)\Big(\sum_j\vert B_{jk}\vert^2\Big)=\Big(\sum_{i,j}\vert A_{ij}\vert^2\Big)\Big(\sum_{j,k}\vert B_{jk}\vert^2\Big)=\lVert A\rVert_F^2\lVert B\rVert_F^2$$이다. $\blacksquare$

**Proposition (norm 비교).** $\lVert A\rVert_{op}\le\lVert A\rVert_F\le\sqrt r\,\lVert A\rVert_{op}$($r=\operatorname{rank}A$).

*Proof.* $\lVert A\rVert_F^2=\sum_{i=1}^r\sigma_i^2\ge\sigma_1^2=\lVert A\rVert_{op}^2$이고, $\sigma_i\le\sigma_1$이라 $\sum_{i=1}^r\sigma_i^2\le r\sigma_1^2$이다. $\blacksquare$

## Low-rank approximation과 Eckart–Young 정리

SVD의 첫 몇개의 항만을 사용하여 행렬을 근사하는 것을 low-rank approximation이라고 한다. 이렇게 행렬의 rank를 낮춘 근사를 사용하면 수치해석 등에서 계산량을 줄이는 데에 큰 기여를 한다. 이 approximation의 당위성과 얼마나 근사가 되는지에 대한 사실은 다음 Eckart-Young Theorem으로부터 나온다.

**Theorem (Eckart–Young, operator norm).** $A$의 SVD $A=\sum_{i=1}^r\sigma_iu_iv_i^{\mathsf T}$의 top $k$개 항만 남긴 $$A_k:=\sum_{i=1}^k\sigma_iu_iv_i^{\mathsf T}\quad(k<r)$$은 rank가 $k$ 이하인 행렬 중 $A$와 operator norm으로 가장 가까운 것이다. 다시 말해서, 임의의 $\operatorname{rank}B\le k$에서 $$\lVert A-B\rVert_{op}\ge\lVert A-A_k\rVert_{op}=\sigma_{k+1}.$$

*Proof.* $A-A_k=\sum_{i>k}\sigma_iu_iv_i^{\mathsf T}$이므로 위 Proposition과 같은 계산으로(가장 큰 singular value가 $\sigma_{k+1}$이니) $\lVert A-A_k\rVert_{op}=\sigma_{k+1}$이다.

이제 $\operatorname{rank}B\le k$인 임의의 $B$에서 $\lVert A-B\rVert_{op}\ge\sigma_{k+1}$을 보이자. $\ker B$는 차원이 $\ge n-k$이고 $\operatorname{span}(v_1,\dots,v_{k+1})$은 차원이 $k+1$이므로, 둘의 차원의 합이 $n+1>n$이라 $$\ker B\cap\operatorname{span}(v_1,\dots,v_{k+1})\ne\{0\}$$이다(Grassmann dimension formula, [Vector space]({% post_url 2026-08-05-vector-spaces %})). 이 교집합에서 단위벡터 $x=\sum_{i\le k+1}c_iv_i$($\sum\vert c_i\vert^2=1$)를 하나 고르면 $Bx=0$이라 $(A-B)x=Ax$이고, $$\lVert Ax\rVert^2=\sum_{i\le k+1}\sigma_i^2\vert c_i\vert^2\ge\sigma_{k+1}^2\sum_{i\le k+1}\vert c_i\vert^2=\sigma_{k+1}^2$$이다($i\le k+1$에서 $\sigma_i\ge\sigma_{k+1}$). 그러므로 $$\lVert A-B\rVert_{op}\ge\lVert(A-B)x\rVert=\lVert Ax\rVert\ge\sigma_{k+1}=\lVert A-A_k\rVert_{op}$$이다. $\blacksquare$

**Theorem (Eckart–Young, Frobenius norm).** 같은 $A_k$가 Frobenius norm으로도 최적이다: $\operatorname{rank}B\le k$인 임의의 $B$에서 $$\lVert A-B\rVert_F\ge\lVert A-A_k\rVert_F=\Big(\sum_{i>k}\sigma_i^2\Big)^{1/2}.$$

**Lemma (Weyl's inequality, singular value 버전).** 행렬 $X$에 대해서 $\sigma_i(X)$를 행렬 $X$의 $i$th singular value로, 만약 $i$가 rank보다 크면 0으로 정의하자. 같은 크기의 행렬 $X,Y$와 $i,j\ge1$에서 $$\sigma_{i+j-1}(X+Y)\le\sigma_i(X)+\sigma_j(Y)$$이다.

*Proof.* $X$의 SVD를 $X=\sum_l\sigma_l(X)p_lq_l^{\mathsf T}$라 쓰고, 위 Eckart–Young(operator norm) Theorem의 $A_k$ 구성을 $X$에 그대로 적용해 top $i-1$개 항만 남긴 $$Z_1:=\sum_{l=1}^{i-1}\sigma_l(X)p_lq_l^{\mathsf T}$$로 두면, 그 Theorem에 의해 $\operatorname{rank}Z_1\le i-1$이고 $\lVert X-Z_1\rVert_{op}=\sigma_i(X)$다. 마찬가지로 $Y$의 SVD로 top $j-1$개 항의 합 $Z_2$를 만들면 $\operatorname{rank}Z_2\le j-1$이고 $\lVert Y-Z_2\rVert_{op}=\sigma_j(Y)$다. $Z:=Z_1+Z_2$는 $$\operatorname{rank}Z\le\operatorname{rank}Z_1+\operatorname{rank}Z_2\le(i-1)+(j-1)=(i+j-1)-1$$이므로, 같은 Theorem을 $X+Y$에 $k=(i+j-1)-1$로 적용하면(그 rank 이하인 $Z$가 주는 거리는 $\sigma_{i+j-1}(X+Y)$ 이상이므로) $$\sigma_{i+j-1}(X+Y)\le\lVert(X+Y)-Z\rVert_{op}\le\lVert X-Z_1\rVert_{op}+\lVert Y-Z_2\rVert_{op}=\sigma_i(X)+\sigma_j(Y)$$이다. $\blacksquare$

**Remark.** Weyl's inequality는 원래 singular value가 아니라 Hermitian(self-adjoint) 행렬의 eigenvalue에 대한 것이다: $A,B$가 Hermitian이고 eigenvalue를 내림차순 $\lambda_1\ge\lambda_2\ge\cdots$로 두면 $$\lambda_{i+j-1}(A+B)\le\lambda_i(A)+\lambda_j(B)$$이다. Hermann Weyl이 1912년 논문에서 이 부등식을 보였는데 [8], 이 논문의 주된 목표는 유한행렬이 아니라 (전형적으로 Laplacian 같은) elliptic differential operator의 eigenvalue의 점근적 분포(오늘날 Weyl's law라 불리는 결과)였고, 지금 우리가 쓰는 부등식은 그 증명 과정에서 self-adjoint (compact) operator에 대한 보조정리로 등장한 것이다. 오늘날 흔히 쓰는 유한차원 Hermitian 행렬 버전은 그 특수한 경우다.

singular value 버전은 이 eigenvalue 버전의 따름정리로도 얻을 수 있다. 임의의 행렬 $X$에서 Hermitian dilation $$H(X):=\begin{pmatrix}0&X\\X^\ast&0\end{pmatrix}$$의 eigenvalue가 정확히 $\pm\sigma_1(X),\pm\sigma_2(X),\dots$이고 $H(X+Y)=H(X)+H(Y)$이므로, eigenvalue 버전을 $H(X),H(Y)$에 적용하면 곧바로 나온다.

*Proof of Theorem.* $\operatorname{rank}B\le k$인 임의의 $B$에서, 위 Lemma를 $X:=A-B$, $Y:=B$, $j:=k+1$로 적용하자. $\operatorname{rank}B\le k$라 $\sigma_{k+1}(B)=0$이므로 모든 $i\ge1$에서 $$\sigma_{i+k}(A)=\sigma_{i+(k+1)-1}\big((A-B)+B\big)\le\sigma_i(A-B)+\sigma_{k+1}(B)=\sigma_i(A-B)$$이다. 양변을 제곱해 $i$에 대해 더하면 $$\lVert A-B\rVert_F^2=\sum_i\sigma_i(A-B)^2\ge\sum_i\sigma_{i+k}(A)^2=\sum_{j>k}\sigma_j(A)^2=\lVert A-A_k\rVert_F^2$$이다(마지막 등호는 위 Proposition과 같은 계산). $\blacksquare$

Eckart와 Young이 1936년 원 논문에서 이 Frobenius norm 버전을 증명했고 [6], Mirsky가 1960년 (같은 방식의 Weyl's inequality를 이용해) unitarily invariant norm 전체로 일반화했다 [7].

**Example (rank-$2$ 근사).** $$A=\begin{pmatrix}3&1&0&0\\1&3&0&0\\0&0&2&1\\0&0&1&2\end{pmatrix}$$을 보자. $A$는 symmetric이고 두 $2\times2$ 블록 $$\begin{pmatrix}3&1\\1&3\end{pmatrix},\qquad\begin{pmatrix}2&1\\1&2\end{pmatrix}$$으로 이루어져 있는데, 각각 eigenvalue $4,2$와 $3,1$(둘 다 eigenvector $\frac1{\sqrt2}(1,1)$, $\frac1{\sqrt2}(1,-1)$)을 가지므로(positive definite이라 singular value는 eigenvalue와 같고 $u_i=v_i$), $$\sigma_1=4,\ v_1=\tfrac1{\sqrt2}(1,1,0,0),\qquad\sigma_2=3,\ v_2=\tfrac1{\sqrt2}(0,0,1,1),\qquad\sigma_3=2,\ v_3=\tfrac1{\sqrt2}(1,-1,0,0),\qquad\sigma_4=1,\ v_4=\tfrac1{\sqrt2}(0,0,1,-1)$$이다. 가장 가까운 rank-$2$ 행렬은 $$A_2=\sigma_1v_1v_1^{\mathsf T}+\sigma_2v_2v_2^{\mathsf T}=\begin{pmatrix}2&2&0&0\\2&2&0&0\\0&0&3/2&3/2\\0&0&3/2&3/2\end{pmatrix}$$이고, 남은 singular value가 둘($\sigma_3,\sigma_4$)이라 $$\lVert A-A_2\rVert_{op}=\sigma_3=2,\qquad\lVert A-A_2\rVert_F=\sqrt{\sigma_3^2+\sigma_4^2}=\sqrt5$$로 두 norm의 오차가 서로 다르게 나온다.

## Pseudoinverse와 minimum length solution

[Inner product space]({% post_url 2026-08-08-inner-product-spaces %})에서 $A$가 full column rank가 아니면 least square solution이 여러 개일 수 있었다. 그 중에 제일 작은 norm을 가지는 minimum length solution이 유일하게 존재하는데 이를 SVD를 이용해서 구할 수 있다.

**Definition (Pseudoinverse).** $T:V\to W$의 SVD $Tv_i=\sigma_iu_i$($i\le r$), $Tv_i=0$($i>r$)에 대해 $$T^+u_i:=\frac{v_i}{\sigma_i}\ (i\le r),\qquad T^+u_i:=0\ (i>r)$$로 정의한(선형 확장한) $T^+:W\to V$를 $T$의 (Moore–Penrose) pseudoinverse라 한다.

**Remark (행렬로 표현).** $T$의 SVD를 행렬로 $A=U\Sigma V^\ast$(곧 여기 $U,V$는 SVD의 그 $U,V$)라 쓰면 $$A^+=V\Sigma^+U^\ast$$이고, $\Sigma^+$는 $\Sigma$의 대각성분 $\sigma_i$를 $1/\sigma_i$로 바꾼 것이다.

**Proposition.** $T$가 invertible이면($r=n=m$) $T^+=T^{-1}$이다.

*Proof.* $T$가 invertible이면 $r=n=m$이라 모든 $i$에서 $Tv_i=\sigma_iu_i$($\sigma_i>0$)이고 $u_1,\dots,u_n$은 $W$의 orthonormal basis 전체다. $T^+$의 정의로 $$T^+Tv_i=T^+(\sigma_iu_i)=\sigma_i\cdot\frac{v_i}{\sigma_i}=v_i$$이므로 $T^+T$는 $V$의 basis $v_1,\dots,v_n$ 위에서 항등이라 $T^+T=I_V$다. $T$가 invertible이므로 양변에 우측에서 $T^{-1}$을 곱하면 $T^+=T^{-1}$이다. $\blacksquare$


**Theorem (Minimum Length Least Squares Solution).** $Ax=b$의 least square solution 전체 중 $\hat x:=A^+b$가 length가 가장 짧은 유일한 것이다.

*Proof.* $v_1,\cdots,v_n$을 $V$의 column들이라고 하면 $N(A)=\operatorname{span}(v_{r+1},\dots,v_n)$, $R(A)=\operatorname{span}(v_1,\dots,v_r)$이다. $A^+b=\sum_{i\le r}\langle b,u_i\rangle v_i/\sigma_i$는 이 $R(A)$에 있다.

$A^+b$가 least square solution임을 보이자. $$A(A^+b)=\sum_{i\le r}\langle b,u_i\rangle\frac{Av_i}{\sigma_i}=\sum_{i\le r}\langle b,u_i\rangle u_i$$인데 $u_1,\dots,u_r$이 $C(A)$의 orthonormal basis이므로 이는 $b$의 $C(A)$ 위 orthogonal projection이다. 따라서 $A^+b$는 least square solution이다.

이제 최소 length를 보이자. $\hat x$가 임의의 least square solution이면 $A\hat x=A(A^+b)$이므로 $\hat x=A^+b+z$인 $z\in N(A)$가 있다. $A^+b\in R(A)$이므로 $A^+b\perp z$이고, Pythagoras로 $$\lVert\hat x\rVert^2=\lVert A^+b\rVert^2+\lVert z\rVert^2\ge\lVert A^+b\rVert^2$$이며 등호는 $z=0$일 때뿐이다. $\blacksquare$

Minimum length solution은 least square solution 중에 $R(A)$에 포함된 유일한 solution이기도 하다.

**Example (minimum length solution).** $$A=\begin{pmatrix}1&1&0\\0&1&1\end{pmatrix},\qquad b=(1,1)$$을 보자($\operatorname{rank}A=2<n=3$이라 $$N(A)\ne\{0\}$$, 곧 $Ax=b$의 해가 무한히 많다). $$AA^{\mathsf T}=\begin{pmatrix}2&1\\1&2\end{pmatrix}$$의 eigenvalue는 $3,1$이므로 $\sigma_1=\sqrt3$, $\sigma_2=1$이고 $$u_1=\frac1{\sqrt2}(1,1),\quad u_2=\frac1{\sqrt2}(1,-1),\qquad v_1=\frac{A^{\mathsf T}u_1}{\sigma_1}=\frac1{\sqrt6}(1,2,1),\quad v_2=\frac{A^{\mathsf T}u_2}{\sigma_2}=\frac1{\sqrt2}(1,0,-1)$$이다. $\langle b,u_1\rangle=\sqrt2$, $\langle b,u_2\rangle=0$이므로 $$A^+b=\frac{\sqrt2}{\sigma_1}v_1+\frac0{\sigma_2}v_2=\frac13(1,2,1)$$이 minimum length solution이다(길이 $\sqrt6/3$). $N(A)=\operatorname{span}(1,-1,1)$이므로, 위 Remark대로 $Ax=b$의 solution 전체는 $$x=\frac13(1,2,1)+t(1,-1,1)\quad(t\in\mathbb{R})$$이고, 예컨대 $t=1$인 $(4/3,-1/3,4/3)$(길이 $\sqrt{33}/3$)처럼 다른 해들은 모두 이보다 길다.

pseudoinverse는 E. H. Moore가 1920년에 [4], Roger Penrose가 1955년 SVD를 이용해 독립적으로 재발견하며 [5] 오늘날의 이름을 얻었다.

## 참고문헌

1. Beltrami, E. (1873). Sulle funzioni bilineari. *Giornale di Matematiche ad Uso degli Studenti delle Università Italiane*, 11, 98–106.
2. Jordan, C. (1874). Mémoire sur les formes bilinéaires. *Journal de Mathématiques Pures et Appliquées*, 19, 35–54.
3. Autonne, L. (1902). Sur les groupes linéaires, réels et orthogonaux. *Bulletin de la Société Mathématique de France*, 30, 121–134.
4. Moore, E. H. (1920). On the reciprocal of the general algebraic matrix. *Bulletin of the American Mathematical Society*, 26, 394–395.
5. Penrose, R. (1955). A generalized inverse for matrices. *Proceedings of the Cambridge Philosophical Society*, 51(3), 406–413.
6. Eckart, C., & Young, G. (1936). The approximation of one matrix by another of lower rank. *Psychometrika*, 1(3), 211–218.
7. Mirsky, L. (1960). Symmetric gauge functions and unitarily invariant norms. *Quarterly Journal of Mathematics*, 11(1), 50–59.
8. Weyl, H. (1912). Das asymptotische Verteilungsgesetz der Eigenwerte linearer partieller Differentialgleichungen (mit einer Anwendung auf die Theorie der Hohlraumstrahlung). *Mathematische Annalen*, 71(4), 441–479.
