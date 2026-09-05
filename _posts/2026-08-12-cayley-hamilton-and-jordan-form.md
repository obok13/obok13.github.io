---
layout: post
title: "Cayley–Hamilton and Jordan form"
date: 2026-08-12
mathematicians: [Cayley, Hamilton, Frobenius, Jordan, Weierstrass, Kronecker]
---

## Minimal polynomial

**Definition (Minimal Polynomial).** $p(A)=0$을 만족하는 monic polynomial 중 차수가 가장 낮은 것을 $A$의 minimal polynomial이라 하고 $m_A$로 쓴다.

**Proposition (Divisibility).** If $p(A)=0$ then $m_A\mid p$.

*Proof.* $p$를 $m_A$로 나눠 $p=qm_A+r$($\deg r<\deg m_A$)라 하면 $r(A)=p(A)-q(A)m_A(A)=0$인데, $m_A$가 최소 차수이므로 $r=0$이다. $\blacksquare$

**Theorem.** $m_A$ uniquely exists.

*Proof.* $A\in F^{n\times n}$에 대해 $n\times n$ 행렬들의 공간은 차원이 $n^2$이라, $I,A,A^2,\dots,A^{n^2}$의 $n^2+1$개가 linearly dependent이다. 따라서 $p(A)=0$인 $0$이 아닌 polynomial $p$가 존재한다. 그 중 차수가 minimal한 것이 $m_A$이다. 유일성은, 두 minimal polynomial이 서로를 나누고 둘 다 monic이라 같아진다는 데서 나온다. 

**Proposition (근과 eigenvalue).** $m_A$의 근은 정확히 $A$의 eigenvalue다.

*Proof.* $Av=\lambda v$ ($v\ne0$)이면 $0=m_A(A)v=m_A(\lambda)v$라 $m_A(\lambda)=0$이다. 역으로 $m_A(\lambda)=0$이면 $m_A=(x-\lambda)q$인데 $\deg q<\deg m_A$라 $q(A)\ne0$이므로 $q(A)w\ne0$인 $w$가 있고, $(A-\lambda I)\,q(A)w=m_A(A)w=0$이라 $q(A)w$가 $\lambda$의 eigenvector다. 따라서 $\lambda$는 eigenvalue다. $\blacksquare$

## Cayley–Hamilton 정리

minimal polynomial의 차수는 아직 알 수 없지만, characteristic polynomial $p_A(\lambda)=\det(A-\lambda I)$는 항상 $A$를 근으로 가진다.

**Theorem (Cayley–Hamilton).** 모든 정사각행렬 $A$에 대해 $p_A(A)=0$이다.

*Proof.* cofactor matrix 항등식을 $A-\lambda I$에 적용하자. $A-\lambda I$의 cofactor matrix를 $C(\lambda)$라 하면 $(A-\lambda I)\,C(\lambda)^{\mathsf T}=\det(A-\lambda I)\,I=p_A(\lambda)I$이다. $C(\lambda)^{\mathsf T}$는 성분이 $\lambda$에 대한 $n-1$차 이하 polynomial이라, 행렬 계수로 $C(\lambda)^{\mathsf T}=\sum_{k=0}^{n-1}\lambda^kB_k$로 쓸 수 있다. $p_A(\lambda)=\sum_{k=0}^{n}c_k\lambda^k$라 하면 위 항등식의 양변에서 $\lambda^k$의 계수를 비교해
$$AB_0=c_0I,\qquad AB_k-B_{k-1}=c_kI\ (1\le k\le n-1),\qquad -B_{n-1}=c_nI$$
를 얻는다. $k$번째 식에 왼쪽으로 $A^k$를 곱해 모두 더하면 좌변이 telescope로 상쇄되어 $0$이 되고, 우변은 $\sum_k c_kA^k=p_A(A)$이다. 그러므로 $p_A(A)=0$이다. $\blacksquare$

**Corollary.** $m_A\mid p_A$이다. 따라서 $\deg m_A\le n$이고, $m_A$와 $p_A$는 근(=eigenvalue)이 같다(multiplicity만 다를 수 있다).

