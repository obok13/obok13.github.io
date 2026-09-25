---
layout: post
title: "Determinant"
date: 2026-08-09
mathematicians: [Leibniz, Seki, Cramer, Vandermonde, Laplace, Cauchy, Newton, de Moivre, Lebesgue]
---

## Determinant

체 $F$(예: $\mathbb{R}$, $\mathbb{C}$) 위의 정사각행렬 $A\in F^{n\times n}$에 대해서 행을 $r_1,\dots,r_n$이라고 하자.

**Definition (Determinant).** 각 행에 대한 함수 $D:F^{n\times n}\to F$가 다음을 만족하면 determinant라 하고 $\det$로 쓴다.

- (i) **multilinear**: 각 행에 대해 따로따로 linear이다, 곧 $D(\cdots,\alpha r+\beta r',\cdots)=\alpha D(\cdots,r,\cdots)+\beta D(\cdots,r',\cdots)$.
- (ii) **alternating**: 두 행이 같으면 $D=0$이다.
- (iii) **normalized**: $D(I)=1$.

정의에서 곧바로 계산 규칙 몇 가지가 따라 나온다.

**Proposition (elementary row operation의 효과).** determinant는 다음을 만족한다.

- (a) 두 행을 맞바꾸면 sign이 바뀐다.
- (b) 한 행에 스칼라 $c$를 곱하면 값도 $c$배가 된다.
- (c) 한 행에 다른 행의 스칼라배를 더해도 값은 변하지 않는다.
- (d) 어떤 행이 $0$이면 $\det A=0$이다.

*Proof.* (b)는 multilinearity 그 자체다. (d)는 그 행에 $0=0\cdot0$을 넣어 (b)에서 나온다. (a): 두 행 $r,s$ 자리에 $r+s$를 함께 넣으면 alternating으로 $0$인데, multilinearity로 펼치면 $D(\cdots,r,\cdots,r,\cdots)+D(\cdots,r,\cdots,s,\cdots)+D(\cdots,s,\cdots,r,\cdots)+D(\cdots,s,\cdots,s,\cdots)$이고 양 끝 두 항이 alternating으로 $0$이라 $D(\cdots,r,\cdots,s,\cdots)=-D(\cdots,s,\cdots,r,\cdots)$이다. (c): 행 $r_i$에 $c\,r_j$를 더하면 multilinearity로 $\det A+c\,D(\cdots,r_j,\cdots,r_j,\cdots)$인데 뒤 항은 두 행이 같아 $0$이다. $\blacksquare$

(c)가 핵심이다. Gaussian elimination에서 쓰는 소거 연산이 determinant를 바꾸지 않으므로, 행 교환의 sign과 pivot들만 추적하면 determinant를 계산할 수 있다. 뒤에서 다시 다룬다.

## Big formula

determinant의 존재성과 유일성을 보일 수 있다. 먼저 permutation $\sigma\in S_n$에 대해, $i<j$이면서 $\sigma(i)>\sigma(j)$인 쌍의 개수를 inversion 수라 하고 $\operatorname{sgn}(\sigma):=(-1)^{(\text{inversion 수})}$로 둔다. 이는 $\sigma$를 transposition(두 원소만 맞바꾸는 permutation)들의 곱으로 쓸 때 그 개수의 홀짝과 일치하며, $\operatorname{sgn}(\sigma\tau)=\operatorname{sgn}(\sigma)\operatorname{sgn}(\tau)$이고 transposition 하나의 sign은 $-1$이다.

**Theorem (존재와 유일성, Leibniz Formula).** 각 $n$에 대해 determinant는 유일하게 존재하며
$$\det A=\sum_{\sigma\in S_n}\operatorname{sgn}(\sigma)\,\prod_{i=1}^{n}a_{i,\sigma(i)}$$
로 주어진다.

