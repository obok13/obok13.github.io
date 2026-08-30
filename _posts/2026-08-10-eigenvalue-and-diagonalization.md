---
layout: post
title: "Eigenvalue and diagonalization"
date: 2026-08-10
mathematicians: [Hilbert, Fibonacci, de Moivre, Binet]
---

## Eigenvalue와 eigenvector

**Definition (Eigenvalue, Eigenvector).** vector space $V$ 위의 linear operator $T:V\to V$에 대해, $Tv=\lambda v$를 만족하는 $0$이 아닌 $v\in V$가 존재하면 $\lambda\in F$를 $T$의 eigenvalue, $v$를 $\lambda$에 대한 eigenvector라 한다.

"eigenvalue"라는 이름은 David Hilbert가 적분방정식을 연구하며 쓴 독일어 "Eigenwert"(고유한 값)에서 왔다 [1].

**Example (미분 operator).** 매끄러운 함수들의 공간에서 $D=\dfrac{d}{dx}$를 보자. 모든 $\lambda\in\mathbb{R}$에 대해 $De^{\lambda x}=\lambda e^{\lambda x}$이므로 $\lambda$가 eigenvalue이고 $e^{\lambda x}$가 eigenvector다. 무한차원에서는 이렇게 eigenvalue가 연속적으로 무한히 많을 수 있다.

사실 $e^{\lambda x}$뿐 아니라 이것의 상수배는 모두 $\lambda$의 eigenvector가 된다.

**Definition (Eigenspace).** eigenvalue $\lambda$에 대해 $$E_\lambda:=\{\,v\in V:Tv=\lambda v\,\}=\ker(T-\lambda I)$$를 $\lambda$의 eigenspace라 한다. $E_\lambda$는 $V$의 subspace이고, $\lambda$가 eigenvalue인 것은 $$E_\lambda\ne\{0\}$$인 것과 동치다.

## Characteristic polynomial

$V$가 유한차원일 때, 즉 $T$가 행렬로 표현될 때 eigenvalue를 구하는 방법은 determinant를 이용하는 것이다. $A\in F^{n\times n}$에 대해 $\lambda$가 eigenvalue인 것은 $A-\lambda I$가 injective가 아닌 것, 곧 singular인 것과 같고, 이는 $\det(A-\lambda I)=0$과 동치다.

**Definition (Characteristic Polynomial).** $p_A(\lambda):=\det(A-\lambda I)$를 $A$의 characteristic polynomial이라 한다. 이는 $\lambda$에 대한 $n$차 polynomial이며, 그 근이 곧 $A$의 eigenvalue다.

eigenvalue의 존재는 체 $F$에 달렸다. $\mathbb{C}$처럼 대수적으로 닫힌 체에서는 $n\ge1$일 때 characteristic polynomial이 반드시 근을 가지므로 eigenvalue가 항상 존재한다. 반면 $\mathbb{R}$ 위에서는 없을 수도 있다. 예컨대 $90^\circ$ 회전 $$\begin{pmatrix}0&-1\\1&0\end{pmatrix}$$의 characteristic polynomial은 $\lambda^2+1$이라 real eigenvalue가 없다.

**Example (계산).** $$A=\begin{pmatrix}2&1\\1&2\end{pmatrix}$$의 characteristic polynomial은 $$\det\begin{pmatrix}2-\lambda&1\\1&2-\lambda\end{pmatrix}=(2-\lambda)^2-1=\lambda^2-4\lambda+3=(\lambda-1)(\lambda-3)$$이다. eigenvalue는 $1,3$이고, $$E_1=\operatorname{span}\{(1,-1)\},\quad E_3=\operatorname{span}\{(1,1)\}$$이다.

**Example (triangular matrix).** upper triangular matrix(특히 diagonal matrix)의 characteristic polynomial은 대각성분으로 $\prod_i(a_{ii}-\lambda)$이므로, eigenvalue가 곧 대각성분들이다.

**Example (projection).** $P^2=P$인 projection의 eigenvalue는 $0$ 또는 $1$뿐이다. $Pv=\lambda v$이면 $\lambda v=P^2v=P(\lambda v)=\lambda^2v$이라 $\lambda^2=\lambda$이기 때문이다.

