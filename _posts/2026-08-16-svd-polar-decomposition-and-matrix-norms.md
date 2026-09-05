---
layout: post
title: "SVD, polar decomposition, and matrix norms"
date: 2026-08-16
mathematicians: [Beltrami, Jordan, Autonne, Moore, Penrose, Eckart, Young, Mirsky]
---

## SVD와 polar decomposition

**Theorem (Singular Value Decomposition).** $T:V\to W$가 유한차원 inner product space 사이의 linear map($\dim V=n$, $\dim W=m$)이면, $V$의 orthonormal basis $v_1,\dots,v_n$과 $W$의 orthonormal basis $u_1,\dots,u_m$, 그리고 $$\sigma_1\ge\dots\ge\sigma_r>0$$($r=\operatorname{rank}T$)이 존재해 $$Tv_i=\sigma_iu_i\ (i\le r),\qquad Tv_i=0\ (i>r)$$이다. 행렬로는 $A=U\Sigma V^*$($U,V$는 unitary, $\Sigma$는 대각성분이 $\sigma_1,\dots,\sigma_r,0,\dots,0$인, 일반적으로 정사각이 아닌 대각행렬)이다.

*Proof.* $T^*T:V\to V$는 $(T^*T)^*=T^*T^{**}=T^*T$라 self-adjoint이고, $\langle T^*Tv,v\rangle=\langle Tv,Tv\rangle=\lVert Tv\rVert^2\ge0$이라 positive semidefinite다. spectral theorem으로 orthonormal eigenbasis $v_1,\dots,v_n$과 eigenvalue $\lambda_1\ge\dots\ge\lambda_n\ge0$을 잡고 $\sigma_i:=\sqrt{\lambda_i}$로 두자. $$T^*Tv=0\iff\lVert Tv\rVert^2=\langle T^*Tv,v\rangle=0\iff Tv=0$$이라 $\ker(T^*T)=\ker T$이고, 따라서 $\operatorname{rank}(T^*T)=\operatorname{rank}T=r$, 곧 $\lambda_i>0$인 것은 정확히 $i\le r$일 때다.

$i\le r$에서 $u_i:=Tv_i/\sigma_i$로 두면 $$\langle u_i,u_j\rangle=\frac{\langle Tv_i,Tv_j\rangle}{\sigma_i\sigma_j}=\frac{\langle T^*Tv_i,v_j\rangle}{\sigma_i\sigma_j}=\frac{\lambda_i\langle v_i,v_j\rangle}{\sigma_i\sigma_j}=\delta_{ij}$$($\sigma_i^2=\lambda_i$를 썼다)이라 $u_1,\dots,u_r$은 orthonormal이다. 이를 $W$의 orthonormal basis $u_1,\dots,u_m$으로 확장한다(Gram–Schmidt). $i>r$에서는 $\lambda_i=0$이라 (단위벡터 $v_i$에서) $$\lVert Tv_i\rVert^2=\langle T^*Tv_i,v_i\rangle=\lambda_i=0,$$ 곧 $Tv_i=0$이다. $\blacksquare$

**Definition (Singular Value).** $\sigma_1\ge\dots\ge\sigma_r>0$을 $T$의 singular value라 한다(나머지는 $0$으로 채운다).

SVD가 갖는 힘은 eigenvalue decomposition과 달리 정사각·normal이라는 조건이 전혀 필요 없다는 데 있다. 기하적으로, $V$의 unit sphere는 $T$를 거쳐 $W$ 안에서 반지름이 $\sigma_1,\dots,\sigma_r$이고 축의 방향이 $u_1,\dots,u_r$인 ellipsoid로 사상된다: 단위벡터 $x=\sum_ic_iv_i$($\sum_ic_i^2=1$)의 상은 $Tx=\sum_i\sigma_ic_iu_i$이고, $u_i$ 방향 성분이 $\sigma_ic_i$이므로 $$\sum_i\Big(\frac{\sigma_ic_i}{\sigma_i}\Big)^2=\sum_ic_i^2=1$$이 정확히 그 ellipsoid의 방정식이다.

**Example (rank $1$ 행렬의 SVD).** $$A=\begin{pmatrix}1&1\\1&1\end{pmatrix}$$을 보자. $$A^{\mathsf T}A=\begin{pmatrix}2&2\\2&2\end{pmatrix}$$의 eigenvalue는 $4,0$이고 eigenvector는 각각 $\frac1{\sqrt2}(1,1),\frac1{\sqrt2}(1,-1)$이다. 곧 $\sigma_1=2$, $v_1=\frac1{\sqrt2}(1,1)$이고 $$u_1=\frac{Av_1}{\sigma_1}=\frac1{2}\cdot\frac1{\sqrt2}\begin{pmatrix}2\\2\end{pmatrix}=\frac1{\sqrt2}\begin{pmatrix}1\\1\end{pmatrix}$$이다. $\operatorname{rank}A=1$이라 $\sigma_2=0$이고, $$A=\sigma_1u_1v_1^{\mathsf T}=2\cdot\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix}$$로 확인된다.