**Example ($2\times2$).** $2\times2$ 행렬 $$A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$$의 characteristic polynomial은 $p_A(\lambda)=\lambda^2-(a+d)\lambda+(ad-bc)$이라, Cayley–Hamilton은 trace $a+d$와 determinant $ad-bc$로 적은 $A^2-(a+d)A+(ad-bc)I=0$을 준다. 구체적으로 $$A=\begin{pmatrix}1&1\\0&1\end{pmatrix}$$이면 $p_A(\lambda)=(1-\lambda)^2$이라 $(A-I)^2=0$을 주장하는데, 실제로 $$(A-I)^2=\begin{pmatrix}0&1\\0&0\end{pmatrix}^2=\begin{pmatrix}0&0\\0&0\end{pmatrix}$$이다. 여기서는 $(A-I)\ne0$이므로 $m_A=(x-1)^2=p_A$이다.

이 정리는 Arthur Cayley가 1858년 행렬을 다룬 논문에서 진술하고 $2\times2$, $3\times3$의 경우를 손으로 확인한 데서 이름을 얻었는데, 그는 일반적인 경우의 증명은 "굳이 할 필요를 느끼지 못했다"고 적었다 [1]. William Rowan Hamilton은 그보다 앞서 quaternion을 다루며 관련된 특수한 경우에 이르렀고 [2], 일반적인 증명은 Georg Frobenius가 1878년에 주었다 [3].

## Invariant subspace

Endomorphism and Perron–Frobenius 글에서 invariant subspace의 정의($AW\subseteq W$이면 $A$-invariant, $W$ 위의 restriction $A\vert_W$)와 그것이 주는 block-triangular 표현을 이미 다뤘다. restriction은 minimal polynomial과 characteristic polynomial을 모두 물려받는다.

**Proposition (restriction의 minimal polynomial).** $W$가 $A$-invariant이면 $m_{A\vert_W}\mid m_A$이다.

*Proof.* $W$가 $A$-invariant이라 $A\vert_W$의 거듭제곱은 $A$의 거듭제곱을 $W$로 제한한 것이고, 따라서 임의의 polynomial $q$에서 $q(A\vert_W)=q(A)\vert_W$이다. 여기에 $q=m_A$를 넣으면 $m_A(A)=0$이라 $m_A(A\vert_W)=m_A(A)\vert_W=0$, 곧 $m_A$가 $A\vert_W$를 소멸시킨다. minimal polynomial은 자신을 소멸시키는 polynomial을 모두 나누므로(divisibility), $A\vert_W$를 소멸시키는 $m_A$에 대해 $m_{A\vert_W}\mid m_A$이다. $\blacksquare$

**Proposition (restriction의 characteristic polynomial).** $W$가 $A$-invariant이면 $p_{A\vert_W}\mid p_A$이다.

*Proof.* block-triangular Proposition의 basis에서 $A$의 행렬이 $$\begin{pmatrix}B&C\\0&D\end{pmatrix}$$ 꼴이고 $B$가 $A\vert_W$의 행렬이다. block triangular 행렬의 determinant는 대각 block들의 determinant의 곱이므로(Leibniz formula에서 왼쪽 아래 block을 지나는 permutation은 $0$인 성분을 지나 사라진다) $$p_A=\det(A-xI)=\det(B-xI)\det(D-xI)=p_{A\vert_W}\det(D-xI)$$이다. 곧 $p_{A\vert_W}\mid p_A$이다. $\blacksquare$

## Diagonalizability Criterion

**Lemma (coprime kernel).** $p(A)=0$이고 $p=p_1p_2$, $\gcd(p_1,p_2)=1$이면 $V=\ker p_1(A)\oplus\ker p_2(A)$이다.

*Proof.* $\gcd$가 $1$이라 $a p_1+b p_2=1$인 polynomial $a,b$가 있고, $A$를 넣으면 $a(A)p_1(A)+b(A)p_2(A)=I$이다. 임의의 $v$에 대해 $v=b(A)p_2(A)v+a(A)p_1(A)v$인데, 첫 항은 $p_1(A)$가 $0$으로 보내고($p_1(A)b(A)p_2(A)v=b(A)p(A)v=0$) 둘째 항은 $p_2(A)$가 $0$으로 보내므로 $V=\ker p_1(A)+\ker p_2(A)$이다. 또 $v\in\ker p_1(A)\cap\ker p_2(A)$이면 $v=a(A)p_1(A)v+b(A)p_2(A)v=0$이라 합이 direct sum이다. $\blacksquare$

**Theorem (Diagonalizability Criterion).** $A$ is diagonalizable iff $m_A$ is product of distinct linear factors.

