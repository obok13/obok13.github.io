---
layout: post
title: "Tensor product and exterior algebra"
date: 2026-08-17
mathematicians: [Grassmann]
---

## Tensor product

**Definition (Tensor Product).** 유한차원 $V,W$에 대해 basis $v_1,\dots,v_m$($V$), $w_1,\dots,w_n$($W$)를 고르고, 형식적 기호 $v_i\otimes w_j$($1\le i\le m$, $1\le j\le n$)를 basis로 갖는 $mn$차원 vector space를 $V\otimes W$라 하자. $v=\sum_ic_iv_i$, $w=\sum_jd_jw_j$에 대해 $$v\otimes w:=\sum_{i,j}c_id_j\,(v_i\otimes w_j)$$로 두면 $\otimes:V\times W\to V\otimes W$는 bilinear map이다.

**Proposition (Dimension).** $\dim(V\otimes W)=(\dim V)(\dim W)$.

*Proof.* 정의에서 $v_i\otimes w_j$($1\le i\le m$, $1\le j\le n$)가 basis이므로 그 개수 $mn=(\dim V)(\dim W)$가 차원이다. $\blacksquare$

**Theorem (Universal Property).** 임의의 bilinear map $B:V\times W\to U$에 대해, $B=L\circ\otimes$인 linear map $L:V\otimes W\to U$가 유일하게 존재한다.

*Proof.* basis 위에서 $L(v_i\otimes w_j):=B(v_i,w_j)$로 정의하고 선형으로 확장하면(basis에서의 값이 $L$을 결정하므로 well-defined) $$L(v\otimes w)=L\Big(\sum_{i,j}c_id_j\,v_i\otimes w_j\Big)=\sum_{i,j}c_id_jB(v_i,w_j)=B\Big(\sum_ic_iv_i,\sum_jd_jw_j\Big)=B(v,w)$$이다(마지막 등호는 $B$가 bilinear라는 데서 나온다). 유일성은, $L,L'$이 둘 다 $L\circ\otimes=L'\circ\otimes=B$를 만족하면 basis $v_i\otimes w_j=\otimes(v_i,w_j)$ 위에서 $L,L'$이 일치하고 이것이 basis 전체이므로 $L=L'$이기 때문이다. $\blacksquare$

Linear map 글의 Quotient space 절에서 본 universal property(quotient map이 $W$를 $0$으로 만드는 map을 가장 경제적으로 담는 것)와 같은 패턴이다. 여기서는 "bilinear한 것을 linear로 바꾸는" 가장 경제적인 대상이 $V\otimes W$다.

**Remark (basis 무관성).** $V\otimes W$의 정의는 basis 선택에 의존하는 듯 보이지만, 다른 basis로 만든 $(V\otimes W)'$의 $\otimes':V\times W\to(V\otimes W)'$도 bilinear map이므로 universal property로 $\Phi:V\otimes W\to(V\otimes W)'$인 linear map이(그리고 대칭적으로 반대 방향 $\Psi$도) 유일하게 나온다. $\Psi\circ\Phi$는 $\otimes$를 보존하는 $V\otimes W\to V\otimes W$인 map인데 identity도 그런 map이라 유일성으로 $\Psi\circ\Phi=\mathrm{id}$이고 마찬가지로 $\Phi\circ\Psi=\mathrm{id}$이므로, $V\otimes W\cong(V\otimes W)'$이 basis 선택과 무관하게 표준적으로 성립한다.

**Corollary.** bilinear form $B:V\times W\to F$ 전체는 $\operatorname{Hom}(V\otimes W,F)=(V\otimes W)^*$와 (universal property에서 $U=F$로 두어 나오는 $B\leftrightarrow L$ 대응으로) 동일시된다.

bilinear map은 한 인수를 고정하면 나머지 인수에 대한 linear map이 되므로, universal property를 이렇게 "커링(currying)"해도 정보가 그대로 보존된다.

**Theorem (Tensor-Hom Adjunction).** 자연스러운 isomorphism $$\operatorname{Hom}(U\otimes V,W)\cong\operatorname{Hom}(U,\operatorname{Hom}(V,W))$$가 성립한다.