**Example (rank $2$, $3\times2$ 행렬의 SVD).** $$A=\begin{pmatrix}1&0\\1&1\\0&1\end{pmatrix}$$을 보자. $$A^{\mathsf T}A=\begin{pmatrix}2&1\\1&2\end{pmatrix}$$은 Eigenvalue and diagonalization 글에서 다룬 행렬로, eigenvalue $3,1$과 eigenvector $\frac1{\sqrt2}(1,1),\frac1{\sqrt2}(1,-1)$을 가진다. 곧 $\sigma_1=\sqrt3$, $\sigma_2=1$이고 $$v_1=\frac1{\sqrt2}\binom11,\quad v_2=\frac1{\sqrt2}\binom1{-1},\qquad u_1=\frac{Av_1}{\sigma_1}=\frac1{\sqrt6}\begin{pmatrix}1\\2\\1\end{pmatrix},\quad u_2=\frac{Av_2}{\sigma_2}=\frac1{\sqrt2}\begin{pmatrix}1\\0\\-1\end{pmatrix}$$이다. $\operatorname{rank}A=2<m=3$이라 $W=\mathbb{R}^3$의 orthonormal basis를 완성하려면 $u_1,u_2$에 orthogonal한 $$u_3=\frac1{\sqrt3}\begin{pmatrix}1\\-1\\1\end{pmatrix}$$를 (Gram–Schmidt로) 하나 더 골라야 한다. $A$의 두 열이 일차독립이라 $$\ker A=\{0\}$$이므로, $V=\mathbb{R}^2$ 쪽에는 $0$인 singular value가 없다.

**Remark (singular value는 유일하지만 singular vector는 아니다).** $\sigma_1,\dots,\sigma_r$은 $T^*T$의 (음이 아닌) eigenvalue이므로 $T$에 의해 완전히 결정되어 유일하다. 그러나 $v_i,u_i$는 그렇지 않다. eigenvalue $\lambda_i$의 eigenspace가 $2$차원 이상이면 그 안에서 orthonormal basis를 고르는 방법이 여럿이고, $\lambda_i$가 단순해도 $v_i\mapsto-v_i$(복소수에서는 $v_i\mapsto e^{i\theta}v_i$)와 $u_i\mapsto-u_i$($e^{i\theta}u_i$)를 같이 하면 $\sigma_iu_iv_i^{\mathsf T}$는 바뀌지 않으면서 $v_i,u_i$ 각각은 다른 선택이 된다.

**Corollary (SVD와 spectral decomposition의 관계).** $T$가 self-adjoint이면 singular value는 eigenvalue의 절댓값이다: $\sigma_i=\vert\lambda_i\vert$이고, $\lambda_i\ge0$인 곳에서는 $u_i=v_i$, $\lambda_i<0$인 곳에서는 $u_i=-v_i$로 잡을 수 있다. 특히 $T$가 positive semidefinite이면 SVD는 spectral decomposition과 정확히 같다($\sigma_i=\lambda_i$, $u_i=v_i$).

*Proof.* $T$가 self-adjoint이면 $T^*T=T^2$이고, $T$의 (spectral theorem이 주는) eigenbasis에서 $T^2$의 eigenvalue는 $\lambda_i^2$이므로 $\sigma_i=\sqrt{\lambda_i^2}=\vert\lambda_i\vert$이며 같은 eigenvector를 $v_i$로 잡을 수 있다. $Tv_i=\lambda_iv_i$인데, $\lambda_i\ge0$이면 이는 $\sigma_iv_i$라 $u_i=v_i$이고, $\lambda_i<0$이면 $\lambda_iv_i=\sigma_i(-v_i)$라 $u_i=-v_i$가 필요하다. $\blacksquare$

**Corollary (Polar Decomposition).** invertible $T:V\to V$는 $T=UP$($U$는 unitary, $P=\sqrt{T^*T}$는 positive definite self-adjoint)로 유일하게 쓰인다.