*Proof.* ($\Rightarrow$) $A$가 diagonalizable이면 eigenvector들이 $V$의 basis를 이룬다. 서로 다른 eigenvalue를 $\lambda_1,\dots,\lambda_r$이라 하고 $g(x)=\prod_i(x-\lambda_i)$라 두자. 인수들이 서로 교환하고 $\lambda_j$-eigenvector는 인수 $(A-\lambda_jI)$가 $0$으로 보내므로, $g(A)$는 모든 eigenvector를, 따라서 basis 전체를 $0$으로 보내 $g(A)=0$이다. 그러면 divisibility로 $m_A\mid g$인데, $g$가 서로 다른 일차식들의 곱이니 그 약수 $m_A$도 중근 없는 일차식들의 곱이다.

($\Leftarrow$) $m_A=\prod_i(x-\lambda_i)$가 서로 다른 일차식들의 곱이면 인수 $(x-\lambda_i)$들이 pairwise coprime이고 $m_A(A)=0$이므로, coprime kernel lemma를 반복 적용하면 $V=\bigoplus_i\ker(A-\lambda_iI)=\bigoplus_iE_{\lambda_i}$이다. 각 eigenspace의 basis를 모으면 eigenvector로 이루어진 $V$의 basis가 되어 $A$가 diagonalizable이다. $\blacksquare$

**Corollary (제한의 diagonalizability).** diagonalizable 행렬을 그 invariant subspace로 제한한 것도 다시 diagonalizable이다.

*Proof.* $A$가 diagonalizable이면 criterion으로 $m_A$가 중근 없는 일차식들의 곱이다. invariant subspace $W$에 대해 위 Proposition으로 $m_{A\vert_W}\mid m_A$라 $m_{A\vert_W}$도 중근이 없고, 다시 criterion으로 $A\vert_W$가 diagonalizable이다. $\blacksquare$

**Corollary (Simultaneous Diagonalization).** diagonalizable 행렬 $A,B$에 대해 다음이 동치다. (i) $AB=BA$이다. (ii) 어떤 invertible $P$로 $P^{-1}AP$와 $P^{-1}BP$가 둘 다 diagonal이다(공통 eigenvector basis).

*Proof.* (ii)$\Rightarrow$(i): $P^{-1}AP=D_1$, $P^{-1}BP=D_2$가 diagonal이면 diagonal끼리는 commute하므로 $AB=PD_1D_2P^{-1}=PD_2D_1P^{-1}=BA$이다. (i)$\Rightarrow$(ii): $A$가 diagonalizable이라 $F^n=\bigoplus_\lambda E_\lambda(A)$이다. $AB=BA$이면 각 $x\in E_\lambda(A)$에서 $A(Bx)=B(Ax)=\lambda(Bx)$라 $Bx\in E_\lambda(A)$, 곧 $B$가 각 $E_\lambda(A)$를 보존한다. 위 corollary로 $B$를 $E_\lambda(A)$로 제한한 것이 다시 diagonalizable이므로 각 $E_\lambda(A)$ 안에서 $B$의 eigenvector로 된 basis를 고를 수 있고, 이들은 $E_\lambda(A)$에 있으니 $A$의 eigenvector이기도 하다. 모든 $\lambda$에서 모으면 $A$와 $B$를 동시에 diagonalize하는 공통 basis다. $\blacksquare$

중근을 허용하면(일차식들의 곱이기만 하면) diagonal 대신 upper triangular까지는 언제나 도달한다.

**Theorem (Triangularizability).** $A$의 characteristic polynomial $p_A$가 $F$ 위에서 일차식들의 곱으로 분해되면, 그리고 그럴 때만, $A$는 upper triangular matrix와 similar하다. 특히 $F$가 대수적으로 닫혔으면(예: $\mathbb{C}$) 모든 $A$가 그렇다.

