---
layout: post
title: "Dual space and Riesz representation"
date: 2026-08-13
mathematicians: [Eilenberg, Mac Lane, Riesz, Fréchet]
---

## Dual space

**Definition (Dual Space).** vector space $V$에서 스칼라 $F$로 가는 linear map을 linear functional이라 하고, 그 전체 $$V^*:=\{\,\varphi:V\to F \text{ linear}\,\}=\mathcal{L}(V,F)$$를 $V$의 dual space라 한다. $V^*$는 pointwise 연산으로 vector space다.

엄밀히는 여기서 정의한 $V^*$는 topology 없이 정의되는 algebraic dual이다. $V$에 norm이나 topology가 있으면 그중 연속인(bounded) linear functional만 모은 continuous dual을 따로 다루는 것이 보통인데, 유한차원에서는 모든 linear functional이 자동으로 연속이라 두 dual이 일치하지만, 무한차원에서는 서로 다른 대상이 되고 continuous dual이 훨씬 작다.

**Example (좌표 뽑기).** $\mathbb{R}^n$에서 $i$번째 좌표를 뽑는 $x\mapsto x_i$는 linear functional이다.

**Example (한 점에서의 값매김).** $\mathbb{R}[x]$에서 한 점 $c$에서 값매김하는 $p\mapsto p(c)$는 linear functional이다.

**Example (정적분).** $\mathbb{R}[x]$에서 정적분 $p\mapsto\int_0^1 p$는 linear functional이다.

**Example ($k$차 계수 뽑기).** $\mathbb{R}[x]$에서 $k$차 계수를 뽑는 $p\mapsto p^{(k)}(0)/k!$은 linear functional이다.

**Definition, Theorem (Dual Basis).** $V$가 유한차원이고 basis가 $v_1,\dots,v_n$일 때 $$v_i^*(v_j)=\delta_{ij}$$로 정한 $v_i^*\in V^*$들을 dual basis라 한다. 이들은 $V^*$의 basis를 이루며 특히 $\dim V^*=\dim V$이다.

*Proof.* $\varphi\in V^*$에 대해 $\varphi(v_j)=c_j$라 하면 $\varphi$와 $\sum_ic_iv_i^*$가 모든 $v_j$에서 값이 같아($\sum_ic_iv_i^*(v_j)=c_j$) linear map으로서 같다. 따라서 $v_i^*$들이 $V^*$를 생성한다. 또 $\sum_ic_iv_i^*=0$이면 $v_j$를 넣어 $c_j=0$이니 일차독립이다. $\blacksquare$

유한차원에서 $\dim V^*=\dim V$이라 $V\cong V^*$이지만, 이 isomorphism은 basis를 골라야 나오는 것이라 자연스럽지 않다. 반면 $V$를 한 번 더 dual한 $V^{**}$로 가는 map은 basis 없이 정해진다.

**Definition (Double Dual, Evaluation Map).** $v\in V$에 대해 $\operatorname{ev}_v:V^*\to F$, $\operatorname{ev}_v(\varphi)=\varphi(v)$는 $V^*$ 위의 functional, 곧 $V^{**}$의 원소다. 이로써 map $$\Phi:V\to V^{**},\qquad \Phi(v)=\operatorname{ev}_v$$가 정해진다.

**Theorem.** $\Phi$는 injective linear map이고, $V$가 유한차원이면 isomorphism이다. 게다가 그 정의에는 basis가 개입하지 않는다.

*Proof.* linear는 명백하다. $v\ne0$이면 $v$를 basis로 확장해 $\varphi(v)=1$인 functional $\varphi$를 만들 수 있어 $\operatorname{ev}_v(\varphi)=1\ne0$, 곧 $\Phi(v)\ne0$이라 injective다. 유한차원에서는 $\dim V^{**}=\dim V^*=\dim V$라 injective가 곧 isomorphism이다. $\blacksquare$

