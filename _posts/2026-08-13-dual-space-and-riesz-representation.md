---
layout: post
title: "Dual space and Riesz representation"
date: 2026-08-13
mathematicians: [Eilenberg, Mac Lane, Riesz, Fréchet, Erdős, Kaplansky]
---

## Dual space

**Definition (Dual Space).** vector space $V$에서 스칼라 $F$로 가는 linear map을 linear functional이라 하고, 그 전체 $$V^*:=\{\,\varphi:V\to F \text{ linear}\,\}=\mathcal{L}(V,F)$$를 $V$의 dual space라 한다. $V^\ast $는 pointwise 연산으로 vector space다.

엄밀히는 여기서 정의한 $V^\ast $를 algebraic dual이라고 하고 vector space에 toplogy 구조를 주게 되면 algebraic 대신 continuous linear functional만 모은 continuous dual을 생각하는 것이 일반적이다. Finite dimension에서는 모든 linear functional이 연속이지만 infinite dimension에서는 다르기 때문에 continuous dual이 algebraic dual보다 훨씬 작다.

**Example (좌표 뽑기).** $\mathbb{R}^n$에서 $i$번째 좌표를 뽑는 $x\mapsto x_i$는 linear functional이다.

**Example (한 점에서의 값매김).** $\mathbb{R}[x]$에서 한 점 $c$에서 값매김하는 $p\mapsto p(c)$는 linear functional이다.

**Example (정적분).** $\mathbb{R}[x]$에서 정적분 $p\mapsto\int_0^1 p$는 linear functional이다.

**Definition, Theorem (Dual Basis).** $V$가 유한차원이고 basis가 $v_1,\dots,v_n$일 때 $$v_i^*(v_j)=\delta_{ij}$$로 정한 $v_i^\ast \in V^\ast $들을 dual basis라 한다. 이들은 $V^\ast $의 basis를 이루며 특히 $\dim V^\ast =\dim V$이다.

*Proof.* $\varphi\in V^\ast $에 대해 $\varphi(v_j)=c_j$라 하면 $\varphi$와 $\sum_ic_iv_i^\ast $가 모든 $v_j$에서 값이 같아($\sum_ic_iv_i^\ast (v_j)=c_j$) linear map으로서 같다. 따라서 $v_i^\ast $들이 $V^\ast $를 생성한다. 또 $\sum_ic_iv_i^\ast =0$이면 $v_j$를 넣어 $c_j=0$이니 일차독립이다. $\blacksquare$

위와 같이 $V$와 $V^\ast$ 사이의 대응을 생각하려면 basis를 하나 골라야 한다. 또 다른 방법으로는 inner product를 하나 고정하면, basis 선택 없이도 $V$와 $V^\ast $를 잇는 대응이 생긴다.

고정된 $u\in V$에 대해 $v\mapsto\langle v,u\rangle$은 (첫 인수에 대한 선형성으로) $V$ 위의 linear functional이다. 이 대응을 $$R:V\to V^*,\qquad R(u):=\langle\cdot,u\rangle$$이라 쓰자.

**Theorem (Riesz Representation, 유한차원).** $V$가 유한차원 inner product space이면, 임의의 $\varphi\in V^\ast $에 대해 $$\varphi(v)=\langle v,u\rangle\quad\text{for all }v\in V$$를 만족하는 $u\in V$가 유일하게 존재한다. 곧 $R:V\to V^\ast $는 전단사다.

*Proof.* $e_1,\dots,e_n$을 $V$의 orthonormal basis라 하자(Gram–Schmidt로 존재, Inner product space 글). $u:=\sum_i\overline{\varphi(e_i)}\,e_i$로 두면, $v=\sum_ic_ie_i$ ($c_i=\langle v,e_i\rangle$)에 대해 $$\langle v,u\rangle=\sum_ic_i\,\overline{\overline{\varphi(e_i)}}=\sum_ic_i\varphi(e_i)=\varphi\Big(\sum_ic_ie_i\Big)=\varphi(v)$$이다(둘째 등호는 $\langle e_i,e_j\rangle=\delta_{ij}$와 둘째 인수의 켤레선형성, 넷째 등호는 $\varphi$의 선형성). 존재가 보였다. 유일성은, $\langle v,u\rangle=\langle v,u'\rangle$이 모든 $v$에서 성립하면 $v=u-u'$을 넣어 $\lVert u-u'\rVert^2=0$, 곧 $u=u'$이기 때문이다. $\blacksquare$

