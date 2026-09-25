---
layout: post
title: "Tensor product and exterior algebra"
date: 2026-08-17
mathematicians: [Samuel, Eilenberg, Mac Lane, Grassmann]
---

## Universal property

**Definition (Universal Object).** $X$가 일반적인 set, $Y$가 vector space이고 $\iota:X\to Y$가 어떤 성질 $P$를 만족하며, $Y$와 scalar field가 같은 vector space $Z$와 $P$를 만족하는 $g:X\to Z$에 대해 $g=h\circ\iota$인 linear map $h:Y\to Z$가 유일하게 존재하면, $(Y,\iota)$를 $X$에 대한(그리고 $P$에 관한) universal object라 하고, $Y$가 만족하는 이 성질을 universal property라고 한다.

**Proposition (Universal Object는 canonical하게 유일하다).** $(Y,\iota)$, $(Y',\iota')$가 모두 $X$에 대한 universal object면, $\Phi\circ\iota=\iota'$인 isomorphism $\Phi:Y\to Y'$가 유일하게 존재한다.

*Proof.* $\iota'$가 $P$를 만족하는 $X\to Y'$인 map이므로 $Y$의 universal property를 적용해 $\iota'=\Phi\circ\iota$인 linear map $\Phi:Y\to Y'$를 얻는다. 대칭적으로 $\iota=\Psi\circ\iota'$인 linear map $\Psi:Y'\to Y$를 얻는다. $\Psi\circ\Phi$(linear map들의 합성이라 linear map이다)와 $$\mathrm{id}_Y$$가 둘 다 $\iota=(\cdot)\circ\iota$를 만족하므로, $Y$의 universal property의 유일성(적용 대상 $Z=Y$, $g=\iota$)으로 $$\Psi\circ\Phi=\mathrm{id}_Y$$이고 마찬가지로 $$\Phi\circ\Psi=\mathrm{id}_{Y'}$$다.$\blacksquare$

Universal property는 사실 vector space와 linear map 뿐 아니라 다른 일반적인 수학 객체에도 적용할 수 있다. Pierre Samuel의 1948년 논문에서 topological space와 continuous map에 대해서 이러한 universal property가 처음으로 체계적으로 다뤄졌다. 이후 Samuel Eilenberg와 Saunders Mac Lane이 만든([Dual space and Riesz representation]({% post_url 2026-08-13-dual-space-and-riesz-representation %})에서 이미 본 두 사람이다) category theory 언어로, 이 schema는 "$X$에서 나가는(혹은 들어오는) $P$-map들의 category에서의 initial(혹은 terminal) object"로 완전히 일반화된다.

예를 들어, [Vector spaces]({% post_url 2026-08-05-vector-spaces %})에서 본 direct sum을 universal object로 정의할 수 있다. 앞에서는 direct sum을 한 vector space 안의 두 subspace에 대해서 정의했지만, scalar field가 같기만 하면 임의의 두 vector space $V,W$에 대해서도 아래와 같이 direct sum을 정의해볼 수 있다.

**Definition (Direct sum).** $V,W$가 같은 field $F$ 위의 vector space일 때, $$V\oplus W:=\{(v,w):v\in V,w\in W\}$$에 $$(v_1,w_1)+(v_2,w_2):=(v_1+v_2,w_1+w_2),\qquad c(v,w):=(cv,cw)$$로 연산을 주면 $V\oplus W$는 vector space가 되고, 이를 direct sum이라 한다.

**Remark.** $v\mapsto(v,0)$, $w\mapsto(0,w)$로 $V,W$를 각각 $V\oplus W$의 subspace로 보면 이 두 subspace의 교집합이 $\lbrace 0\rbrace $이고 그 합이 $V\oplus W$ 전체이므로, 이는 기존 direct sum의 정의를 그대로 회복한다. $V$의 basis $\lbrace b_i\rbrace _{i\in I}$와 $W$의 basis $\lbrace c_j\rbrace _{j\in J}$에 대해 $(b_i,0)$와 $(0,c_j)$를 모두 모으면 $V\oplus W$의 basis가 되므로 direct sum의 철학은 두 basis를 그저 나란히 합쳐 놓는 것이라 할 수 있다. 그래서 유한차원이면 $\dim(V\oplus W)=\dim V+\dim W$이 성립한다.

**Example. (Direct sum)** $X=V\times W$, $P=$"linear"라고 하면 direct sum은 $X$에 대한 universal object가 된다. Direct sum의 construction은 위와 같으며 $\iota(v,w)=(v,w)$이다.

## Tensor product

Tensor product를 정의하는 여러 방법이 있지만 가장 깔끔한 것은 다음과 같이 universal object로 정의하는 것이다.

**Definition (Tensor Product).** 같은 scalar field를 가지는 $V,W$의 tensor product는 $X=V\times W$, $P=$"bilinear"일 때 $X$에 대한 universal object를 tensor product라고 한다. 이를 $V \otimes W$라고 표기하며, 그 universal object를 이루는 $\iota$가 $(v,w)$에 대응시키는 $V \otimes W$의 vector를 $v \otimes w$로 표기한다.

임의의 두 $V,W$에 대해서 tensor product가 존재하는지는 위 정의와 별개의 문제이다. 실제로는 tensor product는 항상 존재하며 두 basis의 cartesian product를 생각해보면 된다. Direct sum이 두 basis의 union인 것과는 대조적이다.

**Proposition (존재성).** $V,W$의 basis를 각각 $\lbrace b_i\rbrace _{i\in I}$, $\lbrace c_j\rbrace _{j\in J}$라 하자. $I\times J$에서 $F$로 가는, 유한개의 $(i,j)$에서만 값이 $0$이 아닌 함수 전체를 pointwise 연산으로 vector space로 보고 이를 $V\otimes W$라 하자. $(i,j)$에서만 $1$이고 나머지에서 $0$인 함수를 $b_i\otimes c_j$라 하고, 임의의 vector $v=\sum_ip_ib_i$, $w=\sum_jq_jc_j$에 대해 $$v\otimes w:=\sum_{i,j}p_iq_j\,(b_i\otimes c_j)$$로 정의하자. 그러면 $(V\otimes W,\otimes)$는 universal property를 만족한다. 즉 $V,W$의 tensor product다.

*Proof.* 먼저 $\otimes$가 bilinear임을 보이자. $v=\sum_ip_ib_i$, $v'=\sum_ip_i'b_i$, $w=\sum_jq_jc_j$, $c\in F$라 하면 $v+v'=\sum_i(p_i+p_i')b_i$, $cv=\sum_i(cp_i)b_i$이므로 정의에서 바로 $$(v+v')\otimes w=\sum_{i,j}(p_i+p_i')q_j\,(b_i\otimes c_j)=v\otimes w+v'\otimes w,\qquad(cv)\otimes w=c(v\otimes w)$$가 나온다. $w$쪽 선형성도 대칭적으로 같다.

