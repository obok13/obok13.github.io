---
layout: post
title: "Gaussian elimination"
date: 2026-08-07
mathematicians: [Gauss, Wilhelm Jordan]
---

## $Ax=b$의 해

여기서는 행렬 $A$로 표현되는 연립방정식 $Ax=b$를 어떻게 풀 것인가를 다룬다. $A\in F^{m\times n}$, $b\in F^m$라고 하면

**Proposition (해의 구조).** $Ax=b$가 해를 가지는 것은 $b\in C(A)$인 것과 동치다. 해가 있을 때 particular solution 하나를 $x_p$라 하면 해 전체는
$$\{\,x_p+z : z\in N(A)\,\}$$
이다. 따라서 해가 유일한 것은 $$N(A)=\{0\}$$인 것과 동치이고, 그렇지 않으면 해는 없거나 무한히 많다.

*Proof.* $Ax=b$가 풀린다는 것은 $b$가 열들의 조합, 곧 $b\in C(A)$라는 뜻이다. $x_p$가 해이면 $A(x_p+z)=b+Az=b$ ($z\in N(A)$)이라 $x_p+z$도 해이고, 역으로 $x$가 해이면 $A(x-x_p)=0$이라 $x-x_p\in N(A)$이다. $\blacksquare$

존재는 $C(A)$가, 자유도는 $N(A)$가 결정한다. 이제 이 두 공간을 손으로 계산하는 도구가 소거법이다.

## Echelon form

**Definition (Elementary Row Operations).** 행렬에 가하는 다음 세 연산을 elementary row operation이라 한다. (1) 두 행을 맞바꾼다. (2) 한 행에 $0$이 아닌 스칼라를 곱한다. (3) 한 행에 다른 행의 스칼라배를 더한다.

각 elementary row operation은 항등행렬에 그 연산을 가해 얻는 elementary matrix $E$를 왼쪽에 곱하는 것과 같고, 이 $E$는 가역이다. 그리고 augmented matrix $$[\,A\mid b\,]$$에 elementary row operation을 가하는 것은 연립방정식을 동치로 바꾸는 것이라 해집합을 보존한다.

**Definition (Row Echelon Form).** 다음을 만족하는 행렬을 행 사다리꼴(row echelon form, REF)이라 한다. 각 행에서 처음 나오는 $0$이 아닌 성분(pivot)이 바로 윗 행의 pivot보다 오른쪽에 있고, 어떤 pivot 아래의 성분은 모두 $0$이다.

**Theorem.** 임의의 행렬은 유한 번의 elementary row operation으로 REF가 된다. 이때 pivot의 개수는 $\operatorname{rank}A$와 같다.

*Proof.* 왼쪽 열부터 $0$이 아닌 성분을 pivot으로 골라 그 아래를 (3)번 연산으로 소거하고, 다음 열로 내려가며 반복하면 REF에 도달한다. pivot이 있는 열들은 앞선 열들의 조합이 아닌 열이고, 이들이 $C(A)$의 기저를 이루므로 pivot 개수는 $\dim C(A)=\operatorname{rank}A$이다. $\blacksquare$

**Example (소거).** $A=\begin{pmatrix}1&2&1\\2&4&3\end{pmatrix}$에서 둘째 행에 첫째 행의 $-2$배를 더하면 $\begin{pmatrix}1&2&1\\0&0&1\end{pmatrix}$이 되어 REF다. pivot은 1열과 3열에 있고 $\operatorname{rank}A=2$이다.

## RREF와 Gauss-Jordan

REF에서 한 걸음 더 나아가면 표준형에 도달한다.

**Definition (Reduced Row Echelon Form).** REF이면서 모든 pivot이 $1$이고, 각 pivot이 자기 열에서 유일한 $0$이 아닌 성분인 행렬을 기약 행 사다리꼴(reduced row echelon form, RREF)이라 한다.

아래로만 소거하는 Gauss 소거법에서 멈추지 않고 pivot 위쪽까지 마저 소거해 RREF에 이르는 방법을 Gauss-Jordan 소거법이라 한다. REF는 소거 순서에 따라 여러 개가 나올 수 있지만, RREF는 그렇지 않다.

