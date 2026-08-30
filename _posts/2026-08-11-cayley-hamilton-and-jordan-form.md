---
layout: post
title: "Cayley–Hamilton and Jordan form"
date: 2026-08-11
mathematicians: [Cayley, Hamilton, Frobenius, Jordan, Weierstrass]
---

## Minimal polynomial

**Definition (Minimal Polynomial).** $p(A)=0$을 만족하는 monic polynomial 중 차수가 가장 낮은 것을 $A$의 minimal polynomial이라 하고 $m_A$로 쓴다.

**Proposition (Divisibility).** If $p(A)=0$ then $m_A\mid p$.

*Proof.* $p$를 $m_A$로 나눠 $p=qm_A+r$($\deg r<\deg m_A$)라 하면 $r(A)=p(A)-q(A)m_A(A)=0$인데, $m_A$가 최소 차수이므로 $r=0$이다. $\blacksquare$

**Theorem.** $m_A$ uniquely exists.

*Proof.* $A\in F^{n\times n}$에 대해 $n\times n$ 행렬들의 공간은 차원이 $n^2$이라, $I,A,A^2,\dots,A^{n^2}$의 $n^2+1$개가 linearly dependent이다. 따라서 $p(A)=0$인 $0$이 아닌 polynomial $p$가 존재한다. 유일성은, 두 minimal polynomial이 서로를 나누고 둘 다 monic이라 같아진다는 데서 나온다. 

**Proposition (근과 eigenvalue).** $m_A$의 근은 정확히 $A$의 eigenvalue다.

*Proof.* $Av=\lambda v$ ($v\ne0$)이면 $0=m_A(A)v=m_A(\lambda)v$라 $m_A(\lambda)=0$이다. 역으로 $m_A(\lambda)=0$이면 $m_A=(x-\lambda)q$인데 $\deg q<\deg m_A$라 $q(A)\ne0$이므로 $q(A)w\ne0$인 $w$가 있고, $(A-\lambda I)\,q(A)w=m_A(A)w=0$이라 $q(A)w$가 $\lambda$의 eigenvector다. 따라서 $\lambda$는 eigenvalue다. $\blacksquare$

## Cayley–Hamilton 정리

minimal polynomial의 차수는 아직 알 수 없지만, characteristic polynomial $p_A(\lambda)=\det(A-\lambda I)$는 항상 $A$를 근으로 가진다.

**Theorem (Cayley–Hamilton).** 모든 정사각행렬 $A$에 대해 $p_A(A)=0$이다.

*Proof.* Determinant 글의 adjugate 항등식에서 $(A-\lambda I)\operatorname{adj}(A-\lambda I)=\det(A-\lambda I)\,I=p_A(\lambda)I$이다. $\operatorname{adj}(A-\lambda I)$는 성분이 $\lambda$에 대한 $n-1$차 이하 polynomial이라, 행렬 계수로 $\operatorname{adj}(A-\lambda I)=\sum_{k=0}^{n-1}\lambda^kB_k$로 쓸 수 있다. $p_A(\lambda)=\sum_{k=0}^{n}c_k\lambda^k$라 하면 위 항등식의 양변에서 $\lambda^k$의 계수를 비교해
$$AB_0=c_0I,\qquad AB_k-B_{k-1}=c_kI\ (1\le k\le n-1),\qquad -B_{n-1}=c_nI$$
를 얻는다. $k$번째 식에 왼쪽으로 $A^k$를 곱해 모두 더하면 좌변이 telescope로 상쇄되어 $0$이 되고, 우변은 $\sum_k c_kA^k=p_A(A)$이다. 그러므로 $p_A(A)=0$이다. $\blacksquare$

**Corollary.** $m_A\mid p_A$이다. 따라서 $\deg m_A\le n$이고, $m_A$와 $p_A$는 근(=eigenvalue)이 같다(multiplicity만 다를 수 있다).

**Example ($2\times2$).** $$A=\begin{pmatrix}1&1\\0&1\end{pmatrix}$$은 $p_A(\lambda)=(1-\lambda)^2$이라 Cayley–Hamilton은 $(A-I)^2=0$을 주장한다. 실제로 $$(A-I)^2=\begin{pmatrix}0&1\\0&0\end{pmatrix}^2=\begin{pmatrix}0&0\\0&0\end{pmatrix}$$이다. 여기서는 $(A-I)\ne0$이므로 $m_A=(x-1)^2=p_A$이다.

## Diagonalizability와 minimal polynomial

두 kernel을 쪼개는 다음 보조정리가 핵심 도구다.

