---
layout: post
title: "Bilinear forms and positive definite operator"
date: 2026-08-15
mathematicians: [Grassmann, Cholesky, Sylvester, Strang]
---

## Multilinear form

**Definition (Multilinear Form).** $k$개의 변수를 받는 $$B:\underbrace{V\times\cdots\times V}_{k}\to F$$가 각 변수마다 따로 linear이면 $k$-linear form이라 한다. bilinear form은 $k=2$인 경우다.

**Definition (Symmetric, Antisymmetric, Alternating).** $k$-linear form $B$가 임의의 permutation $\sigma\in S_k$와 임의의 $v_1,\dots,v_k$에서 $$B(v_{\sigma(1)},\dots,v_{\sigma(k)})=B(v_1,\dots,v_k)$$를 만족하면 symmetric, $$B(v_{\sigma(1)},\dots,v_{\sigma(k)})=\operatorname{sgn}(\sigma)\,B(v_1,\dots,v_k)$$를 만족하면 antisymmetric(또는 skew-symmetric)이라 한다. 어떤 $i\ne j$에서 $v_i=v_j$일 때 언제나 값이 $0$이면 alternating이라 한다. $k=2$이면 symmetric은 $B(u,w)=B(w,u)$, antisymmetric은 $B(u,w)=-B(w,u)$가 된다.

**Proposition.** alternating이면 언제나 antisymmetric이다. characteristic이 $2$가 아니면 그 역도 성립해 antisymmetric과 alternating이 같은 뜻이 되지만, characteristic이 $2$인 체에서는 antisymmetric이 symmetric과 같아져($-1=1$이므로) alternating보다 훨씬 약한 조건이 된다.

*Proof.* 임의의 permutation은 인접한 두 자리를 맞바꾸는 transposition들의 합성이므로, $i,i+1$번째 자리에만 $u,w$를 넣고 나머지 $k-2$개 자리는 고정한 경우만 보면 충분하다(이하 $B(\dots,u,w,\dots)$는 그렇게 넣은 값을 뜻한다). $$0=B(\dots,u+w,u+w,\dots)=B(\dots,u,u,\dots)+B(\dots,u,w,\dots)+B(\dots,w,u,\dots)+B(\dots,w,w,\dots)$$인데 alternating이라 양 끝 두 항이 $0$이므로 $B(\dots,u,w,\dots)=-B(\dots,w,u,\dots)$, 곧 그 두 자리를 바꾸면 sign이 뒤집힌다(characteristic과 무관하게 성립). 이것이 모든 인접한 자리에서 성립하므로 antisymmetric이다. characteristic이 $2$가 아니면 역으로, antisymmetric인 $B$에 같은 자리 두 곳에 같은 벡터 $v$를 넣으면 $B(\dots,v,v,\dots)=-B(\dots,v,v,\dots)$에서 $2B(\dots,v,v,\dots)=0$이라 $B(\dots,v,v,\dots)=0$, 곧 alternating이다. $\blacksquare$

일반 $k$-linear form에서 alternating의 힘은 $k=\dim V$일 때 가장 두드러진다.

**Theorem (determinant는 유일한 alternating $n$-linear form).** $n$차원 $V$에서 alternating $n$-linear form 전체는 $1$차원 vector space를 이룬다. $F^n$의 표준 basis에서 값이 $1$인 유일한 것이 determinant다.

[Determinant]({% post_url 2026-08-09-determinant %})에서 세운 공리, 곧 행에 대해 alternating multilinear이고 $\det I=1$이라는 것이 바로 이 정리의 다른 얼굴이다. determinant가 그 공리로 유일하게 정해진 까닭은 결국 alternating $n$-linear form 공간이 $1$차원이기 때문이며, 그 유일성은 [Determinant]({% post_url 2026-08-09-determinant %})의 Leibniz 전개 논증이 그대로 보인다.

여기서 다룬 multilinear·alternating form의 뿌리는 Hermann Grassmann이 1844년 《Die lineale Ausdehnungslehre》에서 세운 확장론이다 [1]. Grassmann은 오늘날의 vector space, 일차독립, 차원, 그리고 wedge product에 해당하는 것을 이미 담았지만, 서술이 지나치게 추상적이고 철학적이어서 당대에는 거의 읽히지 않았고 수십 년이 지나서야 제대로 평가받았다.

## Bilinear form

아래에서는 $k=2$인 경우, 곧 bilinear form $B:V\times V\to F$만 다룬다.

**Definition (Gram Matrix).** basis $v_1,\dots,v_n$에 대해 $G_{ij}=B(v_i,v_j)$로 정한 행렬 $G$를 $B$의 Gram matrix라 한다. 좌표로 쓰면 $B(u,w)=[u]^{\mathsf T}G\,[w]$이다. Gram matrix는 $B$와 basis를 고르는 순간 그 정의식만으로 바로 계산되는 값이라, non-degenerate 같은 추가 조건 없이 항상 존재한다(존재 자체는 자명하고, 아래에서 보듯 basis에 따라 바뀔 뿐이다).

**Example (부호 있는 넓이).** $\mathbb{R}^2$에서 $B(u,w)=u_1w_2-u_2w_1$은 alternating bilinear form이고 두 벡터가 이루는 평행사변형의 부호 있는 넓이를 준다. 표준 basis에서 Gram matrix는 $$\begin{pmatrix}0&1\\-1&0\end{pmatrix}$$이고, 이것이 $2\times2$ determinant다.

operator와 bilinear form은 basis 변환에서 서로 다르게 변한다.

**Proposition (congruence).** 새 basis를 열로 갖는 change-of-basis 행렬을 $P$라 하면 Gram matrix는 $G\mapsto P^{\mathsf T}GP$로 바뀐다.

*Proof.* 새 basis $v_j'=\sum_iP_{ij}v_i$에 대해 $$G'_{jl}=B(v_j',v_l')=\sum_{i,k}P_{ij}P_{kl}B(v_i,v_k)=\sum_{i,k}P_{ij}G_{ik}P_{kl}=(P^{\mathsf T}GP)_{jl}$$이다. $\blacksquare$

operator는 basis 변환에서 similarity $A\mapsto P^{-1}AP$로, bilinear form은 congruence $G\mapsto P^{\mathsf T}GP$로 변한다. $P^{-1}$과 $P^{\mathsf T}$가 다르므로 이 둘은 서로 다른 동치 관계이며, 그래서 operator의 불변량(eigenvalue)과 bilinear form의 불변량(signature, 아래 Quadratic form 절에서 정의한다)이 갈린다.