같은 $V\cong V^*$와 $V\cong V^{**}$인데도 전자는 basis를 필요로 하고 후자는 그렇지 않다는 이 대비는 수학사에서 중요한 역할을 했다. Samuel Eilenberg와 Saunders Mac Lane은 1945년 논문에서 바로 이 double dual isomorphism을 "자연스러운" 동형의 표준 예로 삼아 category theory의 natural transformation 개념을 정의했다 [1].

transpose도 dual space 위에서 좌표 없이 정의된다.

**Definition (Dual Map, Transpose).** linear map $T:V\to W$에 대해 $$T^*:W^*\to V^*,\qquad T^*(\varphi)=\varphi\circ T$$를 $T$의 dual map(또는 transpose)이라 한다. $T^*(\varphi)=\varphi\circ T$는 공역의 functional $\varphi$를 $T$를 따라 정의역으로 끌어온 것이라 pullback이라고도 부른다. 합성으로 되돌려 공역의 대상을 정의역의 대상으로 만드는 이 pullback의 패턴은 수학 전반에서 반복해서 등장한다.

**Theorem ($T\mapsto T^*$의 성질).** $T\mapsto T^*$는 $$\mathcal{L}(V,W)\to\mathcal{L}(W^*,V^*)$$인 linear map이고, $V,W$가 유한차원이면 isomorphism이다.

*Proof.* $(aS+bT)^*(\varphi)=\varphi\circ(aS+bT)=a(\varphi\circ S)+b(\varphi\circ T)=aS^*(\varphi)+bT^*(\varphi)$이므로 linear다. injective를 보자: $T^*=0$이라 하면 모든 $\varphi\in W^*$에서 $\varphi\circ T=0$이다. $T\ne0$이면 $Tv\ne0$인 $v$가 있는데, 위 Double Dual 정리의 증명에서 보였듯 $0\ne w\in W$마다 $\varphi(w)\ne0$인 $\varphi\in W^*$가 있으므로 $w=Tv$에 그런 $\varphi$를 고르면 $T^*(\varphi)(v)=\varphi(Tv)\ne0$이라 $T^*\ne0$이다. 대우를 취하면 $T\mapsto T^*$가 injective다. 유한차원에서는 행렬 표현으로 $$\dim\mathcal{L}(V,W)=\dim V\dim W=\dim W^*\dim V^*=\dim\mathcal{L}(W^*,V^*)$$이므로(Dual Basis로 $\dim V^*=\dim V$, $\dim W^*=\dim W$) 같은 차원의 공간 사이의 injective linear map은 isomorphism이다. $\blacksquare$

**Proposition.** $V,W$의 basis와 그 dual basis에 대해 $T$의 행렬이 $A$이면 $T^*$의 행렬은 $A^{\mathsf T}$이다.

*Proof.* $T(v_j)=\sum_iA_{ij}w_i$라 하면 $T^*(w_k^*)=w_k^*\circ T$의 $v_j$에서의 값은 $w_k^*(T(v_j))=A_{kj}$이다. 따라서 $T^*(w_k^*)=\sum_jA_{kj}v_j^*$이고, 이 계수 $A_{kj}$가 $T^*$ 행렬의 $(j,k)$ 성분이라 $A^{\mathsf T}$다. $\blacksquare$

이것이 Linear map 글에서 "행과 열을 맞바꾸는 연산"으로 도입한 transpose의 좌표 없는 정체다.

**Definition (Annihilator).** subspace $U\subseteq V$에 대해 $$U^\circ:=\{\,\varphi\in V^*:\varphi(u)=0\ \text{for all}\ u\in U\,\}\subseteq V^*$$를 $U$의 annihilator라 한다.

**Theorem.** 유한차원 $V$에서 $\dim U^\circ=\dim V-\dim U$이고, $V\cong V^{**}$로 동일시하면 $(U^\circ)^\circ=U$이다.