**Proposition.** $A$와 $A^{\mathsf T}$는 같은 characteristic polynomial을 가지며, 따라서 eigenvalue도 같다.

*Proof.* $\det(A^{\mathsf T}-\lambda I)=\det\big((A-\lambda I)^{\mathsf T}\big)=\det(A-\lambda I)$이다(Determinant 글의 transpose 성질). $\blacksquare$

eigenvalue는 같지만 eigenvector까지 같을 이유는 없다.

## Diagonalization

**Definition (Diagonalizable).** $A\in F^{n\times n}$이 어떤 invertible $P$와 diagonal matrix $D$로 $A=PDP^{-1}$로 쓰이면 diagonalizable이라 한다.

$A=PDP^{-1}$은 $A$가 diagonal matrix $D$와 similar하다는 뜻이다. Linear map 글의 기저 변환으로 읽으면, $P$의 열인 eigenvector들을 기저로 잡을 때 그 기저에서 $A$가 $D$로 표현된다는 것이다. 대각화란 결국 선형사상이 diagonal로 보이는 기저를 찾는 일이다.

**Theorem (eigenvector basis).** $A$가 diagonalizable인 것은 $F^n$이 $A$의 eigenvector로 이루어진 basis를 가지는 것과 동치다.

*Proof.* $A=PDP^{-1}$이면 $AP=PD$이라, $P$의 $j$번째 열 $p_j$에 대해 $Ap_j=d_{jj}p_j$이다. $P$가 invertible이라 그 열들이 basis이고 각각 eigenvector다. 역으로 eigenvector $p_1,\dots,p_n$이 basis를 이루면 이들을 열로 하는 $P$는 invertible이고, 대응 eigenvalue를 대각에 놓은 $D$에 대해 $AP=PD$, 곧 $A=PDP^{-1}$이다. $\blacksquare$

**Example (diagonalization).** 앞의 $$A=\begin{pmatrix}2&1\\1&2\end{pmatrix}$$은 eigenvalue $1,3$과 eigenvector $(1,-1),(1,1)$을 가지므로, $$P=\begin{pmatrix}1&1\\-1&1\end{pmatrix},\qquad D=\begin{pmatrix}1&0\\0&3\end{pmatrix}$$로 두면 $A=PDP^{-1}$이다.

**Example (diagonalizable이 아닌 행렬).** $$A=\begin{pmatrix}1&1\\0&1\end{pmatrix}$$의 characteristic polynomial은 $(1-\lambda)^2$이라 eigenvalue가 $1$ 하나(multiplicity $2$)다. 그런데 $$E_1=\ker(A-I)=\ker\begin{pmatrix}0&1\\0&0\end{pmatrix}=\operatorname{span}\{(1,0)\}$$로 차원이 $1$뿐이라, eigenvector로 $F^2$의 basis를 만들 수 없다. 따라서 $A$는 diagonalizable이 아니다.

참고로 diagonalizable과 invertible은 아무런 상관이 없다. $A$가 invertible인 것은 $0$이 eigenvalue가 아닌 것($\det A\ne0$)과 같고, diagonalizable인 것은 eigenvector basis의 존재라 서로 다른 질문이기 때문이다. 네 조합이 모두 실현된다.

**Example (둘 다 성립).** $I$는 invertible이고 diagonal이다.

**Example (diagonalizable이지만 not invertible).** $$\begin{pmatrix}0&0\\0&0\end{pmatrix}$$은 이미 diagonal이라 diagonalizable이지만, $\det=0$이라 invertible이 아니다.

**Example (invertible이지만 not diagonalizable).** $$\begin{pmatrix}1&1\\0&1\end{pmatrix}$$은 $\det=1$이라 invertible이지만 위에서 보았듯 diagonalizable이 아니다.

**Example (둘 다 아님).** $$\begin{pmatrix}0&1\\0&0\end{pmatrix}$$은 $\det=0$이라 not invertible이고, eigenvalue가 $0$ 하나(multiplicity $2$)인데 $E_0$가 차원 $1$이라 not diagonalizable이다.

diagonalizable이 되는 가장 쉬운 충분조건은 eigenvalue가 모두 다른 것이다.