다음으로 $\lbrace b_i\otimes c_j\rbrace $가 $V\otimes W$의 basis임을 보이자. $V\otimes W$의 임의의 원소(유한개의 $(i,j)$에서만 값이 $0$이 아닌 함수) $f$는 $f=\sum_{i,j}f(i,j)\,(b_i\otimes c_j)$(유한합)로 쓰이므로 $\lbrace b_i\otimes c_j\rbrace $는 $V\otimes W$를 span한다. 또한 $\sum_{i,j}c_{ij}\,(b_i\otimes c_j)$가 $0$함수라면 이 함수를 $(i,j)$에서 값을 취해보면(각 $b_i\otimes c_j$가 서로 다른 점에서만 $1$인 indicator function이므로) 바로 $c_{ij}=0$이 나오므로 일차독립이다.

이제 universal property를 확인하자. 임의의 bilinear map $B:V\times W\to U$에 대해 $L(b_i\otimes c_j):=B(b_i,c_j)$로 basis 위에서 정의하고 선형으로 확장하면 linear map $L:V\otimes W\to U$를 얻는다. 임의의 $v=\sum_ip_ib_i,w=\sum_jq_jc_j$에 대해 $$L(v\otimes w)=\sum_{i,j}p_iq_j\,L(b_i\otimes c_j)=\sum_{i,j}p_iq_j\,B(b_i,c_j)=B(v,w)$$인데(마지막 등호는 $B$의 bilinearity), 곧 $L\circ\otimes=B$다. 유일성은 $\lbrace b_i\otimes c_j\rbrace $가 $V\otimes W$를 span하므로 $L$의 값이 그 위에서 강제된다는 데서 나온다. $\blacksquare$

이러한 tensor product의 construction은 basis의 선택에 의존하지만 이 역시 universal property를 만족하기 때문에 universal object의 성질에 따라 모든 construction이 isomorphic하다.

**Corollary (Dimension).** 유한차원 $V,W$에서 $\dim(V\otimes W)=(\dim V)(\dim W)$.

*Proof.* $V,W$의 basis를 $v_1,\dots,v_m$, $w_1,\dots,w_n$이라 하고, 위 Proposition에서 $b_i=v_i$, $c_j=w_j$로 택해 tensor product를 구성하면, $\lbrace v_i\otimes w_j\rbrace $가 $V\otimes W$의 basis이므로 $\dim(V\otimes W)=mn=(\dim V)(\dim W)$다. $\blacksquare$

**Corollary.** $B(V,W) \cong (V\otimes W)^\ast $

**Example.** $V=W=\mathbb{R}^2$에서 표준 basis로 $\dim(V\otimes W)=4$이고, $e_1\otimes e_1,e_1\otimes e_2,e_2\otimes e_1,e_2\otimes e_2$가 basis다. $$(1,1)\otimes(1,-1)=e_1\otimes e_1-e_1\otimes e_2+e_2\otimes e_1-e_2\otimes e_2$$처럼 전개된다.

**Example (simple tensor가 아닌 원소).** 같은 $V\otimes W=\mathbb{R}^2\otimes\mathbb{R}^2$에서 $e_1\otimes e_1+e_2\otimes e_2$는 어떤 $v,w\in\mathbb{R}^2$에 대해서도 $v\otimes w$ 꼴로 쓰이지 않는다. basis $e_i\otimes e_j$에서의 좌표를 행렬 $C=(c_{ij})$로 모으면, $v\otimes w=\sum_{i,j}v_iw_j\,e_i\otimes e_j$의 좌표행렬은 $vw^{\mathsf T}$(rank가 $0$ 또는 $1$)인 반면, $e_1\otimes e_1+e_2\otimes e_2$의 좌표행렬은 $I$로 rank가 $2$이기 때문이다.

**Example (다항식).** $F[x]$는 monomial $1,x,x^2,\dots$을 basis로 갖는 무한차원 vector space이므로, 위 construction이 그대로 적용되어 $$F[x]\otimes F[y]\cong F[x,y]\qquad(x^i\otimes y^j\leftrightarrow x^iy^j)$$가 성립한다. 두 변수 polynomial 공간이 monomial들의 tensor product인 것이다.

## Tensor product의 성질

**Proposition.**
- 교환: $V\otimes W\cong W\otimes V$
- 결합: $(U\otimes V)\otimes W\cong U\otimes(V\otimes W)$
- 분배: $U\otimes(V\oplus W)\cong(U\otimes V)\oplus(U\otimes W)$
- dual: $(V\otimes W)^\ast \cong V^\ast \otimes W^\ast $