*Proof.* $L:U\otimes V\to W$가 주어지면 각 $u\in U$마다 $v\mapsto L(u\otimes v)$가 $V\to W$인 linear map이고, $u\mapsto\big(v\mapsto L(u\otimes v)\big)$ 자체도 $u$에 대해 linear이므로(둘 다 $L$과 $\otimes$가 각 인수에 linear라는 데서 나온다) 이는 $\Phi(L)\in\operatorname{Hom}(U,\operatorname{Hom}(V,W))$를 정의한다. 역으로 $\Psi:U\to\operatorname{Hom}(V,W)$가 주어지면 $(u,v)\mapsto\Psi(u)(v)$가 $U\times V\to W$인 bilinear map이므로(각 인수에 대한 선형성이 $\Psi$의 선형성과 각 $\Psi(u)$의 선형성에서 각각 나온다), universal property로 유일한 $\Theta(\Psi)\in\operatorname{Hom}(U\otimes V,W)$가 나온다. $\Phi,\Theta$가 basic tensor $u\otimes v$ 위에서 서로 역임이 정의에서 바로 확인되므로 둘은 서로 역인 isomorphism이다. $\blacksquare$

$W=F$로 두면 앞의 Corollary가 다시 나오는데, 여기서 한 걸음 더 나아가 $$\operatorname{Hom}(U\otimes V,F)\cong\operatorname{Hom}(U,\operatorname{Hom}(V,F))=\operatorname{Hom}(U,V^*)$$이므로, $U,V$ 위의 bilinear form 전체는 $U$에서 $V^*$로 가는 linear map 전체와도 동일시된다(한 벡터 $u$를 넣으면 $B(u,\cdot)\in V^*$를 내놓는 대응이다).

**Proposition (기본 법칙).** 자연스러운 isomorphism으로 다음이 성립한다. $$V\otimes W\cong W\otimes V\quad\text{(교환)},\qquad(U\otimes V)\otimes W\cong U\otimes(V\otimes W)\quad\text{(결합)},$$ $$U\otimes(V\oplus W)\cong(U\otimes V)\oplus(U\otimes W)\quad\text{(분배)},\qquad(V\otimes W)^*\cong V^*\otimes W^*\quad\text{(dual)}.$$

*Proof.* 교환: $(v,w)\mapsto w\otimes v$가 $V\times W\to W\otimes V$인 bilinear map이므로 universal property로 $V\otimes W\to W\otimes V$인 linear map이 나오고, 대칭적으로 반대 방향도 나와(basis에서 서로 역임이 확인된다) 서로 역이다. 결합·분배도 양쪽의 자연스러운 basis(각각 $u_i\otimes v_j\otimes w_k$류, $u_i\otimes v_j$와 $u_i\otimes w_k$류)를 대응시키는 같은 논증으로 확인된다. dual: basis에서 $(v_i\otimes w_j)^*\leftrightarrow v_i^*\otimes w_j^*$의 대응이 $$\big(v_i^*\otimes w_j^*\big)(v_k\otimes w_l):=v_i^*(v_k)\,w_j^*(w_l)=\delta_{ik}\delta_{jl}$$을 만족해 정확히 dual basis를 주므로 isomorphism이다. $\blacksquare$

**Example.** $\operatorname{Hom}(V,W)\cong V^*\otimes W$다: $\varphi\otimes w$($\varphi\in V^*$, $w\in W$)를 rank $1$(또는 $0$) linear map $v\mapsto\varphi(v)w$로 대응시키면, 차원이 같고($\dim(V^*\otimes W)=(\dim V)(\dim W)=\dim\operatorname{Hom}(V,W)$) $v_i^*\otimes w_j$가 $(i,j)$ 성분만 $1$인 표준 행렬 단위 $E_{ji}$에 대응함을 확인하면 isomorphism임이 보인다.

**Example (trace는 evaluation pairing이다).** $W=V$인 경우를 보면, $\operatorname{Hom}(V,V)\cong V^*\otimes V$라는 위 대응 아래 trace는 정확히 evaluation map(또는 contraction) $$V^*\otimes V\to F,\qquad\varphi\otimes v\mapsto\varphi(v)$$에 대응한다. 실제로 basis $e_1,\dots,e_n$과 dual basis $e_1^*,\dots,e_n^*$에서 $\varphi\otimes v$에 대응하는 linear map $u\mapsto\varphi(u)v$의 행렬은 $(i,j)$ 성분이 $\varphi(e_j)v_i$이므로, 그 trace는 $$\sum_i\varphi(e_i)v_i=\varphi\Big(\sum_iv_ie_i\Big)=\varphi(v)$$로 정확히 evaluation 값과 같다.

