---
layout: post
title: "Bilinear forms, quadratic forms, and positive operators"
date: 2026-08-15
mathematicians: [Grassmann, Cholesky, Sylvester]
---

## Bilinear form과 multilinear form

**Definition (Bilinear Form).** $$B:V\times V\to F$$가 각 변수에 대해 따로 linear이면 bilinear form이라 한다.

**Definition (Gram Matrix).** basis $v_1,\dots,v_n$에 대해 $G_{ij}=B(v_i,v_j)$로 정한 행렬 $G$를 $B$의 Gram matrix라 한다. 좌표로 쓰면 $B(u,w)=[u]^{\mathsf T}G\,[w]$이다.

operator와 bilinear form은 basis 변환에서 서로 다르게 변한다.

**Proposition (congruence).** 새 basis를 열로 갖는 change-of-basis 행렬을 $P$라 하면 Gram matrix는 $G\mapsto P^{\mathsf T}GP$로 바뀐다.

*Proof.* 새 basis $v_j'=\sum_iP_{ij}v_i$에 대해 $$G'_{jl}=B(v_j',v_l')=\sum_{i,k}P_{ij}P_{kl}B(v_i,v_k)=\sum_{i,k}P_{ij}G_{ik}P_{kl}=(P^{\mathsf T}GP)_{jl}$$이다. $\blacksquare$

operator는 basis 변환에서 similarity $A\mapsto P^{-1}AP$로, bilinear form은 congruence $G\mapsto P^{\mathsf T}GP$로 변한다. $P^{-1}$과 $P^{\mathsf T}$가 다르므로 이 둘은 서로 다른 동치 관계이며, 그래서 operator의 불변량(eigenvalue 등)과 bilinear form의 불변량(signature 등)이 갈린다.

변수를 $2$개에서 $k$개로 늘리면 multilinear form이 되는데, symmetric·antisymmetric·alternating 같은 대칭성은 bilinear form에 국한되지 않고 이 일반적인 수준에서 한 번에 정의하는 것이 경제적이다.

**Definition (Multilinear Form).** $k$개의 변수를 받는 $$B:\underbrace{V\times\cdots\times V}_{k}\to F$$가 각 변수마다 따로 linear이면 $k$-linear form이라 한다. bilinear form은 $k=2$인 경우다.

**Definition (Symmetric, Antisymmetric, Alternating).** $k$-linear form $B$가 임의의 permutation $\sigma\in S_k$와 임의의 $v_1,\dots,v_k$에서 $$B(v_{\sigma(1)},\dots,v_{\sigma(k)})=B(v_1,\dots,v_k)$$를 만족하면 symmetric, $$B(v_{\sigma(1)},\dots,v_{\sigma(k)})=\operatorname{sgn}(\sigma)\,B(v_1,\dots,v_k)$$를 만족하면 antisymmetric(또는 skew-symmetric)이라 한다. 어떤 $i\ne j$에서 $v_i=v_j$일 때 언제나 값이 $0$이면 alternating이라 한다. $k=2$이면 symmetric은 $B(u,w)=B(w,u)$, antisymmetric은 $B(u,w)=-B(w,u)$가 된다.

**Proposition.** alternating이면 언제나 antisymmetric이다. 표수가 $2$가 아니면 그 역도 성립해 antisymmetric과 alternating이 같은 뜻이 되지만, 표수가 $2$인 체에서는 antisymmetric이 symmetric과 같아져($-1=1$이므로) alternating보다 훨씬 약한 조건이 된다.

*Proof.* 임의의 permutation은 인접한 두 자리를 맞바꾸는 transposition들의 합성이므로, $i,i+1$번째 자리에만 $u,w$를 넣고 나머지 $k-2$개 자리는 고정한 경우만 보면 충분하다(이하 $B(\dots,u,w,\dots)$는 그렇게 넣은 값을 뜻한다). $$0=B(\dots,u+w,u+w,\dots)=B(\dots,u,u,\dots)+B(\dots,u,w,\dots)+B(\dots,w,u,\dots)+B(\dots,w,w,\dots)$$인데 alternating이라 양 끝 두 항이 $0$이므로 $B(\dots,u,w,\dots)=-B(\dots,w,u,\dots)$, 곧 그 두 자리를 바꾸면 sign이 뒤집힌다(표수와 무관하게 성립). 이것이 모든 인접한 자리에서 성립하므로 antisymmetric이다. 표수가 $2$가 아니면 역으로, antisymmetric인 $B$에 같은 자리 두 곳에 같은 벡터 $v$를 넣으면 $B(\dots,v,v,\dots)=-B(\dots,v,v,\dots)$에서 $2B(\dots,v,v,\dots)=0$이라 $B(\dots,v,v,\dots)=0$, 곧 alternating이다. $\blacksquare$

이제부터는 다시 $k=2$인 bilinear form으로 돌아와, Gram matrix가 있어야 뜻이 통하는 개념들을 본다.