**Theorem (독립성).** 서로 다른 eigenvalue $\lambda_1,\dots,\lambda_k$에 대한 eigenvector $v_1,\dots,v_k$는 linearly independent이다.

*Proof.* $k$에 대한 induction. $\sum_{i=1}^{k}c_iv_i=0$에 $T-\lambda_k I$를 적용하면 $v_k$ 항이 사라져 $\sum_{i=1}^{k-1}c_i(\lambda_i-\lambda_k)v_i=0$이다. induction 가정으로 $v_1,\dots,v_{k-1}$이 independent이므로 $c_i(\lambda_i-\lambda_k)=0$이고, $\lambda_i\ne\lambda_k$라 $c_i=0$ ($i<k$)이다. 그러면 $c_kv_k=0$에서 $c_k=0$이다. $\blacksquare$

**Corollary (서로 다른 $n$개의 eigenvalue).** $n\times n$ 행렬이 서로 다른 $n$개의 eigenvalue를 가지면 diagonalizable이다.

*Proof.* 각 eigenvalue에서 eigenvector를 하나씩 고르면 위 독립성 정리로 $n$개가 linearly independent라 $F^n$의 basis를 이룬다. 위 eigenvector basis 정리로 diagonalizable이다. $\blacksquare$

역은 성립하지 않는다. 서로 다른 eigenvalue가 $n$개보다 적어도 diagonalizable일 수 있다(예: $I$는 eigenvalue가 $1$ 하나뿐이지만 이미 diagonal이다). 반면 아예 diagonalizable이 아닌 행렬도 있다.

diagonalizable이 되는 또 다른 충분조건은 symmetric이라는 것이다. 심지어 eigenvalue가 모두 real이며 eigenvector가 모두 orthogonal이라는 강력한 결과가 성립한다. 이는 다른 포스트에서 다룬다.

## Trace, determinant와 eigenvalue

characteristic polynomial의 계수는 eigenvalue의 대칭식을 담는다. 그중 가장 기본이 determinant와 trace다.

**Proposition.** characteristic polynomial이 $F$에서 완전히 인수분해되면(eigenvalue $\lambda_1,\dots,\lambda_n$, multiplicity 포함) $$\det A=\prod_{i=1}^{n}\lambda_i,\qquad \operatorname{tr}A=\sum_{i=1}^{n}\lambda_i$$이다.

*Proof.* $p_A(\lambda)=\det(A-\lambda I)=\prod_{i=1}^n(\lambda_i-\lambda)$이다. $\lambda=0$을 넣으면 $\det A=\prod_i\lambda_i$이다. trace는 $\lambda^{n-1}$의 계수를 비교해 얻는다. $\det(A-\lambda I)$를 Leibniz formula로 펼치면 $\lambda^{n-1}$ 항은 대각 곱 $\prod_i(a_{ii}-\lambda)$에서만 나와 그 계수가 $(-1)^{n-1}\operatorname{tr}A$인데, $\prod_i(\lambda_i-\lambda)$에서 같은 계수는 $(-1)^{n-1}\sum_i\lambda_i$이라 둘이 같다. $\blacksquare$

## $A^n$의 eigenvector와 eigenvalue

eigenvector는 $A^n$에 그대로 실려 간다.

**Proposition.** $Av=\lambda v$이면 모든 $n\ge1$에서 $A^nv=\lambda^n v$이다. $A$가 invertible이면($\lambda\ne0$) $A^{-1}v=\lambda^{-1}v$도 성립한다.

*Proof.* $A^nv=A^{n-1}(\lambda v)=\lambda\,A^{n-1}v$로 induction하면 $A^nv=\lambda^n v$이다. invertible이면 $Av=\lambda v$의 양변에 $A^{-1}$을 곱해 $v=\lambda A^{-1}v$, 곧 $A^{-1}v=\lambda^{-1}v$이다. $\blacksquare$

$A$가 diagonalizable이면 $A=PDP^{-1}$에서 $A^n=PD^nP^{-1}$이므로 $A^n$을 한 번에 계산할 수 있다.