*Proof.* 교환: $(v,w)\mapsto w\otimes v$가 $V\times W\to W\otimes V$인 bilinear map이므로 universal property로 $V\otimes W\to W\otimes V$인 linear map이 나오고, 대칭적으로 반대 방향도 나와(basis에서 서로 역임이 확인된다) 서로 역이다. 결합·분배도 양쪽의 자연스러운 basis(각각 $u_i\otimes v_j\otimes w_k$류, $u_i\otimes v_j$와 $u_i\otimes w_k$류)를 대응시키는 같은 논증으로 확인된다. dual: basis에서 $(v_i\otimes w_j)^\ast \leftrightarrow v_i^\ast \otimes w_j^\ast $의 대응이 $$\big(v_i^*\otimes w_j^*\big)(v_k\otimes w_l):=v_i^*(v_k)\,w_j^*(w_l)=\delta_{ik}\delta_{jl}$$을 만족해 정확히 dual basis를 주므로 isomorphism이다. $\blacksquare$

**Theorem (Tensor-Hom Adjunction).** 자연스러운 isomorphism $$\operatorname{Hom}(U\otimes V,W)\cong\operatorname{Hom}(U,\operatorname{Hom}(V,W))$$가 성립한다.

*Proof.* $L:U\otimes V\to W$가 주어지면 각 $u\in U$마다 $v\mapsto L(u\otimes v)$가 $V\to W$인 linear map이고, $u\mapsto\big(v\mapsto L(u\otimes v)\big)$ 자체도 $u$에 대해 linear이므로(둘 다 $L$과 $\otimes$가 각 인수에 linear라는 데서 나온다) 이는 $\Phi(L)\in\operatorname{Hom}(U,\operatorname{Hom}(V,W))$를 정의한다. 역으로 $\Psi:U\to\operatorname{Hom}(V,W)$가 주어지면 $(u,v)\mapsto\Psi(u)(v)$가 $U\times V\to W$인 bilinear map이므로(각 인수에 대한 선형성이 $\Psi$의 선형성과 각 $\Psi(u)$의 선형성에서 각각 나온다), universal property로 유일한 $\Theta(\Psi)\in\operatorname{Hom}(U\otimes V,W)$가 나온다. $\Phi,\Theta$가 basic tensor $u\otimes v$ 위에서 서로 역임이 정의에서 바로 확인되므로 둘은 서로 역인 isomorphism이다. $\blacksquare$

$W=F$로 두면 $\operatorname{Hom}(U \otimes V, F) \cong \operatorname{Hom}(U,V^\ast) \cong B(U,V)$가 다시 나온다. 여기서 $\operatorname{Hom}(U,V^\ast) \cong B(U,V)$는 한 벡터 $u$를 넣으면 $B(u,\cdot)\in V^\ast $를 내놓는 대응이다.

**Proposition.** $V$ 또는 $W$가 유한차원이면 $\operatorname{Hom}(V,W)\cong V^\ast \otimes W$다.

*Proof.* $\Phi:V^\ast \otimes W\to\operatorname{Hom}(V,W)$를 $\varphi\otimes w\mapsto(v\mapsto\varphi(v)w)$(rank $1$ 또는 $0$인 linear map)로 두고 선형으로 확장하자.

$V$가 유한차원인 경우: basis $v_1,\dots,v_m$과 dual basis $v_1^\ast ,\dots,v_m^\ast $를 택하면 $V^\ast \otimes W$의 임의의 원소는 $\sum_iv_i^\ast \otimes u_i$(유일한 $u_1,\dots,u_m\in W$) 꼴로 유일하게 쓰이고, $\Phi\big(\sum_iv_i^\ast \otimes u_i\big)$는 $v_i\mapsto u_i$($i=1,\dots,m$)인 linear map이다. $V$가 유한차원이라 basis 위의 값 $(u_1,\dots,u_m)\in W^m$을 자유롭게 지정하는 것과 linear map $V\to W$ 하나를 지정하는 것이 정확히 같으므로 $\Phi$는 bijective하다.

$W$가 유한차원인 경우: basis $w_1,\dots,w_n$을 택하면 $V^\ast \otimes W$의 임의의 원소는 $\sum_j\varphi_j\otimes w_j$(유일한 $\varphi_1,\dots,\varphi_n\in V^\ast $) 꼴로 유일하게 쓰이고, $\Phi\big(\sum_j\varphi_j\otimes w_j\big)$는 $v\mapsto\sum_j\varphi_j(v)w_j$인 linear map이다. 역으로 임의의 linear map $S:V\to W$는 $w_j$가 basis이므로 $S(v)=\sum_j\varphi_j(v)w_j$인 유일한 좌표함수 $\varphi_1,\dots,\varphi_n:V\to F$를 주는데, 각 $\varphi_j$는 $S$와 $j$번째 좌표사영의 합성이라 linear이므로 $V^\ast $의 원소다. 곧 $S\leftrightarrow(\varphi_1,\dots,\varphi_n)$이 서로 역인 대응이라 $\Phi$는 bijective하다. $\blacksquare$

**Example ($V,W$가 모두 무한차원이면 실패한다).** $V=W$가 무한차원이고 basis $e_1,e_2,\dots$라 하자. $$\operatorname{id}_V\in\operatorname{Hom}(V,V)$$는 $\Phi$의 image에 들지 않는다: $$\Phi\big(\sum_{k=1}^N\varphi_k\otimes w_k\big)$$의 image는 언제나 유한차원 부분공간 $\operatorname{span}(w_1,\dots,w_N)$에 들어 있는데, $$\operatorname{id}_V$$의 image는 무한차원인 $V$ 전체이기 때문이다. 곧 $V,W$가 모두 무한차원이면 위 Proposition은 일반적으로 성립하지 않는다.

**Proposition (trace는 evaluation pairing이다).** $V$가 유한차원이고 $T\in\operatorname{Hom}(V,V)$이면, $T$를 어떤 basis에서 나타낸 행렬 $A$의 (basis에 무관한) trace $\operatorname{tr}(T):=\sum_iA_{ii}$는, 위 Proposition의 isomorphism $\operatorname{Hom}(V,V)\cong V^\ast \otimes V$($W=V$인 경우) 아래 $T$에 대응하는 tensor를 evaluation pairing $$V^\ast \otimes V\to F,\qquad\varphi\otimes v\mapsto\varphi(v)$$으로 보낸 값과 정확히 같다.