*Proof.* $U$의 basis를 $V$의 basis $u_1,\dots,u_k,u_{k+1},\dots,u_n$($u_1,\dots,u_k$가 $U$의 basis)으로 확장하고 dual basis $u_i^*$를 잡으면, $\varphi=\sum_ic_iu_i^*$가 $U^\circ$에 드는 것은 $\varphi(u_j)=c_j=0$($j\le k$)인 것과 동치다. 따라서 $U^\circ=\operatorname{span}(u_{k+1}^*,\dots,u_n^*)$이라 차원이 $n-k$다. $(U^\circ)^\circ$는 차원이 $n-(n-k)=k=\dim U$이고 $U\subseteq(U^\circ)^\circ$가 자명하므로 $U$와 같다. $\blacksquare$

**Theorem (Transpose와 annihilator).** linear map $T:V\to W$에 대해 $$\ker T^*=(\operatorname{im}T)^\circ,\qquad \operatorname{im}T^*=(\ker T)^\circ.$$

*Proof.* $\varphi\in\ker T^*\iff\varphi\circ T=0\iff\varphi$가 $\operatorname{im}T$ 위에서 $0\iff\varphi\in(\operatorname{im}T)^\circ$이라 첫 식이 나온다. 둘째 식은 $\operatorname{im}T^*\subseteq(\ker T)^\circ$가 자명하고, 차원이 $\dim\operatorname{im}T^*=\dim W-\dim\ker T^*=\dim W-\dim(\operatorname{im}T)^\circ=\operatorname{rank}T$이며 $\dim(\ker T)^\circ=\dim V-\dim\ker T=\operatorname{rank}T$로 같으므로 나온다. $\blacksquare$

**Corollary.** $T$가 injective이면 $T^*$는 surjective이고, $T$가 surjective이면 $T^*$는 injective이다.

*Proof.* $T$가 injective이면 $$\ker T=\{0\}$$이라 $(\ker T)^\circ=V^*$(자명한 subspace의 annihilator는 전체다)이고, 위 정리로 $\operatorname{im}T^*=(\ker T)^\circ=V^*$이니 $T^*$가 surjective다. $T$가 surjective이면 $\operatorname{im}T=W$라 $$(\operatorname{im}T)^\circ=\{0\}$$(전체 공간의 annihilator는 $0$뿐이다)이고, 위 정리로 $$\ker T^*=(\operatorname{im}T)^\circ=\{0\}$$이니 $T^*$가 injective다. $\blacksquare$

첫 식은 $\operatorname{rank}T^*=\operatorname{rank}T$, 곧 row rank와 column rank가 같다는 것을 좌표 없이 준다. inner product를 얹으면 annihilator가 orthogonal complement로 바뀌고, 이 두 식이 Linear map 글의 네 subspace 직교 관계가 된다.

direct sum의 dual도 dual들의 direct sum으로 조각난다(적어도 유한개일 때는 그렇다).

**Theorem (Dual of a Finite Direct Sum).** $$(V_1\oplus V_2)^*\;\cong\;V_1^*\oplus V_2^*.$$ 구체적으로 $\varphi\mapsto(\varphi\vert_{V_1},\varphi\vert_{V_2})$가 그 isomorphism이다.

*Proof.* 이 대응이 linear임은 분명하다. injective: $\varphi\vert_{V_1}=0$, $\varphi\vert_{V_2}=0$이면 $V=V_1\oplus V_2$의 임의의 $v=v_1+v_2$에서 $\varphi(v)=\varphi(v_1)+\varphi(v_2)=0$이라 $\varphi=0$이다. surjective: 임의의 $(\varphi_1,\varphi_2)\in V_1^*\oplus V_2^*$에 대해 $\varphi(v_1+v_2):=\varphi_1(v_1)+\varphi_2(v_2)$로 두면 direct sum에서 분해가 유일하므로 well-defined인 linear functional이 되고, $\varphi\vert_{V_1}=\varphi_1$, $\varphi\vert_{V_2}=\varphi_2$이다. $\blacksquare$