**Definition (Non-degenerate).** bilinear form $B$가 $u\mapsto B(u,\cdot)$을 $V\to V^\ast$인 injective map으로 만들면(곧 모든 $w$에서 $B(u,w)=0$이면 $u=0$이면) non-degenerate라 한다.

**Proposition.** 유한차원에서 $B$가 non-degenerate인 것은 Gram matrix $G$가 invertible인 것과 동치다.

*Proof.* $u\mapsto B(u,\cdot)$를 좌표로 옮기면 $x\mapsto x^{\mathsf T}G$(행벡터로의 대응)이다. 이 map이 injective인 것은 $x^{\mathsf T}G=0\Rightarrow x=0$, 곧 $G$가 invertible인 것과 동치다. $\blacksquare$

**Example (non-degenerate가 아닌 bilinear form).** $\mathbb{R}^2$에서 $B(u,w):=u_1w_1$(첫 좌표만 곱함)은 symmetric bilinear form이지만, $u=(0,1)\ne0$에서 모든 $w$에 대해 $B(u,w)=0$이라 non-degenerate가 아니다. 실제로 Gram matrix $$G=\begin{pmatrix}1&0\\0&0\end{pmatrix}$$은 invertible이 아니다.

두 bilinear form도 서로 간섭하지 않게 합칠 수 있다.

**Definition (Direct Sum of Bilinear Forms).** $(V_1,B_1)$, $(V_2,B_2)$에 대해 $V_1\oplus V_2$ 위에 $$(B_1\oplus B_2)\big((u_1,u_2),(w_1,w_2)\big):=B_1(u_1,w_1)+B_2(u_2,w_2)$$로 정의한 것을 $B_1$과 $B_2$의 direct sum이라 한다.

**Proposition.** $V_1,V_2$의 기저를 이어붙인 기저에서 $B_1\oplus B_2$의 Gram matrix는 $B_1,B_2$의 Gram matrix를 대각으로 놓은 block-diagonal 행렬이다. 또 $B_1\oplus B_2$가 non-degenerate인 것은 $B_1,B_2$가 둘 다 non-degenerate인 것과 동치다.

*Proof.* $(u_1,0)$과 $(0,u_2)$ 꼴의 기저 벡터에 정의를 그대로 적용하면 $$(B_1\oplus B_2)\big((u_1,0),(w_1,0)\big)=B_1(u_1,w_1),\qquad (B_1\oplus B_2)\big((0,u_2),(0,w_2)\big)=B_2(u_2,w_2)$$이고, 서로 다른 쪽을 섞으면(예: $(u_1,0)$과 $(0,w_2)$) $0$이므로 Gram matrix가 block-diagonal이다. block-diagonal 행렬이 invertible인 것은 각 block이 invertible인 것과 동치이므로, 앞 Proposition으로 non-degenerate 조건도 그대로 나뉜다. $\blacksquare$

**Definition (Left Radical, Right Radical).** bilinear form $B:V\times V\to F$에 대해 $$\{\,v\in V:B(v,w)=0\text{ for all }w\in V\,\}$$를 $B$의 left radical, $$\{\,v\in V:B(w,v)=0\text{ for all }w\in V\,\}$$를 right radical이라 한다.

일반적인 bilinear form에서는 $B(u,w)=0$이 $B(w,u)=0$을 보장하지 않아 left radical과 right radical이 서로 다른 부분공간으로 갈린다. Symmetric, antisymmetric bilinear form의 경우는 이를 보장하므로 left radical과 right radical이 같으므로 이를 그냥 radical로 정의할 수 있다. 또한 inner product의 orthogonality 개념을 symmetric, antisymmetric bilinear form에 대해 일반화 할 수 있다.

**Definition (Orthogonal, Radical).** symmetric 또는 antisymmetric bilinear form $B$에 대해 $B(u,w)=0$이면 $u\perp w$라 쓴다. subspace $W\subseteq V$에 대해 $$W^{\perp_B}:=\{\,v\in V:B(v,w)=0\text{ for all }w\in W\,\}$$를 $W$의 ($B$에 대한) orthogonal complement라 한다. radical은 이 $W$를 $V$ 자신으로 특수화한 경우, 곧 $$V^{\perp_B}=\{\,v\in V:B(v,w)=0\text{ for all }w\in V\,\}$$ 이다.

**Proposition.** $B$가 non-degenerate인 것은 radical이 $$\{0\}$$인 것과 같은 말이다.

**Theorem (차원).** 유한차원 $V$ 위에서 $B$가 non-degenerate이면, 임의의 부분공간 $W\subseteq V$에서 $$\dim W^{\perp_B}=\dim V-\dim W$$이다.

*Proof.* $\beta:V\to V^\ast$, $\beta(v):=B(v,\cdot)$로 두면 $\ker\beta$가 $B$의 radical, 곧 $$\{0\}$$이라 $\beta$는 injective이고, $\dim V^\ast=\dim V$이니(유한차원) isomorphism이다. $w\in W^{\perp_B}$인 것은 모든 $u\in W$에서 $\beta(w)(u)=B(w,u)=0$, 곧 $\beta(w)\in W^\circ$(annihilator)인 것과 같으므로 $W^{\perp_B}=\beta^{-1}(W^\circ)$이다. $\beta$가 isomorphism이므로 $\dim W^{\perp_B}=\dim W^\circ=\dim V-\dim W$이다(Annihilator Theorem, [Dual space and Riesz representation]({% post_url 2026-08-13-dual-space-and-riesz-representation %})). $\blacksquare$

inner product의 orthogonal complement와 다른 점은, 여기서는 $B$가 non-degenerate라 하더라도 $V=W\oplus W^{\perp_B}$가 보장되지 않는다는 것이다. $B(v,v)=0$인 $v\ne0$(isotropic vector라 한다)가 있으면 $W=\operatorname{span}(v)$가 자기 자신의 orthogonal complement에 들어가 버려 직합이 무너질 수 있다.