*Proof.* basis $e_1,\dots,e_n$과 dual basis $e_1^\ast ,\dots,e_n^\ast $를 고르면, 위 Proposition의 대응 아래 $T$는 $$\sum_ie_i^\ast \otimes Te_i$$에 대응한다(실제로 이 tensor를 $\Phi$로 보내면 $e_k\mapsto\sum_ie_i^\ast (e_k)Te_i=Te_k$라 정확히 $T$를 준다). $Te_i=\sum_jA_{ji}e_j$이므로 $e_i^\ast (Te_i)=A_{ii}$이고, 따라서 evaluation pairing 값은 $$\sum_ie_i^\ast (Te_i)=\sum_iA_{ii}=\operatorname{tr}(T)$$다. $\blacksquare$

**Definition (다중 Tensor Product).** 같은 scalar field를 가지는 $V_1,\dots,V_k$의 tensor product는 $X=V_1\times\cdots\times V_k$, $P=$"$k$-linear"일 때 $X$에 대한 universal object를 말한다. 이를 $V_1\otimes\cdots\otimes V_k$라 표기하며, 그 universal object를 이루는 $\iota$가 $(v_1,\dots,v_k)$에 대응시키는 vector를 $v_1\otimes\cdots\otimes v_k$라 표기한다.

**Remark.** 다중 tensor product의 존재성도 basis의 Cartesian product를 이용한 construction으로 보일 수 있다.

**Remark.** $V^{\otimes k}:=V \otimes \cdots \otimes V$

**Remark.** 무한개의 vector space에 대한 tensor product도 존재는 한다. $X:=\prod_iV_i$, $P=$"각 좌표에 대해 linear"로 두면, $X$에 대한 tensor product가 된다. 그러나 유한개일 때처럼 $\iota$를 구성하려고 하면 실패한다. 예를 들어 모든 $i\in\mathbb{N}$에서 $V_i=\mathbb{R}^2$이고 $v_i=e_1+e_2$라 하자. Multilinearity로 $\bigotimes_iv_i$를 전개하면 항이 무한개가 나오기 때문에 $\iota$가 잘 정의되지 않는다. $\iota$는 다음과 같은 방식으로 구성할 수 있다. $x\in X$마다 basis vector $\delta_x$를 하나씩 대응시켜서 이 basis로 span된 vector space $V$를 만든다. 그리고 index $i$ 하나를 고정할 때마다 그 자리에서 덧셈과 스칼라곱을 보존해야 한다는 관계식들을 전부 모아 생성하는 부분공간 $N$으로 quotient해 $Y:=V/N$을 만들고, $\iota(x):=\delta_x+N$으로 정의한다. $N$의 정의에 따라 $\iota$는 $P$-map이다. 임의의 $P$-map $g:X\to Z$가 주어지면, $V$가 $X$ 위의 free vector space이므로 $\delta_x\mapsto g(x)$로 정의하고 선형으로 확장한 linear map $\hat g:V\to Z$가 유일하게 존재한다. $g$가 $P$를 만족한다는 것은 정확히 $\hat g$가 $N$의 모든 생성원 위에서 $0$이 된다는 뜻이므로 $N\subseteq\ker\hat g$이고, 이로부터 $h([\delta_x]):=\hat g(\delta_x)=g(x)$로 잘 정의된 linear map $h:Y\to Z$를 얻는다. $h\circ\iota=g$이고, $\lbrace [\delta_x]\rbrace _{x\in X}$가 $Y$를 span하므로 $h$는 유일하다. 하지만 이러한 construction은 유한개일 때와 달리 유용하지는 않기 때문에 tensor product는 주로 유한개일 때만 생각한다.

**Theorem (다중 tensor product의 결합성).** $$(V_1\otimes V_2)\otimes V_3\cong V_1\otimes V_2\otimes V_3$$이고, 같은 논증으로 임의의 개수·임의의 괄호 위치에 대해서도 성립한다.

*Proof.* $(V_1\otimes V_2)\otimes V_3$가 $V_1\times V_2\times V_3$에 대한 tri-linear universal property를 만족함을 보이면 충분하다: Universal Object는 canonical하게 유일하므로, 이를 보이면 $(V_1\otimes V_2)\otimes V_3$는 (basis 선택과 무관하게) $V_1\otimes V_2\otimes V_3$와 canonical하게 isomorphic하기 때문이다. $\iota(v_1,v_2,v_3):=(v_1\otimes v_2)\otimes v_3$는 각 성분의 bilinearity에서 바로 tri-linear다. 임의의 tri-linear map $B:V_1\times V_2\times V_3\to U$가 주어지면, 각 $v_3$마다 $(v_1,v_2)\mapsto B(v_1,v_2,v_3)$가 bilinear이므로 $V_1\otimes V_2$의 universal property로 linear map $L_{v_3}:V_1\otimes V_2\to U$를 얻고, $(t,v_3)\mapsto L_{v_3}(t)$는 $t$에 대해 linear(정의에서 바로 나온다)이고 $v_3$에 대해서도 linear($B$가 세 번째 성분에 linear라는 데서 $L_{v_3}$가 $v_3$에 linear하게 의존한다)이므로 $(V_1\otimes V_2)\times V_3\to U$인 bilinear map이다. 여기에 다시 $(V_1\otimes V_2)\otimes V_3$의 universal property를 적용하면 $\iota$를 거쳐 $B$를 재현하는 linear map $(V_1\otimes V_2)\otimes V_3\to U$를 얻고, 이는 $\iota$의 image가 span하므로 유일하다. 곧 $((V_1\otimes V_2)\otimes V_3,\iota)$는 tri-linear map에 대한 universal object다. 이 논증을 반복하면 임의의 개수·괄호 위치에서도 같은 결론을 얻으므로, 이후로는 괄호 없이 $V_1\otimes\cdots\otimes V_k$라 써도 무방하다. $\blacksquare$

## Operator의 Tensor Product