*Proof.* $P:=\sqrt{T^*T}$로 두면 $T$가 invertible이라 $T^*T$가 invertible, 곧 $P$도 invertible(eigenvalue가 모두 양수)이다. $U:=TP^{-1}$로 두면 $$U^*U=P^{-1}T^*TP^{-1}=P^{-1}P^2P^{-1}=I$$이라 $U$는 unitary이고 $T=UP$다. 유일성: $T=UP=U'P'$이면 $$T^*T=PU^*UP=P^2,\qquad T^*T=P'U'^*U'P'=P'^2$$이라 $P,P'$가 둘 다 $T^*T$의 positive square root, 유일성으로 $P=P'$이고 $U=TP^{-1}=U'$이다. $\blacksquare$

**Remark.** $T$가 invertible이 아니면 $\ker T$ 위에서 $U$를 임의로(단, 전체가 unitary가 되도록) 조정해야 하고, 이는 SVD $T=U_0\Sigma V_0^*$에서 $U:=U_0V_0^*$, $P:=V_0\Sigma V_0^*$로 얻어진다.

SVD는 Eugenio Beltrami가 1873년 [1], Camille Jordan이 1874년 [2] 각자 독립적으로 실수 정사각행렬에 대해 증명했다. 복소수·직사각 행렬까지 다루는 polar decomposition은 Léon Autonne이 1902년 완성했다 [3].

## Pseudoinverse와 minimum length solution

Inner product space 글에서 $A$가 full column rank가 아니면 least square solution이 여러 개일 수 있어 그중 length가 가장 짧은 minimum length solution을 찾는 문제를 뒤로 미뤄 두었다. SVD가 그 도구다.

**Definition (Pseudoinverse).** $T:V\to W$의 SVD $Tv_i=\sigma_iu_i$($i\le r$), $Tv_i=0$($i>r$)에 대해 $$T^+u_i:=\frac{v_i}{\sigma_i}\ (i\le r),\qquad T^+u_i:=0\ (i>r)$$로 정의한(선형 확장한) $T^+:W\to V$를 $T$의 (Moore–Penrose) pseudoinverse라 한다. 행렬로는 $A^+=V\Sigma^+U^*$이고 $\Sigma^+$는 $\Sigma$의 대각성분 $\sigma_i$를 $1/\sigma_i$로 바꾼 것이다. $T$가 invertible이면($r=n=m$) $T^+=T^{-1}$이다.

**Theorem (Minimum Length Least Squares Solution).** $Ax=b$의 least square solution(Inner product space 글, Normal Equations) 전체 중 $\hat x:=A^+b$가 length가 가장 짧은 유일한 것이다.

*Proof.* $i>r$에서 $Av_i=0$이므로 $$\operatorname{span}(v_{r+1},\dots,v_n)\subseteq\ker A$$이고, 차원이 $n-r=\dim\ker A$와 같으므로 $$\ker A=\operatorname{span}(v_{r+1},\dots,v_n),\qquad(\ker A)^{\perp}=\operatorname{span}(v_1,\dots,v_r)$$이다. $A^+b=\sum_{i\le r}\langle b,u_i\rangle v_i/\sigma_i$는 이 span에 있다.

$A^+b$가 least square solution임을 보이자. $$A(A^+b)=\sum_{i\le r}\langle b,u_i\rangle\frac{Av_i}{\sigma_i}=\sum_{i\le r}\langle b,u_i\rangle u_i$$인데 $u_1,\dots,u_r$이 $\operatorname{im}A$의 orthonormal basis이므로(SVD 정리) 이는 $b$의 $\operatorname{im}A$ 위 orthogonal projection이다. $Ax$($x\in V$)가 $\operatorname{im}A$ 전체를 훑으므로 $\lVert Ax-b\rVert$를 최소화하는 것은 $Ax$를 이 projection으로 만드는 것과 같다(Best Approximation Theorem, Inner product space 글). $A(A^+b)$가 정확히 그 값이므로 $A^+b$는 least square solution이다.

이제 최소 length를 보이자. $\hat x$가 임의의 least square solution이면 $A\hat x=A(A^+b)$이므로 $\hat x=A^+b+z$인 $z\in\ker A$가 있다. $A^+b\in(\ker A)^{\perp}$이므로 $A^+b\perp z$이고, Pythagoras로 $$\lVert\hat x\rVert^2=\lVert A^+b\rVert^2+\lVert z\rVert^2\ge\lVert A^+b\rVert^2$$이며 등호는 $z=0$일 때뿐이다. $\blacksquare$