**Theorem (RREF의 유일성).** 모든 행렬의 RREF는 유일하다.

*Proof.* elementary row operation은 가역행렬 $E$를 왼쪽에 곱하는 것이고, $E$가 가역이므로 열들 사이의 일차결합 관계가 보존된다. 즉 $\sum_j c_j a_j=0$인 것과 $\sum_j c_j(Ea_j)=0$인 것이 동치다. 그러면 "어떤 열이 앞선 열들의 일차결합인가"(곧 non-pivot 열이 무엇이고 그 조합의 계수가 얼마인가)가 $A$만으로 정해진다. RREF에서 pivot 열은 standard basis vector가 되고 non-pivot 열은 앞선 pivot 열들로 그 계수만큼 표현되므로, RREF의 모든 성분이 이 불변 정보로 결정된다. 따라서 RREF는 유일하다. $\blacksquare$

**Example (RREF).** $A=\begin{pmatrix}2&4&6\\2&8&10\end{pmatrix}$를 보자. $R_2\leftarrow R_2-R_1$로 소거하면 REF $\begin{pmatrix}2&4&6\\0&4&4\end{pmatrix}$을 얻는데, pivot이 $2,4$라 아직 $1$이 아니다. 각 pivot 행을 그 pivot으로 나눠($R_1\leftarrow\tfrac12R_1$, $R_2\leftarrow\tfrac14R_2$)
$$\begin{pmatrix}1&2&3\\0&1&1\end{pmatrix}$$
로 만든 뒤, 2열 pivot 위쪽을 $R_1\leftarrow R_1-2R_2$로 마저 소거하면 RREF $\begin{pmatrix}1&0&1\\0&1&1\end{pmatrix}$에 이른다.

## $Ax=b$의 general solution

RREF는 해를 통째로 읽게 해준다. augmented matrix $$[\,A\mid b\,]$$를 RREF로 만들면, pivot이 있는 변수(pivot variable)와 그렇지 않은 변수(free variable)로 갈린다. free variable의 개수는 $n-r$로 $\dim N(A)$와 같다.

**Theorem (general solution).** $Ax=b$가 무모순이면(즉 $b$ 쪽 열에 pivot이 생기지 않으면) 그 해는
$$x = x_p + t_1s_1 + \cdots + t_{n-r}s_{n-r}$$
꼴이다. 여기서 $x_p$는 free variable을 모두 $0$으로 둔 particular solution이고, $s_1,\dots,s_{n-r}$은 free variable을 하나씩만 $1$로 두어 얻는 $N(A)$의 기저(special solution)다.

*Proof.* RREF에서 pivot variable을 free variable로 풀어낸 것이 곧 위 표현이며, $x_p$는 particular solution, $\operatorname{span}\{s_i\}=N(A)$이므로 앞 Proposition의 $x_p+N(A)$와 일치한다. $\blacksquare$

**Example (general solution).** $A=\begin{pmatrix}1&2&1\\2&4&3\end{pmatrix}$, $b=(3,7)$을 보자. augmented matrix를 소거하면 둘째 행이 $(0,0,1\mid 1)$이 되어 $x_3=1$이고, 첫째 행에서 $x_1+2x_2+x_3=3$, 즉 $x_1=2-2x_2$이다. $x_2$가 free variable이므로 general solution은
$$x = (2,0,1) + x_2\,(-2,1,0)$$
이다. particular solution $(2,0,1)$에 $N(A)$의 기저 $(-2,1,0)$이 붙었다.

## LU 분해

소거 과정을 버리지 않고 기록하면 행렬 분해가 된다. 행 교환 없이 소거할 수 있는 경우, 아래로 소거하는 (3)번 연산들은 모두 unit lower triangular elementary matrix를 왼쪽에 곱하는 것이라, 그 역들을 모으면 lower triangular matrix $L$이 되고 소거 결과 $U$는 upper triangular matrix(REF)이 된다.

**Theorem (LU Decomposition).** 정사각행렬 $A$를 행 교환 없이 소거할 수 있으면 $A=LU$로 쓸 수 있다. 여기서 $L$은 대각이 모두 $1$이고 소거에 쓴 배수(multiplier)를 성분으로 갖는 lower triangular matrix이고, $U$는 upper triangular matrix이다.