*Proof.* $D$가 정의의 세 성질을 만족한다고 하자. standard basis로 $i$번째 행을 $r_i=\sum_{j}a_{ij}e_j$로 쓰고 multilinearity로 펼치면
$$D(A)=\sum_{j_1,\dots,j_n}a_{1j_1}\cdots a_{nj_n}\,D(e_{j_1},\dots,e_{j_n})$$
이다. alternating이라 $j_1,\dots,j_n$에 중복이 있으면 그 항은 $0$이니, 남는 것은 $(j_1,\dots,j_n)=(\sigma(1),\dots,\sigma(n))$인 permutation $\sigma$뿐이다. 행을 표준 순서로 정렬하는 데 필요한 맞바꿈의 sign이 $\operatorname{sgn}(\sigma)$이므로 $D(e_{\sigma(1)},\dots,e_{\sigma(n)})=\operatorname{sgn}(\sigma)\,D(e_1,\dots,e_n)=\operatorname{sgn}(\sigma)$이다. 이를 대입하면 위 공식을 얻으니, 세 성질을 만족하는 함수는 있어도 하나뿐이다(uniqueness). 거꾸로 이 공식이 실제로 세 성질을 만족함은 직접 확인된다. 각 항이 각 행에 대해 linear라 multilinear이고, 두 행 $k,l$이 같으면 $\sigma$와 $\sigma\circ(k\,l)$의 항이 sign만 반대라 상쇄되어 alternating이며, $A=I$이면 $\sigma=\mathrm{id}$인 항만 살아남아 값이 $1$이다. 따라서 determinant는 존재한다. $\blacksquare$

**Example ($2\times2$).** $n=2$이면 $S_2$가 두 원소라 $$\det\begin{pmatrix}a&b\\c&d\end{pmatrix}=ad-bc$$이다.

**Example ($3\times3$).** $n=3$이면 $S_3$의 여섯 permutation에서
$$\det\begin{pmatrix}a_{11}&a_{12}&a_{13}\\a_{21}&a_{22}&a_{23}\\a_{31}&a_{32}&a_{33}\end{pmatrix}=a_{11}a_{22}a_{33}+a_{12}a_{23}a_{31}+a_{13}a_{21}a_{32}-a_{13}a_{22}a_{31}-a_{11}a_{23}a_{32}-a_{12}a_{21}a_{33}$$
이 나온다. 이를 첫 행 기준으로 묶으면
$$\det A=a_{11}\det\begin{pmatrix}a_{22}&a_{23}\\a_{32}&a_{33}\end{pmatrix}-a_{12}\det\begin{pmatrix}a_{21}&a_{23}\\a_{31}&a_{33}\end{pmatrix}+a_{13}\det\begin{pmatrix}a_{21}&a_{22}\\a_{31}&a_{32}\end{pmatrix}$$
처럼 sign을 번갈아 붙인 $2\times2$ determinant들의 합이 된다. 이것이 아래에서 다룰 cofactor expansion의 $n=3$ 경우이고, $3\times3$을 손으로 계산할 때 자주 쓰는 방식이다.

이 공식 자체는 행렬 개념보다 앞선다. Leibniz가 1693년 l'Hôpital에게 보낸 편지에서 연립방정식의 풀이를 이 꼴로 적었고 [1], 일본에서는 그보다 앞서 1683년 Seki Takakazu가 독립적으로 같은 것에 도달했다 [2].

## Row reduction으로 계산하기

**Proposition (triangular matrix).** upper triangular matrix(또는 lower triangular matrix)의 determinant는 diagonal 성분의 곱이다.

*Proof.* upper triangular이면 $i>\sigma(i)$인 $i$가 하나라도 있는 항은 그 자리 성분이 $0$이라 사라진다. 모든 $i$에서 $\sigma(i)\ge i$인 permutation은 $\sigma=\mathrm{id}$뿐이므로, Leibniz formula에서 살아남는 항은 $a_{11}a_{22}\cdots a_{nn}$ 하나다. $\blacksquare$

임의의 $A$는 elementary row operation으로 upper triangular $U$가 된다. 위 Proposition (a)(c)에 의해 소거(행에 다른 행의 배수를 더하기)는 determinant를 바꾸지 않고, 행 교환은 sign만 뒤집으므로, $s$번의 행 교환으로 $A$를 $U$로 만들면
$$\det A=(-1)^{s}\,u_{11}u_{22}\cdots u_{nn}$$
이다. 이 알고리즘의 연산량은 Leibniz formula의 $O(n!)$보다 훨씬 줄어든 $O(n^3)$이다.