**Example (minimum length solution).** $$A=\begin{pmatrix}1&1\end{pmatrix},\qquad b=(2)$$을 보자($$N(A)=\operatorname{span}(1,-1)\ne\{0\}$$이라 $x_1+x_2=2$의 해가 무한히 많다). $$A^{\mathsf T}A=\begin{pmatrix}1&1\\1&1\end{pmatrix}$$의 eigenvalue는 $2,0$이라 $\sigma_1=\sqrt2$, $v_1=\frac1{\sqrt2}(1,1)$이고 $u_1=Av_1/\sigma_1=1$(스칼라, $W=\mathbb{R}$)이다. 곧 $$A^+b=\frac{\langle b,u_1\rangle}{\sigma_1}v_1=\frac2{\sqrt2}\cdot\frac1{\sqrt2}(1,1)=(1,1)$$이 minimum length solution이다. 실제로 $x_1+x_2=2$ 위의 점 중 origin에 가장 가까운 것은 $(1,1)$(길이 $\sqrt2$)이고, 예컨대 $(2,0)$은 같은 직선 위에 있지만 길이가 $2$로 더 길다.

pseudoinverse는 E. H. Moore가 1920년에 [4], Roger Penrose가 1955년 SVD를 이용해 독립적으로 재발견하며 [5] 오늘날의 이름을 얻었다.

## Matrix norm

**Definition (Frobenius norm, Operator norm).** $$\lVert A\rVert_F:=\sqrt{\operatorname{tr}(A^*A)},\qquad\lVert A\rVert_{op}:=\max_{\lVert x\rVert=1}\lVert Ax\rVert$$(max은 단위구가 컴팩트라 extreme value theorem으로 존재한다). Frobenius norm은 Dual space and Riesz representation 글의 Riesz representation 절에서 쓴 행렬의 inner product $\langle A,B\rangle=\operatorname{tr}(B^*A)$가 주는 norm이다.

**Proposition.** $$\lVert A\rVert_{op}=\sigma_1,\qquad\lVert A\rVert_F=\Big(\sum_{i=1}^r\sigma_i^2\Big)^{1/2}$$($\sigma_i$는 $A$의 singular value).

*Proof.* $A$의 SVD로 $\lVert x\rVert=1$을 $x=\sum_ic_iv_i$($\sum_i\vert c_i\vert^2=1$)라 쓰면 $$\lVert Ax\rVert^2=\Big\lVert\sum_i\sigma_ic_iu_i\Big\rVert^2=\sum_i\sigma_i^2\vert c_i\vert^2\le\sigma_1^2\sum_i\vert c_i\vert^2=\sigma_1^2$$이고 등호는 $x=v_1$에서 성립하므로 $\lVert A\rVert_{op}=\sigma_1$이다. Frobenius는 $$\lVert A\rVert_F^2=\operatorname{tr}(A^*A)=\sum_i\lambda_i(A^*A)=\sum_i\sigma_i^2$$이다(trace는 eigenvalue의 합, Eigenvalue and diagonalization 글). $\blacksquare$

**Definition (Submultiplicative).** norm $\lVert\cdot\rVert$가 $\lVert AB\rVert\le\lVert A\rVert\lVert B\rVert$를 만족하면 submultiplicative라 한다.

**Proposition.** operator norm과 Frobenius norm은 모두 submultiplicative다.

*Proof.* operator norm: $\lVert x\rVert=1$에서 $\lVert ABx\rVert\le\lVert A\rVert_{op}\lVert Bx\rVert\le\lVert A\rVert_{op}\lVert B\rVert_{op}$이므로 $\max$를 취하면 나온다. Frobenius norm: Cauchy–Schwarz(Inner product space 글)로 $$\lVert AB\rVert_F^2=\sum_{i,k}\Big\vert\sum_jA_{ij}B_{jk}\Big\vert^2\le\sum_{i,k}\Big(\sum_j\vert A_{ij}\vert^2\Big)\Big(\sum_j\vert B_{jk}\vert^2\Big)=\Big(\sum_{i,j}\vert A_{ij}\vert^2\Big)\Big(\sum_{j,k}\vert B_{jk}\vert^2\Big)=\lVert A\rVert_F^2\lVert B\rVert_F^2$$이다. $\blacksquare$

**Proposition (norm 비교).** $\lVert A\rVert_{op}\le\lVert A\rVert_F\le\sqrt r\,\lVert A\rVert_{op}$($r=\operatorname{rank}A$).

*Proof.* $\lVert A\rVert_F^2=\sum_{i=1}^r\sigma_i^2\ge\sigma_1^2=\lVert A\rVert_{op}^2$이고, $\sigma_i\le\sigma_1$이라 $\sum_{i=1}^r\sigma_i^2\le r\sigma_1^2$이다. $\blacksquare$

행렬노름의 나머지 일반 이론(condition number, 다른 $p$-norm과의 비교 등)은 뒤의 행렬 도구 글에서 다룬다.

## Low-rank approximation과 Eckart–Young 정리