**Definition (Linear map의 Tensor Product).** $S:V_1\to W_1$, $T:V_2\to W_2$에 대해 $(v,w)\mapsto Sv\otimes Tw$는 $V_1\times V_2\to W_1\otimes W_2$인 bilinear map이므로, universal property로 $$S\otimes T:V_1\otimes V_2\to W_1\otimes W_2,\qquad(S\otimes T)(v\otimes w)=Sv\otimes Tw$$인 linear map이 유일하게 정해진다.

**Proposition (합성).** 합성 가능할 때 $$(S_1\otimes T_1)\circ(S_2\otimes T_2)=(S_1\circ S_2)\otimes(T_1\circ T_2).$$

*Proof.* 양변을 $v\otimes w$ 꼴(이들이 span하므로 이걸로 충분하다)에 적용하면 $$(S_1\otimes T_1)\big((S_2\otimes T_2)(v\otimes w)\big)=(S_1\otimes T_1)(S_2v\otimes T_2w)=S_1S_2v\otimes T_1T_2w=\big((S_1S_2)\otimes(T_1T_2)\big)(v\otimes w)$$로 일치한다. $\blacksquare$

$S,T$가 각각 eigenvector를 가지면 그 tensor도 eigenvector가 된다.

**Proposition ($S\otimes T$의 eigenvalue).** $S:V\to V$, $T:W\to W$가 $Sv=\lambda v$, $Tw=\mu w$인 eigenvector $v,w$를 가지면, $v\otimes w$는 $S\otimes T$의 eigenvalue $\lambda\mu$짜리 eigenvector다. 특히 $S,T$가 각각 eigenbasis $v_1,\dots,v_m$(eigenvalue $\lambda_i$), $w_1,\dots,w_n$(eigenvalue $\mu_j$)로 diagonalizable이면, $S\otimes T$는 eigenbasis $v_i\otimes w_j$로 diagonalizable이고 그 eigenvalue 전체가 $$\{\lambda_i\mu_j\}$$다.

*Proof.* $(S\otimes T)(v\otimes w)=Sv\otimes Tw=\lambda v\otimes\mu w=\lambda\mu\,(v\otimes w)$이다. $S,T$가 각각 eigenbasis를 가지면 $v_i\otimes w_j$들이(basis의 tensor라) $V\otimes W$의 basis를 이루고, 각각이 이 계산으로 eigenvalue $\lambda_i\mu_j$의 eigenvector이므로 $S\otimes T$가 이 basis에서 diagonal이다. $\blacksquare$

**Proposition (Kronecker product).** $S:F^m\to F^p$, $T:F^n\to F^q$의 행렬이 각각 $A,B$이면, basis $e_i\otimes f_j$를 $(i,j)$의 사전식 순서로 나열한 좌표에서 $S\otimes T$의 행렬은 $(pq)\times(mn)$ Kronecker product
$$A\otimes B:=\begin{pmatrix}A_{11}B&\cdots&A_{1m}B\\\vdots&&\vdots\\A_{p1}B&\cdots&A_{pm}B\end{pmatrix}$$
이다.

*Proof.* $$(S\otimes T)(e_i\otimes f_j)=Se_i\otimes Tf_j=\Big(\sum_aA_{ai}e_a\Big)\otimes\Big(\sum_bB_{bj}f_b\Big)=\sum_{a,b}A_{ai}B_{bj}\,(e_a\otimes f_b)$$이므로, 입력 $e_i\otimes f_j$의 상에서 $e_a\otimes f_b$의 계수는 $A_{ai}B_{bj}$다. 행-block을 $a$, 열-block을 $i$로 묶으면 그 block은 $(b,j)$ 성분이 $A_{ai}B_{bj}$인 행렬, 곧 $A_{ai}B$이므로 정확히 위 block 행렬이다. $\blacksquare$

**Example (Kronecker product 계산).** $$A=\begin{pmatrix}1&2\\3&4\end{pmatrix},\qquad B=\begin{pmatrix}0&1\\1&0\end{pmatrix}$$이면 $$A\otimes B=\begin{pmatrix}0&1&0&2\\1&0&2&0\\0&3&0&4\\3&0&4&0\end{pmatrix}$$이다.

**Corollary (trace의 곱셈성).** $$\operatorname{tr}(S\otimes T)=\operatorname{tr}(S)\operatorname{tr}(T).$$

*Proof.* Kronecker product $A\otimes B$의 diagonal 성분은 block $(i,i)=A_{ii}B$의 diagonal 성분, 곧 $A_{ii}B_{jj}$이므로 $$\operatorname{tr}(S\otimes T)=\sum_{i,j}A_{ii}B_{jj}=\Big(\sum_iA_{ii}\Big)\Big(\sum_jB_{jj}\Big)=\operatorname{tr}(S)\operatorname{tr}(T)$$이다. $\blacksquare$

**Corollary (Determinant의 곱셈성).** $S:V\to V$, $T:W\to W$의 characteristic polynomial이 각각 $F$에서 일차식들의 곱으로 분해되면(eigenvalue $\lambda_1,\dots,\lambda_m$, $\mu_1,\dots,\mu_n$, multiplicity 포함), $$\det(S\otimes T)=(\det S)^{n}(\det T)^{m}.$$

*Proof.* [Cayley-Hamilton and Jordan form]({% post_url 2026-08-12-cayley-hamilton-and-jordan-form %})의 Triangularizability로 $S,T$의 basis를 각각 잘 골라 그 행렬 $A,B$가 upper triangular(대각 성분이 각각 $\lambda_1,\dots,\lambda_m$, $\mu_1,\dots,\mu_n$)가 되게 할 수 있다. basis $e_i\otimes f_j$를 $(i,j)$의 사전식 순서로 나열하면 $S\otimes T$의 행렬은 Kronecker product $A\otimes B$인데, $(i,j),(k,l)$ 성분이 $A_{ik}B_{jl}$이고 $(i,j)$가 사전식으로 $(k,l)$보다 뒤라면($i>k$이거나 $i=k,j>l$) $A,B$가 upper triangular라 이 성분이 $0$이다. 곧 $A\otimes B$도 upper triangular이고, 그 대각 성분(위치 $(i,j),(i,j)$)은 $A_{ii}B_{jj}=\lambda_i\mu_j$이므로 $$\det(S\otimes T)=\prod_{i,j}\lambda_i\mu_j=\Big(\prod_i\lambda_i\Big)^n\Big(\prod_j\mu_j\Big)^m=(\det S)^n(\det T)^m$$이다. $\blacksquare$