**Example (row operation 계산).** $$A=\begin{pmatrix}2&1&1\\4&3&3\\8&7&9\end{pmatrix}$$의 determinant를 구하자. $R_2\leftarrow R_2-2R_1$, $R_3\leftarrow R_3-4R_1$, 이어 $R_3\leftarrow R_3-3R_2$로 소거하면 (Gaussian elimination 글의 LU 예와 같은 과정) $$U=\begin{pmatrix}2&1&1\\0&1&1\\0&0&2\end{pmatrix}$$이 되고 행 교환이 없었으므로 $\det A=2\cdot1\cdot2=4$이다.

## Determinant의 성질

**Proposition (transpose).** $\det(A^{\mathsf T})=\det A$.

*Proof.* Leibniz formula에서 $A^{\mathsf T}$의 성분은 $$(A^{\mathsf T})_{i,\sigma(i)}=a_{\sigma(i),i}$$이다. 곱 $\prod_i a_{\sigma(i),i}$에서 인수 순서를 $\sigma(i)$가 커지는 순으로 다시 배열하면 $\prod_i a_{i,\sigma^{-1}(i)}$이고, $\operatorname{sgn}(\sigma)=\operatorname{sgn}(\sigma^{-1})$이므로 $\sigma\mapsto\sigma^{-1}$로 합을 다시 매기면 $\det A$와 같다. $\blacksquare$

transpose가 determinant를 바꾸지 않으므로, 행에 대해 성립하는 모든 성질(multilinear, alternating, row operation)은 열에 대해서도 그대로 성립한다.

**Theorem (Multiplicativity).** $\det(AB)=\det A\,\det B$.

*Proof.* $B$를 고정하고 $D(A):=\det(AB)$를 $A$의 행에 대한 함수로 본다. $AB$의 $i$번째 행은 ($A$의 $i$번째 행)$\cdot B$라 $A$의 각 행에 linear이고, $A$의 두 행이 같으면 $AB$의 두 행도 같아 $0$이므로, $D$는 multilinear이고 alternating이다. 그런데 Big formula의 uniqueness 논증은 normalization을 쓰기 전까지 그대로여서, multilinear·alternating 함수는 $D(A)=D(I)\det A$를 만족한다. 여기서 $D(I)=\det(IB)=\det B$이므로 $\det(AB)=\det A\,\det B$이다. $\blacksquare$

**Corollary (invertibility와 inverse).** $A$가 invertible인 것은 $\det A\ne0$인 것과 동치이며, 그때 $\det(A^{-1})=1/\det A$이다.

*Proof.* $A$가 invertible이면 $AA^{-1}=I$에 multiplicativity를 쓰면 $\det A\,\det(A^{-1})=\det I=1$이라 $\det A\ne0$이고 $\det(A^{-1})=1/\det A$이다. 역으로 $A$가 singular이면 행들이 linearly dependent라 어떤 행이 나머지의 결합이고, 그 행에서 결합을 빼면(row operation, determinant 불변) $0$인 행이 생겨 $\det A=0$이다. $\blacksquare$

multiplicativity 덕분에, 유한차원 벡터공간의 endomorphism에도 기저에 무관하게 determinant를 줄 수 있다.

**Definition (Determinant of an Operator).** 유한차원 $V$의 endomorphism $T$에 대해, 한 기저에서의 행렬 표현 $[T]$의 determinant를 $T$의 determinant $\det T$라 한다.

**Proposition (well-defined).** $\det T$가 잘 정의된다. 즉, basis 선택에 상관 없이 $\det T$의 값이 같다.

*Proof.* 다른 기저에서의 행렬 표현은 어떤 invertible $P$로 $[T]'=P^{-1}[T]P$이므로, multiplicativity로 $$\det[T]'=\det(P^{-1})\det[T]\det P=\det[T]$$이다($\det(P^{-1})\det P=\det I=1$이기 때문이다). $\blacksquare$

**Proposition (Matrix Determinant Lemma).** $u,v\in F^n$에 대해 $\det(I+uv^{\mathsf T})=1+v^{\mathsf T}u$이다.