**Definition (Non-degenerate).** bilinear form $B$가 $u\mapsto B(u,\cdot)$을 $V\to V^*$인 injective map으로 만들면(곧 모든 $w$에서 $B(u,w)=0$이면 $u=0$이면) non-degenerate라 한다.

**Proposition.** 유한차원에서 $B$가 non-degenerate인 것은 Gram matrix $G$가 invertible인 것과 동치다.

*Proof.* $u\mapsto B(u,\cdot)$를 좌표로 옮기면 $x\mapsto x^{\mathsf T}G$(행벡터로의 대응)이다. 이 map이 injective인 것은 $x^{\mathsf T}G=0\Rightarrow x=0$, 곧 $G$가 invertible인 것과 동치다. $\blacksquare$

**Example (non-degenerate가 아닌 bilinear form).** $\mathbb{R}^2$에서 $B(u,w):=u_1w_1$(첫 좌표만 곱함)은 symmetric bilinear form이지만, $u=(0,1)\ne0$에서 모든 $w$에 대해 $B(u,w)=0$이라 non-degenerate가 아니다. 실제로 Gram matrix $$G=\begin{pmatrix}1&0\\0&0\end{pmatrix}$$은 invertible이 아니다.

**Definition (Positive Definite).** ordered field(예: $\mathbb{R}$) 위의 symmetric bilinear form $B$가 모든 $v\ne0$에서 $B(v,v)>0$을 만족하면 positive definite라 한다.

**Proposition.** positive definite bilinear form은 non-degenerate다.

*Proof.* $u\ne0$이면 $B(u,u)>0\ne0$이라 $B(u,\cdot)$이 zero functional이 아니므로, $u\mapsto B(u,\cdot)$이 injective, 곧 non-degenerate다. $\blacksquare$

실수 위의 inner product의 정의(대칭성, 선형성, 양의 정부호성)는 정확히 positive definite symmetric bilinear form이며, dot product가 그 표준적인 예다.

두 bilinear form도 서로 간섭하지 않게 합칠 수 있다.

**Definition (Direct Sum of Bilinear Forms).** $(V_1,B_1)$, $(V_2,B_2)$에 대해 $V_1\oplus V_2$ 위에 $$(B_1\oplus B_2)\big((u_1,u_2),(w_1,w_2)\big):=B_1(u_1,w_1)+B_2(u_2,w_2)$$로 정의한 것을 $B_1$과 $B_2$의 direct sum이라 한다.

**Proposition.** $V_1,V_2$의 기저를 이어붙인 기저에서 $B_1\oplus B_2$의 Gram matrix는 $B_1,B_2$의 Gram matrix를 대각으로 놓은 block-diagonal 행렬이다. 또 $B_1\oplus B_2$가 non-degenerate인 것은 $B_1,B_2$가 둘 다 non-degenerate인 것과 동치다.

*Proof.* $(u_1,0)$과 $(0,u_2)$ 꼴의 기저 벡터에 정의를 그대로 적용하면 $$(B_1\oplus B_2)\big((u_1,0),(w_1,0)\big)=B_1(u_1,w_1),\qquad (B_1\oplus B_2)\big((0,u_2),(0,w_2)\big)=B_2(u_2,w_2)$$이고, 서로 다른 쪽을 섞으면(예: $(u_1,0)$과 $(0,w_2)$) $0$이므로 Gram matrix가 block-diagonal이다. block-diagonal 행렬이 invertible인 것은 각 block이 invertible인 것과 동치이므로, 앞 Proposition으로 non-degenerate 조건도 그대로 나뉜다. $\blacksquare$

inner product의 orthogonality도 symmetric 또는 antisymmetric bilinear form으로 일반화된다. 일반적인(symmetric도 antisymmetric도 아닌) bilinear form에서는 $B(u,w)=0$이 $B(w,u)=0$을 보장하지 않아 orthogonal이 $u,w$에 대해 대칭인 관계가 되지 못하고, 대신 left radical $$\{\,v\in V:B(v,w)=0\text{ for all }w\in V\,\}$$와 right radical $$\{\,v\in V:B(w,v)=0\text{ for all }w\in V\,\}$$가 서로 다른 부분공간으로 갈린다. symmetric이든 antisymmetric이든 $B(u,w)=0$과 $B(w,u)=0$은(둘 중 하나가 다른 하나의 $\pm1$배이므로) 항상 동시에 성립하거나 동시에 실패해 이 문제가 사라지므로, orthogonal은 이 두 경우에 대해서만 다룬다.

**Definition (Orthogonal, Radical).** symmetric 또는 antisymmetric bilinear form $B$에 대해 $B(u,w)=0$이면 $u\perp w$라 쓴다(위에서 본 대로 이 관계는 $u,w$에 대해 대칭이다). subspace $W\subseteq V$에 대해 $$W^{\perp_B}:=\{\,v\in V:B(v,w)=0\text{ for all }w\in W\,\}$$를 $W$의 ($B$에 대한) orthogonal complement라 하고, $V^{\perp_B}$를 $B$의 radical이라 한다. $B$가 non-degenerate인 것은 radical이 $$\{0\}$$인 것과 같은 말이다.