이 분해가 있으면 $Ax=b$는 $Ly=b$를 forward substitution으로, $Ux=y$를 back substitution으로 풀어 두 번의 triangular system으로 쪼개진다.

**Example (LU).** $A=\begin{pmatrix}2&1&1\\4&3&3\\8&7&9\end{pmatrix}$를 소거하자. 1열에서 $R_2\leftarrow R_2-2R_1$, $R_3\leftarrow R_3-4R_1$ (multiplier $2,4$)을 하면
$$\begin{pmatrix}2&1&1\\0&1&1\\0&3&5\end{pmatrix}$$
이 되고, 이어 2열에서 $R_3\leftarrow R_3-3R_2$ (multiplier $3$)을 하면 upper triangular matrix
$$U=\begin{pmatrix}2&1&1\\0&1&1\\0&0&2\end{pmatrix}$$
을 얻는다. 소거하며 $L$의 $(i,j)$ 자리에 "$j$열을 소거할 때 $i$행에 쓴 배수"를 그대로 담으면
$$L=\begin{pmatrix}1&0&0\\2&1&0\\4&3&1\end{pmatrix}$$
이 되고 $A=LU$가 확인된다. 이것이 LU 분해를 구하는 알고리즘이다.

$U$의 대각 성분(=pivot)을 뽑아 diagonal matrix $D$로 모으고 $U=DU'$($U'$은 대각이 $1$인 upper triangular matrix)로 쓰면, lower triangular·diagonal·upper triangular로 깔끔히 분리된 $A=LDU'$을 얻는다. 이를 LDU 분해라 한다.

**Example (LDU).** 위 $U$의 pivot이 $2,1,2$이므로 $D=\operatorname{diag}(2,1,2)$이고
$$U'=\begin{pmatrix}1&\tfrac12&\tfrac12\\0&1&1\\0&0&1\end{pmatrix}, \qquad A=\begin{pmatrix}1&0&0\\2&1&0\\4&3&1\end{pmatrix}\!\begin{pmatrix}2&0&0\\0&1&0\\0&0&2\end{pmatrix}\!\begin{pmatrix}1&\tfrac12&\tfrac12\\0&1&1\\0&0&1\end{pmatrix}$$
이다.

이 분해는 유일하다.

**Proposition (LDU의 유일성).** 가역행렬 $A$가 행 교환 없이 $A=LDU'$($L$은 unit lower triangular, $D$는 diagonal, $U'$은 unit upper triangular)로 분해되면 $L,D,U'$은 유일하게 정해진다.