## Exterior algebra와 wedge product

**Definition (Algebra).** $F$ 위의 vector space $A$에 bilinear map $\cdot:A\times A\to A$(곱)이 주어져 있으면 $A$를 $F$ 위의 algebra라 한다. 이 곱이 associative, 즉 임의의 $a,b,c\in A$에 대해 $(a\cdot b)\cdot c=a\cdot(b\cdot c)$를 만족하면 $A$를 $F$ 위의 associative algebra라 한다.

**Definition (Graded Algebra).** Algebra $A$가 vector space로서 $A=\bigoplus_{k\ge0}A_k$로 decompose되고, 곱이 $A_p\cdot A_q\subseteq A_{p+q}$(임의의 $p,q\ge0$)를 만족하면 $A$를 graded algebra라 한다.

**Definition (Exterior Power).** $V^{\otimes k}$ 안에서, 어떤 자리에 같은 벡터가 두 번 나오는 $v_1\otimes\cdots\otimes v_k$($v_i=v_j$, $i\ne j$인 경우) 전체가 생성하는 부분공간을 $N_k$라 하면, $$\Lambda^kV:=V^{\otimes k}/N_k$$를 $k$번째 exterior power라 하고, $v_1\wedge\cdots\wedge v_k$를 $v_1\otimes\cdots\otimes v_k$의 $\Lambda^kV$에서의 image라 한다.

**Proposition (기본 성질).** $\wedge$는 $k$-linear이고 alternating이다: 두 자리를 바꾸면 부호가 바뀌고 $v_1,\dots,v_k$가 linearly dependent이면 $v_1\wedge\cdots\wedge v_k=0$이다.

*Proof.* $\otimes$가 $k$-linear이고 $\wedge$는 그 quotient map이므로 $\wedge$도 $k$-linear다. $v_i=v_j$($i\ne j$)이면 $v_1\otimes\cdots\otimes v_k\in N_k$(정의 그 자체)이므로 $v_1\wedge\cdots\wedge v_k=0$이다.

두 자리를 바꾸면 부호가 바뀐다는 것은 다음에서 나온다. $i,j$번째 자리에 똑같이 $v_i+v_j$를 넣으면 반복되는 벡터가 생기므로 $$v_1\wedge\cdots\wedge(v_i+v_j)\wedge\cdots\wedge(v_i+v_j)\wedge\cdots\wedge v_k=0$$이다. 좌변을 $k$-linear로 전개하면 $i,j$ 자리가 각각 $v_i,v_i$인 항과 $v_j,v_j$인 항은 반복되는 벡터가 있어 $0$이 되어 사라지고, $$v_1\wedge\cdots\wedge v_i\wedge\cdots\wedge v_j\wedge\cdots\wedge v_k+v_1\wedge\cdots\wedge v_j\wedge\cdots\wedge v_i\wedge\cdots\wedge v_k=0$$만 남으므로, $i,j$ 자리를 바꾸면 부호가 바뀐다.

$v_1,\dots,v_k$가 linearly dependent이면 어떤 $v_m=\sum_{l\ne m}c_lv_l$로 쓰이는데, 이를 $m$번째 자리에 넣고 $k$-linear로 전개하면 각 항에서 $v_l$이 $m$번째와 $l$번째 두 자리에 겹쳐 나와(반복되는 벡터라) 모든 항이 $0$이므로 $v_1\wedge\cdots\wedge v_k=0$이다. $\blacksquare$

**Definition (Exterior Algebra).** $$\Lambda(V):=\bigoplus_{k=0}^n\Lambda^kV\qquad(\Lambda^0V:=F,\ \Lambda^1V:=V)$$는 곱을 basic wedge의 concatenation $$(v_1\wedge\cdots\wedge v_p)\wedge(w_1\wedge\cdots\wedge w_q):=v_1\wedge\cdots\wedge v_p\wedge w_1\wedge\cdots\wedge w_q\in\Lambda^{p+q}V$$로 정의하면 associative algebra를 이룬다. 이 곱은 $\Lambda^pV\wedge\Lambda^qV\subseteq\Lambda^{p+q}V$를 만족하므로 $\Lambda(V)$는 graded algebra이기도 하다.

**Proposition (Graded Commutativity).** $\alpha\in\Lambda^pV$, $\beta\in\Lambda^qV$이면 $$\alpha\wedge\beta=(-1)^{pq}\beta\wedge\alpha.$$

*Proof.* $\alpha=v_1\wedge\cdots\wedge v_p$, $\beta=w_1\wedge\cdots\wedge w_q$인 경우만 보면 충분하다(일반적인 경우는 이런 basic wedge들의 일차결합이므로 선형성으로 확장된다). $v_1\wedge\cdots\wedge v_p\wedge w_1\wedge\cdots\wedge w_q$에서 $w_1$을 인접한 자리를 바꾸는 $p$번의 swap으로 맨 앞까지 옮기면 부호가 $(-1)^p$ 붙고, 같은 방식으로 $w_2,\dots,w_q$를 차례로 $v$들 앞으로 옮기면 전체 $pq$번의 swap, 곧 $(-1)^{pq}$가 붙어 $\beta\wedge\alpha=w_1\wedge\cdots\wedge w_q\wedge v_1\wedge\cdots\wedge v_p$가 된다. $\blacksquare$

**Theorem (차원).** $\dim V=n$, basis $e_1,\dots,e_n$이면 $$\{e_{i_1}\wedge\cdots\wedge e_{i_k}:1\le i_1<\cdots<i_k\le n\}$$이 $\Lambda^kV$의 basis이고, $\dim\Lambda^kV=\binom nk$다.