**Example.** $V=W=\mathbb{R}^2$에서 $\dim(V\otimes W)=4$이고, $e_1\otimes e_1,e_1\otimes e_2,e_2\otimes e_1,e_2\otimes e_2$가 basis다. $$(1,1)\otimes(1,-1)=e_1\otimes e_1-e_1\otimes e_2+e_2\otimes e_1-e_2\otimes e_2$$처럼 전개된다.

**Example (simple tensor가 아닌 원소).** 같은 $V\otimes W=\mathbb{R}^2\otimes\mathbb{R}^2$에서 $e_1\otimes e_1+e_2\otimes e_2$는 어떤 $v,w\in\mathbb{R}^2$에 대해서도 $v\otimes w$ 꼴로 쓰이지 않는다. basis $e_i\otimes e_j$에서의 좌표를 행렬 $C=(c_{ij})$로 모으면, $v\otimes w=\sum_{i,j}v_iw_j\,e_i\otimes e_j$의 좌표행렬은 $vw^{\mathsf T}$(rank가 $0$ 또는 $1$)인 반면, $e_1\otimes e_1+e_2\otimes e_2$의 좌표행렬은 $I$로 rank가 $2$이기 때문이다. 이렇게 simple tensor들의 합으로만 표현되는 "얽힌(entangled)" 원소가 존재한다는 것이 $V\otimes W$가 $V\times W$보다 훨씬 큰 대상이라는 사실의 정확한 의미다.

**Example (다항식).** 유한차원을 넘어서면 $F[x]\otimes F[y]\cong F[x,y]$(두 변수 polynomial, $x^i\otimes y^j\leftrightarrow x^iy^j$)도 성립한다. 이 글은 유한차원만 다루지만, tensor product의 universal property 자체는 무한차원에서도(구성만 약간 손보면) 통한다.

**Theorem (다중 tensor product과 multilinear map).** $V_1\otimes\cdots\otimes V_k$를 같은 방식으로 정의하면, $k$-linear map $V_1\times\cdots\times V_k\to U$ 전체는 linear map $V_1\otimes\cdots\otimes V_k\to U$ 전체와 (같은 universal property로) 일대일 대응한다. 특히 $k$-linear form(Bilinear forms, quadratic forms, and positive operators 글)은 $(V^{\otimes k})^*$의 원소다.

**Definition (Linear map의 Tensor Product).** $S:V_1\to W_1$, $T:V_2\to W_2$에 대해 $(v,w)\mapsto Sv\otimes Tw$는 $V_1\times V_2\to W_1\otimes W_2$인 bilinear map이므로, universal property로 $$S\otimes T:V_1\otimes V_2\to W_1\otimes W_2,\qquad(S\otimes T)(v\otimes w)=Sv\otimes Tw$$인 linear map이 유일하게 정해진다.

**Proposition (합성).** 합성 가능할 때 $$(S_1\otimes T_1)\circ(S_2\otimes T_2)=(S_1\circ S_2)\otimes(T_1\circ T_2).$$

*Proof.* 양변을 $v\otimes w$ 꼴(이들이 span하므로 이걸로 충분하다)에 적용하면 $$(S_1\otimes T_1)\big((S_2\otimes T_2)(v\otimes w)\big)=(S_1\otimes T_1)(S_2v\otimes T_2w)=S_1S_2v\otimes T_1T_2w=\big((S_1S_2)\otimes(T_1T_2)\big)(v\otimes w)$$로 일치한다. $\blacksquare$

$S,T$가 각각 eigenvector를 가지면 그 tensor도 eigenvector가 된다.