*Proof.* $L_1D_1U_1'=L_2D_2U_2'$이라 하자. $L_2^{-1}L_1=D_2U_2'U_1'^{-1}D_1^{-1}$인데 좌변은 unit lower triangular, 우변은 upper triangular이므로 양변은 대각이 $1$인 diagonal, 곧 $I$다. 따라서 $L_1=L_2$이고, 남은 $D_1U_1'=D_2U_2'$에서 양변의 대각(= $U'$의 대각이 $1$이므로 각각 $D_1,D_2$)을 비교하면 $D_1=D_2$, 이어 $U_1'=U_2'$이다. $\blacksquare$

## PA=LU와 PA=LDU

pivot 자리에 $0$이 나오면 행을 바꿔야 한다. 소거 중에 필요한 행 교환들을 하나의 permutation matrix $P$로 모으면 다음이 성립한다.

**Theorem.** 임의의 행렬 $A$에 대해 $PA=LU$인 permutation matrix $P$, unit lower triangular matrix $L$, row echelon form $U$가 존재한다. 앞서처럼 $U=DU'$로 pivot을 뽑으면 $PA=LDU'$이 된다.

여기서 $P$ 자체는 유일하지 않다. 피벗으로 어느 행을 끌어올릴지에 따라 여러 $P$가 가능하고 그에 따라 $L,U$도 달라진다. 그러나 $P$를 하나 고정해 $PA$가 행 교환 없이 소거되면, $PA$에 위 LDU 유일성이 그대로 적용되어 $L,D,U'$이 유일하게 정해진다.

**Example (PA=LDU, 그리고 RREF).** 직사각행렬
$$A=\begin{pmatrix}0&1&2&2\\2&4&2&6\\4&8&6&14\end{pmatrix}$$
를 소거하자. $(1,1)$ 성분이 $0$이라 $R_1\leftrightarrow R_2$로 행을 바꾼다. 이 교환을 담은 $P=\begin{pmatrix}0&1&0\\1&0&0\\0&0&1\end{pmatrix}$에 대해 $PA$를 소거하면, $R_3\leftarrow R_3-2R_1$ 뒤
$$U=\begin{pmatrix}2&4&2&6\\0&1&2&2\\0&0&2&2\end{pmatrix}, \qquad L=\begin{pmatrix}1&0&0\\0&1&0\\2&0&1\end{pmatrix}$$
로 $PA=LU$이다. pivot이 $2,1,2$이므로 $D=\operatorname{diag}(2,1,2)$, $U'=\begin{pmatrix}1&2&1&3\\0&1&2&2\\0&0&1&1\end{pmatrix}$로 갈라 $PA=LDU'$을 얻는다.

여기서 멈추지 않고 pivot을 $1$로 만든 뒤 위쪽까지 소거하면(Gauss-Jordan) RREF
$$\begin{pmatrix}1&0&0&2\\0&1&0&0\\0&0&1&1\end{pmatrix}$$
에 이른다. pivot이 1·2·3열, free variable이 4열이라 $\operatorname{rank}A=3$, $\dim N(A)=1$임이 한눈에 읽힌다.

연립방정식을 소거로 푸는 방법 자체는 아주 오래되어 중국의 《구장산술》 방정(方程) 장에 이미 나타난다 [1]. 오늘날의 이름은 Gauss가 천체 궤도 계산의 최소제곱에서 체계적으로 쓴 데서 왔고 [2], 위쪽까지 완전히 소거하는 변형은 측지학자 Wilhelm Jordan의 이름을 붙여 Gauss-Jordan 소거법이라 부른다 [3].

## 역행렬

정사각행렬에서 소거가 끝까지 통하면 그 자체가 역행렬을 준다.

**Definition (Inverse).** 정사각행렬 $A\in F^{n\times n}$에 대해 $AB=BA=I$인 $B$가 있으면 $A$를 가역(invertible)이라 하고 $B$를 $A^{-1}$로 쓴다. 가역이 아닌 정사각행렬은 singular(특이행렬)이라 한다.

**Proposition (역행렬의 유일성).** 가역행렬의 역행렬은 유일하다.

*Proof.* $B,B'$이 모두 $A$의 역행렬이면 $B'=B'(AB)=(B'A)B=B$이다. $\blacksquare$

**Theorem (가역성 동치조건).** 정사각행렬 $A\in F^{n\times n}$에 대해 다음은 모두 동치다. (a) $A$가 가역이다. (b) $$N(A)=\{0\}$$. (c) $\operatorname{rank}A=n$. (d) $A$의 열이 $F^n$의 기저다. (e) 모든 $b$에 대해 $Ax=b$가 유일한 해를 가진다. (f) $A$의 RREF가 $I$다.

*Proof.* (b)$\iff$(c)는 rank-nullity($n=\operatorname{rank}A+\dim N(A)$)에서, (c)$\iff$(d)는 $n$개의 일차독립인 열이 곧 기저라는 데서 나온다. (c)$\iff$(f)는 pivot이 $n$개면 RREF가 $I$이기 때문이다. (e)는 앞 Proposition에서 존재($C(A)=F^n$)와 유일($N(A)=\{0\}$)을 합친 것이라 (b),(c)와 동치다. 끝으로 RREF가 $I$이면 소거에 쓴 가역행렬들의 곱 $E_k\cdots E_1$이 $A$의 양쪽 역행렬이 되어 (a)가 나오고, 역으로 가역이면 (e)가 성립한다. $\blacksquare$

$(AB)^{-1}=B^{-1}A^{-1}$, $(A^{-1})^{-1}=A$, $(A^{\mathsf T})^{-1}=(A^{-1})^{\mathsf T}$도 정의에서 곧바로 확인된다.