**Example (isotropic vector와 무너지는 직합).** $\mathbb{R}^2$ 위의 symmetric bilinear form $$B(x,y):=x_1y_1-x_2y_2$$를 보자(radical이 $$\{0\}$$이라 $V$ 전체에서 non-degenerate다). $W=\operatorname{span}(1,1)$을 보면 $B((1,1),(1,1))=1-1=0$이라 $v=(1,1)$이 isotropic이고, 실제로 $$W^{\perp_B}=\{(v_1,v_2):v_1-v_2=0\}=\operatorname{span}(1,1)=W$$이다. 차원은 $\dim W^{\perp_B}=1=2-1$로 위 정리에 맞지만, $$W\cap W^{\perp_B}=W\ne\{0\}$$이라 $V=W\oplus W^{\perp_B}$는 성립하지 않는다.

**Example (dot product).** $\mathbb{R}^n$의 dot product $B(u,w)=\sum_iu_iw_i$은 $G=I$인 symmetric bilinear form이다.

## Quadratic form

**Definition (Quadratic Form).** 실수 vector space $V$ 위의 symmetric bilinear form $B$에 대해 $q(v):=B(v,v)$를 $B$가 주는 quadratic form이라 한다.

basis를 고르면 $B$의 Gram matrix $A$(위 Bilinear form 절)에 대해 $$q(x)=B(x,x)=x^{\mathsf T}Ax=\sum_{i,j}A_{ij}x_ix_j$$이다. 따라서 quadratic form은 homogeneous degree $2$ polynomial이다.

**Definition (Positive Definite).** Quadratic form $B$가 모든 $v\ne0$에서 $B(v,v)>0$을 만족하면 positive definite라 한다.

**Proposition.** positive definite bilinear form은 non-degenerate다.

*Proof.* $u\ne0$이면 $B(u,u)>0\ne0$이라 $B(u,\cdot)$이 zero functional이 아니므로, $u\mapsto B(u,\cdot)$이 injective, 곧 non-degenerate다. $\blacksquare$

**Example (Inner Product).** 실수 위의 inner product의 정의(대칭성, 선형성, 양의 정부호성)는 정확히 positive definite symmetric bilinear form이며, dot product가 그 표준적인 예다.

Positive definite bilinear form $B$의 quadratic form은 기하적으로 뚜렷한 그림을 가진다. 표준 basis에서 $B$의 Gram matrix를 $A$라 하면($B$가 symmetric이므로 $A$도 symmetric이다), 표준 inner product에서 $x^{\mathsf T}x=1$이 단위구를 나타내듯이 $x^{\mathsf T}Ax=B(x,x)=1$이 그 단위구를 $A$의 eigenvalue 방향으로 늘이거나 줄인 ellipsoid가 된다.

**Proposition (Ellipsoid).** positive definite bilinear form $B$의 (표준 basis에서의) Gram matrix $A\in\mathbb{R}^{n\times n}$에 대해 $$\{x\in\mathbb{R}^n:x^{\mathsf T}Ax=1\}$$은 ellipsoid다.

*Proof.* $A$가 symmetric이므로 real spectral theorem으로 orthonormal eigenbasis $q_1,\dots,q_n$과 eigenvalue $\lambda_1,\dots,\lambda_n$을 잡을 수 있다. $\lambda_i=q_i^{\mathsf T}Aq_i=B(q_i,q_i)>0$($B$가 positive definite이므로)이라 eigenvalue는 모두 양수다. $x=\sum_ic_iq_i$로 쓰면 $$x^{\mathsf T}Ax=\sum_i\lambda_ic_i^2=1,\qquad\text{곧}\qquad\sum_i\Big(\frac{c_i}{1/\sqrt{\lambda_i}}\Big)^2=1$$인데, 이는 $q_i$가 좌표축이고 그 방향의 반지름이 $1/\sqrt{\lambda_i}$인 ellipsoid의 표준 방정식이다. $\blacksquare$

**Example (Ellipsoid).** positive definite bilinear form $B(x,y)=2x_1y_1+x_2y_2$의 Gram matrix $$A=\begin{pmatrix}2&0\\0&1\end{pmatrix}$$(eigenvalue $2,1$)에서 $x^{\mathsf T}Ax=2x_1^2+x_2^2=1$은 반지름이 $1/\sqrt2,1$인 타원이다.

eigenvalue의 부호가 섞이면 그림이 사뭇 달라진다.

**Example (Saddle).** $$A=\begin{pmatrix}1&0\\0&-1\end{pmatrix}$$(eigenvalue $1,-1$)이 주는 $q(x)=x_1^2-x_2^2$를 보자. 그래프 $z=q(x)$는 원점에서 $x_1$ 방향으로는 증가하고 $x_2$ 방향으로는 감소하는 saddle point를 가지는 hyperbolic paraboloid이고, level set $\lbrace x:q(x)=1\rbrace=\lbrace x_1^2-x_2^2=1\rbrace$은 ellipsoid 대신 hyperbola다. 이렇게 eigenvalue의 부호가 양수와 음수로 섞인 경우를 다루려면 양수·음수가 각각 몇 개인지를 basis에 무관하게 세는 개념이 필요한데, 이것이 아래에서 다룰 signature다.

## Sylvester's law of inertia