**Proposition ($S\otimes T$의 eigenvalue).** $S:V\to V$, $T:W\to W$가 $Sv=\lambda v$, $Tw=\mu w$인 eigenvector $v,w$를 가지면, $v\otimes w$는 $S\otimes T$의 eigenvalue $\lambda\mu$짜리 eigenvector다. 특히 $S,T$가 각각 eigenbasis $v_1,\dots,v_m$(eigenvalue $\lambda_i$), $w_1,\dots,w_n$(eigenvalue $\mu_j$)로 diagonalizable이면, $S\otimes T$는 eigenbasis $v_i\otimes w_j$로 diagonalizable이고 그 eigenvalue 전체가 $$\{\lambda_i\mu_j\}$$다.

*Proof.* $(S\otimes T)(v\otimes w)=Sv\otimes Tw=\lambda v\otimes\mu w=\lambda\mu\,(v\otimes w)$이다. $S,T$가 각각 eigenbasis를 가지면 $v_i\otimes w_j$들이(basis의 tensor라) $V\otimes W$의 basis를 이루고, 각각이 이 계산으로 eigenvalue $\lambda_i\mu_j$의 eigenvector이므로 $S\otimes T$가 이 basis에서 diagonal이다. $\blacksquare$

좌표로 내려가면 $S\otimes T$의 행렬은 두 행렬의 성분을 모두 곱해 이어붙인 꼴이 된다.

**Proposition (Kronecker product).** $S:F^m\to F^p$, $T:F^n\to F^q$의 행렬이 각각 $A,B$이면, basis $e_i\otimes f_j$를 $(i,j)$의 사전식 순서로 나열한 좌표에서 $S\otimes T$의 행렬은 $(pq)\times(mn)$ Kronecker product
$$A\otimes B:=\begin{pmatrix}A_{11}B&\cdots&A_{1m}B\\\vdots&&\vdots\\A_{p1}B&\cdots&A_{pm}B\end{pmatrix}$$
이다.

*Proof.* $$(S\otimes T)(e_i\otimes f_j)=Se_i\otimes Tf_j=\Big(\sum_aA_{ai}e_a\Big)\otimes\Big(\sum_bB_{bj}f_b\Big)=\sum_{a,b}A_{ai}B_{bj}\,(e_a\otimes f_b)$$이므로, 입력 $e_i\otimes f_j$의 상에서 $e_a\otimes f_b$의 계수는 $A_{ai}B_{bj}$다. 행-block을 $a$, 열-block을 $i$로 묶으면 그 block은 $(b,j)$ 성분이 $A_{ai}B_{bj}$인 행렬, 곧 $A_{ai}B$이므로 정확히 위 block 행렬이다. $\blacksquare$

**Example (Kronecker product 계산).** $$A=\begin{pmatrix}1&2\\3&4\end{pmatrix},\qquad B=\begin{pmatrix}0&1\\1&0\end{pmatrix}$$이면 $$A\otimes B=\begin{pmatrix}0&1&0&2\\1&0&2&0\\0&3&0&4\\3&0&4&0\end{pmatrix}$$이다.

**Corollary (trace의 곱셈성).** $$\operatorname{tr}(S\otimes T)=\operatorname{tr}(S)\operatorname{tr}(T).$$

*Proof.* Kronecker product $A\otimes B$의 diagonal 성분은 block $(i,i)=A_{ii}B$의 diagonal 성분, 곧 $A_{ii}B_{jj}$이므로 $$\operatorname{tr}(S\otimes T)=\sum_{i,j}A_{ii}B_{jj}=\Big(\sum_iA_{ii}\Big)\Big(\sum_jB_{jj}\Big)=\operatorname{tr}(S)\operatorname{tr}(T)$$이다. $\blacksquare$

## Exterior algebra와 wedge product

Bilinear forms, quadratic forms, and positive operators 글에서 "alternating multilinear 관점을 $k<n$개의 변수로 넓히면 exterior algebra가 나온다"고 미뤄 둔 것이 이것이다.

**Definition (Exterior Power).** $V^{\otimes k}$ 안에서, 어떤 자리에 같은 벡터가 두 번 나오는 $v_1\otimes\cdots\otimes v_k$($v_i=v_j$, $i\ne j$인 경우) 전체가 생성하는 부분공간을 $N_k$라 하면, $$\Lambda^kV:=V^{\otimes k}/N_k$$를 $k$번째 exterior power라 하고, $v_1\wedge\cdots\wedge v_k$를 $v_1\otimes\cdots\otimes v_k$의 $\Lambda^kV$에서의 image라 한다.