정사각행렬에서는 한쪽 역행렬만 있어도 곧 양쪽 역행렬이 된다.

**Proposition.** 정사각 $A$에 대해 $BA=I$이면 $AB=I$이고 $B=A^{-1}$이다. $AB=I$인 경우도 마찬가지다. 즉 정사각행렬에서는 left inverse의 존재와 right inverse의 존재가 동치이고, 둘은 같은 행렬이다.

*Proof.* $BA=I$이면 $Ax=0\Rightarrow x=BAx=0$이라 $$N(A)=\{0\}$$, 위 정리에 의해 $A$는 가역이다. 그러면 $B=B(AA^{-1})=(BA)A^{-1}=A^{-1}$이므로 $B$는 양쪽 역행렬이다. $AB=I$인 경우는 전치를 취해 $B^{\mathsf T}A^{\mathsf T}=I$에 위 논증을 적용하면 된다. $\blacksquare$

역행렬을 실제로 구하는 방법이 위 증명에 이미 들어 있다.

**Theorem (Gauss-Jordan으로 역행렬).** 가역인 $A$에 대해 augmented matrix $$[\,A\mid I\,]$$를 RREF로 만들면 왼쪽이 $I$가 되고, 그때 오른쪽이 $A^{-1}$이다.

*Proof.* elementary row operation은 왼쪽 곱이므로, RREF로 만드는 과정은 어떤 가역행렬 $M=E_k\cdots E_1$을 왼쪽에 곱하는 것이다. 왼쪽 블록이 $MA=I$가 되었다면 $M=A^{-1}$이고, 같은 연산이 오른쪽 블록 $I$에는 $MI=A^{-1}$을 남긴다. $\blacksquare$

**Example (역행렬).** $A=\begin{pmatrix}1&0&1\\2&1&2\\1&1&2\end{pmatrix}$의 역행렬을 구하자. augmented matrix $$[\,A\mid I\,]$$에 Gauss-Jordan을 적용한다.
$$\left[\begin{array}{ccc}1&0&1\\2&1&2\\1&1&2\end{array}\middle\vert\begin{array}{ccc}1&0&0\\0&1&0\\0&0&1\end{array}\right]$$
1열 아래를 $R_2\leftarrow R_2-2R_1$, $R_3\leftarrow R_3-R_1$로 소거하면
$$\left[\begin{array}{ccc}1&0&1\\0&1&0\\0&1&1\end{array}\middle\vert\begin{array}{ccc}1&0&0\\-2&1&0\\-1&0&1\end{array}\right]$$
이고, 2열 아래를 $R_3\leftarrow R_3-R_2$로 소거하면
$$\left[\begin{array}{ccc}1&0&1\\0&1&0\\0&0&1\end{array}\middle\vert\begin{array}{ccc}1&0&0\\-2&1&0\\1&-1&1\end{array}\right]$$
이다. 이제 위쪽을 $R_1\leftarrow R_1-R_3$로 소거하면 왼쪽이 $I$가 된다.
$$\left[\begin{array}{ccc}1&0&0\\0&1&0\\0&0&1\end{array}\middle\vert\begin{array}{ccc}0&1&-1\\-2&1&0\\1&-1&1\end{array}\right]$$
왼쪽이 $I$이므로 오른쪽이 역행렬이고, 따라서 $$A^{-1}=\begin{pmatrix}0&1&-1\\-2&1&0\\1&-1&1\end{pmatrix}$$이다. 실제로 $AA^{-1}=I$로 확인된다.

## left inverse와 right inverse

정사각이 아니면 양쪽 역행렬은 불가능하지만, 한쪽 역행렬은 존재할 수 있다. 그 조건은 지난 글의 injective/surjective와 정확히 맞물린다.

**Theorem (한쪽 역행렬).** $A\in F^{m\times n}$에 대해:
1. left inverse($BA=I_n$인 $B$)가 존재 $\iff x\mapsto Ax$가 injective $\iff N(A)=\{0\}\iff\operatorname{rank}A=n$ (full column rank).
2. right inverse($AC=I_m$인 $C$)가 존재 $\iff x\mapsto Ax$가 surjective $\iff C(A)=F^m\iff\operatorname{rank}A=m$ (full row rank).
3. 양쪽 역행렬이 모두 존재 $\iff m=n=\operatorname{rank}A$, 곧 $A$가 정사각이면서 가역이다.