*Proof.* 먼저 span함을 보이자. $V^{\otimes k}$가 basis tensor $e_{j_1}\otimes\cdots\otimes e_{j_k}$($1\le j_1,\dots,j_k\le n$, 순서·중복 무관) 전체로 span된다는 것은 Dimension Corollary의 증명과 같은 방식(각 $v_l$을 basis로 전개해 $k$-linear로 펼치는 것)으로 확인되므로, 그 quotient인 $\Lambda^kV$는 $e_{j_1}\wedge\cdots\wedge e_{j_k}$ 전체로 span된다. 이 중 어떤 두 index가 같으면 위 Proposition으로 $0$이고, 서로 다르면 오름차순으로 재배열할 때 같은 Proposition의 부호 규칙으로 부호만 바뀌므로, 결국 오름차순 index $I=(i_1<\cdots<i_k)$인 $e_{i_1}\wedge\cdots\wedge e_{i_k}$들만으로도 span된다.

다음으로 일차독립을 보이자. 오름차순 $I=(i_1<\cdots<i_k)$마다 $$\varphi_I(v_1,\dots,v_k):=\det\big((v_l)_{i_m}\big)_{m,l=1}^k$$($(v_l)\_{i_m}$은 $v_l$의 $e_{i_m}$ 방향 좌표)로 두면, determinant가 각 행·열에 alternating multilinear이므로([Determinant]({% post_url 2026-08-09-determinant %}) 글) $\varphi_I$는 $v_1,\dots,v_k$에 대해 alternating $k$-linear form이다. Tensor product의 universal property($U=F$인 경우)로 $\varphi_I$는 linear map $\Phi_I:V^{\otimes k}\to F$를 유도하는데, $\varphi_I$가 alternating이라는 것은 정확히 $\Phi_I$가 $N_k$(반복되는 벡터들이 생성하는 부분공간) 위에서 $0$이라는 뜻이므로, $\Phi_I$는 quotient를 타고 내려가는 linear functional $\overline\Phi_I:\Lambda^kV\to F$를 준다. 오름차순 $J=(j_1<\cdots<j_k)$에 대해 $J\ne I$이면 어떤 $i_m\notin J$가 있어 그 행이 전부 $0$이 되므로 $\varphi_I(e_{j_1},\dots,e_{j_k})=0$이고, $J=I$이면 단위행렬의 determinant라 $1$이니, $\overline\Phi_I(e_{j_1}\wedge\cdots\wedge e_{j_k})=\delta_{IJ}$다. 따라서 $\sum_Jc_J\,e_{j_1}\wedge\cdots\wedge e_{j_k}=0$에 $\overline\Phi_I$를 적용하면 $c_I=0$이 나오므로 일차독립이다. $\blacksquare$

**Corollary.** $k>n$이면 $$\Lambda^kV=\{0\}$$이다($\binom nk=0$). $k=n$이면 $\dim\Lambda^nV=1$이다.

**Example.** $\mathbb{R}^3$에서 $\Lambda^2\mathbb{R}^3$은 $\binom32=3$차원이고, $e_1\wedge e_2,e_2\wedge e_3,e_3\wedge e_1$이 그 basis다. $u\wedge v$의 이 basis에서의 좌표는 정확히 cross product $u\times v$의 좌표와 같다(성분을 직접 전개하면 확인된다): $$u\wedge v=(u_2v_3-u_3v_2)\,e_2\wedge e_3+(u_3v_1-u_1v_3)\,e_3\wedge e_1+(u_1v_2-u_2v_1)\,e_1\wedge e_2.$$ 곧 cross product는 $3$차원에서만 통하는 wedge product의 특수한 얼굴이다. 이는 나중에 de Rham cohomology와도 연계되는 개념이다.

**Definition (Linear map의 Wedge Product).** $T:V\to V$에 대해 $$\Lambda^kT:\Lambda^kV\to\Lambda^kV,\qquad\Lambda^kT(v_1\wedge\cdots\wedge v_k):=Tv_1\wedge\cdots\wedge Tv_k$$로 정의한다(우변이 $k$-linear·alternating을 그대로 물려받으므로 basic wedge에서 정의한 뒤 선형으로 잘 확장된다).

**Proposition (합성).** $$\Lambda^k(S\circ T)=\Lambda^kS\circ\Lambda^kT.$$

*Proof.* basic wedge에 대입하면 $$\Lambda^k(ST)(v_1\wedge\cdots\wedge v_k)=STv_1\wedge\cdots\wedge STv_k=\Lambda^kS(Tv_1\wedge\cdots\wedge Tv_k)=\Lambda^kS\big(\Lambda^kT(v_1\wedge\cdots\wedge v_k)\big)$$로 양변이 basic wedge 위에서 일치하고, 이들이 span하므로 전체에서 일치한다. $\blacksquare$

**Theorem (Determinant는 $\Lambda^n$의 scaling factor).** $k=n$인 경우 $\Lambda^nV$가 $1$차원이므로 $\Lambda^nT$는 어떤 스칼라를 곱하는 map이고, 그 스칼라는 $\det T$다.

*Proof.* basis $e_1,\dots,e_n$에서 $Te_j=\sum_iA_{ij}e_i$이므로 $$Te_1\wedge\cdots\wedge Te_n=\sum_{i_1,\dots,i_n}A_{i_11}\cdots A_{i_nn}\,e_{i_1}\wedge\cdots\wedge e_{i_n}$$인데, alternating이라 $i_1,\dots,i_n$에 중복이 있으면 $0$이 되어 permutation $\sigma$인 경우만 남고, $e_{\sigma(1)}\wedge\cdots\wedge e_{\sigma(n)}=\operatorname{sgn}(\sigma)\,e_1\wedge\cdots\wedge e_n$이므로 $$Te_1\wedge\cdots\wedge Te_n=\Big(\sum_\sigma\operatorname{sgn}(\sigma)A_{\sigma(1)1}\cdots A_{\sigma(n)n}\Big)e_1\wedge\cdots\wedge e_n=\det(A)\,e_1\wedge\cdots\wedge e_n$$이다([Determinant]({% post_url 2026-08-09-determinant %}) 글의 Leibniz formula, 정확히 이 식이다). $\blacksquare$