**Proposition (기본 성질).** $\wedge$는 $k$-linear이고 alternating이다: 두 자리를 바꾸면 부호가 바뀌고(Bilinear forms, quadratic forms, and positive operators 글의 Proposition, 표수가 $2$가 아니면 antisymmetric과 alternating이 같은 뜻임을 이미 보았다), $v_1,\dots,v_k$가 일차종속이면(특히 두 개가 같으면) $v_1\wedge\cdots\wedge v_k=0$이다.

*Proof.* $k$-linear임과 두 자리를 바꾸면 부호가 바뀐다는 것은 정의(같은 벡터가 겹치면 $0$)에서 나온다. $v_1,\dots,v_k$가 일차종속이면 어떤 $v_i=\sum_{j\ne i}c_jv_j$로 쓰이는데, 이를 $\wedge$에 넣고 $k$-linear로 전개하면 각 항이 $v_j$가 $i$번째와 $j$번째 두 자리에 겹쳐 나오는 항들의 합이 되어(alternating이므로) 모두 $0$이다. $\blacksquare$

**Proposition (Graded Commutativity).** $\alpha\in\Lambda^pV$, $\beta\in\Lambda^qV$이면 $$\alpha\wedge\beta=(-1)^{pq}\beta\wedge\alpha.$$

*Proof.* $\alpha=v_1\wedge\cdots\wedge v_p$, $\beta=w_1\wedge\cdots\wedge w_q$인 경우만 보면 충분하다(일반적인 경우는 이런 basic wedge들의 일차결합이므로 선형성으로 확장된다). $v_1\wedge\cdots\wedge v_p\wedge w_1\wedge\cdots\wedge w_q$에서 $w_1$을 인접한 자리를 바꾸는 $p$번의 swap으로 맨 앞까지 옮기면 부호가 $(-1)^p$ 붙고, 같은 방식으로 $w_2,\dots,w_q$를 차례로 $v$들 앞으로 옮기면 전체 $pq$번의 swap, 곧 $(-1)^{pq}$가 붙어 $\beta\wedge\alpha=w_1\wedge\cdots\wedge w_q\wedge v_1\wedge\cdots\wedge v_p$가 된다. $\blacksquare$

**Theorem (차원).** $\dim V=n$, basis $e_1,\dots,e_n$이면 $$\{e_{i_1}\wedge\cdots\wedge e_{i_k}:1\le i_1<\cdots<i_k\le n\}$$이 $\Lambda^kV$의 basis이고, $\dim\Lambda^kV=\binom nk$다.

*Proof(스케치).* $\wedge$가 alternating이라 첨자를 오름차순으로 재배열해도(부호만 바뀌므로) 임의의 $v_1\wedge\cdots\wedge v_k$가 이 basis 원소들의 일차결합으로 써지니 span한다. 일차독립은, 오름차순 첨자 $I=(i_1<\cdots<i_k)$마다 $v_1,\dots,v_k$의 $e_{i_1},\dots,e_{i_k}$ 방향 좌표들로 만든 $k\times k$ 부분행렬의 determinant를 주는 alternating $k$-linear form $\varphi_I$를 만들 수 있고, 오름차순 첨자 $J$에서 $\varphi_I(e_{j_1},\dots,e_{j_k})=\delta_{IJ}$이므로, $\sum_Ic_I\,e_{i_1}\wedge\cdots\wedge e_{i_k}=0$에 각 $\varphi_I$를 적용하면 $c_I=0$이 나온다.

**Corollary.** $k>n$이면 $$\Lambda^kV=\{0\}$$이다($\binom nk=0$). $k=n$이면 $\dim\Lambda^nV=1$이다.

$\Lambda^nV$가 $1$차원이라는 사실이 determinant의 진짜 정체다.

**Definition (Linear map의 Wedge Product).** $T:V\to V$에 대해 $$\Lambda^kT:\Lambda^kV\to\Lambda^kV,\qquad\Lambda^kT(v_1\wedge\cdots\wedge v_k):=Tv_1\wedge\cdots\wedge Tv_k$$로 정의한다(우변이 $k$-linear·alternating을 그대로 물려받으므로 basic wedge에서 정의한 뒤 선형으로 잘 확장된다).