이 정리는 Frigyes Riesz와 Maurice Fréchet가 1907년 각자 독립적으로, $L^2$ 위의 연속 linear functional이 inner product로 표현된다는 것을 보인 데서 이름을 얻었다 [1][2]. 여기서 다룬 것은 그 유한차원 축소판이고, 완비성과 연속성이 걸린 진짜 정리는 함수해석 글에서 Hilbert space에 대해 다시 다룬다.

**Proposition.** $R:V\to V^\ast $는 전단사이고, 실수 위에서는 linear isomorphism이지만 복소수 위에서는 conjugate-linear($R(au+bu')=\bar aR(u)+\bar bR(u')$)이다.

*Proof.* 전단사는 위 정리 그 자체다(존재가 surjective를, 유일성이 $R(u)=R(u')\Rightarrow u=u'$인 injective를 준다: 실제로 $R(u)=0$이면 $\langle v,u\rangle=0$이 모든 $v$에서 성립하고 특히 $v=u$에서 $\lVert u\rVert^2=0$이라 $u=0$이다). $R(au+bu')(v)=\langle v,au+bu'\rangle=\bar a\langle v,u\rangle+\bar b\langle v,u'\rangle$은 둘째 인수의 켤레선형성에서 바로 나온다. $\blacksquare$

**Example (좌표).** $\mathbb{R}^n$의 dot product에서, 좌표 functional $\varphi(x)=\sum_ia_ix_i$의 Riesz representative는 $u=(a_1,\dots,a_n)$ 그 자체다.

**Example (trace).** $n\times n$ 실행렬 공간에 Frobenius inner product $\langle A,B\rangle:=\operatorname{tr}(B^{\mathsf T}A)$를 주자. trace functional $\varphi(A)=\operatorname{tr}A$의 Riesz representative는 항등행렬 $I$다. 실제로 $\langle A,I\rangle=\operatorname{tr}(I^{\mathsf T}A)=\operatorname{tr}A=\varphi(A)$이다.

무한차원에서는 위와 같은 일대일 대응이 존재하지 않는다.

**Example (무한차원에서 무너지는 것).** $V=\mathbb{R}[x]$는 basis $1,x,x^2,\dots$가 가산이다. 각 $x^k$에 대한 계수 뽑기 $e_k^\ast $들은 여전히 일차독립이지만 $V^\ast $를 생성하지는 못한다. 예컨대 모든 계수를 더하는 functional $\varphi:\sum_ka_kx^k\mapsto\sum_ka_k$(유한합이라 잘 정의됨)는 어떤 $e_k^\ast $들의 유한 일차결합으로도 표현되지 않는다.

사실 이는 우연이 아니라 일반적인 현상이다: $V$가 무한차원이면 $V^\ast $는 basis 하나로는 결코 따라잡을 수 없을 만큼 커진다.

**Theorem (Erdős–Kaplansky).** $V$가 field $F$ 위의 무한차원 vector space이고 $B$가 그 basis이면 $$\dim V^\ast =\vert F\vert^{\vert B\vert}$$이고, Cantor's theorem($\vert F\vert\ge2$이므로 $\vert F\vert^{\vert B\vert}\ge2^{\vert B\vert}>\vert B\vert$)에 의해 이는 언제나 $\dim V=\vert B\vert$보다 (cardinality로서) 진짜로 크다. 곧 유한차원에서 성립한 Dual Basis 정리의 $\dim V^\ast =\dim V$는 무한차원에서는 등호는커녕 방향 자체가 뒤집힌다.

$B$에서 $F$로 가는 임의의 함수가 $B$가 basis라는 사실 덕에 유일하게 $V$ 위의 linear functional로 확장되므로, $V^\ast $가 (집합으로서) $F^B$와 일대일 대응한다는 것까지는 어렵지 않다. 하지만 이로부터 $\dim V^\ast $ 자체가 정확히 $\vert F\vert^{\vert B\vert}$라는 cardinal과 같다는 것을 보이려면 무한 cardinal에 대한 조합론적 논증이 더 필요하다 [4].

## Dual of direct sum

**Theorem (Dual of a Finite Direct Sum).** $$(V_1\oplus V_2)^*\;\cong\;V_1^*\oplus V_2^*.$$ 구체적으로 $\varphi\mapsto(\varphi\vert_{V_1},\varphi\vert_{V_2})$가 그 isomorphism이다.

*Proof.* 이 대응이 linear임은 분명하다. injective: $\varphi\vert_{V_1}=0$, $\varphi\vert_{V_2}=0$이면 $V=V_1\oplus V_2$의 임의의 $v=v_1+v_2$에서 $\varphi(v)=\varphi(v_1)+\varphi(v_2)=0$이라 $\varphi=0$이다. surjective: 임의의 $(\varphi_1,\varphi_2)\in V_1^\ast \oplus V_2^\ast $에 대해 $\varphi(v_1+v_2):=\varphi_1(v_1)+\varphi_2(v_2)$로 두면 direct sum에서 분해가 유일하므로 well-defined인 linear functional이 되고, $\varphi\vert_{V_1}=\varphi_1$, $\varphi\vert_{V_2}=\varphi_2$이다. $\blacksquare$

같은 논증이 유한개의 직합 $V_1\oplus\cdots\oplus V_n$에도 그대로 확장된다. 무한개의 직합에서는 앞의 $\mathbb{R}[x]$ 예시를 생각해보면 직합의 dual이 dual의 직합과 isomorphic하지 않는다는 것을 쉽게 알 수 있다.

## Double dual

$V$에 dual을 두 번 취한 double dual을 생각해보면 특정 basis나 inner product 없이도 $V$에서 $V^{\ast\ast}$로 가는 자연스러운 injection을 생각해볼 수 있다.

**Definition (Double Dual, Evaluation Map).** $v\in V$에 대해 $$\operatorname{ev}_v:V^\ast \to F$$, $$\operatorname{ev}_v(\varphi)=\varphi(v)$$는 $V^\ast $ 위의 functional, 곧 $V^{\ast \ast }$의 원소다. 이로써 map $$\Phi:V\to V^{**},\qquad \Phi(v)=\operatorname{ev}_v$$가 정해진다.

**Theorem.** $\Phi$는 injective linear map이고, $V$가 유한차원이면 isomorphism이다. 게다가 그 정의에는 basis가 개입하지 않는다.

*Proof.* linear는 명백하다. $v\ne0$이면 $v$를 basis로 확장해 $\varphi(v)=1$인 functional $\varphi$를 만들 수 있어 $$\operatorname{ev}_v(\varphi)=1\ne0$$, 곧 $\Phi(v)\ne0$이라 injective다. 유한차원에서는 $\dim V^{\ast \ast }=\dim V^\ast =\dim V$라 injective가 곧 isomorphism이다. $\blacksquare$

$V$와 dual의 대응은 basis를 필요로 하고 double dual은 그렇지 않다는 이 대비는 수학사에서 중요한 역할을 했다. Samuel Eilenberg와 Saunders Mac Lane은 1945년 논문에서 바로 이 double dual isomorphism을 "자연스러운" 동형의 표준 예로 삼아 category theory의 natural transformation 개념을 정의했다 [3].

## Dual map

**Definition (Dual Map, Transpose).** linear map $T:V\to W$에 대해 $$T^*:W^*\to V^*,\qquad T^*(\varphi)=\varphi\circ T$$를 $T$의 dual map(또는 transpose)이라 한다. $T^\ast (\varphi)=\varphi\circ T$는 공역의 functional $\varphi$를 $T$를 따라 정의역으로 끌어온 것이라 pullback이라고도 부른다. 합성으로 되돌려 공역의 대상을 정의역의 대상으로 만드는 이 pullback의 패턴은 수학 전반에서 반복해서 등장한다.

**Theorem ($T\mapsto T^\ast $의 성질).** $T\mapsto T^\ast $는 $$\mathcal{L}(V,W)\to\mathcal{L}(W^*,V^*)$$인 linear map이고, $V,W$가 유한차원이면 isomorphism이다.

*Proof.* $(aS+bT)^\ast (\varphi)=\varphi\circ(aS+bT)=a(\varphi\circ S)+b(\varphi\circ T)=aS^\ast (\varphi)+bT^\ast (\varphi)$이므로 linear다. injective를 보자: $T^\ast =0$이라 하면 모든 $\varphi\in W^\ast $에서 $\varphi\circ T=0$이다. $T\ne0$이면 $Tv\ne0$인 $v$가 있는데, 위 Double Dual 정리의 증명에서 보였듯 $0\ne w\in W$마다 $\varphi(w)\ne0$인 $\varphi\in W^\ast $가 있으므로 $w=Tv$에 그런 $\varphi$를 고르면 $T^\ast (\varphi)(v)=\varphi(Tv)\ne0$이라 $T^\ast \ne0$이다. 대우를 취하면 $T\mapsto T^\ast $가 injective다. 유한차원에서는 행렬 표현으로 $$\dim\mathcal{L}(V,W)=\dim V\dim W=\dim W^*\dim V^*=\dim\mathcal{L}(W^*,V^*)$$이므로(Dual Basis로 $\dim V^\ast =\dim V$, $\dim W^\ast =\dim W$) 같은 차원의 공간 사이의 injective linear map은 isomorphism이다. $\blacksquare$

**Proposition (dual map의 대수적 성질).** 앞 정리의 linearity($(aS+bT)^\ast =aS^\ast +bT^\ast $)에 더해, 합성 가능한 linear map $T:V\to W$, $S:W\to X$에 대해 $$(ST)^\ast =T^\ast S^\ast ,\qquad I_V^\ast =I_{V^\ast }$$이고, $T$가 invertible이면 $(T^{-1})^\ast =(T^\ast )^{-1}$이다.

*Proof.* $\varphi\in X^\ast $마다 $(ST)^\ast (\varphi)=\varphi\circ(ST)=(\varphi\circ S)\circ T=T^\ast (\varphi\circ S)=T^\ast (S^\ast (\varphi))$이므로 $(ST)^\ast =T^\ast S^\ast $다. $I_V^\ast (\varphi)=\varphi\circ I_V=\varphi$이므로 $I_V^\ast =I_{V^\ast }$다. $T$가 invertible이면 $(T^{-1})^\ast T^\ast =(TT^{-1})^\ast =I_W^\ast =I_{W^\ast }$이고 $T^\ast (T^{-1})^\ast =(T^{-1}T)^\ast =I_{V^\ast }$이므로 $(T^{-1})^\ast =(T^\ast )^{-1}$이다. $\blacksquare$

**Proposition.** $V,W$의 basis와 그 dual basis에 대해 $T$의 행렬이 $A$이면 $T^\ast $의 행렬은 $A^{\mathsf T}$이다.

*Proof.* $T(v_j)=\sum_iA_{ij}w_i$라 하면 $T^\ast (w_k^\ast )=w_k^\ast \circ T$의 $v_j$에서의 값은 $w_k^\ast (T(v_j))=A_{kj}$이다. 따라서 $T^\ast (w_k^\ast )=\sum_jA_{kj}v_j^\ast $이고, 이 계수 $A_{kj}$가 $T^\ast $ 행렬의 $(j,k)$ 성분이라 $A^{\mathsf T}$다. $\blacksquare$

## Annihilator

**Definition (Annihilator).** subspace $U\subseteq V$에 대해 $$U^\circ:=\{\,\varphi\in V^*:\varphi(u)=0\ \text{for all}\ u\in U\,\}\subseteq V^*$$를 $U$의 annihilator라 한다.

**Theorem.** 유한차원 $V$에서 $\dim U^\circ=\dim V-\dim U$이고, $V\cong V^{\ast \ast }$로 동일시하면 $(U^\circ)^\circ=U$이다.

*Proof.* $U$의 basis를 $V$의 basis $u_1,\dots,u_k,u_{k+1},\dots,u_n$($u_1,\dots,u_k$가 $U$의 basis)으로 확장하고 dual basis $u_i^\ast $를 잡으면, $\varphi=\sum_ic_iu_i^\ast $가 $U^\circ$에 드는 것은 $\varphi(u_j)=c_j=0$($j\le k$)인 것과 동치다. 따라서 $U^\circ=\operatorname{span}(u_{k+1}^\ast ,\dots,u_n^\ast )$이라 차원이 $n-k$다. $(U^\circ)^\circ$는 차원이 $n-(n-k)=k=\dim U$이고 $U\subseteq(U^\circ)^\circ$가 자명하므로 $U$와 같다. $\blacksquare$

**Theorem (Transpose와 annihilator).** linear map $T:V\to W$에 대해 $$\ker T^*=(\operatorname{im}T)^\circ,\qquad \operatorname{im}T^*=(\ker T)^\circ.$$

*Proof.* $\varphi\in\ker T^\ast \iff\varphi\circ T=0\iff\varphi$가 $\operatorname{im}T$ 위에서 $0\iff\varphi\in(\operatorname{im}T)^\circ$이라 첫 식이 나온다. 둘째 식은 $\operatorname{im}T^\ast \subseteq(\ker T)^\circ$가 자명하고, 차원이 $\dim\operatorname{im}T^\ast =\dim W-\dim\ker T^\ast =\dim W-\dim(\operatorname{im}T)^\circ=\operatorname{rank}T$이며 $\dim(\ker T)^\circ=\dim V-\dim\ker T=\operatorname{rank}T$로 같으므로 나온다. $\blacksquare$

**Corollary.** $T$가 injective이면 $T^\ast $는 surjective이고, $T$가 surjective이면 $T^\ast $는 injective이다.

*Proof.* $T$가 injective이면 $$\ker T=\{0\}$$이라 $(\ker T)^\circ=V^\ast $(자명한 subspace의 annihilator는 전체다)이고, 위 정리로 $\operatorname{im}T^\ast =(\ker T)^\circ=V^\ast $이니 $T^\ast $가 surjective다. $T$가 surjective이면 $\operatorname{im}T=W$라 $$(\operatorname{im}T)^\circ=\{0\}$$(전체 공간의 annihilator는 $0$뿐이다)이고, 위 정리로 $$\ker T^*=(\operatorname{im}T)^\circ=\{0\}$$이니 $T^\ast $가 injective다. $\blacksquare$

위 결과로부터 Fundamental Theorem of Linear Algebra를 행렬 없이 증명 가능하다.

**Corollary (Fundamental Theorem of Linear Algebra I: 차원, 좌표 없이).** $r:=\operatorname{rank}T$라 하면 $$\dim\operatorname{im}T=r,\quad\dim\ker T=\dim V-r,\quad\dim\operatorname{im}T^\ast =r,\quad\dim\ker T^\ast =\dim W-r$$이고, 특히 $\operatorname{rank}T^\ast =\operatorname{rank}T$(row rank = column rank)다.

*Proof.* 앞의 두 식은 $T$에 대한 rank-nullity 그 자체다. Transpose와 annihilator 정리의 $\ker T^\ast =(\operatorname{im}T)^\circ$와 annihilator의 dim 정리로 $$\dim\ker T^\ast =\dim(\operatorname{im}T)^\circ=\dim W-\dim\operatorname{im}T=\dim W-r$$이고, $T^\ast $에 대한 rank-nullity로 $$\dim\operatorname{im}T^\ast =\dim W^\ast -\dim\ker T^\ast =\dim W-(\dim W-r)=r$$이다. $\blacksquare$

$V=F^n$, $W=F^m$이고 $T$가 행렬 $A$로 표현되면 $\operatorname{im}T=C(A)$, $\ker T=N(A)$이며 $T^\ast $의 행렬은 $A^{\mathsf T}$이므로(Dual Map의 Proposition) $\operatorname{im}T^\ast =C(A^{\mathsf T})$, $\ker T^\ast =N(A^{\mathsf T})$다. 위 네 식은 정확히 $$\dim C(A)=r,\quad\dim N(A)=n-r,\quad\dim C(A^{\mathsf T})=r,\quad\dim N(A^{\mathsf T})=m-r$$이 되어, Linear maps and matrices 글의 Fundamental Theorem of Linear Algebra(차원) 그 자체다.

**Corollary (Fundamental Theorem of Linear Algebra II: 네 부분공간의 직교, 좌표 없이).** $V=F^n$, $W=F^m$이 표준 inner product를 갖고 $T:V\to W$가 행렬 $A$로 표현되면 $$N(A^{\mathsf T})=C(A)^\perp\quad(F^m\text{ 안에서}),\qquad C(A^{\mathsf T})=N(A)^\perp\quad(F^n\text{ 안에서})$$이다.

*Proof.* Riesz map $R$이 annihilator를 orthogonal complement로 옮긴다는 것을 보이자: subspace $U$와 $v\in V$에 대해 $$v\in U^\perp\iff\langle v,w\rangle=0\ (\forall w\in U)\iff\langle w,v\rangle=0\ (\forall w\in U)\iff R(v)(w)=0\ (\forall w\in U)\iff R(v)\in U^\circ$$이므로(둘째 동치는 $0$의 켤레도 $0$이라는 것, 셋째 동치는 $R(v):=\langle\cdot,v\rangle$의 정의) $R(U^\perp)=U^\circ$다. 이 식별 아래 $T^\ast $는 $A^{\mathsf T}$가 되므로(앞의 Proposition), Transpose와 annihilator 정리의 두 식 $\ker T^\ast =(\operatorname{im}T)^\circ$, $\operatorname{im}T^\ast =(\ker T)^\circ$가 정확히 위 두 식이 된다. $\blacksquare$

## 참고문헌

1. Riesz, F. (1907). Sur une espèce de géométrie analytique des systèmes de fonctions sommables. *Comptes Rendus de l'Académie des Sciences*, 144, 1409–1411.
2. Fréchet, M. (1907). Sur les ensembles de fonctions et les opérateurs linéaires. *Comptes Rendus de l'Académie des Sciences*, 144, 1414–1416.
3. Eilenberg, S., & Mac Lane, S. (1945). General Theory of Natural Equivalences. *Transactions of the American Mathematical Society*, 58(2), 231–294.
4. Köthe, G. (1983). *Topological Vector Spaces I*. Springer-Verlag, p. 75.