determinant의 alternating multilinear한 성격, Leibniz formula, 그리고 "$n$개를 넘는 벡터는 언제나 일차종속"이라는 사실(그래서 $k>n$에서 $\Lambda^kV=0$)이 모두 이 하나의 $1$차원 공간 $\Lambda^nV$로부터 나온다.

**Definition (Orientation).** $\dim\Lambda^nV=1$이므로, $\Lambda^nV\setminus\lbrace 0\rbrace $ 위에 $$\omega\sim\omega'\;:\Leftrightarrow\;\omega'=c\omega\text{인 }c>0\text{이 존재}$$로 동치관계를 주면 동치류가 정확히 두 개 나온다. 이 두 동치류 중 하나를 고르는 것을 $V$에 orientation을 준다고 하고, 그 동치류의 대표 $\omega\in\Lambda^nV\setminus\lbrace 0\rbrace $를 명시해 $(V,\omega)$를 oriented vector space라 한다.

**Remark.** $\Lambda^nV\setminus\lbrace 0\rbrace$ 위에서 고른 원소는 $V$의 basis들의 wedge product이다. $\omega \sim \omega'$인 것은 각각을 이루는 basis 간의 change-of-basis 행렬 $P$의 determinant가 양수인 것과 동치이다. ($c=\det P$)

**Theorem (Wedge product의 dual).** 자연스러운 isomorphism $$\Lambda^k(V^*)\cong(\Lambda^kV)^*$$가 성립하고, 이는 $V$ 위의 alternating $k$-linear form 전체([Bilinear forms, quadratic forms, and positive operators]({% post_url 2026-08-15-bilinear-quadratic-forms-and-positive-operators %}))와 정확히 같은 공간이다.

*Proof.* $\varphi_1,\dots,\varphi_k\in V^\ast $에 대해 $$(\varphi_1\wedge\cdots\wedge\varphi_k)(v_1,\dots,v_k):=\det\big(\varphi_i(v_j)\big)$$($k\times k$ 행렬의 determinant)로 두면, determinant가 각 행·열에 alternating multilinear이므로([Determinant]({% post_url 2026-08-09-determinant %}) 글) 우변은 $v_1,\dots,v_k$에 대해서도 $\varphi_1,\dots,\varphi_k$에 대해서도 alternating $k$-linear다. basis $e_1,\dots,e_n$과 dual basis $e_1^\ast ,\dots,e_n^\ast $에서 오름차순 첨자 $I,J$마다 $$\big(e_{i_1}^*\wedge\cdots\wedge e_{i_k}^*\big)(e_{j_1},\dots,e_{j_k})=\delta_{IJ}$$이므로(대각 성분만 $1$인 permutation matrix의 determinant), $\Lambda^k(V^\ast )$의 basis $$\{e_{i_1}^*\wedge\cdots\wedge e_{i_k}^*\}$$가 $\Lambda^kV$의 basis에 대한 dual basis로 정확히 대응해 isomorphism을 준다. $\blacksquare$

**Theorem (Direct Sum의 Exterior Power).** $$\Lambda^k(V\oplus W)\cong\bigoplus_{i+j=k}\Lambda^iV\otimes\Lambda^jW.$$

*Proof.* $V,W\subseteq V\oplus W$로 보면 $(\alpha,\beta)\mapsto\alpha\wedge\beta$($\alpha\in\Lambda^iV$, $\beta\in\Lambda^jW$)가 $\Lambda^iV\times\Lambda^jW\to\Lambda^k(V\oplus W)$인 bilinear map이라 Tensor product 절의 universal property로 $\Lambda^iV\otimes\Lambda^jW\to\Lambda^k(V\oplus W)$인 map이 나오고, $i+j=k$에서 모두 모으면 $$\bigoplus_{i+j=k}\Lambda^iV\otimes\Lambda^jW\longrightarrow\Lambda^k(V\oplus W)$$가 된다. $V$의 basis $e_1,\dots,e_m$과 $W$의 basis $f_1,\dots,f_n$을 합친 것이 $V\oplus W$의 basis이므로, 양쪽에서 오름차순 첨자로 basis를 세면 차원이 $$\dim\Lambda^k(V\oplus W)=\binom{m+n}k=\sum_{i+j=k}\binom mi\binom nj=\sum_{i+j=k}\dim(\Lambda^iV\otimes\Lambda^jW)$$로 같다(Vandermonde의 항등식). 위 map이 각 첨자 조합의 basis 원소를 서로 다른 basis 원소로 보내므로(오름차순으로 $V$쪽 $i$개, $W$쪽 $j$개를 뽑아 합친 것과 정확히 대응) basis를 basis로 보내는 isomorphism이다. $\blacksquare$

이 글에서 다룬, $k$개의 벡터가 만드는 도형의 넓이·부피 같은 대상을 좌표 없이 다루기 위해 곱을 $k$-linear하면서 alternating이도록 요구하는 관점의 뿌리는 Hermann Grassmann이 1844년 《Die lineale Ausdehnungslehre》에서 세운 확장론이다 [2]. Grassmann은 오늘날의 vector space, 일차독립, 차원, 그리고 wedge product에 해당하는 것을 이미 담았지만, 서술이 지나치게 추상적이고 철학적이어서 당대에는 거의 읽히지 않았고 수십 년이 지나서야 제대로 평가받았다.

## 참고문헌

1. Samuel, P. (1948). On universal mappings and free topological groups. *Bulletin of the American Mathematical Society*, 54(6), 591–598.
2. Grassmann, H. (1844). *Die lineale Ausdehnungslehre, ein neuer Zweig der Mathematik*. Leipzig: Otto Wigand.