*Proof.* (1) $BA=I_n$이면 $Ax=0$에서 $x=BAx=0$이라 injective다. 역으로 injective, 즉 $A$가 $F^n$을 $C(A)$로 일대일 대응시키면, 이 대응의 역을 $C(A)$ 위에서 정의하고 $F^m$의 나머지 방향으로는 아무렇게나 선형 확장한 $B$가 $BA=I_n$을 만족한다. injective $\iff N(A)=\{0\}\iff\operatorname{rank}A=n$은 지난 글에서 보았다. (2) $AC=I_m$이면 임의의 $b$가 $A(Cb)=b$로 상에 있어 surjective다. 역으로 surjective이면 $F^m$의 standard basis 각각의 원상을 골라 열로 세운 $C$가 $AC=I_m$을 준다. (3)은 (1)과 (2)를 합치면 $n=\operatorname{rank}A=m$이다. $\blacksquare$

정사각이 아닌 경우 한쪽 역행렬은 유일하지 않다(확장의 자유가 있기 때문이다). 양쪽 역행렬만 유일하다.

**Example (left inverse).** $A=\begin{pmatrix}1&0\\0&1\\1&1\end{pmatrix}$은 $3\times2$이고 열이 일차독립이라 full column rank다. $B=\begin{pmatrix}1&0&0\\0&1&0\end{pmatrix}$이 $BA=I_2$를 만족하는 left inverse인데, $B=\begin{pmatrix}0&-1&1\\-1&0&1\end{pmatrix}$ 역시 $BA=I_2$라 left inverse가 여럿임을 볼 수 있다.

**Example (right inverse).** $A=\begin{pmatrix}1&0&1\\0&1&1\end{pmatrix}$은 $2\times3$이고 행이 일차독립이라 full row rank다. $C=\begin{pmatrix}1&0\\0&1\\0&0\end{pmatrix}$이 $AC=I_2$인 right inverse이고, $C=\begin{pmatrix}0&-1\\-1&0\\1&1\end{pmatrix}$ 역시 $AC=I_2$라 right inverse도 여럿이다.

한쪽 역행렬을 실행렬에서는 $A^{\mathsf T}A$로 명시적으로 만들 수 있는데, 그 바탕에 다음 사실이 있다.

**Proposition.** 실행렬 $A\in\mathbb{R}^{m\times n}$에 대해 $N(A^{\mathsf T}A)=N(A)$이다. 특히 $A$가 full column rank이면 $A^{\mathsf T}A$($n\times n$)는 가역이다.

*Proof.* $Ax=0$이면 당연히 $A^{\mathsf T}Ax=0$이다. 역으로 $A^{\mathsf T}Ax=0$이면 $\lVert Ax\rVert^2=x^{\mathsf T}A^{\mathsf T}Ax=0$이라 $Ax=0$이다(여기서 실수 성분의 표준 내적을 썼다). 따라서 두 null space가 같다. full column rank이면 $$N(A)=\{0\}$$이므로 $$N(A^{\mathsf T}A)=\{0\}$$, 곧 정사각행렬 $A^{\mathsf T}A$가 가역이다. $\blacksquare$

이 덕분에 full column rank인 실행렬은 $B=(A^{\mathsf T}A)^{-1}A^{\mathsf T}$라는 명시적 left inverse를 가진다($BA=(A^{\mathsf T}A)^{-1}A^{\mathsf T}A=I_n$).

## 참고문헌

1. *구장산술(九章算術)* (Nine Chapters on the Mathematical Art), 방정(方程) 장, 대략 기원후 1세기.
2. Gauss, C. F. (1809). *Theoria motus corporum coelestium in sectionibus conicis solem ambientium*. Hamburg: Perthes & Besser.
3. Jordan, W. (1888). *Handbuch der Vermessungskunde*, Band 1. Stuttgart: Metzler.