*Proof.* $u=0$이면 양변이 $1$이다. $u\ne0$이면 $u$를 첫 벡터로 하는 basis를 잡아 그 coordinate로 옮기면(similarity transform은 multiplicativity로 determinant를 보존한다) $uv^{\mathsf T}$는 첫 행만 $0$이 아닌 행렬이 되고, $I+uv^{\mathsf T}$는 upper triangular처럼 diagonal 아래가 정리되어 diagonal 성분의 곱이 $1+v^{\mathsf T}u$가 된다. $\blacksquare$

**Example (diagonal과 나머지가 다른 행렬).** diagonal 성분이 모두 $a$, 나머지 성분이 모두 $b$인 $n\times n$ 행렬 $A$를 보자. $\mathbf{1}=(1,\dots,1)^{\mathsf T}$로 두면 $A=(a-b)I+b\,\mathbf{1}\mathbf{1}^{\mathsf T}$이므로, $a\ne b$일 때 multiplicativity와 Matrix Determinant Lemma로
$$\det A=(a-b)^{n}\det\!\Big(I+\tfrac{b}{a-b}\mathbf{1}\mathbf{1}^{\mathsf T}\Big)=(a-b)^{n}\Big(1+\tfrac{b}{a-b}\,\mathbf{1}^{\mathsf T}\mathbf{1}\Big)=(a-b)^{n-1}\big(a+(n-1)b\big)$$
이다($\mathbf{1}^{\mathsf T}\mathbf{1}=n$). $a=b$이면 모든 행이 같아 $\det A=0$인데, 위 식에 $a=b$를 넣어도 ($n\ge2$) $0$이라 연속적으로 이어진다.

multiplicativity와 이 성질들은 Augustin-Louis Cauchy가 1815년 논문에서 처음 체계적으로 정리했고, 오늘날의 "déterminant"라는 이름과 이론의 골격도 그 논문에서 나왔다 [6].

## Cofactor expansion과 inverse

Big formula의 항들을 한 행의 성분별로 묶으면 recursive expansion이 나온다. $A$에서 $i$번째 행과 $j$번째 열을 지운 $(n-1)\times(n-1)$ 행렬의 determinant를 minor $M_{ij}$라 하고, $C_{ij}:=(-1)^{i+j}M_{ij}$를 cofactor라 한다.

**Theorem (Cofactor Expansion).** 임의의 행 $i$에 대해 $\det A=\sum_{j=1}^{n}a_{ij}C_{ij}$이고, 임의의 열 $j$에 대해 $\det A=\sum_{i=1}^{n}a_{ij}C_{ij}$이다.

*Proof.* Leibniz formula에서 $i$번째 행의 성분 $a_{ij}$가 곱에 들어가는 항들을 모으면, $\sigma(i)=j$인 permutation들의 합이다. 이 조건 아래의 합은 sign $(-1)^{i+j}$를 빼면 정확히 $i$행 $j$열을 지운 행렬의 Leibniz formula, 곧 $M_{ij}$가 된다. 따라서 $a_{ij}$의 계수가 $C_{ij}$이다. 열에 대한 expansion은 transpose에 적용하면 나온다. $\blacksquare$

cofactor expansion은 Laplace expansion이라고도 하며, Pierre-Simon Laplace가 1772년 논문에서 제시했다 [5].

**Example ($3\times3$ 계산).** $$A=\begin{pmatrix}1&2&3\\0&4&5\\1&0&6\end{pmatrix}$$을 첫 행으로 cofactor expansion하면 $$\det A=1\det\begin{pmatrix}4&5\\0&6\end{pmatrix}-2\det\begin{pmatrix}0&5\\1&6\end{pmatrix}+3\det\begin{pmatrix}0&4\\1&0\end{pmatrix}=1\cdot24-2\cdot(-5)+3\cdot(-4)=22$$이다.

**Example (recurrence와 Fibonacci).** diagonal 성분이 $1$, 바로 위 diagonal이 $1$, 바로 아래 diagonal이 $-1$이고 나머지가 $0$인 $n\times n$ tridiagonal matrix의 determinant $D_n$을 첫 행으로 cofactor expansion하면 $D_n=D_{n-1}+D_{n-2}$가 된다. $D_1=1$, $D_2=2$에서 시작하니 $D_n$은 Fibonacci 수 $F_{n+1}$이다. 하나의 determinant가 recurrence를 통해 수열로 이어지는 예다.