**Theorem (차원).** 유한차원 $V$ 위에서 $B$가 non-degenerate이면, 임의의 부분공간 $W\subseteq V$에서 $$\dim W^{\perp_B}=\dim V-\dim W$$이다.

*Proof.* $\beta:V\to V^*$, $\beta(v):=B(v,\cdot)$로 두면 $\ker\beta$가 $B$의 radical, 곧 $$\{0\}$$이라 $\beta$는 injective이고, $\dim V^*=\dim V$이니(유한차원) isomorphism이다. $w\in W^{\perp_B}$인 것은 모든 $u\in W$에서 $\beta(w)(u)=B(w,u)=0$, 곧 $\beta(w)\in W^\circ$(annihilator)인 것과 같으므로 $W^{\perp_B}=\beta^{-1}(W^\circ)$이다. $\beta$가 isomorphism이므로 $\dim W^{\perp_B}=\dim W^\circ=\dim V-\dim W$이다(Annihilator Theorem, Dual space and Riesz representation 글). $\blacksquare$

inner product의 orthogonal complement와 다른 점은, 여기서는 $V=W\oplus W^{\perp_B}$가 보장되지 않는다는 것이다. $B(v,v)=0$인 $v\ne0$(isotropic vector라 한다)가 있으면 $W=\operatorname{span}(v)$가 자기 자신의 orthogonal complement에 들어가 버려 직합이 무너질 수 있다.

**Example (isotropic vector와 무너지는 직합).** $\mathbb{R}^2$ 위의 symmetric bilinear form $$B(x,y):=x_1y_1-x_2y_2$$를 보자(radical이 $$\{0\}$$이라 $V$ 전체에서 non-degenerate다). $W=\operatorname{span}(1,1)$을 보면 $B((1,1),(1,1))=1-1=0$이라 $v=(1,1)$이 isotropic이고, 실제로 $$W^{\perp_B}=\{(v_1,v_2):v_1-v_2=0\}=\operatorname{span}(1,1)=W$$이다. 차원은 $\dim W^{\perp_B}=1=2-1$로 위 정리에 맞지만, $$W\cap W^{\perp_B}=W\ne\{0\}$$이라 $V=W\oplus W^{\perp_B}$는 성립하지 않는다.

**Example (dot product).** $\mathbb{R}^n$의 dot product $B(u,w)=\sum_iu_iw_i$은 $G=I$인 symmetric bilinear form이다.

**Example (부호 있는 넓이).** $\mathbb{R}^2$에서 $B(u,w)=u_1w_2-u_2w_1$은 alternating bilinear form이고 두 벡터가 이루는 평행사변형의 부호 있는 넓이를 준다. Gram matrix는 $$G=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$$이다. 이것이 $2\times2$ determinant다.

일반 $k$-linear form에서 alternating의 힘은 $k=\dim V$일 때 가장 두드러진다.

**Theorem (determinant는 유일한 alternating $n$-linear form).** $n$차원 $V$에서 alternating $n$-linear form 전체는 $1$차원 vector space를 이룬다. $F^n$의 표준 basis에서 값이 $1$인 유일한 것이 determinant다.

Determinant 글에서 세운 공리, 곧 행에 대해 alternating multilinear이고 $\det I=1$이라는 것이 바로 이 정리의 다른 얼굴이다. determinant가 그 공리로 유일하게 정해진 까닭은 결국 alternating $n$-linear form 공간이 $1$차원이기 때문이며, 그 유일성은 Determinant 글의 Leibniz 전개 논증이 그대로 보인다. 이 alternating multilinear 관점을 $k<n$개의 변수로 넓히면 exterior algebra가 나오는데, 이는 Tensor product and exterior algebra 글에서 다룬다.

여기서 다룬 multilinear·alternating form의 뿌리는 Hermann Grassmann이 1844년 《Die lineale Ausdehnungslehre》에서 세운 확장론이다 [1]. Grassmann은 오늘날의 vector space, 일차독립, 차원, 그리고 wedge product에 해당하는 것을 이미 담았지만, 서술이 지나치게 추상적이고 철학적이어서 당대에는 거의 읽히지 않았고 수십 년이 지나서야 제대로 평가받았다.

## Positive operator

**Definition (Positive Semidefinite, Positive Definite).** self-adjoint $T:V\to V$가 모든 $v$에서 $\langle Tv,v\rangle\ge0$이면 positive semidefinite, 모든 $v\ne0$에서 $\langle Tv,v\rangle>0$이면 positive definite라 한다.

복소수 위에서는 self-adjoint라는 조건이 저절로 따라온다는 놀라운 사실이 있다.

**Proposition.** 복소수 inner product space에서 linear map $T$가 모든 $v$에서 $\langle Tv,v\rangle\in\mathbb{R}$이면 $T$는 self-adjoint다.