같은 논증이 유한개의 직합 $V_1\oplus\cdots\oplus V_n$에도 그대로 확장된다. 그런데 무한히 많은 개수로 가면 사정이 달라진다.

**Theorem (Dual of a General Direct Sum).** 임의의(무한이어도 되는) index 집합 $I$와 부분공간 $$\{V_i\}_{i\in I}$$의 직합 $V=\bigoplus_{i\in I}V_i$에 대해 $$V^*\;\cong\;\prod_{i\in I}V_i^*,$$ 여기서 $\prod_{i\in I}V_i^*$는 (유한 support 조건 없이) 각 $\varphi_i\in V_i^*$를 하나씩 고른 모임 $$(\varphi_i)_{i\in I}$$ 전체다.

*Proof.* $V$의 원소는 유한개를 제외한 나머지가 $0$인 $$(v_i)_{i\in I}$$($v_i\in V_i$)이므로, $\varphi\in V^*$에 대해 $\varphi\big(\sum_iv_i\big)=\sum_i\varphi(v_i)$(유한합)가 각 $\varphi\vert_{V_i}=\varphi_i\in V_i^*$만으로 완전히 결정된다. 거꾸로 $I$가 무한이어도 $$(\varphi_i)_{i\in I}\in\prod_iV_i^*$$를 임의로 고르면 $$\varphi\Big(\sum_iv_i\Big):=\sum_i\varphi_i(v_i)$$(유한합이라 well-defined)가 linear functional을 준다. 그러므로 $$\varphi\mapsto(\varphi\vert_{V_i})_{i\in I}$$가 $V^*$와 $\prod_iV_i^*$ 사이의 전단사이고 linear인 대응이다. $\blacksquare$

$I$가 유한하면 유한 support 조건이 자동으로 만족되어 $\prod_iV_i^*=\bigoplus_iV_i^*$이므로 앞 정리로 되돌아간다. 하지만 $I$가 무한이면 $\prod_iV_i^*$가 $\bigoplus_iV_i^*$보다 훨씬 크다. 바로 이 간극이 다음 예에서 dual space가 무한차원에서 원래 공간보다 커지는 이유다.

**Example (무한차원에서 무너지는 것).** $V=\mathbb{R}[x]$는 basis $1,x,x^2,\dots$가 가산이다. 각 $x^k$에 대한 계수 뽑기 $e_k^*$들은 여전히 일차독립이지만 $V^*$를 생성하지는 못한다. 예컨대 모든 계수를 더하는 functional $\varphi:\sum_ka_kx^k\mapsto\sum_ka_k$(유한합이라 잘 정의됨)는 어떤 $e_k^*$들의 유한 일차결합으로도 표현되지 않는다. 실제로 $V^*$는 formal power series 전체와 동일시되어 $V$보다 크고, $\Phi:V\to V^{**}$는 injective이지만 surjective가 아니어서 유한차원의 $V\cong V^{**}$가 성립하지 않는다.

## Riesz representation theorem

위에서 유한차원 $V$는 $V^*$와 isomorphism을 가지지만 그 isomorphism은 basis를 골라야 나온다는 것을 보았다. inner product를 하나 고정하면, basis 선택 없이도 $V$와 $V^*$를 잇는 대응이 생긴다.

고정된 $u\in V$에 대해 $v\mapsto\langle v,u\rangle$은 (첫 인수에 대한 선형성으로) $V$ 위의 linear functional이다. 이 대응을 $$R:V\to V^*,\qquad R(u):=\langle\cdot,u\rangle$$이라 쓰자.

**Theorem (Riesz Representation, 유한차원).** $V$가 유한차원 inner product space이면, 임의의 $\varphi\in V^*$에 대해 $$\varphi(v)=\langle v,u\rangle\quad\text{for all }v\in V$$를 만족하는 $u\in V$가 유일하게 존재한다. 곧 $R:V\to V^*$는 전단사다.