**Proposition (합성).** $$\Lambda^k(S\circ T)=\Lambda^kS\circ\Lambda^kT.$$

*Proof.* basic wedge에 대입하면 $$\Lambda^k(ST)(v_1\wedge\cdots\wedge v_k)=STv_1\wedge\cdots\wedge STv_k=\Lambda^kS(Tv_1\wedge\cdots\wedge Tv_k)=\Lambda^kS\big(\Lambda^kT(v_1\wedge\cdots\wedge v_k)\big)$$로 양변이 basic wedge 위에서 일치하고, 이들이 span하므로 전체에서 일치한다. $\blacksquare$

**Theorem (Determinant는 $\Lambda^n$의 scaling factor).** $k=n$인 경우 $\Lambda^nV$가 $1$차원이므로 $\Lambda^nT$는 어떤 스칼라를 곱하는 map이고, 그 스칼라는 $\det T$다.

*Proof.* basis $e_1,\dots,e_n$에서 $Te_j=\sum_iA_{ij}e_i$이므로 $$Te_1\wedge\cdots\wedge Te_n=\sum_{i_1,\dots,i_n}A_{i_11}\cdots A_{i_nn}\,e_{i_1}\wedge\cdots\wedge e_{i_n}$$인데, alternating이라 $i_1,\dots,i_n$에 중복이 있으면 $0$이 되어 permutation $\sigma$인 경우만 남고, $e_{\sigma(1)}\wedge\cdots\wedge e_{\sigma(n)}=\operatorname{sgn}(\sigma)\,e_1\wedge\cdots\wedge e_n$이므로 $$Te_1\wedge\cdots\wedge Te_n=\Big(\sum_\sigma\operatorname{sgn}(\sigma)A_{\sigma(1)1}\cdots A_{\sigma(n)n}\Big)e_1\wedge\cdots\wedge e_n=\det(A)\,e_1\wedge\cdots\wedge e_n$$이다(Determinant 글의 Leibniz formula, 정확히 이 식이다). $\blacksquare$

determinant의 alternating multilinear한 성격, Leibniz formula, 그리고 "$n$개를 넘는 벡터는 언제나 일차종속"이라는 사실(그래서 $k>n$에서 $\Lambda^kV=0$)이 모두 이 하나의 $1$차원 공간 $\Lambda^nV$로부터 나온다.

**Theorem (Wedge product의 dual).** 자연스러운 isomorphism $$\Lambda^k(V^*)\cong(\Lambda^kV)^*$$가 성립하고, 이는 $V$ 위의 alternating $k$-linear form 전체(Bilinear forms, quadratic forms, and positive operators 글)와 정확히 같은 공간이다.

*Proof.* $\varphi_1,\dots,\varphi_k\in V^*$에 대해 $$(\varphi_1\wedge\cdots\wedge\varphi_k)(v_1,\dots,v_k):=\det\big(\varphi_i(v_j)\big)$$($k\times k$ 행렬의 determinant)로 두면, determinant가 각 행·열에 alternating multilinear이므로(Determinant 글) 우변은 $v_1,\dots,v_k$에 대해서도 $\varphi_1,\dots,\varphi_k$에 대해서도 alternating $k$-linear다. basis $e_1,\dots,e_n$과 dual basis $e_1^*,\dots,e_n^*$에서 오름차순 첨자 $I,J$마다 $$\big(e_{i_1}^*\wedge\cdots\wedge e_{i_k}^*\big)(e_{j_1},\dots,e_{j_k})=\delta_{IJ}$$이므로(대각 성분만 $1$인 permutation matrix의 determinant), $\Lambda^k(V^*)$의 basis $$\{e_{i_1}^*\wedge\cdots\wedge e_{i_k}^*\}$$가 $\Lambda^kV$의 basis에 대한 dual basis로 정확히 대응해 isomorphism을 준다. $\blacksquare$

**Theorem (Direct Sum의 Exterior Power).** $$\Lambda^k(V\oplus W)\cong\bigoplus_{i+j=k}\Lambda^iV\otimes\Lambda^jW.$$

