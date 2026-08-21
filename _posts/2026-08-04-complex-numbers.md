---
layout: post
title: "복소수 (Complex Numbers)"
date: 2026-08-04
mathematicians: [Cardano, Bombelli, de Moivre, Euler, Wessel, Argand, Gauss, Hamilton, d'Alembert]
---

## 복소수의 등장

복소수가 처음 수면 위로 떠오른 것은 Cardano가 1545년 《Ars Magna》에서 삼차방정식을 풀 때다 [1]. 일반 삼차방정식은 간단한 치환으로 $t^3+pt+q=0$ 꼴로 바꿀 수 있고, 그 근은 Cardano 공식

$$t = \sqrt[3]{-\frac{q}{2}+\sqrt{R}} + \sqrt[3]{-\frac{q}{2}-\sqrt{R}}, \qquad R := \frac{q^2}{4}+\frac{p^3}{27}$$

로 주어진다. 그런데 $R<0$이면 서로 다른 실근이 셋인데도 공식이 음수의 제곱근 $\sqrt{R}$을 강제로 거친다. 이 상황을 casus irreducibilis라 부른다. 답은 멀쩡한 실수인데, 거기에 이르는 라디칼 경로가 "존재하지 않는" 수를 통과하는 것이다. 놀랍게도 이 수를 형식적인 기호로 받아들이고 계산을 밀어붙이면 허수부가 끝에서 상쇄되며 진짜 실근이 나온다.

**Example (Bombelli, 1572).** $x^3=15x+4$, 즉 $p=-15$, $q=-4$의 경우 $R=\dfrac{16}{4}+\dfrac{(-15)^3}{27}=4-125=-121$이므로 $\sqrt{R}=\sqrt{-121}=11i$이고

$$x = \sqrt[3]{2+11i} + \sqrt[3]{2-11i}$$

이다. Bombelli는 $\sqrt[3]{2+11i}=2+i$라고 짐작했는데, 실제로 $(2+i)^3 = 8+12i+6i^2+i^3 = 8+12i-6-i = 2+11i$로 맞아떨어진다. 켤레도 $\sqrt[3]{2-11i}=2-i$이므로 $x=(2+i)+(2-i)=4$이고, $4^3=64=15\cdot4+4$이니 정말로 근이다. 허수는 중간 계산에만 나타났다가 깨끗이 사라졌다. Bombelli는 1572년 《Algebra》에서 이런 "불가능한 수"들의 사칙연산 규칙을 처음 체계적으로 정리해 실제 계산의 도구로 삼았다 [2].

이차방정식에서는 음수의 판별식이 그저 "실근 없음"을 뜻해 무시하면 그만이지만, 삼차방정식에서는 원하는 실근이 버젓이 존재하는데도 복소수를 반드시 통과해야 한다. 수학이 복소수를 진지하게 받아들이기 시작한 진짜 출발점이 여기다.

복소수는 흔히 "$\sqrt{-1}$을 $i$라 부르자"로 도입되지만, 과연 그런 대상이 정말 존재하는가? Hamilton은 1837년에 복소수를 실수 순서쌍으로 못박고, 곱셈을 규칙으로 정하는 것으로 복소수를 정의했다 [8].

**Definition (Complex Numbers).** $\mathbb{C}$는 실수 순서쌍 $(a,b)$ 전체의 집합 $\mathbb{R}^2$에 다음 덧셈과 곱셈을 준 것이다.
$$(a,b)+(c,d):=(a+c,\ b+d), \qquad (a,b)\cdot(c,d):=(ac-bd,\ ad+bc).$$
$(a,0)$을 실수 $a$와 동일시하고 $i:=(0,1)$로 쓰면 $i^2=(0,1)(0,1)=(-1,0)=-1$이고, 임의의 $(a,b)$는 $(a,0)+(b,0)(0,1)=a+bi$로 쓰인다. $a=\operatorname{Re}z$를 실수부, $b=\operatorname{Im}z$를 허수부라 한다.

**Theorem.** $\mathbb{C}$ is a field.

*Proof.* 덧셈과 곱셈이 교환·결합·분배법칙을 만족함은 정의를 성분으로 풀면 실수의 사칙연산으로 귀착된다. 덧셈 항등원은 $0=(0,0)$, 곱셈 항등원은 $1=(1,0)$이다. $z=a+bi\ne0$이면 $a^2+b^2>0$이고

$$z^{-1} = \frac{a-bi}{a^2+b^2}$$

이 $zz^{-1}=1$을 만족하므로 곱셈 역원이 존재한다. $\blacksquare$



## 켤레와 절댓값

**Definition (Conjugate, Modulus).** $z=a+bi$의 켤레(conjugate)는 $\bar z:=a-bi$, 절댓값(modulus)은 $\vert z\vert:=\sqrt{a^2+b^2}$이다.

정의에서 곧바로 $z\bar z=a^2+b^2=\vert z\vert^2$, $\operatorname{Re}z=\tfrac12(z+\bar z)$, $\operatorname{Im}z=\tfrac1{2i}(z-\bar z)$가 나온다.

**Proposition (기본 성질).** For all $z,w\in\mathbb{C}$:
1. $\overline{z+w}=\bar z+\bar w$ and $\overline{zw}=\bar z\,\bar w$.
2. $\vert zw\vert=\vert z\vert\,\vert w\vert$.
3. (Triangle inequality) $\vert z+w\vert\le\vert z\vert+\vert w\vert$.

*Proof.* (1)은 성분 계산에서 바로 나온다. (2)는 (1)을 써서 $\vert zw\vert^2=zw\overline{zw}=zw\bar z\bar w=(z\bar z)(w\bar w)=\vert z\vert^2\vert w\vert^2$이다. (3)은 $\operatorname{Re}\zeta\le\vert\zeta\vert$와 $\vert\bar w\vert=\vert w\vert$를 써서

$$\vert z+w\vert^2 = (z+w)\overline{(z+w)} = \vert z\vert^2 + 2\operatorname{Re}(z\bar w) + \vert w\vert^2 \le \vert z\vert^2 + 2\vert z\vert\vert w\vert + \vert w\vert^2 = \big(\vert z\vert+\vert w\vert\big)^2$$

이고 양변에 제곱근을 취하면 된다. $\blacksquare$

절댓값 $\vert z\vert$은 $\mathbb{C}=\mathbb{R}^2$ 위의 평범한 유클리드 거리이고, 두 복소수 사이의 거리는 $\vert z-w\vert$이다. 즉 복소수의 대수 구조와 평면의 기하 구조가 한 몸이다.

## 복소평면과 극형식

$z=a+bi$를 평면 위의 점 $(a,b)$로 보는 그림을 복소평면(complex plane)이라 한다. 이 기하적 표현은 Wessel이 1799년에 [5], 이어 Argand가 1806년에 [6] 제시했고, Gauss가 널리 퍼뜨리며 "복소수(complex number)"라는 이름을 정착시켰다.

극좌표를 쓰면 $z\ne0$은 $r=\vert z\vert$과 각 $\theta$로

$$z = r(\cos\theta + i\sin\theta)$$

로 쓰인다. 이 $\theta$를 $z$의 편각(argument) $\arg z$라 한다. 극형식에서 곱셈의 뜻이 선명해진다.

**Proposition.** $z_1=r_1(\cos\theta_1+i\sin\theta_1)$, $z_2=r_2(\cos\theta_2+i\sin\theta_2)$이면
$$z_1z_2 = r_1r_2\big(\cos(\theta_1+\theta_2) + i\sin(\theta_1+\theta_2)\big).$$

*Proof.* 곱을 전개하고 코사인·사인의 덧셈정리 $\cos\theta_1\cos\theta_2-\sin\theta_1\sin\theta_2=\cos(\theta_1+\theta_2)$, $\sin\theta_1\cos\theta_2+\cos\theta_1\sin\theta_2=\sin(\theta_1+\theta_2)$를 쓰면 된다. $\blacksquare$

즉 복소수 $z$를 곱하는 것은 평면을 $\arg z$만큼 회전하고 $\vert z\vert$배 확대하는 변환이다.

## Euler's Formula

지수함수를 복소수까지 넓히면 극형식이 한결 깔끔해진다. 급수 $\sum_{n=0}^\infty z^n/n!$은 $\sum \vert z\vert^n/n!<\infty$이므로 모든 복소수 $z$에서 절대수렴하고, 이를 $e^z$로 정의한다. 순허수 $z=i\theta$를 넣고 $i$의 거듭제곱이 $1,i,-1,-i$를 주기적으로 도는 것을 이용해 실수부와 허수부로 나누면 다음을 얻는다.

**Theorem (Euler's Formula).** For every $\theta\in\mathbb{R}$,
$$e^{i\theta} = \cos\theta + i\sin\theta.$$

*Proof.* 절대수렴하므로 항의 순서를 재배열해 짝수 차수와 홀수 차수로 나눌 수 있다. $i^{2k}=(-1)^k$, $i^{2k+1}=(-1)^k i$이므로

$$e^{i\theta} = \sum_{n=0}^\infty \frac{(i\theta)^n}{n!} = \sum_{k=0}^\infty \frac{(-1)^k\theta^{2k}}{(2k)!} + i\sum_{k=0}^\infty \frac{(-1)^k\theta^{2k+1}}{(2k+1)!} = \cos\theta + i\sin\theta$$

인데, 마지막 두 급수는 각각 $\cos\theta$, $\sin\theta$의 Taylor 급수다. $\blacksquare$

$\theta=\pi$를 넣으면 $e^{i\pi}+1=0$이라는 유명한 항등식이 나온다. 극형식은 이제 $z=re^{i\theta}$로 짧아지고, 곱셈의 회전 성질은 지수법칙 $e^{i\theta_1}e^{i\theta_2}=e^{i(\theta_1+\theta_2)}$ 그 자체가 된다. 이 표기와 급수를 통한 복소지수의 취급은 Euler가 1748년 《Introductio in analysin infinitorum》에서 확립했다 [4].

**Corollary (de Moivre's Theorem).** For every integer $n$,
$$(\cos\theta + i\sin\theta)^n = \cos(n\theta) + i\sin(n\theta).$$

*Proof.* $e^{i\theta}$의 극형식에 지수법칙을 반복 적용하면 $(e^{i\theta})^n=e^{in\theta}$이다. $\blacksquare$

이 등식은 de Moivre가 18세기 초에 사실상 알고 있던 것으로, Euler의 공식이 그 배경을 한눈에 설명해준다 [3].

## 대수학의 기본정리

실수 위에서는 $x^2+1=0$처럼 근이 없는 다항식이 있다. 복소수로 넓히면 이런 결핍이 완전히 사라진다.

**Theorem (Fundamental Theorem of Algebra).** Every nonconstant polynomial with complex coefficients has a root in $\mathbb{C}$. Equivalently, a degree-$n$ complex polynomial factors as $a\prod_{k=1}^n(z-\alpha_k)$ into linear factors, counted with multiplicity.

이것을 두고 $\mathbb{C}$가 대수적으로 닫혔다(algebraically closed)고 한다. 증명은 여러 가지가 있으나 모두 이 글의 도구를 넘어선다(복소해석의 Liouville 정리를 쓰는 것이 가장 짧고, 위상적·대수적 증명도 있다). 널리 받아들여진 첫 증명은 Gauss가 1799년 박사학위 논문에서 주었는데 [7], 여기에도 뒤에 메워야 할 위상적 간극이 있었다. 그보다 앞서 d'Alembert가 1746년에 시도한 증명도 있어 이 정리를 d'Alembert–Gauss 정리라 부르기도 한다 [9]. 완전한 증명은 복소해석 글로 미룬다.

## 참고문헌

1. Cardano, G. (1545). *Artis magnae, sive de regulis algebraicis liber unus (Ars Magna)*. Nürnberg.
2. Bombelli, R. (1572). *L'Algebra*. Bologna.
3. de Moivre, A. (1730). *Miscellanea Analytica de Seriebus et Quadraturis*. London.
4. Euler, L. (1748). *Introductio in analysin infinitorum*. Lausanne.
5. Wessel, C. (1799). Om Directionens analytiske Betegning. *Nye Samling af det Kongelige Danske Videnskabernes Selskabs Skrifter*, 5, 469–518.
6. Argand, J.-R. (1806). *Essai sur une manière de représenter les quantités imaginaires dans les constructions géométriques*. Paris.
7. Gauss, C. F. (1799). *Demonstratio nova theorematis omnem functionem algebraicam rationalem integram unius variabilis in factores reales primi vel secundi gradus resolvi posse*. Helmstedt.
8. Hamilton, W. R. (1837). Theory of Conjugate Functions, or Algebraic Couples; with a Preliminary and Elementary Essay on Algebra as the Science of Pure Time. *Transactions of the Royal Irish Academy*, 17, 293–422.
9. d'Alembert, J. le R. (1746). Recherches sur le calcul intégral. *Histoire de l'Académie royale des sciences et belles-lettres de Berlin*, 2, 182–224.