**Lemma (coprime kernel).** $p(A)=0$이고 $p=p_1p_2$, $\gcd(p_1,p_2)=1$이면 $V=\ker p_1(A)\oplus\ker p_2(A)$이다.

*Proof.* $\gcd$가 $1$이라 $a p_1+b p_2=1$인 polynomial $a,b$가 있고, $A$를 넣으면 $a(A)p_1(A)+b(A)p_2(A)=I$이다. 임의의 $v$에 대해 $v=b(A)p_2(A)v+a(A)p_1(A)v$인데, 첫 항은 $p_1(A)$가 죽이고($p_1(A)b(A)p_2(A)v=b(A)p(A)v=0$) 둘째 항은 $p_2(A)$가 죽이므로 $V=\ker p_1(A)+\ker p_2(A)$이다. 또 $v\in\ker p_1(A)\cap\ker p_2(A)$이면 $v=a(A)p_1(A)v+b(A)p_2(A)v=0$이라 합이 direct sum이다. $\blacksquare$

**Theorem (Diagonalizability Criterion).** $A$가 diagonalizable인 것은 $m_A$가 서로 다른 일차식들의 곱인 것(중근이 없는 것)과 동치다.

*Proof.* $A$가 diagonalizable이면 서로 다른 eigenvalue $\lambda_1,\dots,\lambda_r$의 eigenvector가 $V$를 span하고 각 eigenvector를 $\prod_i(A-\lambda_i I)$가 죽이므로 $\prod_i(A-\lambda_iI)=0$, 곧 $m_A\mid\prod_i(x-\lambda_i)$라 $m_A$에 중근이 없다. 역으로 $m_A=\prod_i(x-\lambda_i)$가 서로 다른 일차식들의 곱이면, coprime kernel lemma를 반복 적용해 $V=\bigoplus_i\ker(A-\lambda_iI)=\bigoplus_iE_{\lambda_i}$이므로 eigenvector로 이루어진 basis가 있어 diagonalizable이다. $\blacksquare$

이 판정은 Eigenvalue 글에서 미뤄 둔 사실, 곧 diagonalizable 행렬의 invariant subspace로의 제한이 다시 diagonalizable이라는 것도 곧바로 준다. 제한의 minimal polynomial은 전체 $m_A$를 나누므로 여전히 중근이 없기 때문이다.

중근을 허용하면(일차식들의 곱이기만 하면) diagonal 대신 upper triangular까지는 언제나 도달한다.

**Theorem (Triangularizability).** 다음이 동치다. (i) $A$가 upper triangular matrix와 similar하다. (ii) $p_A$가 $F$ 위에서 일차식들의 곱으로 분해된다. (iii) $m_A$가 $F$ 위에서 일차식들의 곱으로 분해된다. 특히 $F$가 대수적으로 닫혔으면 모든 $A$가 이 성질을 가진다.