**Theorem (Eckart–Young, operator norm).** SVD $A=\sum_{i=1}^r\sigma_iu_iv_i^{\mathsf T}$의 top $k$개 항만 남긴 $$A_k:=\sum_{i=1}^k\sigma_iu_iv_i^{\mathsf T}\quad(k<r)$$은 rank가 $k$ 이하인 행렬 중 $A$와 operator norm으로 가장 가까운 것이다: 임의의 $\operatorname{rank}B\le k$에서 $$\lVert A-B\rVert_{op}\ge\lVert A-A_k\rVert_{op}=\sigma_{k+1}.$$

*Proof.* $A-A_k=\sum_{i>k}\sigma_iu_iv_i^{\mathsf T}$이므로 위 Proposition과 같은 계산으로(가장 큰 singular value가 $\sigma_{k+1}$이니) $\lVert A-A_k\rVert_{op}=\sigma_{k+1}$이다.

이제 $\operatorname{rank}B\le k$인 임의의 $B$에서 $\lVert A-B\rVert_{op}\ge\sigma_{k+1}$을 보이자. $\ker B$는 차원이 $\ge n-k$이고 $\operatorname{span}(v_1,\dots,v_{k+1})$은 차원이 $k+1$이므로, 둘의 차원의 합이 $n+1>n$이라 $$\ker B\cap\operatorname{span}(v_1,\dots,v_{k+1})\ne\{0\}$$이다(Grassmann dimension formula, Vector space 글). 이 교집합에서 단위벡터 $x=\sum_{i\le k+1}c_iv_i$($\sum\vert c_i\vert^2=1$)를 하나 고르면 $Bx=0$이라 $(A-B)x=Ax$이고, $$\lVert Ax\rVert^2=\sum_{i\le k+1}\sigma_i^2\vert c_i\vert^2\ge\sigma_{k+1}^2\sum_{i\le k+1}\vert c_i\vert^2=\sigma_{k+1}^2$$이다($i\le k+1$에서 $\sigma_i\ge\sigma_{k+1}$). 그러므로 $$\lVert A-B\rVert_{op}\ge\lVert(A-B)x\rVert=\lVert Ax\rVert\ge\sigma_{k+1}=\lVert A-A_k\rVert_{op}$$이다. $\blacksquare$

**Theorem (Eckart–Young, Frobenius norm).** 같은 $A_k$가 Frobenius norm으로도 최적이다: $\operatorname{rank}B\le k$인 임의의 $B$에서 $$\lVert A-B\rVert_F\ge\lVert A-A_k\rVert_F=\Big(\sum_{i>k}\sigma_i^2\Big)^{1/2}.$$

증명은 operator norm의 경우처럼 단순하지 않고, singular value의 min-max 특성화(Weyl's inequality 계열)가 필요하다. Eckart와 Young이 1936년 원 논문에서 보인 것이 바로 이것이고 [6], Mirsky가 1960년 unitarily invariant norm 전체로 일반화했다 [7]. 이 글에서는 증명하지 않고 결과만 인용한다.

**Example (rank-$1$ 근사).** $$A=\begin{pmatrix}3&0\\0&1\end{pmatrix}$$은 이미 대각이라 $\sigma_1=3,\sigma_2=1$, $u_i=v_i=e_i$다. 가장 가까운 rank-$1$ 행렬은 $$A_1=\begin{pmatrix}3&0\\0&0\end{pmatrix},\qquad\lVert A-A_1\rVert_{op}=\lVert A-A_1\rVert_F=1=\sigma_2$$이다.

## 참고문헌

1. Beltrami, E. (1873). Sulle funzioni bilineari. *Giornale di Matematiche ad Uso degli Studenti delle Università Italiane*, 11, 98–106.
2. Jordan, C. (1874). Mémoire sur les formes bilinéaires. *Journal de Mathématiques Pures et Appliquées*, 19, 35–54.
3. Autonne, L. (1902). Sur les groupes linéaires, réels et orthogonaux. *Bulletin de la Société Mathématique de France*, 30, 121–134.
4. Moore, E. H. (1920). On the reciprocal of the general algebraic matrix. *Bulletin of the American Mathematical Society*, 26, 394–395.
5. Penrose, R. (1955). A generalized inverse for matrices. *Proceedings of the Cambridge Philosophical Society*, 51(3), 406–413.
6. Eckart, C., & Young, G. (1936). The approximation of one matrix by another of lower rank. *Psychometrika*, 1(3), 211–218.
7. Mirsky, L. (1960). Symmetric gauge functions and unitarily invariant norms. *Quarterly Journal of Mathematics*, 11(1), 50–59.