*Proof.* ($\Leftarrow$) upper triangular $T$와 similar하면 $p_A=p_T$이고, $p_T(x)=\prod_i(x-t_{ii})$가 대각성분에서 오는 일차식들의 곱이다. ($\Rightarrow$) $\dim V$에 대한 induction. $p_A$가 근 $\lambda$를 가지므로 eigenvector가 있고, 그것을 첫 벡터로 하는 basis에서 $A$가 $$\begin{pmatrix}\lambda&\ast\\0&A'\end{pmatrix}$$ 꼴이 된다. 이때 $p_A=(x-\lambda)\,p_{A'}$이라 $p_{A'}$도 $F$ 위에서 일차식들의 곱이고, induction으로 $A'$이 upper triangular와 similar이므로 $A$도 그렇다. $\blacksquare$

심지어 similar에 쓰이는 basis를 orthonormal하게까지 잡을 수 있다는 강력한 결과가 성립한다. 이는 뒤에서 다룬다.

## Primary decomposition

중근이 있어 diagonalization이 막힐 때는, eigenspace $\ker(A-\lambda I)$를 넓힌 공간이 필요하다.

**Definition (Generalized Eigenspace).** eigenvalue $\lambda$에 대해 $G_\lambda:=\ker(A-\lambda I)^n$을 generalized eigenspace라 하고, 그 원소를 generalized eigenvector라 한다.

이제 $F$가 대수적으로 닫혔다고 하자(예: $\mathbb{C}$). 그러면 $p_A$가 $\prod_i(x-\lambda_i)^{m_i}$로 완전히 factorize되고, 공간 전체가 generalized eigenspace들로 쪼개진다.

**Theorem (Primary Decomposition).** $F$가 대수적으로 닫혔으면 $$V=\bigoplus_{i}G_{\lambda_i}$$이고, 각 $G_{\lambda_i}$는 $A$-invariant이며 $\dim G_{\lambda_i}$는 $\lambda_i$의 algebraic multiplicity $m_i$와 같다. 또 $A-\lambda_iI$는 $G_{\lambda_i}$ 위에서 nilpotent이다.

*Proof.* $W_i:=\ker(A-\lambda_iI)^{m_i}$라 두자. Cayley–Hamilton으로 $p_A(A)=0$이고 $p_A=\prod_i(x-\lambda_i)^{m_i}$인데 서로 다른 $(x-\lambda_i)^{m_i}$들이 pairwise coprime이므로, coprime kernel lemma를 반복하면 $V=\bigoplus_iW_i$이다. 각 $W_i$는 $A$와 교환하는 $(A-\lambda_iI)^{m_i}$의 kernel이라 $A$-invariant이고, 그 위에서 $(A-\lambda_iI)^{m_i}=0$이라 $A-\lambda_iI$가 nilpotent이다.

$\dim W_i=m_i$를 본다. $V=\bigoplus_jW_j$가 $A$-invariant 분해라 Endomorphism and Perron–Frobenius 글의 block-diagonal Lemma로 $p_A=\prod_j p_{A\vert_{W_j}}$이고, $W_j$ 위에서 $A-\lambda_jI$가 nilpotent이라 $A\vert_{W_j}$의 eigenvalue가 $\lambda_j$뿐이므로 $p_{A\vert_{W_j}}=(x-\lambda_j)^{\dim W_j}$이다. $p_A=\prod_j(x-\lambda_j)^{m_j}$와 비교하면 $\dim W_j=m_j$이다.

끝으로 $W_i=G_{\lambda_i}$, 곧 $\ker(A-\lambda_iI)^{m_i}=\ker(A-\lambda_iI)^n$을 본다. $m_i\le n$이라 $\subseteq$는 자명하다. 역으로 $v\in\ker(A-\lambda_iI)^n$을 $v=\sum_jw_j$ ($w_j\in W_j$)로 쓰면 $0=(A-\lambda_iI)^nv=\sum_j(A-\lambda_iI)^nw_j$인데 각 항이 $W_j$에 있고 합이 direct sum에서 $0$이라 항마다 $(A-\lambda_iI)^nw_j=0$이다. 그런데 $j\ne i$이면 $A-\lambda_iI$가 $W_j$ 위에서 invertible이다. $W_j$ 위에서 $A-\lambda_iI=(A-\lambda_jI)+(\lambda_j-\lambda_i)I$인데 $A-\lambda_jI$가 nilpotent이고 $\lambda_j-\lambda_i\ne0$이기 때문이다. 일반적으로 nilpotent $N$($N^k=0$)과 스칼라 $c\ne0$에서 $N+cI$는 invertible이다. $(N+cI)v=0$이면 $Nv=-cv$라 $N^kv=(-c)^kv$인데, $N^k=0$이고 $(-c)^k\ne0$이라 $v=0$, 곧 kernel이 $0$이기 때문이다. $N=A-\lambda_jI$, $c=\lambda_j-\lambda_i$가 이 경우다. 그러면 $(A-\lambda_iI)^n$도 $W_j$ 위에서 invertible이라 $(A-\lambda_iI)^nw_j=0$에서 $w_j=0$이고, 남은 것은 $v=w_i\in W_i$이다. 그러므로 $G_{\lambda_i}=W_i$이고, 위 성질들이 모두 $G_{\lambda_i}$에 대한 것이 된다. $\blacksquare$

## Jordan canonical form

모든 정사각행렬이 diagonalizable하지는 않지만 primary decomposition에 의해서 각 $G_{\lambda_i}$ 위에서 $A=\lambda_iI+N_i$ where $N_i$ is nilpotent가 성립한다. Diagonalizable이면 $N_i$가 0인 상황이다. Endomorphism and Perron–Frobenius 글에서 본 대로, nilpotent operator는 strictly upper triangular이기만 한 것이 아니라 chain을 잘 모으면 대각선 바로 위에 $1$이 하나씩만 서는 훨씬 더 정밀한 basis를 가진다. 이로부터 모든 정사각행렬이 Jordan canonical form이라는 특수한 형태와 similar하다는 결과가 나온다.

**Definition (Jordan Block).** $s\times s$ 행렬
$$J_s(\lambda):=\begin{pmatrix}\lambda&1& & \\ &\lambda&1& \\ & &\ddots&\ddots\\ & & &\lambda\end{pmatrix}$$
(대각성분이 모두 $\lambda$이고 바로 위 대각선 성분이 모두 $1$, 나머지 성분은 $0$)을 eigenvalue $\lambda$의 Jordan block이라 한다.

**Lemma (nilpotent Jordan basis).** nilpotent operator $N$을 가진 유한차원 $V$는 $N$에 대한 Jordan chain들의 disjoint union인 basis를 가진다. 곧 $V$가 $N$-cyclic subspace $\langle x,Nx,\dots,N^{s-1}x\rangle$ (단 $N^sx=0$)들의 direct sum이고, 각 chain이 하나의 $J_s(0)$ block을 준다.

*Proof.* $\dim V$에 대한 induction으로 $V$가 $N$-cyclic subspace들의 direct sum임을 보인다. $N=0$이면 임의의 basis의 각 벡터가 길이 $1$짜리 chain이라 성립한다.

$N\ne0$이라 하자. $W=\operatorname{im}N$은 $N(W)\subseteq W$라 $N$-invariant이고 그 위에서 $N\vert_W$도 nilpotent이며, $N\ne0$인 nilpotent라 $\ker N\ne0$이므로(Endomorphism and Perron–Frobenius 글) rank–nullity로 $\dim W=\dim V-\dim\ker N<\dim V$이다. induction 가정으로 $W$는 chain들의 direct sum이다. 그 chain의 generator를 $x_1,\dots,x_r$, 길이를 $d_1,\dots,d_r$이라 하면 $$\{\,N^ax_p: 1\le p\le r,\ 0\le a\le d_p-1\,\}$$이 $W$의 basis다.

이 basis를 $V$의 basis로 키운다. 각 $x_p\in\operatorname{im}N$이라 $x_p=Ny_p$인 $y_p\in V$를 하나씩 고르면, $y_p$가 generate하는 chain은 $y_p,Ny_p,\dots,N^{d_p}y_p$로 길이가 $d_p+1$이다(마지막 벡터는 $N^{d_p}y_p=N^{d_p-1}x_p$). 각 chain의 마지막 벡터 $N^{d_p-1}x_p$는 $\ker N$에 있고 서로 linearly independent하므로($W$ basis의 일부다), $\ker N$의 basis가 되도록 $t_1,\dots,t_s$ ($s=\dim\ker N-r$)를 보태 각각을 길이 $1$ chain으로 삼는다.

이제 generator $y_1,\dots,y_r,t_1,\dots,t_s$의 chain들이 $V$를 direct sum으로 준다고 주장한다. 곧 그 chain 벡터 전체가 $V$의 basis라는 것이고(그러면 모든 벡터가 chain 벡터들의 합으로 유일하게 써진다), 개수가 $$\sum_p(d_p+1)+s=(\dim W+r)+(\dim\ker N-r)=\dim V$$로 $\dim V$와 같으니 linearly independent만 확인하면 된다.

chain 벡터들의 일차결합을 $$\sum_p\sum_{a=0}^{d_p}c_{p,a}N^ay_p+\sum_j e_jt_j=0$$이라 하고 $N$을 적용하자. $Nt_j=0$이고 마지막 벡터가 $N\cdot N^{d_p}y_p=0$으로 사라지며, $a<d_p$에서는 $N^{a+1}y_p=N^ax_p$이므로 $$\sum_p\sum_{a=0}^{d_p-1}c_{p,a}N^ax_p=0$$이 남는다. 이는 $W$의 basis의 일차결합이라 계수 $c_{p,a}$ ($a\le d_p-1$)가 모두 $0$이다. 그러면 처음 식에는 $$\sum_p c_{p,d_p}N^{d_p}y_p+\sum_j e_jt_j=0$$만 남는데, $N^{d_p}y_p$들과 $t_j$들이 $\ker N$의 basis이므로 $c_{p,d_p}$와 $e_j$도 모두 $0$이다. 따라서 모든 계수가 $0$이라 chain 벡터들이 linearly independent이고, $V$가 이 chain들의 direct sum이다.

끝으로 각 chain이 $J_s(0)$ block 하나를 줌을 본다. 길이 $s$인 chain의 cyclic subspace를 kernel 쪽 끝에서부터 $$N^{s-1}x,\ N^{s-2}x,\ \dots,\ Nx,\ x$$ 순으로 나열해 basis로 삼자. $N(N^ix)=N^{i+1}x$이므로 $N$은 이 나열에서 각 벡터를 바로 왼쪽 벡터로 옮기고, 맨 왼쪽 $N^{s-1}x$는 $0$으로 보낸다($N^sx=0$). 그러면 이 basis에서 $N$의 행렬은 대각이 $0$, 바로 위 대각선이 $1$인 $s\times s$ 행렬, 곧 $J_s(0)$이다. chain들을 모두 모으면 $N$이 이 $J_s(0)$ block들의 direct sum으로 나타난다. $\blacksquare$

**Theorem (Jordan Canonical Form).** $F$가 대수적으로 닫혔으면 모든 $A\in F^{n\times n}$은 Jordan block들의 block-diagonal 행렬 $J$와 similar하고, $J$의 block 모임은 순서를 빼면 유일하다. 각 eigenvalue $\lambda$에 대해 $J$ 안의 $\lambda$-block들은 다음으로 결정된다.
- block 크기의 합은 algebraic multiplicity $m_\lambda=\dim G_\lambda$와 같다.
- block의 개수는 geometric multiplicity $\dim\ker(A-\lambda I)$와 같다.
- 가장 큰 block의 크기는 minimal polynomial $m_A$에서 $(x-\lambda)$의 지수와 같다.

*Proof.* **존재.** Primary decomposition으로 $V=\bigoplus_iG_{\lambda_i}$이고 각 $G_{\lambda_i}$ 위에서 $N_i=A-\lambda_iI$가 nilpotent이다. nilpotent Jordan basis Lemma를 $N_i$에 적용하면 $G_{\lambda_i}$가 $N_i$-chain들로 쪼개지고, 각 chain에 $\lambda_iI$를 되살리면 $J_s(\lambda_i)$ block이 되어, 모든 $i$의 basis를 모으면 $A$가 Jordan form으로 표현된다.

**block 크기와 rank.** $A$가 $J$와 similar하니 $r_k=\operatorname{rank}(A-\lambda I)^k=\operatorname{rank}(J-\lambda I)^k$이고, $J-\lambda I$가 block-diagonal이라 이 rank는 각 block의 rank를 더한 것이다. block은 $\lambda$-block이 있고 $\mu \neq \lambda$인 $\mu$에 대해 $\mu$-block이 있다. $\lambda$-block $J_m(\lambda)$에서는 $J_m(\lambda)-\lambda I=J_m(0)$이 nilpotent shift라 그 $k$제곱의 rank가 $\max(m-k,0)$이다. $\mu$-block에서는 $J_m(\mu)-\lambda I$의 대각성분 $\mu-\lambda$가 $0$이 아니라 invertible이므로 그 $k$제곱의 rank가 $k$에 무관하게 언제나 크기 $m$을 가진다. 그러면 $r_{k-1} - r_k$는 $\lambda$-block의 rank 차이이므로 $\max(m-k+1,0)-\max(m-k,0)$인데, 이는 $m\ge k$이면 $1$, $m<k$이면 $0$이다. 그러므로 $r_{k-1}-r_k$는 크기가 $k$ 이상인 $\lambda$-block의 개수와 같다. 그래서 총 $\lambda$-block의 개수는 $k=1$을 대입한 $r_0-r_1=n-\operatorname{rank}(A-\lambda I)=\dim\ker(A-\lambda I)$이므로 block 개수가 geometric multiplicity와 같다. 또 $\lambda$-block들이 채우는 공간은 primary decomposition으로 정확히 $G_\lambda$이니 그 크기의 합은 $\dim G_\lambda=m_\lambda$(algebraic multiplicity)다. 끝으로 $A$와 $J$가 similar라 $m_A=m_J$인데, block-diagonal 행렬은 $q(J)=0$이 각 block에서 $q=0$인 것과 같아 minimal polynomial이 각 block minimal polynomial의 lcm이고, 크기 $m$인 $\lambda$-block이 $(x-\lambda)^m$을 주므로 $m_A$에서 $(x-\lambda)$의 지수는 가장 큰 $\lambda$-block의 크기다.

**유일성.** $r_{k-1}-r_k$는 크기가 $k$ 이상인 $\lambda$-block의 개수와 같으므로 Jordan form은 순서를 빼면 유일하다. $\blacksquare$

이로부터 minimal polynomial이 distinct linear factors로 이우어져 있으면 diagonalizable이라는 점도 확인된다. 제일 큰 Jordan block의 크기가 1이기 때문이다. 또한 minimal polynomial이 characteristic polynomial과 완전히 같으면 각 $\lambda$-block이 모두 Jordan block이다.

**Example (6×6 Jordan form 계산).** $$A=\begin{pmatrix}1&0&0&0&0&0\\-1&1&1&0&0&-1\\0&0&0&1&0&2\\0&0&-1&2&0&1\\0&0&0&0&2&1\\0&0&0&0&0&2\end{pmatrix}$$의 Jordan form을 구해보자. 먼저 characteristic polynomial을 구해보면 $p_A(x)=(x-1)^4(x-2)^2$이다. 즉, eigenvalue는 1, 2이다. 각각의 eigenvector를 구하면 1에 대해서는 $(1,0,1,1,0,0)$, $(0,1,0,0,0,0)$가 나오고 2에 대해서는 $(0,0,0,0,1,0)$가 나온다. $6 \times 6$ 행렬인데 eigenvector가 3개뿐이므로 diagonalizable은 아니다. Jordan form을 구하기 위해서는 nilpotent Jordan basis를 구해야 한다. 각 eigenvector $v$에 대해서 $(A - \lambda I)w = v$를 풀어서 chain을 구해보자.

- $v=(1,0,1,1,0,0)$ ($\lambda=1$): $(A-I)w=v$가 해가 없다. 이 chain은 길이 $1$로 끝난다.
- $v=(0,1,0,0,0,0)$ ($\lambda=1$): $(A-I)w=v$가 $w=(0,0,1,1,0,0)$으로 풀린다. 연장.
- $v=(0,0,0,0,1,0)$ ($\lambda=2$): $(A-2I)w=v$가 $w=(0,0,1,0,0,1)$로 풀린다. 연장.

위 과정을 거쳤음에도 아직 generalized eigenvector가 총 5개 밖에 안 구해졌으므로 새로 얻은 두 vector에서 반복한다.

- $(0,0,1,1,0,0)$ ($\lambda=1$): $(A-I)w=(0,0,1,1,0,0)$이 $w=(0,0,0,1,0,0)$으로 풀린다. 연장.
- $(0,0,1,0,0,1)$ ($\lambda=2$): $(A-2I)w=(0,0,1,0,0,1)$이 해가 없다. 이 chain은 길이 $2$로 끝난다.

따라서 nilpotent Jordan basis를 구성하는 generalized vector 6개를 모두 찾았다. 참고로 마지막 $(0,0,0,1,0,0)$도 $(A-I)w=(0,0,0,1,0,0)$이 해가 없어 그 chain이 길이 $3$으로 끝난다. 이로부터 다음과 같은 Jordan form을 얻는다. $$P^{-1}AP=J=\begin{pmatrix}1&0&0&0&0&0\\0&1&1&0&0&0\\0&0&1&1&0&0\\0&0&0&1&0&0\\0&0&0&0&2&1\\0&0&0&0&0&2\end{pmatrix}$$

여기서 $P$는 위에서 찾은 여섯 chain 벡터를 $J$의 block 순서대로 열에 놓은 행렬 $$P=\begin{pmatrix}1&0&0&0&0&0\\0&1&0&0&0&0\\1&0&1&0&0&1\\1&0&1&1&0&0\\0&0&0&0&1&0\\0&0&0&0&0&1\end{pmatrix}$$이다.

각 $\lambda$-block 크기의 합은 algebraic multiplicity와 같다는 것을 확인할 수 있다. 그리고 가장 큰 block의 크기로부터 $m_A=(x-1)^3(x-2)^2$라는 사실도 알 수 있다.

사실 위와 같이 Jordan form을 구하는 것이 표준적인 방법은 아니다. 오히려 잘못된 결과가 나올 가능성도 있다. $J_3(1)$에 대응하는 generalized eigenvector를 얻기 위해서 $v=(0,1,0,0,0,0)$로부터 시작되는 chain을 만들었는데 이는 $\lambda=1$의 eigenvector가 $(1,0,1,1,0,0)$, $(0,1,0,0,0,0)$로 구해져서 가능한 일이었다. 만약 eigenvector가 $(1,0,1,1,0,0)$과 $(1,1,1,1,0,0)$로 주어졌다면 둘 다 $\operatorname{im}(A-I)$ 밖에 있기 때문에 둘 다 $(A-I)w=v$를 만족하는 $w$를 찾을 수 없어서 알고리즘이 실패한다. 표준적인 방법은 각 eigenvalue $\lambda$에서 $\ker(A-\lambda I)^k$의 차원을 $k=1,2,\dots$로 구하는 것이다. 이 nullity 수열이 block 크기들을 정하고 각 Jordan basis chain을 구할 때 $\ker N^k\setminus\ker N^{k-1}$에서 vector 1개를 뽑아서 $N$을 적용하면서 내려오는 방식이다.

Jordan canonical form은 Camille Jordan이 1870년 permutation group을 다룬 책에서 제시한 것으로 알려져 있지만 [4], 정작 그 책의 표준형은 finite field 위에서의 것이었고, $\mathbb{C}$ 위에서 이와 동치인 elementary divisor 이론은 이미 Karl Weierstrass가 1868년에 세워 둔 것이었다 [5]. 다만 Weierstrass가 다룬 것은 단일 행렬이 아니라 두 bilinear form의 pencil $A-\lambda B$의 동치 분류였고, 단일 행렬의 similarity 분류는 $B=I$로 특수화한 경우다. 이 pencil 이론을 $B$가 invertible이 아닌 singular pencil까지 넓힌 것은 Kronecker의 1874년 논문인데 [6], 같은 해 Jordan과 Kronecker 사이에는 두 이론이 다루는 일반성의 성격을 두고 논쟁이 있었다 [7]. Weierstrass의 정리와 Kronecker의 invariant factor를 하나로 엮어 체의 확장 없이도 성립하는 대수적인 증명을 완성한 것은 Frobenius의 1878년 논문이다 [3].

## 참고문헌

1. Cayley, A. (1858). A Memoir on the Theory of Matrices. *Philosophical Transactions of the Royal Society of London*, 148, 17–37.
2. Hamilton, W. R. (1853). *Lectures on Quaternions*. Dublin: Hodges and Smith.
3. Frobenius, G. (1878). Über lineare Substitutionen und bilineare Formen. *Journal für die reine und angewandte Mathematik*, 84, 1–63.
4. Jordan, C. (1870). *Traité des substitutions et des équations algébriques*. Paris: Gauthier-Villars.
5. Weierstrass, K. (1868). Zur Theorie der bilinearen und quadratischen Formen. *Monatsberichte der Königlich Preussischen Akademie der Wissenschaften zu Berlin*, 310–338.
6. Kronecker, L. (1874). Über Schaaren von quadratischen und bilinearen Formen. *Monatsberichte der Königlich Preussischen Akademie der Wissenschaften zu Berlin*, 59–76.
7. Brechenmacher, F. (2007). La controverse de 1874 entre Camille Jordan et Leopold Kronecker. *Revue d'histoire des mathématiques*, 13(2), 187–257.