*Proof.* $\langle Tv,v\rangle\in\mathbb{R}$은 $\langle Tv,v\rangle=\overline{\langle Tv,v\rangle}=\langle v,Tv\rangle$, 곧 $\langle(T-T^*)v,v\rangle=0$과 같다(모든 $v$에서). $S:=T-T^*$로 두고 $B(u,w):=\langle Su,w\rangle$($u$에 선형, $w$에 켤레선형)라 하면 가정은 $B(v,v)=0$이 모든 $v$에서 성립한다는 것이다. $$0=B(v+w,v+w)=B(v,v)+B(v,w)+B(w,v)+B(w,w)=B(v,w)+B(w,v)$$이고 $$0=B(v+iw,v+iw)=B(v,v)-iB(v,w)+iB(w,v)+B(w,w)=-iB(v,w)+iB(w,v)$$이다(둘째 등호에서 $B(v,iw)=\bar iB(v,w)=-iB(v,w)$, $B(iw,v)=iB(w,v)$, $B(iw,iw)=i\bar iB(w,w)=B(w,w)$을 썼다). 뒤 식에서 $B(w,v)=B(v,w)$이고 이를 앞 식에 넣으면 $2B(v,w)=0$이다. 곧 $B\equiv0$, 곧 $S=T-T^*=0$이다. $\blacksquare$

**Example (실수에서는 성립하지 않음).** $\mathbb{R}^2$에서 $90^\circ$ 회전 $$A=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$$은 $\langle Av,v\rangle=v_1(-v_2)+v_2v_1=0$이 모든 $v$에서 성립하지만(antisymmetric이면 언제나 그렇다) $A^{\mathsf T}=-A\ne A$라 self-adjoint가 아니다. 위 Proposition의 논증은 스칼라 $i$가 없는 실수 위에서는 성립하지 않는다.

**Theorem (Positive Operator의 특성화).** self-adjoint $T:V\to V$에 대해 다음이 동치다. (i) $T$는 positive semidefinite다. (ii) $T$의 모든 eigenvalue가 $\ge0$이다. (iii) $T=S^2$인 positive semidefinite self-adjoint $S$가 유일하게 존재한다. (iv) $T=B^*B$인 linear map $B$가 존재한다.

*Proof.* (i)$\Leftrightarrow$(ii): (복소수) spectral theorem 또는 (실수) principal axis theorem으로 orthonormal eigenbasis $e_1,\dots,e_n$과 eigenvalue $\lambda_1,\dots,\lambda_n$을 잡으면, $v=\sum_ic_ie_i$에서 $$\langle Tv,v\rangle=\sum_i\lambda_i\vert c_i\vert^2$$이다. 이것이 모든 $v$에서 $\ge0$인 것은(각 $e_i$를 넣어 보면 필요조건, 위 식이 충분조건) 모든 $\lambda_i\ge0$인 것과 동치다.

(ii)$\Rightarrow$(iii): 같은 eigenbasis에서 eigenvalue $\sqrt{\lambda_i}$(음이 아닌 실수 제곱근)로 정의한 $S$는 self-adjoint이고 positive semidefinite이며 $S^2$은 eigenvalue가 $\lambda_i$인 같은 operator, 곧 $T$다.

유일성: $S,S'$가 둘 다 $T$의 positive semidefinite self-adjoint square root라 하자. $ST=SS^2=S^3=S^2S=TS$이므로 $S$는 $T$와 commute하고, 마찬가지로 $S'$도 $T$와 commute한다. commute하는 operator는 서로의 eigenspace를 보존하므로(Cayley–Hamilton과 Jordan form 글의 Simultaneous Diagonalization Corollary와 같은 논증) $S$는 $T$의 eigenspace $E_\lambda$를 보존하고, 그 위에서 $S^2=\lambda I$를 만족하는 self-adjoint operator이므로 위와 같은 논증으로 $S\vert_{E_\lambda}$의 eigenvalue는 $\sqrt\lambda$ 하나뿐이라 $S\vert_{E_\lambda}=\sqrt\lambda\,I$다. 같은 논증이 $S'$에도 적용되어 $S'\vert_{E_\lambda}=\sqrt\lambda\,I=S\vert_{E_\lambda}$이고, $T$의 eigenspace들이 $V$ 전체를 생성하므로 $S=S'$이다.

(iii)$\Rightarrow$(iv): $B:=S$로 두면 $B^*B=S^*S=S^2=T$이다($S$가 self-adjoint이므로 $S^*=S$).

(iv)$\Rightarrow$(i): $\langle Tv,v\rangle=\langle B^*Bv,v\rangle=\langle Bv,Bv\rangle=\lVert Bv\rVert^2\ge0$이고, $T^*=(B^*B)^*=B^*B=T$이므로 $T$는 self-adjoint이며 positive semidefinite다. $\blacksquare$

**Corollary (Positive Definite는 Invertible).** positive definite $T$는 invertible이다.

*Proof.* $Tv=0$이면 $\langle Tv,v\rangle=0$인데, $v\ne0$이면 positive definite에서 $\langle Tv,v\rangle>0$이어야 하므로 $v=0$이다. 곧 $$\ker T=\{0\}$$이라 $T$는 invertible이다. $\blacksquare$

