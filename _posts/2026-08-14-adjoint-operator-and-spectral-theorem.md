---
layout: post
title: "Adjoint operator and the spectral theorem"
date: 2026-08-14
mathematicians: [Cauchy, Hermite, Schur]
---

## Adjoint operator

Dual space and Riesz representation 글의 Riesz Representation 정리를 그대로 쓴다.

**Theorem, Definition (Adjoint).** $V,W$가 같은 체 위의 유한차원 inner product space이고 $T:V\to W$가 linear map이면, $$\langle Tv,w\rangle_W=\langle v,T^*w\rangle_V\quad\text{for all }v\in V,\,w\in W$$를 만족하는 linear map $T^*:W\to V$가 유일하게 존재한다. 이를 $T$의 adjoint라 한다.

*Proof.* 각 $w\in W$를 고정하면 $v\mapsto\langle Tv,w\rangle_W$는 $V$ 위의 linear functional이므로, Riesz Representation으로 이를 $\langle v,T^*w\rangle_V$로 나타내는 $T^*w\in V$가 유일하게 정해진다(이로써 함수 $T^*:W\to V$가 well-defined). $T^*$가 linear임은 $$\langle v,T^*(aw+bw')\rangle_V=\langle Tv,aw+bw'\rangle_W=\bar a\langle Tv,w\rangle_W+\bar b\langle Tv,w'\rangle_W=\langle v,aT^*w+bT^*w'\rangle_V$$가 모든 $v$에서 성립하므로 Riesz Representation의 유일성으로 $T^*(aw+bw')=aT^*w+bT^*w'$이기 때문이다. $T^*$의 유일성은, 두 후보 $S,S'$가 모든 $v,w$에서 $\langle v,Sw\rangle=\langle v,S'w\rangle$을 만족하면 Riesz Representation의 유일성으로 $Sw=S'w$가 모든 $w$에서 성립하는 데서 나온다. $\blacksquare$

adjoint는 Dual space and Riesz representation 글의 dual map(transpose) $T^t:W^*\to V^*$, $T^t(\psi)=\psi\circ T$를 Riesz map으로 옮긴 것이다.

**Proposition.** $T^*=R_V^{-1}\circ T^t\circ R_W$.

*Proof.* $R_W(w)=\langle\cdot,w\rangle_W$이므로 $T^t(R_W(w))(v)=R_W(w)(Tv)=\langle Tv,w\rangle_W=\langle v,T^*w\rangle_V=R_V(T^*w)(v)$이고, 이는 $T^t(R_W(w))=R_V(T^*w)$라는 뜻이다. $\blacksquare$

**Proposition (adjoint의 성질).** $(S+T)^*=S^*+T^*$, $(cT)^*=\bar cT^*$, $(T^*)^*=T$, 합성 가능할 때 $(ST)^*=T^*S^*$, $I^*=I$, 그리고 $T$가 invertible이면 $(T^{-1})^*=(T^*)^{-1}$이다.

*Proof.* 앞 네 식은 정의식 $\langle Tv,w\rangle=\langle v,T^*w\rangle$을 정리하고 Riesz Representation의 유일성을 쓰면 나온다. 예컨대 $(T^*)^*=T$는, 정의식의 양변에 켤레를 취하면 $\langle w,Tv\rangle_W=\langle T^*w,v\rangle_V$인데 이것이 정확히 "$T^*$의 adjoint는 $T$다"라는 식이므로 유일성으로 나온다. 나머지도 같은 방식이다. $I^*=I$는 $\langle Iv,w\rangle=\langle v,w\rangle=\langle v,Iw\rangle$에서 유일성으로 나온다. $T$가 invertible이면 $(T^{-1})^*T^*=(TT^{-1})^*=I^*=I$이고 $T^*(T^{-1})^*=(T^{-1}T)^*=I$이므로($(ST)^*=T^*S^*$를 적용) $(T^{-1})^*=(T^*)^{-1}$이다. $\blacksquare$

**Proposition (행렬 표현).** $V,W$의 orthonormal basis에서 $T$의 행렬이 $A$이면, 같은 orthonormal basis에서 $T^*$의 행렬은 $A^*:=\overline{A}^{\mathsf T}$(conjugate transpose, 실수에서는 $A^{\mathsf T}$)이다.

*Proof.* orthonormal basis $e_1,\dots,e_n$($V$), $f_1,\dots,f_m$($W$)에서 $A_{ij}=\langle Te_j,f_i\rangle_W$이다(Inner product space 글에서 본 대로, orthonormal basis에 대한 전개 계수는 그 basis와의 inner product다). $T^*$의 행렬 성분은 $$(A^*)_{ij}=\langle T^*f_j,e_i\rangle_V=\overline{\langle e_i,T^*f_j\rangle_V}=\overline{\langle Te_i,f_j\rangle_W}=\overline{A_{ji}}$$이다. $\blacksquare$

**Proposition (adjoint의 eigenvalue·trace·determinant).** $V=W$(같은 유한차원 inner product space)일 때, $\lambda$가 $T^*$의 eigenvalue인 것은 $\bar\lambda$가 $T$의 eigenvalue인 것과 동치이고, $$\operatorname{tr}(T^*)=\overline{\operatorname{tr}T},\qquad\det(T^*)=\overline{\det T}$$이다.

*Proof.* orthonormal basis에서 $T$의 행렬을 $A$라 하면 $T^*$의 행렬은 $A^*=\overline A^{\mathsf T}$다. determinant는 Leibniz formula로 성분의 polynomial이라 conjugate와 교환되고($\det\overline M=\overline{\det M}$) transpose에는 불변이므로(Determinant 글) $$p_{T^*}(\lambda)=\det(A^*-\lambda I)=\det\big(\overline{A-\bar\lambda I}\big)^{\mathsf T}=\overline{\det(A-\bar\lambda I)}=\overline{p_T(\bar\lambda)}$$이다. 곧 $p_{T^*}(\lambda)=0\iff p_T(\bar\lambda)=0$이라 $\lambda$가 $T^*$의 eigenvalue인 것은 $\bar\lambda$가 $T$의 eigenvalue인 것과 동치다. 이 식에 $\lambda=0$을 넣으면 $\det(A^*)=\overline{\det A}$이고, 양변을 $\lambda$의 polynomial로 보아 $\lambda^{n-1}$의 계수를 비교하면(Eigenvalue and diagonalization 글의 trace–eigenvalue 관계) $\operatorname{tr}(A^*)=\overline{\operatorname{tr}A}$다. $\blacksquare$

**Theorem.** $\ker T^*=(\operatorname{im}T)^{\perp}$이고 $\operatorname{im}T^*=(\ker T)^{\perp}$이다.

*Proof.* $w\in\ker T^*\iff\langle v,T^*w\rangle_V=0\text{ for all }v\iff\langle Tv,w\rangle_W=0\text{ for all }v\iff w\in(\operatorname{im}T)^{\perp}$이라 첫 식이 나온다. 둘째 식은, $v\in\ker T$이면 임의의 $w$에서 $\langle v,T^*w\rangle_V=\langle Tv,w\rangle_W=0$이라 $\operatorname{im}T^*\subseteq(\ker T)^{\perp}$이고, 첫 식(orthogonal decomposition)으로 $$\dim\operatorname{im}T^*=\dim W-\dim\ker T^*=\dim W-\dim(\operatorname{im}T)^{\perp}=\dim\operatorname{im}T$$이며 rank–nullity로 $$\dim(\ker T)^{\perp}=\dim V-\dim\ker T=\operatorname{rank}T=\dim\operatorname{im}T$$로 같은 차원이라 포함이 등식이 된다. $\blacksquare$

Dual space and Riesz representation 글에서 $\ker T^t=(\operatorname{im}T)^\circ$, $\operatorname{im}T^t=(\ker T)^\circ$였던 것이, $R$을 통해 annihilator가 orthogonal complement로 바뀌며 그대로 되살아난 것이다.

**Corollary.** $\operatorname{rank}T^*=\operatorname{rank}T$다. $T$가 injective이면 $T^*$는 surjective이고, $T$가 surjective이면 $T^*$는 injective다.

*Proof.* Dual space and Riesz representation 글의 같은 이름 Corollary와 똑같은 논증이 annihilator 대신 orthogonal complement로 성립한다. $\blacksquare$

**Example (adjoint 계산).** $T:\mathbb{R}^3\to\mathbb{R}^2$, $T(x,y,z)=(x+y,\,y+z)$의 (표준 basis, 곧 orthonormal basis에서의) 행렬은 $$A=\begin{pmatrix}1&1&0\\0&1&1\end{pmatrix}$$이므로 $T^*:\mathbb{R}^2\to\mathbb{R}^3$의 행렬은 $$A^{\mathsf T}=\begin{pmatrix}1&0\\1&1\\0&1\end{pmatrix},\qquad T^*(a,b)=(a,\,a+b,\,b)$$이다.

## Self-adjoint, unitary, normal operator

이제부터는 $T:V\to V$, 곧 하나의 inner product space에서 자기 자신으로 가는 operator만 본다.

**Definition (Self-adjoint, Unitary, Normal).** $T^*=T$이면 self-adjoint(실수에서는 symmetric, 복소수에서는 Hermitian)라 한다. $T^*T=TT^*=I$이면 unitary(실수에서는 orthogonal)라 한다. $TT^*=T^*T$이면 normal이라 한다. self-adjoint와 unitary는 모두 normal이다(각각 $T^*=T$, $T^*T=TT^*=I$에서 자명하다).

**Corollary (행렬로 옮기면).** orthonormal basis에서 $T$의 행렬이 $A$이면(앞 절의 행렬 표현 Proposition으로 $T^*$의 행렬은 $A^*$다), $T$가 self-adjoint인 것은 $A^*=A$(실수에서는 $A^{\mathsf T}=A$인 symmetric matrix)인 것과, $T$가 unitary인 것은 $A^*A=AA^*=I$(실수에서는 $A^{\mathsf T}A=I$인 orthogonal matrix)인 것과, $T$가 normal인 것은 $AA^*=A^*A$인 것과 각각 동치다.

*Proof.* 세 정의식 $T^*=T$, $T^*T=TT^*=I$, $TT^*=T^*T$를 행렬 표현 Proposition으로 그대로 옮긴 것이다. $\blacksquare$

**Proposition (orthogonal projection = self-adjoint idempotent).** idempotent $P$($P^2=P$)가 orthogonal projection인 것은 $P^*=P$인 것과 동치다.

*Proof.* Inner product space 글의 Symmetry criterion 증명에서 transpose를 adjoint로, $\mathbb{R}^n$을 일반 inner product space로 바꾸면 같은 논증이 그대로 성립한다. $\blacksquare$

**Proposition (unitary는 inner product를 보존).** $T^*T=I$인 것은 모든 $v,v'$에서 $\langle Tv,Tv'\rangle=\langle v,v'\rangle$인 것과 동치다. 특히 unitary operator는 norm을 보존한다: $\lVert Tv\rVert=\lVert v\rVert$.

*Proof.* $\langle Tv,Tv'\rangle=\langle v,T^*Tv'\rangle$이므로 $T^*T=I$이면 $\langle Tv,Tv'\rangle=\langle v,v'\rangle$이다. 역으로 이것이 모든 $v,v'$에서 성립하면 $\langle v,(T^*T-I)v'\rangle=0$이 모든 $v,v'$에서 성립하고, $v=(T^*T-I)v'$을 넣으면 $\lVert(T^*T-I)v'\rVert^2=0$이 모든 $v'$에서 성립해 $T^*T=I$다. $v=v'$을 넣으면 norm 보존이 나온다. $\blacksquare$

**Proposition (self-adjoint operator의 eigenvalue는 실수).** $T^*=T$이고 $Tv=\lambda v$ ($v\ne0$)이면 $\lambda\in\mathbb{R}$이다.

*Proof.* $$\lambda\langle v,v\rangle=\langle Tv,v\rangle=\langle v,T^*v\rangle=\langle v,Tv\rangle=\bar\lambda\langle v,v\rangle$$이고 $v\ne0$이라 $\langle v,v\rangle\ne0$이므로 $\lambda=\bar\lambda$, 곧 $\lambda$는 실수다. $\blacksquare$

이 사실을 real symmetric matrix에 처음 증명한 것은 Augustin-Louis Cauchy로, 1829년 행성 운동의 장기섭동을 다루는 "secular equation"을 연구하며 quadratic form의 principal axes를 구하는 문제로 얻었다 [1]. Charles Hermite는 1855년 Cauchy의 논증을 복소수 위로 확장해, $A^*=A$인 행렬(오늘날 Hermitian이라 부른다)의 eigenvalue도 항상 실수임을 보였다 [2].

**Proposition (unitary operator의 eigenvalue는 절댓값 $1$).** $T$가 unitary이고 $Tv=\lambda v$ ($v\ne0$)이면 $\vert\lambda\vert=1$이다.

*Proof.* $\lVert v\rVert=\lVert Tv\rVert=\vert\lambda\vert\,\lVert v\rVert$이고 $\lVert v\rVert\ne0$이므로 $\vert\lambda\vert=1$이다. $\blacksquare$

**Example (normal이지만 self-adjoint도 unitary도 아님).** $$A=\begin{pmatrix}1&-1\\1&1\end{pmatrix}$$을 보자. $$AA^{\mathsf T}=A^{\mathsf T}A=\begin{pmatrix}2&0\\0&2\end{pmatrix}$$이라 $A$는 normal이지만, $A\ne A^{\mathsf T}$라 self-adjoint가 아니고 $A^{\mathsf T}A=2I\ne I$라 unitary(orthogonal)도 아니다. $A$의 eigenvalue는 characteristic polynomial $\lambda^2-2\lambda+2$의 근인 $1\pm i$로, 실수가 아니다.

**Example (normal이 아닌 행렬).** Eigenvalue and diagonalization 글에서 diagonalizable이 아니라고 본 $$\begin{pmatrix}1&1\\0&1\end{pmatrix}$$은 $$\begin{pmatrix}1&1\\0&1\end{pmatrix}\begin{pmatrix}1&0\\1&1\end{pmatrix}=\begin{pmatrix}2&1\\1&1\end{pmatrix}\ne\begin{pmatrix}1&1\\1&2\end{pmatrix}=\begin{pmatrix}1&0\\1&1\end{pmatrix}\begin{pmatrix}1&1\\0&1\end{pmatrix}$$이라 normal도 아니다.

## Schur decomposition와 복소수 spectral theorem

**Theorem (Schur Decomposition).** $V$가 유한차원 복소수 inner product space이면, 임의의 $T:V\to V$가 upper triangular로 표현되는 orthonormal basis가 존재한다. 곧 임의의 복소 정사각행렬 $A$는 $A=UBU^*$($U$는 unitary, $B$는 upper triangular)로 쓰인다.

*Proof.* $\dim V=n$에 대한 induction. $n=1$이면 자명하다. $n>1$이라 하자. $\mathbb{C}$가 대수적으로 닫혀 있으므로 $T$는 eigenvalue $\lambda$와 그 eigenvector를 가지고, 이를 정규화한 단위벡터를 $e_1$이라 하자. $e_1$을 $V$의 orthonormal basis $e_1,e_2,\dots,e_n$으로 확장하고(Gram–Schmidt), $$W:=\operatorname{span}(e_2,\dots,e_n)=e_1^\perp$$이라 하자. $P_W$를 $W$ 위로의 orthogonal projection이라 하고 $S:W\to W$, $S(w):=P_W(Tw)$로 두면, $S$는 $(n-1)$차원 복소수 inner product space $W$ 위의 operator다. induction 가정으로 $S$가 upper triangular가 되는 $W$의 orthonormal basis $f_2,\dots,f_n$이 존재한다.

$e_1,f_2,\dots,f_n$이 원하는 basis다. 이는 $e_1$과 $f_2,\dots,f_n\in W=e_1^\perp$로 이루어진 orthonormal basis다. $Te_1=\lambda e_1$이라 첫 열이 이미 upper triangular 꼴이다. $j\ge2$에서 $V=\operatorname{span}(e_1)\oplus W$가 orthogonal decomposition이므로 $$Tf_j=\langle Tf_j,e_1\rangle e_1+P_W(Tf_j)=\langle Tf_j,e_1\rangle e_1+S(f_j)$$인데, $S(f_j)$는 induction 가정으로 $f_2,\dots,f_j$만의 일차결합이므로 $Tf_j$는 $e_1,f_2,\dots,f_j$만의 일차결합이다. 곧 $T$의 행렬은 이 basis에서 upper triangular다. $\blacksquare$

이는 Cayley–Hamilton과 Jordan form 글의 Triangularizability 정리를 정밀화한 것이다. 그곳에서는 임의의 basis로 similar하게 만들었을 뿐이지만, 여기서는 그 basis를 orthonormal하게, 곧 similarity를 unitary로 골랐다.

**Lemma.** upper triangular이면서 normal인 행렬은 diagonal이다.

*Proof.* $B=(b_{ij})$가 upper triangular($i>j\Rightarrow b_{ij}=0$)이고 normal이라 하자. $$(BB^*)_{ii}=\sum_kb_{ik}\overline{b_{ik}}=\sum_{k\ge i}\vert b_{ik}\vert^2,\qquad(B^*B)_{ii}=\sum_k\overline{b_{ki}}b_{ki}=\sum_{k\le i}\vert b_{ki}\vert^2$$이고 $B$가 normal이므로 이 둘이 모든 $i$에서 같다. $i=1,\dots,n$ 순서로 "$j<i$이면 $b_{ji}=0$"임을 보이면($B$가 upper triangular라 이미 $j>i\Rightarrow b_{ji}=0$이니, 이것까지 더하면 대각 밖이 모두 $0$이라 diagonal이 된다) 된다.

$i=1$일 때 $$(B^*B)_{11}=\vert b_{11}\vert^2$$(합에 $k=1$뿐)이고 $$(BB^*)_{11}=\sum_{k\ge1}\vert b_{1k}\vert^2$$이므로, 등식에서 $b_{1k}=0$ ($k>1$)이 나온다.

$i$번째 단계에서, $j<i$인 모든 $j$에 대해 이미 $b_{jk}=0$ ($k>j$)임을 안다고 하자. 특히 $k=i>j$를 대입하면 $b_{ji}=0$ ($j<i$)이다. 그러면 $$(B^*B)_{ii}=\sum_{k\le i}\vert b_{ki}\vert^2=\vert b_{ii}\vert^2$$(합의 $k<i$ 항이 방금 본 대로 모두 $0$)이고 $$(BB^*)_{ii}=\sum_{k\ge i}\vert b_{ik}\vert^2$$이므로, 등식에서 $b_{ik}=0$ ($k>i$)이 나온다. 이로써 induction이 완성된다. $\blacksquare$

**Theorem (복소수 Spectral Theorem).** 유한차원 복소수 inner product space 위의 $T:V\to V$에 대해 다음이 동치다. (i) $T$는 normal이다. (ii) $T$는 orthonormal eigenbasis를 가진다(곧 $T=UDU^*$, $U$는 unitary, $D$는 diagonal). 특히 이때 $T$가 self-adjoint이면 $D$는 실수 성분만 가지고, $T$가 unitary이면 $D$의 대각성분은 모두 절댓값 $1$이다.

*Proof.* (ii)$\Rightarrow$(i): $T=UDU^*$이면 $T^*=UD^*U^*=U\overline{D}U^*$이고, diagonal 행렬끼리는 commute하므로 $$TT^*=UD\overline{D}U^*=U\overline{D}DU^*=T^*T$$이다.

(i)$\Rightarrow$(ii): Schur decomposition으로 $T=UBU^*$($U$는 unitary, $B$는 upper triangular)라 하자. $T$가 normal이므로 $B=U^*TU$도 normal이다($BB^*=U^*TUU^*T^*U=U^*TT^*U=U^*T^*TU=B^*B$, $U^*U=UU^*=I$를 썼다). 위 Lemma로 $B$는 diagonal이다. 곧 $T=UBU^*$가 orthonormal eigenbasis($U$의 열들)에서의 diagonalization이다.

self-adjoint·unitary의 경우는 앞 절의 Proposition(eigenvalue가 실수·절댓값 $1$)을 diagonal 성분에 그대로 적용한 것이다. $\blacksquare$

## 실수 spectral theorem: principal axis theorem

Eigenvalue and diagonalization 글에서 "real symmetric이면 eigenvalue가 모두 실수이고 eigenvector가 모두 orthogonal이라는 강력한 결과가 성립한다"고 미뤄 둔 것이 이것이다. 다만 실수 위에서는 $\mathbb{C}$처럼 대수적으로 닫혀 있지 않아 eigenvalue 자체의 존재가 자명하지 않으므로, 앞 절의 "self-adjoint의 eigenvalue는 실수"라는 사실만으로는 부족하고 실수 eigenvector의 존재를 직접 보여야 한다. 이 존재는 복소수로 확장하지 않고, 함수의 극한과 연속 글의 extreme value theorem으로 직접 얻는다.

**Theorem (실수 Spectral Theorem, Principal Axis Theorem).** $n\times n$ real symmetric matrix $A$는 orthonormal eigenbasis를 가진다. 곧 $A=QDQ^{\mathsf T}$인 orthogonal $Q$와 실수 diagonal $D$가 존재한다.

*Proof.* $n$에 대한 induction. $n=1$이면 자명하다. $n>1$이라 하자.

먼저 $A$가 (실수 범위 안에서) eigenvector를 가짐을 보인다. $$f:S^{n-1}\to\mathbb{R},\qquad f(x)=\langle Ax,x\rangle=x^{\mathsf T}Ax$$는 단위구 $$S^{n-1}=\{x\in\mathbb{R}^n:\lVert x\rVert=1\}$$ 위의 연속함수이고, $S^{n-1}$은 컴팩트이므로(Heine–Borel) extreme value theorem에 의해 $f$는 어떤 $x_0\in S^{n-1}$에서 최댓값 $\lambda_0:=f(x_0)$을 가진다.

$x_0$가 eigenvector임을 보이자. $x_0$에 orthogonal한 임의의 단위벡터 $v$에 대해 $\gamma(t):=(\cos t)x_0+(\sin t)v$는 $x_0\perp v$라 모든 $t$에서 $\lVert\gamma(t)\rVert=1$, 곧 $S^{n-1}$ 위의 경로다. $A$가 symmetric이라 $\langle Ax_0,v\rangle=\langle x_0,Av\rangle=\langle Av,x_0\rangle$이므로 $$h(t):=f(\gamma(t))=\cos^2t\,\langle Ax_0,x_0\rangle+2\sin t\cos t\,\langle Ax_0,v\rangle+\sin^2t\,\langle Av,v\rangle$$이다. $h$는 $\gamma(0)=x_0$이 $f$의 $S^{n-1}$ 위 최댓값이므로 $t=0$에서 최댓값을 가지는 실수 $1$변수 함수이고, 미분하면 $$h'(t)=-2\cos t\sin t\,\langle Ax_0,x_0\rangle+2\cos(2t)\,\langle Ax_0,v\rangle+2\sin t\cos t\,\langle Av,v\rangle$$이라 $h'(0)=2\langle Ax_0,v\rangle$이다. 내부 최댓값에서 미분은 $0$이어야 하므로(Rolle의 정리가 기대는 것과 같은 사실) $\langle Ax_0,v\rangle=0$이다.

이는 $x_0^\perp$의 모든 단위벡터 $v$, 곧 $x_0^\perp$의 모든 벡터에서 $Ax_0\perp v$라는 뜻이다. 곧 $$Ax_0\in(x_0^\perp)^\perp=\operatorname{span}(x_0)$$(Inner product space 글의 이중 orthogonal complement)이므로 $Ax_0=cx_0$인 $c$가 있고, $\langle Ax_0,x_0\rangle=\lambda_0$에 대입하면 $c=\lambda_0$이다. 곧 $Ax_0=\lambda_0x_0$로 $x_0$는 eigenvalue $\lambda_0\in\mathbb{R}$의 eigenvector다.

이제 $$W:=\operatorname{span}(x_0)^\perp$$를 보면, $w\in W$에서 $$\langle Aw,x_0\rangle=\langle w,Ax_0\rangle=\lambda_0\langle w,x_0\rangle=0$$이라 $Aw\in W$, 곧 $W$는 $A$-invariant다(Endomorphism and Perron–Frobenius 글의 용어). $A\vert_W$는 $$\langle A\vert_Ww,w'\rangle=\langle Aw,w'\rangle=\langle w,Aw'\rangle=\langle w,A\vert_Ww'\rangle$$이라 $W$ 위에서 다시 symmetric이므로, induction 가정으로 $W$가 $A\vert_W$의 orthonormal eigenbasis $x_1,\dots,x_{n-1}$을 가진다. $x_0,x_1,\dots,x_{n-1}$은 $x_0\perp W$이므로 $\mathbb{R}^n$ 전체의 orthonormal eigenbasis다. $\blacksquare$

**Example (앞 예시의 diagonalization).** Eigenvalue and diagonalization 글에서 다룬 $$A=\begin{pmatrix}2&1\\1&2\end{pmatrix}$$은 symmetric이고, eigenvector $(1,-1),(1,1)$을 정규화한 $$Q=\frac1{\sqrt2}\begin{pmatrix}1&1\\-1&1\end{pmatrix}$$이 orthogonal이라(열들이 orthonormal) $A=QDQ^{\mathsf T}$, $$D=\begin{pmatrix}1&0\\0&3\end{pmatrix}$$이다. 그때는 $P^{-1}AP$였던 것이, symmetric이라는 조건 덕에 $Q^{\mathsf T}AQ$로, 곧 역행렬을 구하는 대신 transpose만으로 대각화된다.

**Corollary (eigenspace는 서로 orthogonal하다).** $T$가 (복소수 위에서) normal이거나 (실수 위에서) symmetric이어서 앞의 두 spectral theorem 중 하나로 orthonormal eigenbasis를 가진다고 하자. $\lambda\ne\mu$이면 eigenspace $E_\lambda,E_\mu$(Eigenvalue and diagonalization 글의 표기)는 서로 orthogonal하다: $v\in E_\lambda$, $w\in E_\mu$이면 $v\perp w$. 특히 서로 다른 eigenvalue에 대한 eigenvector는 항상 orthogonal하다.

*Proof.* $e_1,\dots,e_n$을 그 orthonormal eigenbasis, $d_1,\dots,d_n$을 대응하는 eigenvalue라 하자. $v=\sum_ic_ie_i\in E_\lambda$이면 $Tv=\lambda v$에서 $\sum_ic_id_ie_i=\lambda\sum_ic_ie_i$이고, $e_i$들이 일차독립이므로 각 항에서 $c_i(d_i-\lambda)=0$, 곧 $d_i\ne\lambda$인 모든 $i$에서 $c_i=0$이다. 곧 $v$는 $d_i=\lambda$인 $e_i$들만의 일차결합이다. 같은 논증으로 $w\in E_\mu$는 $d_j=\mu$인 $e_j$들만의 일차결합인데, $\lambda\ne\mu$라 두 첨자 집합이 서로소이므로, orthonormal basis의 서로 다른 원소끼리는 orthogonal하다는 사실에서 $\langle v,w\rangle=0$이다. $\blacksquare$

이는 orthonormal eigenbasis의 존재, 곧 unitarily(실수에서는 orthogonally) similar하다는 사실 그 자체에 이미 담긴 내용이다. eigenbasis를 이루는 벡터들은 애초에 orthonormal하도록 고른 것이니 서로 orthogonal한 것이 당연하지만, 이 Corollary는 그보다 조금 더 강하다: 같은 eigenvalue 안에서 어떤 벡터를 고르든 (basis 벡터가 아니어도) 서로 다른 eigenspace에 속한 벡터는 통째로 orthogonal하다. 반면 같은 eigenvalue 안에서는 eigenvector들이 자동으로 orthogonal할 이유가 없다. eigenspace의 차원이 $2$ 이상이면 그 안의 임의의 두 벡터가 orthogonal이 아닐 수 있고, orthonormal이 되려면 Gram–Schmidt로 따로 골라야 한다.

**Remark (orthogonal matrix의 실수 표준형).** 실수 orthogonal 행렬은 실수 성분을 가진 복소수 unitary 행렬이기도 하므로 복소수 spectral theorem을 적용할 수 있지만, 그 orthonormal eigenbasis가 실수일 필요는 없다. Eigenvalue and diagonalization 글의 $90^\circ$ 회전 예시가 그렇다(eigenvalue가 $\pm i$로 복소수다). 실수 범위 안에서 orthogonal 행렬이 갖는 진짜 표준형(block-diagonal, $2\times2$ 회전 block과 $\pm1$의 조합)은 이 글의 범위를 벗어나므로 다루지 않는다.

## 참고문헌

1. Cauchy, A.-L. (1829). Sur l'équation à l'aide de laquelle on détermine les inégalités séculaires des mouvements des planètes. In *Exercices de mathématiques*, vol. 4. Paris.
2. Hermite, C. (1855). Remarque sur un théorème de M. Cauchy. *Comptes Rendus de l'Académie des Sciences*, 41, 181–183.
3. Schur, I. (1909). Über die charakteristischen Wurzeln einer linearen Substitution mit einer Anwendung auf die Theorie der Integralgleichungen. *Mathematische Annalen*, 66(4), 488–510.