**Example (second difference 행렬).** diagonal이 모두 $2$, 바로 위와 바로 아래 diagonal이 $-1$이고 나머지가 $0$인 $n\times n$ tridiagonal matrix의 determinant $D_n$은 같은 방식의 cofactor expansion으로 $D_n=2D_{n-1}-D_{n-2}$를 만족한다. $D_1=2$, $$D_2=\det\begin{pmatrix}2&-1\\-1&2\end{pmatrix}=3$$에서 시작하니 $D_n=n+1$이다.

cofactor를 모으면 inverse 공식이 나온다.

**Definition (Cofactor Matrix).** cofactor $C_{ij}$를 $(i,j)$ 성분으로 갖는 $n\times n$ 행렬 $C=(C_{ij})$를 $A$의 cofactor matrix라 한다.

**Theorem (Inverse via Cofactor Matrix).** cofactor matrix의 transpose $C^{\mathsf T}$($(i,j)$ 성분이 $C_{ji}$)에 대해 $A\,C^{\mathsf T}=C^{\mathsf T}A=(\det A)\,I$이다. 따라서 $A$가 invertible이면 $$A^{-1}=\frac{1}{\det A}\,C^{\mathsf T}$$이다.

*Proof.* $A\,C^{\mathsf T}$의 $(i,i)$ 성분은 $\sum_j a_{ij}C_{ij}=\det A$(cofactor expansion)이다. $i\ne k$인 $(i,k)$ 성분은 $\sum_j a_{ij}C_{kj}$인데($C^{\mathsf T}$의 $(j,k)$ 성분이 $C_{kj}$이므로), 이는 $A$의 $k$번째 행을 $i$번째 행으로 바꾼 행렬(두 행이 같아 determinant가 $0$)을 $k$행으로 cofactor expansion한 것이라 $0$이다. 그러므로 곱이 $(\det A)I$이다. $\blacksquare$

이 항등식은 $\det A=0$인 경우에도, 또 성분에 미지수가 섞인 행렬에도 (양변이 성분들에 대한 polynomial 항등식이라) 그대로 성립한다.

## Cramer's Rule