*Proof.* $V,W\subseteq V\oplus W$로 보면 $(\alpha,\beta)\mapsto\alpha\wedge\beta$($\alpha\in\Lambda^iV$, $\beta\in\Lambda^jW$)가 $\Lambda^iV\times\Lambda^jW\to\Lambda^k(V\oplus W)$인 bilinear map이라 Tensor product 절의 universal property로 $\Lambda^iV\otimes\Lambda^jW\to\Lambda^k(V\oplus W)$인 map이 나오고, $i+j=k$에서 모두 모으면 $$\bigoplus_{i+j=k}\Lambda^iV\otimes\Lambda^jW\longrightarrow\Lambda^k(V\oplus W)$$가 된다. $V$의 basis $e_1,\dots,e_m$과 $W$의 basis $f_1,\dots,f_n$을 합친 것이 $V\oplus W$의 basis이므로, 양쪽에서 오름차순 첨자로 basis를 세면 차원이 $$\dim\Lambda^k(V\oplus W)=\binom{m+n}k=\sum_{i+j=k}\binom mi\binom nj=\sum_{i+j=k}\dim(\Lambda^iV\otimes\Lambda^jW)$$로 같다(Vandermonde의 항등식). 위 map이 각 첨자 조합의 basis 원소를 서로 다른 basis 원소로 보내므로(오름차순으로 $V$쪽 $i$개, $W$쪽 $j$개를 뽑아 합친 것과 정확히 대응) basis를 basis로 보내는 isomorphism이다. $\blacksquare$

exterior algebra를 생각하는 이유는, $k$개의 벡터가 만드는 $k$차원 평행체(parallelepiped)의 부피를 $n$차원 공간 속에서 좌표 없이 다루려는 데 있다. $k=n$일 때 이 부피가 정확히 determinant인 것은 방금 보았고, $k<n$일 때도 $v_1\wedge\cdots\wedge v_k$가 그 $k$차원 평행체를 좌표 없이 대표하는 대상이다(그 "크기"까지 재려면 inner product를 얹어야 하는데, 이는 뒤에서 다룬다). 이 관점은 다변수 미적분에서 곡면의 넓이·다양체의 부피를 재는 differential form으로 이어진다.

**Definition (Orientation).** $\Lambda^nV$의 $0$이 아닌 원소(양의 배수를 같은 것으로 본다) 하나를 고르는 것을 $V$의 orientation이라 한다. 두 basis $e_1,\dots,e_n$과 $e_1',\dots,e_n'$이 같은 orientation을 주는 것은 change-of-basis 행렬의 determinant가 양수인 것과 동치다(방금 정리로 $e_1'\wedge\cdots\wedge e_n'=\det(P)\,e_1\wedge\cdots\wedge e_n$이기 때문이다).

**Example.** $\mathbb{R}^3$에서 $\Lambda^2\mathbb{R}^3$은 $\binom32=3$차원이고, $e_1\wedge e_2,e_2\wedge e_3,e_3\wedge e_1$이 그 basis다. $u\wedge v$의 이 basis에서의 좌표는 정확히 cross product $u\times v$의 좌표와 같다(성분을 직접 전개하면 확인된다): $$u\wedge v=(u_2v_3-u_3v_2)\,e_2\wedge e_3+(u_3v_1-u_1v_3)\,e_3\wedge e_1+(u_1v_2-u_2v_1)\,e_1\wedge e_2.$$ 곧 cross product는 $3$차원에서만 통하는 wedge product의 특수한 얼굴이다.

이 글에서 다룬 multilinear·alternating 관점의 뿌리는 Hermann Grassmann이 1844년 《Die lineale Ausdehnungslehre》에서 세운 확장론이다 [1]. Grassmann은 오늘날의 vector space, 일차독립, 차원, 그리고 wedge product에 해당하는 것을 이미 담았지만, 서술이 지나치게 추상적이고 철학적이어서 당대에는 거의 읽히지 않았고 수십 년이 지나서야 제대로 평가받았다.

## 참고문헌

1. Grassmann, H. (1844). *Die lineale Ausdehnungslehre, ein neuer Zweig der Mathematik*. Leipzig: Otto Wigand.