**Definition ($\sqrt T$).** 위 유일한 positive semidefinite square root를 $\sqrt T$라 쓴다.

**Remark ($B$의 비유일성과 명시적 계산).** (iv)의 $B$는 유일하지 않다. $T=B^*B=(UB)^*(UB)$가 임의의 unitary $U$에서 성립하므로 $B$를 unitary만큼 바꿔도 같은 $T$를 준다. 증명에서 쓴 $B=\sqrt T$는 self-adjoint라는 규범적인 선택이지만 eigenvalue를 구해야 해서 비싸다. 아래 Cholesky Decomposition이 훨씬 값싼 다른 선택을 준다: $T=A$가 행렬로 주어지고 $A=LL^{\mathsf T}$($L$은 lower triangular)이면 $B:=L^{\mathsf T}$로 두어도 $B^{\mathsf T}B=LL^{\mathsf T}=A$이다(실행렬이라 $B^*=B^{\mathsf T}=L$). eigenvalue 계산 없이 사칙연산만으로 끝나는 이 방법이 실제 계산에서 훨씬 널리 쓰인다.

**Theorem (Cholesky Decomposition).** positive definite real symmetric $A\in\mathbb{R}^{n\times n}$은 $A=LL^{\mathsf T}$($L$은 대각성분이 양수인 lower triangular)로 유일하게 decompose된다.

*Proof.* $n$에 대한 induction. $n=1$이면 $A=(a)$, $a>0$이라 $L=(\sqrt a)$다. $n>1$이라 하고 $$A=\begin{pmatrix}a_{11}&b^{\mathsf T}\\b&C\end{pmatrix}$$로 block으로 쓰자. $e_1$을 넣으면 positive definite에서 $a_{11}>0$이다. $$M:=\begin{pmatrix}1&0\\-b/a_{11}&I\end{pmatrix}$$로 두면 직접 계산으로 $$MAM^{\mathsf T}=\begin{pmatrix}a_{11}&0\\0&S\end{pmatrix},\qquad S:=C-\frac{bb^{\mathsf T}}{a_{11}}$$이다($S$는 Schur complement). $M$이 invertible이므로 $z\ne0\Rightarrow M^{\mathsf T}z\ne0$이고 $$z^{\mathsf T}(MAM^{\mathsf T})z=(M^{\mathsf T}z)^{\mathsf T}A(M^{\mathsf T}z)>0$$이라 $MAM^{\mathsf T}$도 positive definite이며, $(0,y)$ 꼴을 넣으면 $S$도 (크기 $(n-1)\times(n-1)$의) positive definite다.

induction 가정으로 $S=L_2L_2^{\mathsf T}$($L_2$는 대각성분이 양수인 lower triangular)라 하자. $$M^{-1}=\begin{pmatrix}1&0\\b/a_{11}&I\end{pmatrix}$$이므로 $$L:=M^{-1}\begin{pmatrix}\sqrt{a_{11}}&0\\0&L_2\end{pmatrix}=\begin{pmatrix}\sqrt{a_{11}}&0\\b/\sqrt{a_{11}}&L_2\end{pmatrix}$$로 두면, $L$은 대각성분이 양수인 lower triangular이고 $$LL^{\mathsf T}=M^{-1}\begin{pmatrix}a_{11}&0\\0&S\end{pmatrix}(M^{-1})^{\mathsf T}=M^{-1}(MAM^{\mathsf T})(M^{-1})^{\mathsf T}=A$$이다.