**Theorem (Cramer's Rule).** $\det A\ne0$이면 $Ax=b$의 유일한 해는 $$x_i=\frac{\det A_i}{\det A}$$로 주어진다. 여기서 $A_i$는 $A$의 $i$번째 열을 $b$로 바꾼 행렬이다.

*Proof.* $A$의 열을 $a_1,\dots,a_n$이라 하면 $b=Ax=\sum_k x_k a_k$이다. determinant를 열에 대한 alternating multilinear로 보고 $A_i$의 $i$번째 열에 이 $b$를 넣으면
$$\det A_i=\det(a_1,\dots,\underbrace{\textstyle\sum_k x_k a_k}_{i\text{번째}},\dots,a_n)=\sum_k x_k\det(a_1,\dots,\overset{i}{a_k},\dots,a_n)$$
인데, $k\ne i$인 항은 $a_k$가 두 번 나타나 alternating으로 $0$이고 $k=i$인 항만 $x_i\det A$로 남는다. 따라서 $\det A_i=x_i\det A$이다. $\blacksquare$

Cramer's rule은 Gabriel Cramer가 1750년 대수곡선을 다루는 책에서 연립방정식의 해를 이 꼴로 제시한 데서 이름을 얻었다 [3]. 해를 닫힌 식으로 준다는 점에서 이론적으로 아름답지만, 각 $\det A_i$를 따로 계산해야 해서 실제 수치 계산에는 Gaussian elimination이 훨씬 빠르다.

## Vandermonde matrix

Big formula를 정면으로 펼치는 대신 성질을 엮으면, 얼핏 복잡해 보이는 determinant도 factorize된 꼴로 단번에 나온다.

**Theorem (Vandermonde).** $x_1,\dots,x_n\in F$에 대해
$$\det\begin{pmatrix}1&x_1&x_1^2&\cdots&x_1^{n-1}\\1&x_2&x_2^2&\cdots&x_2^{n-1}\\\vdots&\vdots&\vdots&&\vdots\\1&x_n&x_n^2&\cdots&x_n^{n-1}\end{pmatrix}=\prod_{1\le i<j\le n}(x_j-x_i).$$

*Proof.* 이 determinant를 $V(x_1,\dots,x_n)$이라 하면, 마지막 변수 $x_n$의 $n-1$차 polynomial이다. $x_n=x_i$ ($i<n$)이면 두 행이 같아 $0$이 되므로 $V$는 $(x_n-x_1)\cdots(x_n-x_{n-1})$을 인수로 가진다. 최고차항 $x_n^{n-1}$의 계수는 cofactor expansion으로 $V(x_1,\dots,x_{n-1})$이므로 $V(x_1,\dots,x_n)=V(x_1,\dots,x_{n-1})\prod_{i<n}(x_n-x_i)$이고, $n$에 대한 induction으로 공식을 얻는다. $\blacksquare$

특히 Vandermonde determinant는 $x_i$가 서로 다를 때만 $0$이 아니다. 이는 서로 다른 $n$개의 점을 지나는 $n-1$차 polynomial이 유일하게 존재한다는 polynomial interpolation의 근거가 된다. 역사적으로 이 determinant는 Alexandre-Théophile Vandermonde의 이름을 달고 있지만, 정작 그의 1772년 논문에는 이 형태가 등장하지 않는다는 유명한 misattribution을 Henri Lebesgue가 지적했다 [7]. 실제로 일반적인 $n$에 대해 이 공식을 증명한 것은 앞서 인용한 Cauchy의 1815년 논문 [6]인데, 그 논문이 바로 determinant를 처음으로 정의한 논문이기도 하다. 그보다도 더 앞서서, 이런 계수를 가진 연립방정식 자체는 Newton이 1711년 유작 *Methodus Differentialis*에서 이미 적어 두었고 [8], 그 해를(오늘날 "Lagrange interpolation formula"라 불리는 꼴로) 처음 명시적인 식으로 쓴 것은 Abraham de Moivre였다 [9]. 다만 둘 다 이를 determinant로 인식하지는 못했다. Vandermonde 자신은 1770년 논문에서 $n=3$인 특수한 경우의 이 곱을 직접 전개했고, 1771년 논문에서는 자신의 조합론적 표기에서 index를 지수로 바꾸면 alternating function이 얻어진다는 관찰을 남겼는데 [4], 후자가 Cauchy(와 Jacobi)에게 영감을 준 것으로 여겨진다 [10].

## 참고문헌

1. Leibniz, G. W. (1693). Lettre à G. F. A. de l'Hôpital (28 avril 1693). In C. I. Gerhardt (Ed.), *Leibnizens mathematische Schriften* (Bd. II, pp. 238–240). Berlin: A. Asher (1850).
2. Seki, T. (1683). *Kai Fukudai no Hō* (解伏題之法) [Method of Solving the Dissimulated Problems].
3. Cramer, G. (1750). *Introduction à l'analyse des lignes courbes algébriques*. Genève: Frères Cramer & Cl. Philibert.
4. Vandermonde, A.-T. (1772). Mémoire sur l'élimination. *Histoire de l'Académie Royale des Sciences (Paris)*, année 1772 (2e partie), 516–532.
5. Laplace, P.-S. (1772). Recherches sur le calcul intégral et sur le système du monde. *Histoire de l'Académie Royale des Sciences (Paris)*, année 1772 (2e partie), 267–376.
6. Cauchy, A.-L. (1815). Mémoire sur les fonctions qui ne peuvent obtenir que deux valeurs égales et de signes contraires par suite des transpositions opérées entre les variables qu'elles renferment. *Journal de l'École Polytechnique*, 10, 29–112.
7. Lebesgue, H. (1937/1958). L'œuvre mathématique de Vandermonde. In *Notices d'Histoire des Mathématiques*. Genève: Université de Genève, 18–39.
8. Newton, I. (1711). Methodus Differentialis. In *Analysis per Quantitatum Series, Fluxiones, ac Differentias*. London: Pearson.
9. de Moivre, A. (1730). *Miscellanea Analytica de Seriebus et Quadraturis*. London, 33–35.
10. Ycart, B. (2013). A case of mathematical eponymy: the Vandermonde determinant. *Revue d'histoire des mathématiques*, 19(1), 43–77.