*Proof.* $e_1,\dots,e_n$을 $V$의 orthonormal basis라 하자(Gram–Schmidt로 존재, Inner product space 글). $u:=\sum_i\overline{\varphi(e_i)}\,e_i$로 두면, $v=\sum_ic_ie_i$ ($c_i=\langle v,e_i\rangle$)에 대해 $$\langle v,u\rangle=\sum_ic_i\,\overline{\overline{\varphi(e_i)}}=\sum_ic_i\varphi(e_i)=\varphi\Big(\sum_ic_ie_i\Big)=\varphi(v)$$이다(둘째 등호는 $\langle e_i,e_j\rangle=\delta_{ij}$와 둘째 인수의 켤레선형성, 넷째 등호는 $\varphi$의 선형성). 존재가 보였다. 유일성은, $\langle v,u\rangle=\langle v,u'\rangle$이 모든 $v$에서 성립하면 $v=u-u'$을 넣어 $\lVert u-u'\rVert^2=0$, 곧 $u=u'$이기 때문이다. $\blacksquare$

**Proposition.** $R:V\to V^*$는 전단사이고, 실수 위에서는 linear isomorphism이지만 복소수 위에서는 conjugate-linear($R(au+bu')=\bar aR(u)+\bar bR(u')$)이다.

*Proof.* 전단사는 위 정리 그 자체다(존재가 surjective를, 유일성이 $R(u)=R(u')\Rightarrow u=u'$인 injective를 준다: 실제로 $R(u)=0$이면 $\langle v,u\rangle=0$이 모든 $v$에서 성립하고 특히 $v=u$에서 $\lVert u\rVert^2=0$이라 $u=0$이다). $R(au+bu')(v)=\langle v,au+bu'\rangle=\bar a\langle v,u\rangle+\bar b\langle v,u'\rangle$은 둘째 인수의 켤레선형성에서 바로 나온다. $\blacksquare$

double dual map $\Phi:V\to V^{**}$는 basis도 inner product도 없이 정해지지만 그 자체로는 $V\to V^*$를 주지 못한다. 반면 $R$은 $V\to V^*$를 직접 주는 대신 inner product의 선택에 의존하고, 복소수 위에서는 온전한 linear map조차 아니다. 두 자연스러움은 서로 다른 대가를 치른다.

**Example (좌표).** $\mathbb{R}^n$의 dot product에서, 좌표 functional $\varphi(x)=\sum_ia_ix_i$의 Riesz representative는 $u=(a_1,\dots,a_n)$ 그 자체다.

**Example (trace).** $n\times n$ 실행렬 공간에 Frobenius inner product $\langle A,B\rangle:=\operatorname{tr}(B^{\mathsf T}A)$를 주자. trace functional $\varphi(A)=\operatorname{tr}A$의 Riesz representative는 항등행렬 $I$다. 실제로 $\langle A,I\rangle=\operatorname{tr}(I^{\mathsf T}A)=\operatorname{tr}A=\varphi(A)$이다.

이 정리는 Frigyes Riesz와 Maurice Fréchet가 1907년 각자 독립적으로, $L^2$ 위의 연속 linear functional이 inner product로 표현된다는 것을 보인 데서 이름을 얻었다 [2][3]. 여기서 다룬 것은 그 유한차원 축소판이고, 완비성과 연속성이 걸린 진짜 정리는 함수해석 글에서 Hilbert space에 대해 다시 다룬다.

## 참고문헌

1. Eilenberg, S., & Mac Lane, S. (1945). General Theory of Natural Equivalences. *Transactions of the American Mathematical Society*, 58(2), 231–294.
2. Riesz, F. (1907). Sur une espèce de géométrie analytique des systèmes de fonctions sommables. *Comptes Rendus de l'Académie des Sciences*, 144, 1409–1411.
3. Fréchet, M. (1907). Sur les ensembles de fonctions et les opérateurs linéaires. *Comptes Rendus de l'Académie des Sciences*, 144, 1414–1416.
