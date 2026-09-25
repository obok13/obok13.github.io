---
layout: post
title: "Adjoint operator and the spectral theorem"
date: 2026-08-14
mathematicians: [Cauchy, Hermite, Schur]
---

## Adjoint operator

**Theorem, Definition (Adjoint).** $V,W$가 같은 체 위의 유한차원 inner product space이고 $T:V\to W$가 linear map이면, $$\langle Tv,w\rangle_W=\langle v,T^*w\rangle_V\quad\text{for all }v\in V,\,w\in W$$를 만족하는 linear map $T^\ast :W\to V$가 유일하게 존재한다. 이를 $T$의 adjoint라 한다.

*Proof.* 각 $w\in W$를 고정하면 $v\mapsto\langle Tv,w\rangle_W$는 $V$ 위의 linear functional이므로, Riesz Representation으로 이를 $\langle v,T^\ast w\rangle_V$로 나타내는 $T^\ast w\in V$가 유일하게 정해진다(이로써 함수 $T^\ast :W\to V$가 well-defined). $T^\ast $가 linear임은 $$\langle v,T^*(aw+bw')\rangle_V=\langle Tv,aw+bw'\rangle_W=\bar a\langle Tv,w\rangle_W+\bar b\langle Tv,w'\rangle_W=\langle v,aT^*w+bT^*w'\rangle_V$$가 모든 $v$에서 성립하므로 Riesz Representation의 유일성으로 $T^\ast (aw+bw')=aT^\ast w+bT^\ast w'$이기 때문이다. $T^\ast $의 유일성은, 두 후보 $S,S'$가 모든 $v,w$에서 $\langle v,Sw\rangle=\langle v,S'w\rangle$을 만족하면 Riesz Representation의 유일성으로 $Sw=S'w$가 모든 $w$에서 성립하는 데서 나온다. $\blacksquare$

**Proposition (adjoint의 성질).** $(S+T)^\ast =S^\ast +T^\ast $, $(cT)^\ast =\bar cT^\ast $, $(T^\ast )^\ast =T$, 합성 가능할 때 $(ST)^\ast =T^\ast S^\ast $, $I^\ast =I$, 그리고 $T$가 invertible이면 $(T^{-1})^\ast =(T^\ast )^{-1}$이다.

*Proof.* 앞 네 식은 정의식 $\langle Tv,w\rangle=\langle v,T^\ast w\rangle$을 정리하고 Riesz Representation의 유일성을 쓰면 나온다. 예컨대 $(T^\ast )^\ast =T$는, 정의식의 양변에 켤레를 취하면 $\langle w,Tv\rangle_W=\langle T^\ast w,v\rangle_V$인데 이것이 정확히 "$T^\ast $의 adjoint는 $T$다"라는 식이므로 유일성으로 나온다. 나머지도 같은 방식이다. $I^\ast =I$는 $\langle Iv,w\rangle=\langle v,w\rangle=\langle v,Iw\rangle$에서 유일성으로 나온다. $T$가 invertible이면 $(T^{-1})^\ast T^\ast =(TT^{-1})^\ast =I^\ast =I$이고 $T^\ast (T^{-1})^\ast =(T^{-1}T)^\ast =I$이므로($(ST)^\ast =T^\ast S^\ast $를 적용) $(T^{-1})^\ast =(T^\ast )^{-1}$이다. $\blacksquare$

**Theorem.** $\ker T^\ast =(\operatorname{im}T)^{\perp}$이고 $\operatorname{im}T^\ast =(\ker T)^{\perp}$이다.

*Proof.* $w\in\ker T^\ast \iff\langle v,T^\ast w\rangle_V=0\text{ for all }v\iff\langle Tv,w\rangle_W=0\text{ for all }v\iff w\in(\operatorname{im}T)^{\perp}$이라 첫 식이 나온다. 둘째 식은, $v\in\ker T$이면 임의의 $w$에서 $\langle v,T^\ast w\rangle_V=\langle Tv,w\rangle_W=0$이라 $\operatorname{im}T^\ast \subseteq(\ker T)^{\perp}$이고, 첫 식(orthogonal decomposition)으로 $$\dim\operatorname{im}T^*=\dim W-\dim\ker T^*=\dim W-\dim(\operatorname{im}T)^{\perp}=\dim\operatorname{im}T$$이며 rank–nullity로 $$\dim(\ker T)^{\perp}=\dim V-\dim\ker T=\operatorname{rank}T=\dim\operatorname{im}T$$로 같은 차원이라 포함이 등식이 된다. $\blacksquare$

**Corollary.** $\operatorname{rank}T^\ast =\operatorname{rank}T$다. $T$가 injective이면 $T^\ast $는 surjective이고, $T$가 surjective이면 $T^\ast $는 injective다.

*Proof.* $\dim\ker T^\ast =\dim(\operatorname{im}T)^{\perp}=\dim W-\dim\operatorname{im}T=\dim W-\operatorname{rank}T$이고, $T^\ast $에 rank-nullity를 적용하면 $\dim W=\operatorname{rank}T^\ast +\dim\ker T^\ast =\operatorname{rank}T^\ast +(\dim W-\operatorname{rank}T)$이므로 $\operatorname{rank}T^\ast =\operatorname{rank}T$다. $T$가 injective이면 $\ker T=\lbrace 0\rbrace $이라 $(\ker T)^{\perp}=V$이고 위 정리로 $\operatorname{im}T^\ast =(\ker T)^{\perp}=V$이니 $T^\ast $가 surjective다. $T$가 surjective이면 $\operatorname{im}T=W$라 $(\operatorname{im}T)^{\perp}=\lbrace 0\rbrace $이고 위 정리로 $\ker T^\ast =(\operatorname{im}T)^{\perp}=\lbrace 0\rbrace $이니 $T^\ast $가 injective다. $\blacksquare$

위 성질들은 모두 dual map의 성질과 유사하다. 이는 우연이 아니며 둘 사이에는 다음과 같은 관계가 있다.

**Proposition.** $T^\ast =R_V^{-1}\circ T^t\circ R_W$.

*Proof.* $R_W(w)=\langle\cdot,w\rangle_W$이므로 $T^t(R_W(w))(v)=R_W(w)(Tv)=\langle Tv,w\rangle_W=\langle v,T^\ast w\rangle_V=R_V(T^\ast w)(v)$이고, 이는 $T^t(R_W(w))=R_V(T^\ast w)$라는 뜻이다. $\blacksquare$

곧 adjoint는 dual map을 Riesz map으로 원래 공간 $V,W$ 위에 옮겨 읽은 것이다. Real vector space에서는 $R$이 진짜 linear isomorphism이라 성질이 완전히 똑같지만 complex vector space에서는 $R$이 conjugate-linear라 옮기는 과정에서 스칼라 곱마다 conjugate가 하나씩 끼어든다. 예를 들어 dual map에서 $(cT)^t=cT^t$였던 것이 adjoint에서는 $(cT)^\ast =\bar cT^\ast $가 되고, 행렬의 transpose $A^{\mathsf T}$가 conjugate transpose $\overline A^{\mathsf T}$가 된다.

**Proposition (행렬 표현).** $V,W$의 orthonormal basis에서 $T$의 행렬이 $A$이면, 같은 orthonormal basis에서 $T^\ast $의 행렬은 $A^\ast :=\overline{A}^{\mathsf T}$(conjugate transpose, 실수에서는 $A^{\mathsf T}$)이다.

*Proof.* orthonormal basis $e_1,\dots,e_n$($V$), $f_1,\dots,f_m$($W$)에서 $A_{ij}=\langle Te_j,f_i\rangle_W$이다(Inner product space 글에서 본 대로, orthonormal basis에 대한 전개 계수는 그 basis와의 inner product다). $T^\ast $의 행렬 성분은 $$(A^*)_{ij}=\langle T^*f_j,e_i\rangle_V=\overline{\langle e_i,T^*f_j\rangle_V}=\overline{\langle Te_i,f_j\rangle_W}=\overline{A_{ji}}$$이다. $\blacksquare$

한 가지 걸리는 점은, dual map의 행렬 공식은 $V,W$의 아무 basis와 그 dual basis에 대해 성립하지만 adjoint에 대해서는 basis가 orthonormal이어야 한다는 것이다. 이유는 다음과 같다. Dual map $T^t:W^\ast \to V^\ast $는 원래 공간과 그 dual space 사이의 map이므로, $V,W$에 basis를 잡으면 dual basis가 자동으로 따라와서 행렬 공식에 쓰인다. 반면 adjoint $T^\ast :W\to V$는 원래 공간끼리의 map이라 따로 딸려오는 dual basis가 없고, $V,W$에 잡은 basis를 도메인과 코도메인 양쪽에 그대로 써서 행렬을 표현해야 한다. 그런데 $T^\ast =R_V^{-1}\circ T^t\circ R_W$이므로, 이 행렬이 dual map의 행렬(transpose)과 맞아떨어지려면 Riesz isomorphism $R$이 그 basis를 정확히 그 dual basis로 보내주어야 한다. 즉 $$R(v_i)(v_j)=\langle v_j,v_i\rangle=\delta_{ij}=v_i^\ast (v_j)$$가 모든 $i,j$에서 성립해 $R(v_i)=v_i^\ast $가 되어야 하는데, 이는 정확히 $$\{v_i\}$$가 orthonormal이라는 뜻이다. 이 경우 $T^t$가 $A$의 $i$번째 행을 그대로 골라 옮겨준 것이 곧 $T^\ast $의 행렬이 된다.

**Proposition (adjoint의 eigenvalue·trace·determinant).** $V=W$(같은 유한차원 inner product space)일 때, $\lambda$가 $T^\ast $의 eigenvalue인 것은 $\bar\lambda$가 $T$의 eigenvalue인 것과 동치이고, $$\operatorname{tr}(T^*)=\overline{\operatorname{tr}T},\qquad\det(T^*)=\overline{\det T}$$이다.

*Proof.* orthonormal basis에서 $T$의 행렬을 $A$라 하면 $T^\ast $의 행렬은 $A^\ast =\overline A^{\mathsf T}$다. determinant는 Leibniz formula로 성분의 polynomial이라 conjugate와 교환되고($\det\overline M=\overline{\det M}$) transpose에는 불변이므로(Determinant 글) $$p_{T^*}(\lambda)=\det(A^*-\lambda I)=\det\big(\overline{A-\bar\lambda I}\big)^{\mathsf T}=\overline{\det(A-\bar\lambda I)}=\overline{p_T(\bar\lambda)}$$이다. 곧 $p_{T^\ast }(\lambda)=0\iff p_T(\bar\lambda)=0$이라 $\lambda$가 $T^\ast $의 eigenvalue인 것은 $\bar\lambda$가 $T$의 eigenvalue인 것과 동치다. 이 식에 $\lambda=0$을 넣으면 $\det(A^\ast )=\overline{\det A}$이고, 양변을 $\lambda$의 polynomial로 보아 $\lambda^{n-1}$의 계수를 비교하면(Eigenvalue and diagonalization 글의 trace–eigenvalue 관계) $\operatorname{tr}(A^\ast )=\overline{\operatorname{tr}A}$다. $\blacksquare$

**Example (adjoint 계산).** $T:\mathbb{R}^3\to\mathbb{R}^2$, $T(x,y,z)=(x+y,\,y+z)$의 (표준 basis, 곧 orthonormal basis에서의) 행렬은 $$A=\begin{pmatrix}1&1&0\\0&1&1\end{pmatrix}$$이므로 $T^\ast :\mathbb{R}^2\to\mathbb{R}^3$의 행렬은 $$A^{\mathsf T}=\begin{pmatrix}1&0\\1&1\\0&1\end{pmatrix},\qquad T^*(a,b)=(a,\,a+b,\,b)$$이다. 실제로 정의식을 확인해보면 $$\langle T(x,y,z),(a,b)\rangle=(x+y)a+(y+z)b=ax+ay+by+bz$$이고 $$\langle (x,y,z),T^\ast (a,b)\rangle=\langle(x,y,z),(a,a+b,b)\rangle=xa+y(a+b)+zb=ax+ay+by+bz$$로 서로 같다.

## Self-adjoint operator

이제부터는 $T:V\to V$, 곧 하나의 inner product space에서 자기 자신으로 가는 operator만 본다.

**Definition (Self-adjoint).** $T^\ast =T$이면 self-adjoint(실수에서는 symmetric, 복소수에서는 Hermitian)라 한다.

**Proposition (행렬로 옮기면).** orthonormal basis에서 $T$의 행렬이 $A$이면(앞 절의 행렬 표현 Proposition으로 $T^\ast $의 행렬은 $A^\ast $다), $T$가 self-adjoint인 것은 $A^\ast =A$(실수에서는 $A^{\mathsf T}=A$인 symmetric matrix)인 것과 동치다.

**Corollary (self-adjoint operator의 eigenvalue는 실수).** $T^\ast =T$이고 $Tv=\lambda v$ ($v\ne0$)이면 $\lambda\in\mathbb{R}$이다.

*Proof.* $$\lambda\langle v,v\rangle=\langle Tv,v\rangle=\langle v,T^*v\rangle=\langle v,Tv\rangle=\bar\lambda\langle v,v\rangle$$이고 $v\ne0$이라 $\langle v,v\rangle\ne0$이므로 $\lambda=\bar\lambda$, 곧 $\lambda$는 실수다. $\blacksquare$

**Corollary.** real symmetric matrix(곧 $A^{\mathsf T}=A$인 실수 행렬 $A$)의 eigenvalue는 모두 실수다.

이 사실을 real symmetric matrix에 처음 증명한 것은 Augustin-Louis Cauchy로, 1829년 행성 운동의 장기섭동을 다루는 "secular equation"을 연구하며 quadratic form의 principal axes를 구하는 문제로 얻었다 [1]. Charles Hermite는 1855년 Cauchy의 논증을 복소수 위로 확장해, $A^\ast =A$인 행렬(오늘날 Hermitian이라 부른다)의 eigenvalue도 항상 실수임을 보였다 [2].

## Unitary operator

**Definition (Unitary).** $T^\ast T=TT^\ast =I$이면 unitary(실수에서는 orthogonal)라 한다.

**Proposition (행렬로 옮기면).** orthonormal basis에서 $T$의 행렬이 $A$이면(Adjoint operator 절의 행렬 표현 Proposition으로 $T^\ast $의 행렬은 $A^\ast $다), $T$가 unitary인 것은 $A^\ast A=AA^\ast =I$(실수에서는 $A^{\mathsf T}A=I$인 orthogonal matrix)인 것과 동치다.

**Proposition (unitary는 inner product를 보존).** $T^\ast T=I$인 것은 모든 $v,v'$에서 $\langle Tv,Tv'\rangle=\langle v,v'\rangle$인 것과 동치다. 특히 unitary operator는 norm을 보존한다: $\lVert Tv\rVert=\lVert v\rVert$.

*Proof.* $\langle Tv,Tv'\rangle=\langle v,T^\ast Tv'\rangle$이므로 $T^\ast T=I$이면 $\langle Tv,Tv'\rangle=\langle v,v'\rangle$이다. 역으로 이것이 모든 $v,v'$에서 성립하면 $\langle v,(T^\ast T-I)v'\rangle=0$이 모든 $v,v'$에서 성립하고, $v=(T^\ast T-I)v'$을 넣으면 $\lVert(T^\ast T-I)v'\rVert^2=0$이 모든 $v'$에서 성립해 $T^\ast T=I$다. $v=v'$을 넣으면 norm 보존이 나온다. $\blacksquare$

**Corollary (unitary operator의 eigenvalue는 절댓값 $1$).** $T$가 unitary이고 $Tv=\lambda v$ ($v\ne0$)이면 $\vert\lambda\vert=1$이다.

*Proof.* $\lVert v\rVert=\lVert Tv\rVert=\vert\lambda\vert\,\lVert v\rVert$이고 $\lVert v\rVert\ne0$이므로 $\vert\lambda\vert=1$이다. $\blacksquare$

## Normal operator

**Definition (Normal).** $TT^\ast =T^\ast T$이면 normal이라 한다.

**Proposition.** self-adjoint와 unitary는 모두 normal이다(각각 $T^\ast =T$, $T^\ast T=TT^\ast =I$에서 자명하다).

**Proposition (행렬로 옮기면).** orthonormal basis에서 $T$의 행렬이 $A$이면(Adjoint operator 절의 행렬 표현 Proposition으로 $T^\ast $의 행렬은 $A^\ast $다), $T$가 normal인 것은 $AA^\ast =A^\ast A$인 것과 동치다.

**Proposition (normal operator의 특성화).** $T$가 normal인 것은 모든 $v\in V$에서 $\lVert Tv\rVert=\lVert T^\ast v\rVert$인 것과 동치다.

*Proof.* $(T^\ast )^\ast =T$이므로 $$\lVert Tv\rVert^2=\langle v,T^\ast Tv\rangle,\qquad\lVert T^\ast v\rVert^2=\langle T^\ast v,T^\ast v\rangle=\langle v,TT^\ast v\rangle$$이다. $T$가 normal이면 $T^\ast T=TT^\ast $이므로 두 값이 같다.

역으로 모든 $v$에서 $\lVert Tv\rVert=\lVert T^\ast v\rVert$라 하자. $S:=T^\ast T-TT^\ast $로 두면 $$S^\ast =(T^\ast T)^\ast -(TT^\ast )^\ast =T^\ast T-TT^\ast =S$$라 $S$는 self-adjoint이고, $$\langle Sv,v\rangle=\langle T^\ast Tv,v\rangle-\langle TT^\ast v,v\rangle=\lVert Tv\rVert^2-\lVert T^\ast v\rVert^2=0$$이 모든 $v$에서 성립한다. $S$가 self-adjoint이므로 $$0=\langle S(v+w),v+w\rangle=\langle Sv,w\rangle+\langle Sw,v\rangle=\langle Sv,w\rangle+\overline{\langle Sv,w\rangle}=2\operatorname{Re}\langle Sv,w\rangle$$이 모든 $v,w$에서 성립하고, 복소수 위에서는 $w$ 대신 $iw$를 넣은 같은 계산으로 $\operatorname{Im}\langle Sv,w\rangle=0$도 나와(실수 위에서는 $\langle Sv,w\rangle$가 이미 실수이므로 $\operatorname{Re}\langle Sv,w\rangle=0$만으로 충분하다) $\langle Sv,w\rangle=0$이 모든 $v,w$에서 성립하므로 $Sv=0$, 곧 $S=0$, 곧 $T^\ast T=TT^\ast $다. $\blacksquare$

**Corollary.** $T$가 normal이면 $\ker T=\ker T^\ast $이고, Adjoint operator 절의 Theorem($\ker T^\ast =(\operatorname{im}T)^{\perp}$)과 결합하면 $\ker T=(\operatorname{im}T)^{\perp}$, 곧 $V=\operatorname{im}T\oplus\ker T$가 orthogonal decomposition이다.

*Proof.* 위 Proposition에서 $Tv=0\iff\lVert Tv\rVert=0\iff\lVert T^\ast v\rVert=0\iff T^\ast v=0$이므로 $\ker T=\ker T^\ast $다. $\blacksquare$

**Corollary (normal operator의 eigenvector).** $T$가 normal이고 $Tv=\lambda v$이면 $T^\ast v=\bar\lambda v$다.

*Proof.* $T-\lambda I$도 normal이다: $$(T-\lambda I)(T-\lambda I)^\ast =TT^\ast -\bar\lambda T-\lambda T^\ast +\vert\lambda\vert^2I=(T-\lambda I)^\ast (T-\lambda I)$$이 $T^\ast T=TT^\ast $에서 나온다. $Tv=\lambda v$이면 $(T-\lambda I)v=0$이므로 위 Corollary를 $T-\lambda I$에 적용하면 $(T-\lambda I)^\ast v=(T^\ast -\bar\lambda I)v=0$, 곧 $T^\ast v=\bar\lambda v$다. $\blacksquare$

**Example (normal이지만 self-adjoint도 unitary도 아님).** $$A=\begin{pmatrix}1&-1\\1&1\end{pmatrix}$$을 보자. $$AA^{\mathsf T}=A^{\mathsf T}A=\begin{pmatrix}2&0\\0&2\end{pmatrix}$$이라 $A$는 normal이지만, $A\ne A^{\mathsf T}$라 self-adjoint가 아니고 $A^{\mathsf T}A=2I\ne I$라 unitary(orthogonal)도 아니다. $A$의 eigenvalue는 characteristic polynomial $\lambda^2-2\lambda+2$의 근인 $1\pm i$로, 실수가 아니다.

**Example (normal이 아닌 행렬).** Eigenvalue and diagonalization 글에서 diagonalizable이 아니라고 본 $$\begin{pmatrix}1&1\\0&1\end{pmatrix}$$은 $$\begin{pmatrix}1&1\\0&1\end{pmatrix}\begin{pmatrix}1&0\\1&1\end{pmatrix}=\begin{pmatrix}2&1\\1&1\end{pmatrix}\ne\begin{pmatrix}1&1\\1&2\end{pmatrix}=\begin{pmatrix}1&0\\1&1\end{pmatrix}\begin{pmatrix}1&1\\0&1\end{pmatrix}$$이라 normal도 아니다.

## Schur decomposition와 복소수 spectral theorem

**Theorem (Schur Decomposition).** $V$가 유한차원 복소수 inner product space이면, 임의의 $T:V\to V$가 upper triangular로 표현되는 orthonormal basis가 존재한다. 곧 임의의 복소 정사각행렬 $A$는 $A=UBU^\ast $($U$는 unitary, $B$는 upper triangular)로 쓰인다.

*Proof.* $\dim V=n$에 대한 induction. $n=1$이면 자명하다. $n>1$이라 하자. $\mathbb{C}$가 대수적으로 닫혀 있으므로 $T$는 eigenvalue $\lambda$와 그 eigenvector를 가지고, 이를 정규화한 단위벡터를 $e_1$이라 하자. $e_1$을 $V$의 orthonormal basis $e_1,e_2,\dots,e_n$으로 확장하고(Gram–Schmidt), $$W:=\operatorname{span}(e_2,\dots,e_n)=e_1^\perp$$이라 하자. $P_W$를 $W$ 위로의 orthogonal projection이라 하고 $S:W\to W$, $S(w):=P_W(Tw)$로 두면, $S$는 $(n-1)$차원 복소수 inner product space $W$ 위의 operator다. induction 가정으로 $S$가 upper triangular가 되는 $W$의 orthonormal basis $f_2,\dots,f_n$이 존재한다.

$e_1,f_2,\dots,f_n$이 원하는 basis다. 이는 $e_1$과 $f_2,\dots,f_n\in W=e_1^\perp$로 이루어진 orthonormal basis다. $Te_1=\lambda e_1$이라 첫 열이 이미 upper triangular 꼴이다. $j\ge2$에서 $V=\operatorname{span}(e_1)\oplus W$가 orthogonal decomposition이므로 $$Tf_j=\langle Tf_j,e_1\rangle e_1+P_W(Tf_j)=\langle Tf_j,e_1\rangle e_1+S(f_j)$$인데, $S(f_j)$는 induction 가정으로 $f_2,\dots,f_j$만의 일차결합이므로 $Tf_j$는 $e_1,f_2,\dots,f_j$만의 일차결합이다. 곧 $T$의 행렬은 이 basis에서 upper triangular다. $\blacksquare$

이는 [Cayley–Hamilton and Jordan form]({% post_url 2026-08-12-cayley-hamilton-and-jordan-form %})의 Triangularizability 정리를 정밀화한 것이다. 그곳에서는 임의의 basis로 similar하게 만들었을 뿐이지만, 여기서는 그 basis를 orthonormal하게, 곧 similarity를 unitary로 골랐다. 이 정밀화는 Issai Schur가 1909년 적분방정식(integral equation) 이론에 응용하며 증명했다 [3].

**Lemma.** upper triangular이면서 normal인 행렬은 diagonal이다.

*Proof.* $B=(b_{ij})$가 standard orthonormal basis $e_1,\dots,e_n$에서 upper triangular($i>j\Rightarrow b_{ij}=0$)이고 normal이라 하자. $n$에 대한 induction. $n=1$이면 자명하다. $n>1$이라 하자.

Upper triangular이므로 $Be_1=b_{11}e_1$, 곧 $e_1$은 $B$의 eigenvector다. 앞 절의 Corollary(normal operator의 eigenvector)로 $B^\ast e_1=\overline{b_{11}}e_1$인데, $B^\ast e_1$의 $e_j$ 성분은 $$(B^\ast )_{j1}=\overline{b_{1j}}$$이므로 $j>1$에서 $\overline{b_{1j}}=0$, 곧 $b_{1j}=0$이다. 곧 $B$의 첫 번째 행도(upper triangular라 첫 번째 열은 이미 대각성분 제외 $0$이니) 대각성분 제외 모두 $0$이다.

이제 $$W:=\operatorname{span}(e_2,\dots,e_n)=e_1^\perp$$로 두자. $j\ge2$에서 $Be_j$의 $e_1$ 성분이 $b_{1j}=0$이라 $B(W)\subseteq W$이고, $B^\ast e_j$의 $e_1$ 성분도 $$(B^\ast )_{1j}=\overline{b_{j1}}=0$$($j\ge2$에서 upper triangular로 $b_{j1}=0$)이라 $B^\ast (W)\subseteq W$다. 곧 $\operatorname{span}(e_1)$과 $W$ 둘 다 $B,B^\ast $ 양쪽에 invariant하므로 $W$ 위에서 $(B\vert_W)^\ast =B^\ast \vert_W$이고, $$B\vert_W(B\vert_W)^\ast =BB^\ast \vert_W=B^\ast B\vert_W=(B\vert_W)^\ast (B\vert_W)$$라 $B\vert_W$도 normal이다. $B\vert_W$는 $e_2,\dots,e_n$에서 여전히 upper triangular이므로 induction 가정으로 diagonal이고, $B$의 첫 행·첫 열은 이미 대각성분만 남았으므로 $B$ 전체가 diagonal이다. $\blacksquare$

**Theorem (복소수 Spectral Theorem).** 유한차원 복소수 inner product space 위의 $T:V\to V$에 대해 다음이 동치다.

- (i) $T$는 normal이다.
- (ii) $T$는 orthonormal eigenbasis를 가진다(곧 $T=UDU^\ast $, $U$는 unitary, $D$는 diagonal).

*Proof.* (ii)$\Rightarrow$(i): $T=UDU^\ast $이면 $T^\ast =UD^\ast U^\ast =U\overline{D}U^\ast $이고, diagonal 행렬끼리는 commute하므로 $$TT^*=UD\overline{D}U^*=U\overline{D}DU^*=T^*T$$이다.

(i)$\Rightarrow$(ii): Schur decomposition으로 $T=UBU^\ast $($U$는 unitary, $B$는 upper triangular)라 하자. $T$가 normal이므로 $B=U^\ast TU$도 normal이다($BB^\ast =U^\ast TUU^\ast T^\ast U=U^\ast TT^\ast U=U^\ast T^\ast TU=B^\ast B$, $U^\ast U=UU^\ast =I$를 썼다). 위 Lemma로 $B$는 diagonal이다. 곧 $T=UBU^\ast $가 orthonormal eigenbasis($U$의 열들)에서의 diagonalization이다. $\blacksquare$

**Corollary (Spectral Decomposition).** 위 diagonalization $T=UDU^\ast $에서 $U$의 $i$번째 열을 $v_i$, 대응하는 diagonal 성분(곧 eigenvalue)을 $\lambda_i$라 하면 $$T=\sum_{i=1}^n\lambda_iv_iv_i^\ast $$이다. 여기서 $v_iv_i^\ast $는 $x\mapsto\langle x,v_i\rangle v_i$로 작동하는 연산자, 곧 $\operatorname{span}(v_i)$ 위로의 orthogonal projection이다. 곧 normal operator는 서로 orthogonal한 rank $1$ projection들을 eigenvalue로 가중합한 것이다.

*Proof.* $U=[v_1\,\vert\,\cdots\,\vert\,v_n]$, $D=\operatorname{diag}(\lambda_1,\dots,\lambda_n)$이므로 $UD=[\lambda_1v_1\,\vert\,\cdots\,\vert\,\lambda_nv_n]$이고 $U^\ast $의 $i$번째 행이 $v_i^\ast $이므로, 행렬곱 $(UD)U^\ast $의 $(p,q)$ 성분은 $$\sum_i\lambda_i(v_i)_p\overline{(v_i)_q}$$로 $\sum_i\lambda_iv_iv_i^\ast $의 $(p,q)$ 성분과 같다. $\blacksquare$

## 실수 spectral theorem: principal axis theorem

Real symmetric matrix는 self-adjoint이므로 복소수 spectral theorem에 의해서 eigenvalue가 real이라는 사실이 바로 나온다. Eigenvector의 성분도 real인데 이는 real matrix의 real eigenvalue에 대한 eigenvector이기 때문이다. 이런 결론은 real symmetric matrix를 complex scalar에서 해석한 결과이다. 아래에서는 scalar field를 real로 한정해서 증명하는 방법을 소개한다.

**Theorem (실수 Spectral Theorem, Principal Axis Theorem).** $n\times n$ real symmetric matrix $A$는 orthonormal eigenbasis를 가진다. 곧 $A=QDQ^{\mathsf T}$인 orthogonal $Q$와 실수 diagonal $D$가 존재한다.

*Proof.* $n$에 대한 induction. $n=1$이면 자명하다. $n>1$이라 하자.

먼저 $A$가 (실수 범위 안에서) eigenvector를 가짐을 보인다. $$f:S^{n-1}\to\mathbb{R},\qquad f(x)=\langle Ax,x\rangle=x^{\mathsf T}Ax$$는 단위구 $$S^{n-1}=\{x\in\mathbb{R}^n:\lVert x\rVert=1\}$$ 위의 연속함수이고, $S^{n-1}$은 컴팩트이므로(Heine–Borel) extreme value theorem에 의해 $f$는 어떤 $x_0\in S^{n-1}$에서 최댓값 $\lambda_0:=f(x_0)$을 가진다.

$x_0$가 eigenvector임을 보이자. $x_0$에 orthogonal한 임의의 단위벡터 $v$에 대해 $\gamma(t):=(\cos t)x_0+(\sin t)v$는 $x_0\perp v$라 모든 $t$에서 $\lVert\gamma(t)\rVert=1$, 곧 $S^{n-1}$ 위의 경로다. $A$가 symmetric이라 $\langle Ax_0,v\rangle=\langle x_0,Av\rangle=\langle Av,x_0\rangle$이므로 $$h(t):=f(\gamma(t))=\cos^2t\,\langle Ax_0,x_0\rangle+2\sin t\cos t\,\langle Ax_0,v\rangle+\sin^2t\,\langle Av,v\rangle$$이다. $h$는 $\gamma(0)=x_0$이 $f$의 $S^{n-1}$ 위 최댓값이므로 $t=0$에서 최댓값을 가지는 실수 $1$변수 함수이고, 미분하면 $$h'(t)=-2\cos t\sin t\,\langle Ax_0,x_0\rangle+2\cos(2t)\,\langle Ax_0,v\rangle+2\sin t\cos t\,\langle Av,v\rangle$$이라 $h'(0)=2\langle Ax_0,v\rangle$이다. 내부 최댓값에서 미분은 $0$이어야 하므로(Rolle의 정리가 기대는 것과 같은 사실) $\langle Ax_0,v\rangle=0$이다.

이는 $x_0^\perp$의 모든 단위벡터 $v$, 곧 $x_0^\perp$의 모든 벡터에서 $Ax_0\perp v$라는 뜻이다. 곧 $$Ax_0\in(x_0^\perp)^\perp=\operatorname{span}(x_0)$$(Inner product space 글의 이중 orthogonal complement)이므로 $Ax_0=cx_0$인 $c$가 있고, $\langle Ax_0,x_0\rangle=\lambda_0$에 대입하면 $c=\lambda_0$이다. 곧 $Ax_0=\lambda_0x_0$로 $x_0$는 eigenvalue $\lambda_0\in\mathbb{R}$의 eigenvector다.

이제 $$W:=\operatorname{span}(x_0)^\perp$$를 보면, $w\in W$에서 $$\langle Aw,x_0\rangle=\langle w,Ax_0\rangle=\lambda_0\langle w,x_0\rangle=0$$이라 $Aw\in W$, 곧 $W$는 $A$-invariant다(Endomorphism and Perron–Frobenius 글의 용어). $A\vert_W$는 $$\langle A\vert_Ww,w'\rangle=\langle Aw,w'\rangle=\langle w,Aw'\rangle=\langle w,A\vert_Ww'\rangle$$이라 $W$ 위에서 다시 symmetric이므로, induction 가정으로 $W$가 $A\vert_W$의 orthonormal eigenbasis $x_1,\dots,x_{n-1}$을 가진다. $x_0,x_1,\dots,x_{n-1}$은 $x_0\perp W$이므로 $\mathbb{R}^n$ 전체의 orthonormal eigenbasis다. $\blacksquare$

**Example (앞 예시의 diagonalization).** Eigenvalue and diagonalization 글에서 다룬 $$A=\begin{pmatrix}2&1\\1&2\end{pmatrix}$$은 symmetric이고, eigenvector $(1,-1),(1,1)$을 정규화한 $$Q=\frac1{\sqrt2}\begin{pmatrix}1&1\\-1&1\end{pmatrix}$$이 orthogonal이라(열들이 orthonormal) $A=QDQ^{\mathsf T}$, $$D=\begin{pmatrix}1&0\\0&3\end{pmatrix}$$이다. 그때는 $P^{-1}AP$였던 것이, symmetric이라는 조건 덕에 $Q^{\mathsf T}AQ$로, 곧 역행렬을 구하는 대신 transpose만으로 대각화된다.

## 참고문헌

1. Cauchy, A.-L. (1829). Sur l'équation à l'aide de laquelle on détermine les inégalités séculaires des mouvements des planètes. In *Exercices de mathématiques*, vol. 4. Paris.
2. Hermite, C. (1855). Remarque sur un théorème de M. Cauchy. *Comptes Rendus de l'Académie des Sciences*, 41, 181–183.
3. Schur, I. (1909). Über die charakteristischen Wurzeln einer linearen Substitution mit einer Anwendung auf die Theorie der Integralgleichungen. *Mathematische Annalen*, 66(4), 488–510.