**Example ($A^n$ 계산).** 앞서 diagonalize한 $$A=\begin{pmatrix}2&1\\1&2\end{pmatrix}=PDP^{-1}$$에서 $D^n=\operatorname{diag}(1,3^n)$이므로
$$A^n=P\begin{pmatrix}1&0\\0&3^n\end{pmatrix}P^{-1}=\frac12\begin{pmatrix}1+3^n&3^n-1\\3^n-1&1+3^n\end{pmatrix}$$
이다($n=1$을 넣으면 $A$로 돌아온다).

$A^nx$ 하나만 필요할 때는 굳이 $A^n$을 다 구하지 않아도 된다. $x$를 eigenvector들의 합으로 쓰면 각 성분에 $\lambda^n$만 곱하면 되기 때문이다. 아래 Fibonacci가 바로 그 계산이다.

**Example (Fibonacci 수열).** $F_0=0$, $F_1=1$, $F_{n+1}=F_n+F_{n-1}$인 Fibonacci 수열을 보자. $$\begin{pmatrix}F_{n+1}\\F_n\end{pmatrix}=\begin{pmatrix}1&1\\1&0\end{pmatrix}\begin{pmatrix}F_n\\F_{n-1}\end{pmatrix}$$이므로, $$A=\begin{pmatrix}1&1\\1&0\end{pmatrix}$$에 대해 $A^n$이 수열을 준다. $A$의 characteristic polynomial은 $\lambda^2-\lambda-1$이라 eigenvalue가 $\varphi=\dfrac{1+\sqrt5}{2}$, $\psi=\dfrac{1-\sqrt5}{2}$로 서로 다르니 $A$는 diagonalizable이다. 그러면 $F_n=c_1\varphi^n+c_2\psi^n$ 꼴이어야 하고, $F_0=0$, $F_1=1$에서 $c_1=\dfrac1{\sqrt5}$, $c_2=-\dfrac1{\sqrt5}$가 나와
$$F_n=\frac{\varphi^n-\psi^n}{\sqrt5}$$
이다. 정수 수열이 무리수의 거듭제곱 $\varphi^n,\psi^n$으로 정확히 표현되는 이 식은 흔히 Binet의 공식이라 불리지만, 이미 de Moivre가 1730년에 같은 꼴을 얻었다 [2][3].

## Commuting 행렬의 simultaneous diagonalization

**Theorem (Simultaneous Diagonalization).** diagonalizable 행렬 $A,B$에 대해 다음이 동치다. (i) $AB=BA$이다. (ii) 어떤 invertible $P$로 $P^{-1}AP$와 $P^{-1}BP$가 둘 다 diagonal이다(공통 eigenvector basis).

*Proof.* (ii)$\Rightarrow$(i): $P^{-1}AP=D_1$, $P^{-1}BP=D_2$가 diagonal이면 diagonal끼리는 commute하므로 $AB=PD_1D_2P^{-1}=PD_2D_1P^{-1}=BA$이다.

(i)$\Rightarrow$(ii): $A$가 diagonalizable이라 $F^n=\bigoplus_\lambda E_\lambda(A)$이다. $AB=BA$이면 $B$가 각 $E_\lambda(A)$를 보존한다. 실제로 $x\in E_\lambda(A)$이면 $A(Bx)=B(Ax)=\lambda(Bx)$라 $Bx\in E_\lambda(A)$이다. diagonalizable 행렬의 invariant subspace로의 제한은 다시 diagonalizable이므로 각 $E_\lambda(A)$ 안에서 $B$의 eigenvector로 된 basis를 고를 수 있고, 이들은 $E_\lambda(A)$에 있으니 $A$의 eigenvector이기도 하다. 모든 $\lambda$에서 모으면 $A$와 $B$를 동시에 diagonalize하는 공통 basis다. $\blacksquare$

## 참고문헌

1. Hilbert, D. (1904). Grundzüge einer allgemeinen Theorie der linearen Integralgleichungen (Erste Mitteilung). *Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen, Mathematisch-Physikalische Klasse*, 1904, 49–91.
2. Binet, J. P. M. (1843). Mémoire sur l'intégration des équations linéaires aux différences finies d'un ordre quelconque, à coefficients variables. *Comptes Rendus de l'Académie des Sciences*, 17, 559–567.
3. de Moivre, A. (1730). *Miscellanea Analytica de Seriebus et Quadraturis*. London: Tonson & Watts.