**Theorem (Sylvester's Law of Inertia, 존재).** 실수 유한차원 $V$ 위의 symmetric bilinear form $B$에 대해, $B(e_i,e_j)=0$ ($i\ne j$)이고 $$B(e_i,e_i)\in\{1,-1,0\}$$인 basis $e_1,\dots,e_n$이 존재한다.

*Proof.* $V$에 임의로 inner product를 하나 주고(예: 어떤 basis를 orthonormal로 선언), 그에 대한 $B$의 Gram matrix $G$를 생각하자(위 Bilinear form 절). $G$는 symmetric이므로 real spectral theorem으로 $G=QDQ^{\mathsf T}$($Q$ orthogonal, $D=\operatorname{diag}(\lambda_1,\dots,\lambda_n)$)이다. 위 congruence 성질로 $Q$의 열을 새 basis $f_1,\dots,f_n$로 삼으면 이 basis에서 $B$의 Gram matrix는 $Q^{\mathsf T}GQ=D$다. $\lambda_i\ne0$인 곳에서 $e_i:=f_i/\sqrt{\vert\lambda_i\vert}$로, $\lambda_i=0$인 곳에서 $e_i:=f_i$로 다시 scale하면(congruence로 $B(e_i,e_i)=\lambda_i/\vert\lambda_i\vert=\operatorname{sign}(\lambda_i)$, $\lambda_i=0$이면 $0$) 원하는 basis를 얻는다. $\blacksquare$

**Definition (Signature).** 위 정리가 주는, $B(e_i,e_j)=0$ ($i\ne j$)이고 $B(e_i,e_i)\in\lbrace 1,-1,0\rbrace $인 basis에서 $B(e_i,e_i)=1$인 개수를 $n_+$, $=-1$인 개수를 $n_-$, $=0$인 개수를 $n_0$이라 하자. 아래 정리로 $(n_+,n_-,n_0)$은 이런 basis를 어떻게 고르든 $B$에 의해서만 정해지는데, 이를 $B$의 signature(또는 inertia)라 한다.

**Theorem (Sylvester's Law of Inertia, 불변성).** signature $(n_+,n_-,n_0)$은 위 대각화 basis의 선택과 무관하게 $B$에 의해서만 결정된다.

*Proof.* 두 basis $e_1,\dots,e_n$과 $e_1',\dots,e_n'$이 모두 이런 대각형($$\{1,-1,0\}$$ 성분)을 준다고 하자. 이 basis에서 $B$의 Gram matrix는 정확히 대각성분이 $1$($n_+$개), $-1$($n_-$개), $0$($n_0$개)인 대각행렬이므로 그 rank는 $n_++n_-=n-n_0$이다. 그런데 congruence $G\mapsto P^{\mathsf T}GP$는 $P$가(change of basis 행렬이라) invertible이므로 rank를 보존한다(invertible 행렬을 양쪽에 곱해도 rank는 바뀌지 않는다는 표준적인 사실이다). 곧 어느 basis에서 계산하든 Gram matrix의 rank는 $B$ 하나로 정해지는 $\operatorname{rank}G$와 같고, 위 계산으로 $n_0=n-\operatorname{rank}G$다. 두 basis 모두 이 값을 주므로 $n_0$은 같다. $n_+=n_+'$임을 보이면 $n_++n_-=n_+'+n_-'=\operatorname{rank}G$에서 $n_-=n_-'$도 따라온다.

두 부분공간 $$P_+:=\operatorname{span}\{e_i:B(e_i,e_i)=1\}$$(차원 $n_+$), $$Z_-':=\operatorname{span}\{e_i':B(e_i',e_i')\le0\}$$(차원 $n-n_+'$)를 두자. $P_+$ 위에서는 $v\ne0\Rightarrow B(v,v)>0$이고(대각형이라 $B(v,v)=\sum c_i^2>0$), $Z_-'$ 위에서는 $B(v,v)\le0$이다(마찬가지로 대각형이라 $B(v,v)=\sum c_i^2B(e_i',e_i')\le0$).

그러면 $$P_+\cap Z_-'=\{0\}$$이다: $v$가 둘 다에 있으면 $B(v,v)>0$($v\ne0$이면)과 $B(v,v)\le0$이 동시에 성립해야 하므로 $v=0$이다. 그러므로 Grassmann dimension formula([Vector space]({% post_url 2026-08-05-vector-spaces %}))로 $$\dim P_++\dim Z_-'\le n,\qquad n_++(n-n_+')\le n,\qquad n_+\le n_+'$$이다. 역할을 바꾸면 $n_+'\le n_+$도 나와 $n_+=n_+'$이다. $\blacksquare$

**Corollary.** $B$가 positive definite인 것은 signature가 $(n,0,0)$($n_+=\dim V$)인 것과 동치다.

Sylvester는 1852년 이 정리를 "law of inertia"라는 이름으로 처음 증명했다 [3](역학에서 관성모멘트의 principal axes를 대각화하는 것과 닮은 현상이라는 데서 이런 이름을 붙였다).

이를 이용하면 symmetric matrix의 경우 signature의 정보가 pivot에 있다는 사실을 알 수 있다. 왜냐하면 symmetric matrix $A$가 $A=LDL^T$ decomposition을 가지므로 $A$와 $D$는 같은 quadratic form의 서로 다른 Gram matrix이기 때문이다. 따라서 $D$의 대각성분 중에 양수, 음수, 0의 개수가 곧 signature가 된다. 참고로 eigenvalue와 $D$의 대각성분은 일반적으로 다르지만 signature는 보존된다는 것이다.

**Example (Pivot으로 signature 계산).** $$A=\begin{pmatrix}1&3\\3&1\end{pmatrix}$$에서 첫 pivot은 $a_{11}=1$이고, 두 번째 행에서 $3\times(\text{첫 행})$을 빼면 $(0,\,1-3\cdot3)=(0,-8)$이 남아 두 번째 pivot은 $-8$이다. 양의 pivot 하나, 음의 pivot 하나이므로 signature는 $(1,1,0)$이다(실제로 eigenvalue는 $4,-2$로, 하나는 양수 하나는 음수라 같은 답을 준다).

**Example (Minkowski form).** 위 Bilinear form 절에서 본 $\mathbb{R}^2$의 $B(x,y)=x_1y_1-x_2y_2$는 이미 대각형이라 signature가 $(1,1,0)$이다. 표준 basis를 어떻게 바꿔도(회전, scaling 등) 양의 대각성분 하나와 음의 대각성분 하나로만 대각화된다는 것이 Sylvester's Law가 주는 정보다.

**Example (다른 basis에서 시작해도 signature는 같다).** $\mathbb{R}^2$에서 $B$의 표준 basis에 대한 Gram matrix가 $$G=\begin{pmatrix}1&2\\2&1\end{pmatrix}$$이라 하자. eigenvalue는 $3,-1$이라 signature는 $(1,1,0)$이다. 실제로 basis를 $f_1=(1,1)$, $f_2=(1,-1)$로 바꾸면 $$B(f_1,f_1)=1+2+2+1=6,\quad B(f_2,f_2)=1-2-2+1=-2,\quad B(f_1,f_2)=1-2+2-1=0$$이라(직접 $x^{\mathsf T}Gy$로 계산) 이미 대각형이고, $e_1=f_1/\sqrt6$, $e_2=f_2/\sqrt2$로 다시 scale하면 $B(e_1,e_1)=1$, $B(e_2,e_2)=-1$로 signature $(1,1,0)$이 다시 확인된다.

## Positive definite operator

**Definition (Positive Semidefinite, Positive Definite).** self-adjoint $T:V\to V$가 모든 $v$에서 $\langle Tv,v\rangle\ge0$이면 positive semidefinite, 모든 $v\ne0$에서 $\langle Tv,v\rangle>0$이면 positive definite라 한다.

사실 complex vector space에 대해서는 $T$가 self-adjoint라는 조건은 생략 가능하다. 왜냐하면 모든 $v$에서 $\langle Tv,v\rangle\ge0$라는 조건 자체가 $T$가 self-adjoint인 것을 보장하기 때문이다. 이는 아래 두개의 proposition 때문이다.

**Proposition.** $V$가 복소수 inner product space이면, 임의의 linear operator $S:V\to V$(self-adjoint일 필요가 없다)에 대해 모든 $v\in V$에서 $\langle Sv,v\rangle=0$이면 $S=0$이다. $V$가 실수 inner product space이면, 이 결론에는 $S$가 self-adjoint라는 가정이 반드시 필요하다.

*Proof.* $B(v,w):=\langle Sv,w\rangle$로 두자. 가정은 모든 $v$에서 $B(v,v)=0$이라는 것이다. $$0=B(v+w,v+w)=B(v,v)+B(w,w)+B(v,w)+B(w,v)=B(v,w)+B(w,v)$$가 모든 $v,w$에서 성립한다.

복소수 위에서는 $w$ 대신 $iw$를 넣어 $$0=B(v+iw,v+iw)=B(v,v)+B(iw,iw)+B(v,iw)+B(iw,v)$$를 계산하면, $B(v,iw)=\langle Sv,iw\rangle=\bar i\langle Sv,w\rangle=-iB(v,w)$이고 $B(iw,v)=\langle S(iw),v\rangle=iB(w,v)$이므로 $0=-iB(v,w)+iB(w,v)$, 곧 $B(w,v)=B(v,w)$다. 이를 앞 식 $B(v,w)+B(w,v)=0$에 넣으면 $2B(v,w)=0$이라 $B(v,w)=0$이 모든 $v,w$에서 성립하고, $v$를 고정하면 $\langle Sv,w\rangle=0$이 모든 $w$에서 성립하므로 $Sv=0$, 곧 $S=0$이다(self-adjoint를 전혀 쓰지 않았다).

실수 위에서는 $i$가 없어 두 번째 식을 얻을 수 없고, $B(v,w)+B(w,v)=0$만으로는 $B(v,w)=0$이 나오지 않는다(antisymmetric인 $B$는 애초에 이 식을 자동으로 만족하기 때문이다. 아래 Example 참고). $S$가 self-adjoint라는 가정을 추가하면 $$B(v,w)=\langle Sv,w\rangle=\langle v,Sw\rangle=\langle Sw,v\rangle=B(w,v)$$(실수라 켤레가 없다)이고, 이를 $B(v,w)+B(w,v)=0$에 넣으면 $2B(v,w)=0$이라 $B(v,w)=0$이 나와 위와 같이 $S=0$이다. $\blacksquare$

**Proposition.** 복소수 inner product space에서 linear map $T$가 모든 $v$에서 $\langle Tv,v\rangle\in\mathbb{R}$이면 $T$는 self-adjoint다.

*Proof.* $\langle Tv,v\rangle\in\mathbb{R}$은 $\langle Tv,v\rangle=\overline{\langle Tv,v\rangle}=\langle v,Tv\rangle$, 곧 $\langle(T-T^\ast)v,v\rangle=0$이 모든 $v$에서 성립한다는 것과 같다. 위 Proposition(복소수의 경우, self-adjoint 가정 없이 성립하는 버전)으로 $T-T^\ast=0$, 곧 $T=T^\ast$다. $\blacksquare$

한편 real vector space에 대해서는 $T$가 self-adjoint라는 가정이 꼭 필요하다.

**Example (self-adjoint 가정이 실수에서는 필수).** $\mathbb{R}^2$에서 $90^\circ$ 회전 $$S=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$$은 $\langle Sv,v\rangle=v_1(-v_2)+v_2v_1=0$이 모든 $v$에서 성립하지만(antisymmetric이면 언제나 그렇다) $S^{\mathsf T}=-S\ne S$라 self-adjoint가 아니고 $S\ne0$이다.

**Remark (bilinear form과의 관계).** Real vector space 사이의 self-adjoint $T$에 대해서 $B(v,w):=\langle Tv,w\rangle$로 두면 $B$는 symmetric bilinear form이고 $T$가 positive (semi)definite인 것은 정확히 이 $B$가 위 Quadratic form 절에서 정의한 positive (semi)definite bilinear form인 것과 같은 말이다.

**Remark (inner product를 주는 positive definite operator).** $T$가 positive definite이면 $\langle u,v\rangle_T:=\langle Tu,v\rangle$는 $V$ 위의 새로운 inner product다. 켤레대칭성 $\langle u,v\rangle_T=\langle Tu,v\rangle=\langle u,Tv\rangle=\overline{\langle Tv,u\rangle}=\overline{\langle v,u\rangle_T}$은 $T$가 self-adjoint라는 데서, 첫 인수 선형성은 $T$가 linear라는 데서, 양의 정부호성은 $T$가 positive definite라는 데서 바로 나온다. 표준 inner product 자체가 $T=I$(positive definite)인 특수한 경우다. Real vector space의 경우, $B(u,w)=\langle Tu,w\rangle$는 symmetric bilinear form이므로 bilinear form 개념에서 정의한 orthogonality가 여기에 그대로 이어진다: $B(u,w)=0$인 $u\perp w$는 정확히 $\langle u,w\rangle_T=0$, 곧 이 새 inner product $\langle\cdot,\cdot\rangle_T$에서의 orthogonality와 같은 말이다.

## Positive definite matrix

Positive definite $T$의 행렬 표현을 $A$라고 하자. 이 때 positive definite operator가 만족하는 조건을 행렬로 표현하면 $x^\ast Ax > 0$이 된다 (실수에서는 $x^{\mathsf T}Ax$). 이로부터 다음과 같은 definition이 나온다.

**Definition (Positive (Semi)Definite Matrix).** Hermitian 행렬 $A\in\mathbb{C}^{n\times n}$가 모든 $x\ne0$에서 $x^\ast Ax>0$을 만족하면 positive definite, $x^\ast Ax\ge0$을 만족하면 positive semidefinite라 한다.

Real vector space 버전은 다음과 같다.

**Definition (Positive (Semi)Definite Matrix).** Symmetric 행렬 $A\in\mathbb{R}^{n\times n}$가 모든 $x\ne0$에서 $x^T Ax>0$을 만족하면 positive definite, $x^T Ax\ge0$을 만족하면 positive semidefinite라 한다.


**Proposition (Hermitian 행렬의 LDU).** Hermitian $A$가 행 교환 없이 $A=LDU'$로 분해되면 $U'=L^\ast$이고 $D$는 실수 대각이다. 곧 $A=LDL^\ast$.

*Proof.* $A=A^\ast$이므로 $$LDU'=A=A^\ast=(LDU')^\ast=U'^\ast D^\ast L^\ast=U'^\ast\overline DL^\ast$$인데 $U'^\ast$는 unit lower triangular, $L^\ast$는 unit upper triangular이므로 이 역시 $A$의 LDU 분해다. [Gaussian elimination]({% post_url 2026-08-07-gaussian-elimination %})의 LDU 분해의 유일성으로 $L=U'^\ast$(곧 $U'=L^\ast$)이고 $D=\overline D$(곧 $D$는 실수 대각)다. $\blacksquare$

**Theorem (Positive Definite 행렬의 여섯 동치조건).** Hermitian $A\in\mathbb{C}^{n\times n}$(실수에서는 symmetric)에 대해 다음이 모두 동치다.

- (a) $A$는 positive definite다.
- (b) $A$의 모든 eigenvalue가 $>0$이다.
- (c) $A$의 모든 leading principal minor $\det A_k$($k=1,\dots,n$; $A_k$는 왼쪽 위 $k\times k$ 부분행렬)가 $>0$이다.
- (d) $A$를 행 교환 없이 소거했을 때 나오는 pivot이 모두 $>0$이다.
- (e) $A=R^\ast R$인 full column rank $R\in\mathbb{C}^{m\times n}$이 존재한다.
- (f) $A=B^2$인 positive definite Hermitian $B$가 유일하게 존재한다.

*Proof.* (a)$\Leftrightarrow$(b): (복소수) spectral theorem 또는 (실수) principal axis theorem으로 orthonormal eigenbasis $e_1,\dots,e_n$과 (실수) eigenvalue $\lambda_1,\dots,\lambda_n$을 잡으면 $x=\sum_ic_ie_i$에서 $$x^\ast Ax=\sum_i\lambda_i\vert c_i\vert^2$$이다. 이것이 모든 $x\ne0$에서 $>0$인 것은(각 $e_i$를 넣어 보면 필요조건, 위 식이 충분조건) 모든 $\lambda_i>0$인 것과 동치다.

(d)$\Leftrightarrow$(c): [Gaussian elimination]({% post_url 2026-08-07-gaussian-elimination %})의 LDU decomposition $A=LDU'$($L,U'$은 unit triangular, $D=\operatorname{diag}(d_1,\dots,d_n)$이 pivot)을 앞 $k$개 행·열로 block 분할하면, $L$이 lower triangular이고 $U'$이 upper triangular라 곱의 왼쪽 위 $k\times k$ block은 각 block의 왼쪽 위 $k\times k$ 부분끼리의 곱, 곧 $A_k=L_kD_kU_k'$이다($L_k,U_k'$은 크기 $k$의 unit triangular). $\det L_k=\det U_k'=1$이므로 $$\det A_k=\det D_k=d_1d_2\cdots d_k,$$ 곧 $d_k=\det A_k/\det A_{k-1}$($\det A_0:=1$)이다. 이 비율 공식으로 모든 $d_k>0$인 것과 모든 $\det A_k>0$인 것이 서로를 강제하며 동치다.

(b)$\Rightarrow$(c): eigenvalue가 모두 양수라 하자. $x\in\mathbb{C}^k$(실수에서는 $\mathbb R^k$), $x\ne0$이면 $(x,0)\in\mathbb{C}^n$도 $\ne0$이라 $$x^\ast A_kx=(x,0)^\ast A(x,0)>0$$이므로 $A_k$도 positive definite이고(principal submatrix라 $A_k$도 Hermitian), 위 (a)$\Leftrightarrow$(b)로 $A_k$의 eigenvalue도 모두 양수이니 $\det A_k=\prod_i\lambda_i(A_k)>0$이다([Eigenvalue and diagonalization]({% post_url 2026-08-10-eigenvalue-and-diagonalization %}); $A_k$가 Hermitian이라 $\det A_k$는 실수이므로 이 부등호가 의미를 가진다).

(c)$\Rightarrow$(a): $\det A_k\ne0$(실제로 $>0$)이 매 단계 유지되어 소거가 행 교환 없이 끝까지 진행되므로 $A=LDU'$을 얻는다. $A$가 Hermitian이므로 위 Proposition(Hermitian 행렬의 LDU)로 $U'=L^\ast$이고 $D$는 실수 대각, 곧 pivot이 모두 실수다. $x\ne0$에서 $y:=L^\ast x\ne0$($L^\ast$가 invertible)이므로 $$x^\ast Ax=x^\ast LDL^\ast x=y^\ast Dy=\sum_id_i\vert y_i\vert^2>0$$이다(위에서 본 대로 모든 $d_i>0$).

(a)$\Leftrightarrow$(e): $R$이 full column rank면 $x\ne0\Rightarrow Rx\ne0$이라 $x^\ast Ax=\lVert Rx\rVert^2>0$이다. 역으로 $A$가 positive definite이면 spectral theorem으로 $A=UDU^\ast$($U$ unitary, $D=\operatorname{diag}(\lambda_i)$, $\lambda_i>0$)라 하고 $$R:=U\operatorname{diag}(\sqrt{\lambda_1},\dots,\sqrt{\lambda_n})U^\ast$$로 두면 $R$은 Hermitian이고 $R^2=U\operatorname{diag}(\lambda_i)U^\ast=A$이며, $R$의 eigenvalue $\sqrt{\lambda_i}>0$이라 $R$은 invertible, 곧 (정사각 invertible 행렬은 항상 full column rank이므로) $R$은 full column rank이고 $R^\ast R=R^2=A$($R$이 Hermitian)다.

(b)$\Rightarrow$(f): 같은 eigenbasis에서 $$B:=U\operatorname{diag}(\sqrt{\lambda_1},\dots,\sqrt{\lambda_n})U^\ast$$로 두면 $B$는 eigenvalue가 모두 $\sqrt{\lambda_i}>0$인 Hermitian, 곧 positive definite이며 $B^2=A$다.

유일성: $B,B'$이 둘 다 $A$의 positive definite Hermitian square root라 하자. $BA=BB^2=B^3=B^2B=AB$이므로 $B$는 $A$와 commute하고, 마찬가지로 $B'$도 $A$와 commute한다. commute하는 Hermitian 행렬은 서로의 eigenspace를 보존하므로([Cayley–Hamilton and Jordan form]({% post_url 2026-08-12-cayley-hamilton-and-jordan-form %})의 Simultaneous Diagonalization Corollary와 같은 논증) $B$는 $A$의 eigenspace $E_\lambda$를 보존하고, 그 위에서 $B^2=\lambda I$를 만족하는 positive definite Hermitian이므로 eigenvalue가 $\sqrt\lambda$ 하나뿐이라 $B\vert_{E_\lambda}=\sqrt\lambda\,I$다. 같은 논증이 $B'$에도 적용되어 $B'\vert_{E_\lambda}=\sqrt\lambda\,I=B\vert_{E_\lambda}$이고, $A$의 eigenspace들이 전체 공간을 생성하므로 $B=B'$이다. 이 유일한 $B$를 $\sqrt A$라 쓴다.

(f)$\Rightarrow$(a): $B$가 positive definite Hermitian이면 $x\ne0$일 때 $B$가 invertible(eigenvalue가 모두 $>0$)이라 $Bx\ne0$이므로 $$x^\ast Ax=x^\ast B^2x=x^\ast B^\ast Bx=\lVert Bx\rVert^2>0$$이다($B^\ast=B$). $\blacksquare$

**Example ($B=\sqrt A$ 계산).** $$A=\begin{pmatrix}5&3\\3&5\end{pmatrix}$$을 보자. trace $10$, determinant $16$에서 특성방정식 $\lambda^2-10\lambda+16=0$을 풀면 eigenvalue $8,2$이고, 대응하는 eigenvector는 $\frac1{\sqrt2}(1,1)$, $\frac1{\sqrt2}(1,-1)$이다. $$U:=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$$(대칭이라 $U=U^{\mathsf T}$)로 두면 $$B=U\begin{pmatrix}\sqrt8&0\\0&\sqrt2\end{pmatrix}U^{\mathsf T}=\frac1{\sqrt2}\begin{pmatrix}3&1\\1&3\end{pmatrix}$$이고, 직접 $$B^2=\frac12\begin{pmatrix}3&1\\1&3\end{pmatrix}\begin{pmatrix}3&1\\1&3\end{pmatrix}=\frac12\begin{pmatrix}10&6\\6&10\end{pmatrix}=\begin{pmatrix}5&3\\3&5\end{pmatrix}=A$$로 확인된다.

**Remark ($R$의 비유일성).** (e)의 $R$은 유일하지 않다. $A=R^\ast R=(QR)^\ast(QR)$이 임의의 unitary $Q$에서 성립하므로 $R$을 unitary만큼 바꿔도 같은 $A$를 준다. 위 Example의 $B$ 자체도 (e)의 $R$로 유효한 선택이지만($R^\ast R=B^2=A$), 앞서 나온 $90^\circ$ 회전 $$Q=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$$을 곱한 $$R:=QB=\frac1{\sqrt2}\begin{pmatrix}-1&-3\\3&1\end{pmatrix}$$도 $R^{\mathsf T}R=B^{\mathsf T}Q^{\mathsf T}QB=B^2=A$를 만족하는 또 다른 선택이다. $R\ne B$이므로 (e)의 $R$은 정말로 유일하지 않다. 이는 (f)의 $B$가 유일한 것과 대조적이다: (f)의 $B$는 그중에서도 positive definite(Hermitian이며 eigenvalue가 양수)라는 훨씬 강한 조건까지 만족해야 하므로, unitary 궤도 $\lbrace QB:Q\text{ unitary}\rbrace$ 안에서 유일하게 결정된다.

이 여섯 조건 중 (a)(b)(c)(d)(e) 다섯 개를 나란히 놓는 방식은 Gilbert Strang의 선형대수학 교재에서 널리 알려졌다. 다만 Strang의 교재에서는 Positive semidefinite의 경우에는 가볍게 넘어간다. 이 포스트에서는 좀 더 자세히 파보자.

**Remark (Positive Semidefinite로 바꾸면).** 다음 다섯 조건은 그대로 등호·유일성 조건만 완화하면 된다.

- (a) 모든 $x$에서 $x^\ast Ax\ge0$
- (b) eigenvalue가 모두 $\ge0$
- (d) 행 교환 없이 소거했을 때 나오는 pivot이 모두 $\ge0$
- (e) $A=R^\ast R$($R$이 full column rank일 필요가 없다)
- (f) $A=B^2$인 positive semidefinite Hermitian $B$가 유일하게 존재한다(유일성 증명은 위와 똑같이 통하고, eigenvalue가 $0$인 곳은 $\sqrt0=0$으로 자연스럽게 들어간다)

(d)는 사실 생각해볼 부분이 있다. pivot이 0인 것을 허용하기 때문에 $A=LDL^\ast$를 계산하는 알고리즘에서 어떤 pivot이 0이 나왔을 때 그 아래 성분을 소거할 수 있는지에 대한 의문이 남는 것이다. 하지만 다음 사실 덕분에 positive semidefinite인 $A$에서는 이런 상황 자체가 일어나지 않는다.

**Proposition.** $A$가 positive semidefinite이고 $a_{ii}=0$이면 $i$번째 행·열 전체가 $0$이다.

*Proof.* 임의의 $j$와 실수 $t$에서 $x:=e_i+te_j$로 두면 $a_{ii}=0$에서 $$0\le x^{\mathsf T}Ax=2ta_{ij}+t^2a_{jj}$$인데, $t\to0$ 근방에서는 일차항 $2ta_{ij}$가 지배적이므로 $a_{ij}\ne0$이면 $t$의 부호를 $a_{ij}$와 반대로 잡아 우변을 음수로 만들 수 있어 모순이다(Hermitian인 경우도 $t$ 대신 적절한 복소수 $s=t\overline{a_{ij}}/\vert a_{ij}\vert$를 넣으면 같은 논증이 통한다). 따라서 $a_{ij}=0$이다. $\blacksquare$

**Example.** $$A=\begin{pmatrix}0&0\\0&1\end{pmatrix}$$에서 $a_{11}=0$이지만 그 아래 $a_{21}=0$이 이미 성립하므로(위 Proposition이 예측하는 대로) 나눗셈 자체가 필요 없다. pivot을 $0$으로 두고 바로 다음 열로 넘어가 pivot $1$을 얻으면, permutation 없이 자연스러운 순서 그대로 pivot $0,1$을 얻는다.

(c)는 사정이 다르다. leading principal minor가 모두 $\ge0$인 것만으로는 부족하다. $$A=\begin{pmatrix}0&0\\0&-1\end{pmatrix}$$은 두 leading principal minor가 각각 $0,0$으로 모두 $\ge0$이지만 eigenvalue $-1<0$이라 positive semidefinite가 아니다. 올바른 조건은 leading이 아니라 모든 principal minor가 $\ge0$인 것이다. 여기서 principal minor란, 지표 집합 $\lbrace1,\dots,n\rbrace$의 공집합이 아닌 부분집합 $S$를 하나 골라 그 $S$에 속한 행·열만 남긴 $\vert S\vert\times\vert S\vert$ 부분행렬 $A_S$의 determinant를 뜻한다(모두 $2^n-1$개이고, leading principal minor는 $S=\lbrace1,\dots,k\rbrace$인 특수한 경우다). 예컨대 $$A=\begin{pmatrix}1&1&0\\1&1&0\\0&0&-1\end{pmatrix}$$은 leading principal minor $\det A_1=1,\det A_2=0,\det A_3=0$이 모두 $\ge0$이지만, leading이 아닌 $S=\lbrace1,3\rbrace$을 고르면 $$A_S=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad\det A_S=-1<0$$이라(실제로 이 $A$는 eigenvalue $2,0,-1$을 가져 positive semidefinite가 아니다) leading이 아닌 principal minor까지 모두 확인해야 함을 보여준다.

## Cholesky decomposition

**Theorem (Cholesky Decomposition).** positive definite Hermitian $A\in\mathbb{C}^{n\times n}$(실수에서는 symmetric)은 $A=LL^\ast$($L$은 대각성분이 양의 실수인 lower triangular)로 유일하게 decompose된다.

*Proof.* $A$가 positive definite이므로 위 (a)$\Rightarrow$(d)로 $A$는 행 교환 없이 소거되어 $A=LDU'$이 되고, 위 Proposition(Hermitian 행렬의 LDU)로 $U'=L^\ast$이고 $D$가 실수 대각이라 $A=LDL^\ast$를 얻으며, 모든 pivot이 $d_i>0$(실수)이다. $$L':=L\cdot\operatorname{diag}(\sqrt{d_1},\dots,\sqrt{d_n})$$(곧 $L$의 $i$번째 열을 $\sqrt{d_i}$배, $d_i$가 실수 양수라 $\sqrt{d_i}$도 실수)로 두면 $L'$은 대각성분이 $\sqrt{d_i}>0$인 lower triangular이고 $$L'L'^\ast=L\operatorname{diag}(d_1,\dots,d_n)L^\ast=LDL^\ast=A$$이다.

유일성. $L''$이 대각성분이 양의 실수인 또 다른 lower triangular이고 $L''L''^\ast=A$라 하자. $\tilde L$을 $L''$의 각 열을 그 대각성분으로 나눈(unit lower triangular) 행렬, $$\tilde D:=\operatorname{diag}(L''_{11},\dots,L''_{nn})$$(대각성분이 양의 실수)이라 하면 $L''=\tilde L\tilde D$이므로 $$A=L''L''^\ast=\tilde L\tilde D^2\tilde L^\ast$$인데, 이는 $A$의 또 다른 $LDU$ 분해($\tilde D^2$이 대각, $\tilde L,\tilde L^\ast$가 unit triangular)이므로 유일성으로 $\tilde L=L$, $\tilde D^2=D$다. $\tilde D$의 대각성분이 양의 실수이므로 $\tilde D=\operatorname{diag}(\sqrt{d_1},\dots,\sqrt{d_n})$로 유일하게 정해지고, 곧 $L''=\tilde L\tilde D=L'$이다. $\blacksquare$

앞서 (e)의 $R$은 유일하지 않다고 했지만, $R$을 정사각 lower triangular(대각성분이 양의 실수)로 제한하면 유일해진다는 것이 바로 위 Theorem이 보여주는 내용이다.

**Example (Cholesky 계산).** $$A=\begin{pmatrix}4&2\\2&3\end{pmatrix}$$을 보자. 행 교환 없이 소거하면 pivot $d_1=a_{11}=4$이고, multiplier $m=2/4=\frac12$로 두 번째 행이 $(2,3)-\frac12(4,2)=(0,2)$가 되어 pivot $d_2=2$다. 곧 $$L=\begin{pmatrix}1&0\\\frac12&1\end{pmatrix},\qquad D=\begin{pmatrix}4&0\\0&2\end{pmatrix}$$이고, 위 증명대로 $L$의 열을 $\sqrt{d_1}=2,\ \sqrt{d_2}=\sqrt2$로 rescale하면 $$L'=\begin{pmatrix}2&0\\1&\sqrt2\end{pmatrix},\qquad L'L'^{\mathsf T}=\begin{pmatrix}4&2\\2&1+2\end{pmatrix}=\begin{pmatrix}4&2\\2&3\end{pmatrix}=A$$로 확인된다.

이 decomposition은 André-Louis Cholesky가 프랑스 육군의 측지학(geodesy) 업무 중 최소제곱 문제를 풀며 고안했다. Cholesky는 1918년 제1차 세계대전에서 전사했고, 생전에 이를 출판하지 않아 동료 장교 Benoit가 1924년 유고를 정리해 대신 발표했다 [2].

## 참고문헌

1. Grassmann, H. (1844). *Die lineale Ausdehnungslehre, ein neuer Zweig der Mathematik*. Leipzig: Otto Wigand.
2. Benoit, Commandant. (1924). Note sur une méthode de résolution des équations normales... (procédé du Commandant Cholesky). *Bulletin Géodésique*, 2, 67–77.
3. Sylvester, J. J. (1852). A demonstration of the theorem that every homogeneous quadratic polynomial is reducible by real orthogonal substitutions to the form of a sum of positive and negative squares. *Philosophical Magazine, Series 4*, 4(23), 138–142.