*Proof.* (i)$\Rightarrow$(ii): upper triangular $T$는 $p_T(\lambda)=\prod_i(t_{ii}-\lambda)$가 일차식들의 곱이고, similar 행렬은 characteristic polynomial이 같다. (ii)$\Rightarrow$(i): $\dim V$에 대한 induction. $p_A$가 근 $\lambda$를 가지므로 eigenvector가 있고, 그것을 첫 벡터로 하는 basis에서 $A$가 $$\begin{pmatrix}\lambda&\ast\\0&A'\end{pmatrix}$$ 꼴이 된다. $p_A=(\lambda-x)\,p_{A'}$이라 $p_{A'}$도 일차식들의 곱이고, induction으로 $A'$이 upper triangular와 similar라 $A$도 그렇다. (ii)$\Leftrightarrow$(iii): $m_A$와 $p_A$는 근(=eigenvalue)이 같으므로, 둘 중 하나가 일차식들로 분해되는 것은 모든 eigenvalue가 $F$에 있다는 한 조건과 동치다. $\blacksquare$

## Generalized eigenspace와 primary decomposition

중근이 있어 diagonalization이 막힐 때는, eigenspace $\ker(A-\lambda I)$를 넓힌 공간이 필요하다.

**Definition (Generalized Eigenspace).** eigenvalue $\lambda$에 대해 $G_\lambda:=\ker(A-\lambda I)^n$을 generalized eigenspace라 하고, 그 원소를 generalized eigenvector라 한다.

이제 $F$가 대수적으로 닫혔다고 하자(예: $\mathbb{C}$). 그러면 $p_A$가 $\prod_i(x-\lambda_i)^{m_i}$로 완전히 factorize되고, 공간 전체가 generalized eigenspace들로 쪼개진다.

**Theorem (Primary Decomposition).** $F$가 대수적으로 닫혔으면 $$V=\bigoplus_{i}G_{\lambda_i}$$이고, 각 $G_{\lambda_i}$는 $A$-invariant이며 $\dim G_{\lambda_i}$는 $\lambda_i$의 algebraic multiplicity $m_i$와 같다. 또 $A-\lambda_iI$는 $G_{\lambda_i}$ 위에서 nilpotent이다.

*Proof.* $W_i:=\ker(A-\lambda_iI)^{m_i}$라 두자. Cayley–Hamilton으로 $p_A(A)=0$이고 $p_A=\prod_i(x-\lambda_i)^{m_i}$인데 서로 다른 $(x-\lambda_i)^{m_i}$들이 pairwise coprime이므로, coprime kernel lemma를 반복하면 $V=\bigoplus_iW_i$이다. 각 $W_i$는 $A$와 교환하는 $(A-\lambda_iI)^{m_i}$의 kernel이라 $A$-invariant이고, 그 위에서 $(A-\lambda_iI)^{m_i}=0$이라 $A-\lambda_iI$가 nilpotent이다. 반면 $j\ne i$이면 $W_j$ 위에서 $A-\lambda_iI=(A-\lambda_jI)+(\lambda_j-\lambda_i)I$인데 $A-\lambda_jI$가 nilpotent이고 $\lambda_j-\lambda_i\ne0$이라 $A-\lambda_iI$가 $W_j$ 위에서 invertible이다.

$\dim W_i=m_i$를 본다. $V=\bigoplus_jW_j$가 $A$-invariant 분해라 이에 맞춘 basis에서 $A$가 block-diagonal이 되어 $p_A=\prod_j p_{A|W_j}$이고, $A|W_j$의 eigenvalue가 $\lambda_j$뿐이라 $p_{A|W_j}=(x-\lambda_j)^{\dim W_j}$이다. $p_A=\prod_j(x-\lambda_j)^{m_j}$와 비교하면 $\dim W_j=m_j$이다.

끝으로 $W_i=G_{\lambda_i}$, 곧 $\ker(A-\lambda_iI)^{m_i}=\ker(A-\lambda_iI)^n$을 본다. $m_i\le n$이라 $\subseteq$는 자명하다. 역으로 $v\in\ker(A-\lambda_iI)^n$을 $v=\sum_jw_j$ ($w_j\in W_j$)로 쓰면 $0=(A-\lambda_iI)^nv=\sum_j(A-\lambda_iI)^nw_j$인데 각 항이 $W_j$에 있고 합이 direct sum에서 $0$이라 항마다 $(A-\lambda_iI)^nw_j=0$이다. $j\ne i$에서는 $A-\lambda_iI$가 $W_j$ 위에서 invertible이라 $w_j=0$이므로 $v=w_i\in W_i$이다. 그러므로 $G_{\lambda_i}=W_i$이고, 위 성질들이 모두 $G_{\lambda_i}$에 대한 것이 된다. $\blacksquare$

primary decomposition은 문제를 "nilpotent 행렬 하나"로 줄여 준다. 각 $G_{\lambda_i}$ 위에서 $A=\lambda_iI+N_i$ ($N_i=A-\lambda_iI$가 nilpotent)이니, nilpotent 부분만 표준형으로 만들면 된다.

## Jordan canonical form

nilpotent operator의 표준형이 Jordan form의 뼈대다. $\lambda$와 크기 $k$에 대해
$$J_k(\lambda)=\begin{pmatrix}\lambda&1&&\\&\lambda&\ddots&\\&&\ddots&1\\&&&\lambda\end{pmatrix}$$
를 Jordan block이라 한다(대각이 $\lambda$, 바로 위 대각선이 $1$, 나머지가 $0$인 $k\times k$ 행렬).

nilpotent 부분의 표준형은 다음 Lemma가 준다.

**Lemma (nilpotent Jordan basis).** nilpotent operator $N$을 가진 유한차원 $V$는 $N$에 대한 Jordan chain들의 disjoint union인 basis를 가진다. 곧 $V$가 $N$-cyclic subspace $\langle x,Nx,\dots,N^{s-1}x\rangle$ (단 $N^sx=0$)들의 direct sum이고, 각 chain이 하나의 $J_s(0)$ block을 준다.

*Proof.* $\dim V$에 대한 induction. $N=0$이면 아무 basis나 모두 길이 $1$ chain이다. $N\ne0$이면 $W=\operatorname{im}N$이 $N$-invariant이고 $N$이 nilpotent라 $W\subsetneq V$이므로, induction 가정으로 $W$가 chain들의 disjoint union인 basis를 가진다. 그 chain들의 top 벡터(각 chain의 첫 원소)를 $x_1,\dots,x_r$, 길이를 $d_1,\dots,d_r$이라 하면 bottom 벡터 $N^{d_p-1}x_p$들은 $\ker N$에 들어 있고 linearly independent다.

각 $x_p\in W=\operatorname{im}N$이라 $x_p=Ny_p$인 $y_p\in V$를 잡아, 그 chain 앞에 $y_p$를 붙여 길이 $d_p+1$의 chain으로 늘린다. 또 bottom 벡터들을 $\ker N$의 basis로 확장하는 여분 벡터 $t_1,\dots,t_s$ ($s=\dim\ker N-r$)를 길이 $1$ chain으로 더한다. 모은 벡터의 개수는 $\sum_p(d_p+1)+s=(\dim W+r)+(\dim\ker N-r)=\operatorname{rank}N+\dim\ker N=\dim V$이다.

이들이 linearly independent임을 보이면 basis다. 일차결합이 $0$이라 하고 $N$을 적용하면 늘어난 chain의 $y_p$가 $x_p$로 내려가고 각 chain의 bottom 벡터와 $t_j$는 사라져, 그 상이 $W$의 원래 basis(늘리기 전 chain들)의 일차결합이 되어 $0$이다. induction의 independence로 그 계수들, 곧 원래 결합에서 bottom 벡터와 $t_j$의 계수를 뺀 나머지가 모두 $0$이다. 그러면 남은 것은 $\ker N$의 basis를 이루는 bottom 벡터들과 $t_j$들의 일차결합이라 나머지 계수도 $0$이다. 늘어난 chain들과 $t_j$ chain들이 곧 $J_s(0)$ block들을 준다. $\blacksquare$

**Theorem (Jordan Canonical Form).** $F$가 대수적으로 닫혔으면 모든 $A\in F^{n\times n}$은 Jordan block들의 block-diagonal 행렬과 similar하며, 그 blocks의 모임은 순서를 빼면 유일하다.

$A$가 이 Jordan form과 similar하다는 것은, Linear map 글의 기저 변환으로 읽으면, 각 chain을 이루는 generalized eigenvector들을 기저로 잡을 때 그 기저에서 $A$가 Jordan form으로 표현된다는 뜻이다. diagonal까지는 못 가더라도 그에 가장 가까운 기저를 찾는 셈이다.

*Proof.* 먼저 존재. Primary decomposition으로 $V=\bigoplus_iG_{\lambda_i}$이고 각 $G_{\lambda_i}$ 위에서 $N_i=A-\lambda_iI$가 nilpotent이다. 위 Lemma를 $N_i$에 적용하면 $G_{\lambda_i}$가 $J_s(0)$들로 쪼개지고, 여기에 $\lambda_iI$를 더하면 $A|G_{\lambda_i}$가 $J_s(\lambda_i)$들의 합이 된다. 모든 $i$에서 모은 basis가 $A$를 Jordan form으로 만든다. 유일성은 rank로 나온다. eigenvalue $\lambda$에 대해 크기가 $k$ 이상인 $\lambda$-block의 개수는 $\operatorname{rank}(A-\lambda I)^{k-1}-\operatorname{rank}(A-\lambda I)^k$와 같다. $J_m(\lambda)$ 하나에서 $(A-\lambda I)^k$의 rank 기여가 $\max(m-k,0)$이라 이 차이가 크기 $\ge k$인 block마다 $1$을 세고, $\mu\ne\lambda$인 block은 $A-\lambda I$가 invertible이라 차이에 기여하지 않기 때문이다. 이 rank들은 similar 변환에 불변이므로 각 eigenvalue의 block 크기 분포가, 따라서 Jordan form이 순서를 빼면 유일하다. $\blacksquare$

Jordan form의 block 구성은 characteristic·minimal polynomial과 두 multiplicity로 완전히 읽힌다. eigenvalue $\lambda$의 **algebraic multiplicity**는 $p_A$에서 $(x-\lambda)$의 지수, **geometric multiplicity**는 $\dim E_\lambda=\dim\ker(A-\lambda I)$다.

**Proposition (block 구조).** eigenvalue $\lambda$에 대해 Jordan form에서:
- $\lambda$-block의 개수는 geometric multiplicity $\dim\ker(A-\lambda I)$와 같다.
- $\lambda$-block 크기의 합은 algebraic multiplicity, 곧 $\dim G_\lambda$와 같다.
- 가장 큰 $\lambda$-block의 크기는 $m_A$에서 $(x-\lambda)$의 지수와 같다.
- 크기가 $k$ 이상인 $\lambda$-block의 개수는 $\operatorname{rank}(A-\lambda I)^{k-1}-\operatorname{rank}(A-\lambda I)^k$이다.

*Proof.* $J_k(\lambda)$ 하나는 eigenvector를 하나만 주므로($\ker(J_k(\lambda)-\lambda I)$가 $1$차원) $\lambda$-block의 개수가 $\dim\ker(A-\lambda I)$다. 크기의 합은 $\lambda$-block들이 채우는 공간이 $G_\lambda$라는 데서 $\dim G_\lambda$(= algebraic multiplicity, primary decomposition)이다. $J_k(\lambda)$의 minimal polynomial은 $(x-\lambda)^k$이고 block-diagonal의 minimal polynomial은 각 block의 lcm이라, $(x-\lambda)$의 지수는 가장 큰 block 크기다. 마지막 rank 공식은 위 유일성 증명에서 보았다. $\blacksquare$

특히 block 개수가 크기의 합을 넘지 못하므로 geometric $\le$ algebraic multiplicity가 다시 나오고, $A$가 diagonalizable인 것은 모든 block이 크기 $1$인 것, 곧 모든 eigenvalue에서 두 multiplicity가 같은 것과 동치다.

**Example (Jordan form 계산).** $$A=\begin{pmatrix}2&1&0\\0&2&1\\0&0&2\end{pmatrix}$$을 보자. $p_A(\lambda)=(2-\lambda)^3$이라 eigenvalue는 $2$(algebraic multiplicity $3$)뿐이다. $N=A-2I$는 $$N=\begin{pmatrix}0&1&0\\0&0&1\\0&0&0\end{pmatrix},\quad N^2=\begin{pmatrix}0&0&1\\0&0&0\\0&0&0\end{pmatrix},\quad N^3=0$$이라 $\ker N$이 차원 $1$, geometric multiplicity가 $1$이다. eigenvector가 하나뿐이라 diagonalizable이 아니고, $N$이 하나의 길이 $3$ chain을 이루므로 $A$의 Jordan form은 단일 block $J_3(2)$, 곧 $A$ 그 자체다.

**Example (같은 eigenvalue, 다른 Jordan form).** $$B=\begin{pmatrix}2&1&0\\0&2&0\\0&0&2\end{pmatrix}$$도 $p_B(\lambda)=(2-\lambda)^3$으로 $A$와 characteristic polynomial이 같지만, $B-2I$의 rank가 $1$이라 $\ker(B-2I)$가 차원 $2$다. Jordan form이 $J_2(2)\oplus J_1(2)$로 $A$와 다르니, characteristic polynomial만으로는 Jordan form이 정해지지 않고 각 거듭제곱의 rank까지 봐야 한다. 참고로 $m_B=(x-2)^2$, $m_A=(x-2)^3$으로 minimal polynomial은 이미 둘을 구분한다.

## 역사

Cayley–Hamilton 정리는 Arthur Cayley가 1858년 행렬을 다룬 논문에서 진술하고 $2\times2$, $3\times3$의 경우를 손으로 확인한 데서 이름을 얻었는데, 그는 일반적인 경우의 증명은 "굳이 할 필요를 느끼지 못했다"고 적었다 [1]. William Rowan Hamilton은 그보다 앞서 quaternion을 다루며 관련된 특수한 경우에 이르렀고 [2], 일반적인 증명은 Georg Frobenius가 1878년에 주었다 [3]. Jordan canonical form은 Camille Jordan이 1870년 permutation group을 다룬 책에서 제시한 것으로 알려져 있지만 [4], 정작 그 책의 표준형은 finite field 위에서의 것이었고, $\mathbb{C}$ 위에서 이와 동치인 elementary divisor 이론은 이미 Karl Weierstrass가 1868년에 세워 둔 것이었다 [5].

## 참고문헌

1. Cayley, A. (1858). A Memoir on the Theory of Matrices. *Philosophical Transactions of the Royal Society of London*, 148, 17–37.
2. Hamilton, W. R. (1853). *Lectures on Quaternions*. Dublin: Hodges and Smith.
3. Frobenius, G. (1878). Über lineare Substitutionen und bilineare Formen. *Journal für die reine und angewandte Mathematik*, 84, 1–63.
4. Jordan, C. (1870). *Traité des substitutions et des équations algébriques*. Paris: Gauthier-Villars.
5. Weierstrass, K. (1868). Zur Theorie der bilinearen und quadratischen Formen. *Monatsberichte der Königlich Preussischen Akademie der Wissenschaften zu Berlin*, 310–338.