유일성. $A=LL^{\mathsf T}=L'L'^{\mathsf T}$이면 $$(L')^{-1}L=L'^{\mathsf T}(L^{\mathsf T})^{-1}$$인데 좌변은 lower triangular끼리의 곱(역행렬도 lower triangular를 보존)이고 우변은 upper triangular끼리의 곱이라, 이 행렬은 대각이다. 대각성분을 비교하면 $(L')^{-1}L$의 $i$번째 대각성분은 $L,L'$ 대각성분의 비 $L_{ii}/L'_{ii}$이고, $L'^{\mathsf T}(L^{\mathsf T})^{-1}$의 $i$번째 대각성분은 그 역수라, 이 대각행렬 $D_0$는 $D_0=D_0^{-1}$을 만족한다. 대각성분이 모두 양수라 $D_0=I$이고, 곧 $L=L'$이다. $\blacksquare$

**Example (Cholesky 계산).** $$A=\begin{pmatrix}4&2\\2&3\end{pmatrix}$$을 보자. $a_{11}=4$, $\sqrt{a_{11}}=2$, $b=2$, $S=3-\dfrac{2\cdot2}{4}=2$, $L_2=\sqrt2$이므로 $$L=\begin{pmatrix}2&0\\1&\sqrt2\end{pmatrix},\qquad LL^{\mathsf T}=\begin{pmatrix}4&2\\2&1+2\end{pmatrix}=\begin{pmatrix}4&2\\2&3\end{pmatrix}=A$$로 확인된다.

이 decomposition은 André-Louis Cholesky가 프랑스 육군의 측지학(geodesy) 업무 중 최소제곱 문제를 풀며 고안했다. Cholesky는 1918년 제1차 세계대전에서 전사했고, 생전에 이를 출판하지 않아 동료 장교 Benoit가 1924년 유고를 정리해 대신 발표했다 [2].

**Theorem (Positive Definite 행렬의 다섯 동치조건).** real symmetric $A\in\mathbb{R}^{n\times n}$에 대해 다음이 모두 동치다. (a) $A$는 positive definite다(모든 $x\ne0$에서 $x^{\mathsf T}Ax>0$). (b) $A$의 모든 eigenvalue가 $>0$이다. (c) $A$의 모든 leading principal minor $\det A_k$($k=1,\dots,n$; $A_k$는 왼쪽 위 $k\times k$ 부분행렬)가 $>0$이다. (d) $A$를 행 교환 없이 소거했을 때 나오는 pivot이 모두 $>0$이다. (e) $A=R^{\mathsf T}R$인 full column rank $R$이 존재한다.

*Proof.* (a)$\Leftrightarrow$(b)는 위 Theorem의 (i)$\Leftrightarrow$(ii)와 같은 계산을 부등호를 strict로 바꿔 반복하면 나온다.

(d)$\Leftrightarrow$(c): Gaussian elimination 글의 LDU decomposition $A=LDU'$($L,U'$은 unit triangular, $D=\operatorname{diag}(d_1,\dots,d_n)$이 pivot)을 앞 $k$개 행·열로 block 분할하면, $L$이 lower triangular이고 $U'$이 upper triangular라 곱의 왼쪽 위 $k\times k$ block은 각 block의 왼쪽 위 $k\times k$ 부분끼리의 곱, 곧 $A_k=L_kD_kU_k'$이다($L_k,U_k'$은 크기 $k$의 unit triangular). $\det L_k=\det U_k'=1$이므로 $$\det A_k=\det D_k=d_1d_2\cdots d_k,$$ 곧 $d_k=\det A_k/\det A_{k-1}$($\det A_0:=1$)이다. 이 비율 공식으로 모든 $d_k>0$인 것과 모든 $\det A_k>0$인 것이 서로를 강제하며 동치다.

(b)$\Rightarrow$(c): eigenvalue가 모두 양수라 하자. $x\in\mathbb{R}^k$, $x\ne0$이면 $(x,0)\in\mathbb{R}^n$도 $\ne0$이라 $$x^{\mathsf T}A_kx=(x,0)^{\mathsf T}A(x,0)>0$$이므로 $A_k$도 positive definite이고, (a)$\Leftrightarrow$(b)로 $A_k$의 eigenvalue도 모두 양수이니 $\det A_k=\prod_i\lambda_i(A_k)>0$이다(Eigenvalue and diagonalization 글).

(c)$\Rightarrow$(a): $\det A_k\ne0$(실제로 $>0$)이 매 단계 유지되어 소거가 행 교환 없이 끝까지 진행되므로 $A=LDU'$을 얻고, $A$가 symmetric이므로 $A=A^{\mathsf T}=U'^{\mathsf T}DL^{\mathsf T}$에서 LDU 분해의 유일성(Gaussian elimination 글)으로 $U'=L^{\mathsf T}$다. $x\ne0$에서 $y:=L^{\mathsf T}x\ne0$($L^{\mathsf T}$가 invertible)이므로 $$x^{\mathsf T}Ax=x^{\mathsf T}LDL^{\mathsf T}x=y^{\mathsf T}Dy=\sum_id_iy_i^2>0$$이다(위에서 본 대로 모든 $d_i>0$).

(a)$\Leftrightarrow$(e): 위 Theorem의 (i)$\Leftrightarrow$(iv)에 $B$의 injectivity(full column rank)를 더한 것이다. $R$이 full column rank면 $x\ne0\Rightarrow Rx\ne0$이라 $x^{\mathsf T}Ax=\lVert Rx\rVert^2>0$이다. 역으로 $A$가 positive definite이면 Cholesky Decomposition으로 $A=LL^{\mathsf T}$($L$은 대각성분이 양수라 invertible)이므로 $R:=L^{\mathsf T}$가 full column rank다. $\blacksquare$

이 다섯 조건을 나란히 놓는 방식은 Gilbert Strang의 선형대수학 교재에서 널리 알려졌다.

## Quadratic form과 Sylvester's law of inertia

위 bilinear form과 positive definite의 정의를 real spectral theorem으로 완전히 분류할 차례다.

**Definition (Quadratic Form).** 실수 vector space $V$ 위의 symmetric bilinear form $B$에 대해 $q(v):=B(v,v)$를 $B$가 주는 quadratic form이라 한다.

basis를 고르면 $B$의 Gram matrix $A$(위 Bilinear form 절)에 대해 $$q(x)=B(x,x)=x^{\mathsf T}Ax=\sum_{i,j}A_{ij}x_ix_j$$로, quadratic form은 정확히 좌표의 이차 동차 quadratic polynomial이다. Positive operator 절의 $\langle Av,v\rangle$도 표준 inner product를 쓰면 같은 식 $v^{\mathsf T}Av$이므로, "positive (semi)definite operator"와 "언제나 양(또는 $0$ 이상)인 값을 가지는 quadratic polynomial"은 같은 대상을 bilinear form과 operator라는 두 각도에서 본 것뿐이다.

**Theorem (Sylvester's Law of Inertia).** 실수 유한차원 $V$ 위의 symmetric bilinear form $B$에 대해, $B(e_i,e_j)=0$ ($i\ne j$)이고 $$B(e_i,e_i)\in\{1,-1,0\}$$인 basis $e_1,\dots,e_n$이 존재한다. 더 나아가, 그런 basis에서 $B(e_i,e_i)=1$인 개수 $n_+$, $=-1$인 개수 $n_-$, $=0$인 개수 $n_0$은 basis 선택과 무관하게 $B$에 의해서만 결정된다. $(n_+,n_-,n_0)$을 $B$의 signature(또는 inertia)라 한다.

*Proof.* **존재.** $V$에 임의로 inner product를 하나 주고(예: 어떤 basis를 orthonormal로 선언), 그에 대한 $B$의 Gram matrix $G$를 생각하자(위 Bilinear form 절). $G$는 symmetric이므로 real spectral theorem으로 $G=QDQ^{\mathsf T}$($Q$ orthogonal, $D=\operatorname{diag}(\lambda_1,\dots,\lambda_n)$)이다. 위 congruence 성질로 $Q$의 열을 새 basis $f_1,\dots,f_n$로 삼으면 이 basis에서 $B$의 Gram matrix는 $Q^{\mathsf T}GQ=D$다. $\lambda_i\ne0$인 곳에서 $e_i:=f_i/\sqrt{\vert\lambda_i\vert}$로, $\lambda_i=0$인 곳에서 $e_i:=f_i$로 다시 scale하면(congruence로 $B(e_i,e_i)=\lambda_i/\vert\lambda_i\vert=\operatorname{sign}(\lambda_i)$, $\lambda_i=0$이면 $0$) 원하는 basis를 얻는다.

**불변성.** 두 basis $e_1,\dots,e_n$과 $e_1',\dots,e_n'$이 모두 이런 대각형($$\{1,-1,0\}$$ 성분)을 준다고 하자. $n_0$은 두 경우 모두 $\dim V-\operatorname{rank}G$(congruence가 rank를 보존하므로 basis 무관)와 같으므로 같다. $n_+=n_+'$임을 보이면 $n_++n_-=n_+'+n_-'=\operatorname{rank}G$에서 $n_-=n_-'$도 따라온다.

두 부분공간 $$P_+:=\operatorname{span}\{e_i:B(e_i,e_i)=1\}$$(차원 $n_+$), $$Z_-':=\operatorname{span}\{e_i':B(e_i',e_i')\le0\}$$(차원 $n-n_+'$)를 두자. $P_+$ 위에서는 $v\ne0\Rightarrow B(v,v)>0$이고(대각형이라 $B(v,v)=\sum c_i^2>0$), $Z_-'$ 위에서는 $B(v,v)\le0$이다(마찬가지로 대각형이라 $B(v,v)=\sum c_i^2B(e_i',e_i')\le0$).

그러면 $$P_+\cap Z_-'=\{0\}$$이다: $v$가 둘 다에 있으면 $B(v,v)>0$($v\ne0$이면)과 $B(v,v)\le0$이 동시에 성립해야 하므로 $v=0$이다. 그러므로 Grassmann dimension formula(Vector space 글)로 $$\dim P_++\dim Z_-'\le n,\qquad n_++(n-n_+')\le n,\qquad n_+\le n_+'$$이다. 역할을 바꾸면 $n_+'\le n_+$도 나와 $n_+=n_+'$이다. $\blacksquare$

**Corollary (Pivot으로 signature 계산하기).** symmetric $A$가 행 교환 없이 소거되면(모든 leading principal minor가 $0$이 아니면), $A=LDL^{\mathsf T}$(Gaussian elimination 글, $D=\operatorname{diag}(d_1,\dots,d_n)$은 pivot)이고, $A$의 signature는 양·음 pivot의 개수로 바로 읽힌다. 곧 eigenvalue를 하나도 구하지 않고 pivot의 부호만으로 signature를 계산할 수 있다.

*Proof.* $P:=(L^{\mathsf T})^{-1}$로 두면 $$P^{\mathsf T}AP=L^{-1}A(L^{\mathsf T})^{-1}=L^{-1}(LDL^{\mathsf T})(L^{\mathsf T})^{-1}=D$$이므로, $P$의 열을 새 basis로 삼으면 $A$의 congruence class 안에서 $D$가 그 Gram matrix다(congruence, 위 Bilinear form 절). $D$는 이미 대각이고, 양의 스칼라로 나누는 정규화는 부호를 보존하므로 위 정리의 불변성 논증을 그대로 적용하면 $D$의 대각성분 중 양수·음수·$0$의 개수, 곧 pivot의 부호별 개수가 $A$의 signature $(n_+,n_-,n_0)$다. $\blacksquare$

**Corollary.** $B$가 positive definite인 것은 signature가 $(n,0,0)$($n_+=\dim V$)인 것과 동치다.

**Proposition (Ellipsoid).** positive definite real symmetric $A\in\mathbb{R}^{n\times n}$에 대해 $$\{x\in\mathbb{R}^n:x^{\mathsf T}Ax=1\}$$은 ellipsoid다.

*Proof.* real spectral theorem의 orthonormal eigenbasis $q_1,\dots,q_n$(eigenvalue $\lambda_1,\dots,\lambda_n>0$, positive definite이므로 모두 양수)에서 $x=\sum_ic_iq_i$로 쓰면 $$x^{\mathsf T}Ax=\sum_i\lambda_ic_i^2=1,\qquad\text{곧}\qquad\sum_i\Big(\frac{c_i}{1/\sqrt{\lambda_i}}\Big)^2=1$$인데, 이는 $q_i$가 좌표축이고 그 방향의 반지름이 $1/\sqrt{\lambda_i}$인 ellipsoid의 표준 방정식이다. $\blacksquare$

이 ellipsoid는 SVD, polar decomposition, and matrix norms 글에서 볼 "단위구의 상"과 반대 방향의 관계에 있다: $A=T^{\mathsf T}T$로 보면 $$\{x:x^{\mathsf T}Ax=1\}=\{x:\lVert Tx\rVert=1\}$$은 $T$에 의해 codomain의 단위구로 사상되는 ellipsoid이고, 그 반지름 $1/\sqrt{\lambda_i}=1/\sigma_i$는 SVD가 주는 반지름 $\sigma_i$의 역수다.

**Example (Ellipsoid).** $$A=\begin{pmatrix}2&0\\0&1\end{pmatrix}$$(eigenvalue $2,1$)에서 $x^{\mathsf T}Ax=2x_1^2+x_2^2=1$은 반지름이 $1/\sqrt2,1$인 타원이다.

**Example (Minkowski form).** 위 Bilinear form 절에서 본 $\mathbb{R}^2$의 $B(x,y)=x_1y_1-x_2y_2$는 이미 대각형이라 signature가 $(1,1,0)$이다. 표준 basis를 어떻게 바꿔도(회전, scaling 등) 양의 대각성분 하나와 음의 대각성분 하나로만 대각화된다는 것이 Sylvester's Law가 주는 정보다.

**Example (다른 basis에서 시작해도 signature는 같다).** $\mathbb{R}^2$에서 $B$의 표준 basis에 대한 Gram matrix가 $$G=\begin{pmatrix}1&2\\2&1\end{pmatrix}$$이라 하자. eigenvalue는 $3,-1$이라 signature는 $(1,1,0)$이다. 실제로 basis를 $f_1=(1,1)$, $f_2=(1,-1)$로 바꾸면 $$B(f_1,f_1)=1+2+2+1=6,\quad B(f_2,f_2)=1-2-2+1=-2,\quad B(f_1,f_2)=1-2+2-1=0$$이라(직접 $x^{\mathsf T}Gy$로 계산) 이미 대각형이고, $e_1=f_1/\sqrt6$, $e_2=f_2/\sqrt2$로 다시 scale하면 $B(e_1,e_1)=1$, $B(e_2,e_2)=-1$로 signature $(1,1,0)$이 다시 확인된다.

이 정리가 중요한 것은, quadratic form을 basis 변환으로 대각형까지 옮기는 방법은 무수히 많지만 그 결과(부호의 개수)만은 basis 선택과 무관하게 절대 바뀌지 않는다는 것을 보장하기 때문이다. 예컨대 이차곡면(conic·quadric)을 좌표변환으로 분류할 때 최종적으로 남는 불변량이 이 signature이고, 다변수 미적분에서 임계점의 종류(극소·극대·안장점)를 Hessian의 signature로 판정하는 것도 같은 원리다(이는 나중 글에서 다룬다). 위 Corollary가 보여주듯 계산적으로도 중요한데, eigenvalue를 구하는 것보다 훨씬 값싼 pivot 계산만으로 signature 전체를 알 수 있기 때문이다.

Sylvester는 1852년 이 정리를 "law of inertia"라는 이름으로 처음 증명했다 [3](역학에서 관성모멘트의 principal axes를 대각화하는 것과 닮은 현상이라는 데서 이런 이름을 붙였다).

## 참고문헌

1. Grassmann, H. (1844). *Die lineale Ausdehnungslehre, ein neuer Zweig der Mathematik*. Leipzig: Otto Wigand.
2. Benoit, Commandant. (1924). Note sur une méthode de résolution des équations normales... (procédé du Commandant Cholesky). *Bulletin Géodésique*, 2, 67–77.
3. Sylvester, J. J. (1852). A demonstration of the theorem that every homogeneous quadratic polynomial is reducible by real orthogonal substitutions to the form of a sum of positive and negative squares. *Philosophical Magazine, Series 4*, 4(23), 138–142.
