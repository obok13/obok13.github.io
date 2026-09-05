# 해석학 블로그 커리큘럼 (v10 · 최종)

**총 929챕터 / 26개 부.**

**기호**

- ⭐ 하중을 받는 챕터
- 🔁 앞 챕터의 회수 지점
- 🔓 미해결 문제
- ⚪ 선택

## 줄기 구조

| 줄기 | 파트 |
|---|---|
| 기초 | 1 논리 → 2 미적분학 → 3 선형대수학 → 4 위상 → 5 다양체 |
| 측도 | 6 측도론과 Lᵖ 공간 |
| 복소 ① | 7 복소해석 I |
| 선형대수 후반 | 8 함수해석 → 9 작용소론 |
| 복소 ② | 10 대수위상 → 11 복소해석 II |
| 미적분 후반 | 12 푸리에 → 13 조화해석 → 14 기하측도론 |
| 미분방정식 | 15 ODE → 16 분포·소볼레프 → 17 PDE와 최적수송 |
| 확률·동역학 | 18 확률 → 19 에르고딕 → 20 미분동역학계 → 21 점근기하해석 |
| 복소 ③ | 22 SCV → 23 복소동역학 → 24 해석적 정수론 |
| 기하 | 25 다양체 위의 해석학 |
| 에필로그 | 26 계산과 결정 가능성 |

---

# 제1부 — 논리와 실수의 구성

*(1–16)*

1. Sets, relations, and functions
2. ⭐ The Axiom of Choice
3. Zorn's lemma and the well-ordering theorem
4. Ordinals and transfinite induction
5. Cardinality and cardinal arithmetic
6. Countable and uncountable sets; Cantor's diagonal argument
7. The Cantor–Schröder–Bernstein theorem
8. The continuum hypothesis (statement only)
9. Construction of ℕ, ℤ, and ℚ
10. ⭐ Construction of ℝ I: Dedekind cuts
11. ⭐ Construction of ℝ II: Cauchy completion of ℚ
12. Uniqueness of the complete ordered field
13. ⭐ The completeness axiom and its equivalent forms
14. The Archimedean property; density of ℚ; uncountability of ℝ
15. Formal systems and first-order logic
16. ⭐ Gödel's incompleteness theorems

---

# 제2부 — 미적분학

*(17–96)*

## 2.1 수열과 급수

17. Sequences and convergence; algebra of limits
18. Monotone convergence; limsup and liminf
19. Cauchy sequences and the completeness of ℝ
20. Subsequences; the Bolzano–Weierstrass theorem
21. Nested intervals; the Heine–Borel theorem on ℝ
22. The number e; elementary limits
23. Series; partial sums; the Cauchy criterion
24. Comparison, ratio, and root tests
25. The integral test; the harmonic series
26. Alternating series; Dirichlet and Abel tests
27. Absolute versus conditional convergence
28. ⭐ The Riemann rearrangement theorem
29. Cauchy products; Mertens' theorem
30. Infinite products
31. Double series and iterated limits
32. Summability methods: Cesàro, Abel, Borel
33. Elementary Tauberian theorems
34. Irrationality and transcendence: e, π, Liouville numbers
    - 🔓 ζ(5)와 γ의 무리성

## 2.2 실함수의 극한과 연속

35. Limits of functions; the ε–δ definition
36. Continuity; the sequential characterization
37. ⭐ Continuous functions on compact sets; the extreme value theorem
38. Uniform continuity
39. The intermediate value theorem
40. Monotone functions and their discontinuity sets
41. Classification of discontinuities; oscillation
42. Convex functions; Jensen's inequality
43. Semicontinuity
44. The Cantor set and the Cantor function
45. Weierstrass' nowhere differentiable function
46. Space-filling curves
47. Cauchy's functional equation 🔁 (2장)

## 2.3 미분

48. The derivative; algebra of derivatives; the chain rule
49. ⭐ The mean value theorem; Rolle and Cauchy versions
50. Darboux's theorem
51. L'Hôpital's rule
52. Higher derivatives; Taylor's theorem with remainder
53. Taylor series and non-analytic smooth functions
54. ⭐ Smooth bump functions
55. The inverse function theorem in one variable
56. Convexity and differentiability
57. Almost-everywhere differentiability of monotone functions (statement)
58. Asymptotic expansions; Landau notation

## 2.4 적분

59. The Darboux–Riemann integral; criteria for integrability
60. Properties of the integral; the fundamental theorem of calculus
61. ⭐ The logarithm and exponential constructed by integration
62. ⭐ Lebesgue's criterion for Riemann integrability
63. The Riemann–Stieltjes integral
64. Functions of bounded variation
65. Total variation; the Jordan decomposition
66. Integration by parts and substitution for Stieltjes integrals
67. ⭐ Integrators as measures: a preview of Lebesgue–Stieltjes theory
68. Improper integrals
69. Techniques of integration
70. Classical integrals: Gaussian, Dirichlet, Frullani
71. The Gamma function on the positive reals
72. The Beta function; Wallis' product; Stirling's formula
73. The Euler–Maclaurin formula
74. ⭐ Failure of limit–integral interchange
75. Numerical quadrature and error estimates ⚪

## 2.5 함수열과 균등수렴

76. Pointwise and uniform convergence
77. ⭐ Uniform convergence and continuity, integration, differentiation
78. The Weierstrass M-test; Dini's theorem
79. Differentiation under the integral sign 🔁 (77장)
80. ⭐ Completeness of C[a,b] under the supremum norm
81. ⭐ The contraction mapping principle on C[a,b] and on closed subsets of ℝⁿ
82. ⭐ Equicontinuity; the Arzelà–Ascoli theorem on C[a,b]
83. ⭐ The Weierstrass approximation theorem (real and complex forms)

## 2.6 멱급수

84. Power series; the Cauchy–Hadamard formula
85. Operations on power series; Abel's theorem
86. ⭐ Real-analytic functions
87. The gap between smooth and analytic
88. ⭐ Fourier series: a first formal encounter
89. Bernoulli numbers; Euler's evaluation of ζ(2n)
90. Divergence phenomena in Fourier series (statement)

## 2.7 복소수

91. Construction of ℂ; algebraic closure
92. Polar form; roots of unity; de Moivre's formula
93. Complex sequences and series
94. Complex power series; exp, sin, cos
95. ⭐ Euler's formula and the problem of the complex logarithm — *문제를 열어둡니다*
96. The Riemann sphere; Möbius transformations, algebraically

---

# 제3부 — 선형대수학

*(97–131)*

## 3.1 구조

97. Fields and vector spaces (axiomatic treatment)
98. Subspaces; sums and direct sums
99. Linear independence, basis, dimension
100. Hamel bases and the axiom of choice 🔁 (2장)
101. Linear maps; kernel and image
102. ⭐ The rank–nullity theorem
103. Matrix representation; change of basis
104. Linear systems; Gaussian elimination; LU decomposition
105. ⭐ Quotient spaces
106. ⭐ The dual space; dual maps; annihilators
107. Bilinear and multilinear forms
108. The determinant as an alternating multilinear form
109. Properties of the determinant; cofactor expansion
110. Trace; similarity invariants
111. Eigenvalues, eigenvectors, the characteristic polynomial
112. Diagonalizability; invariant subspaces
113. The minimal polynomial; the Cayley–Hamilton theorem
114. ⭐ Generalized eigenspaces; nilpotent operators; the Jordan canonical form

## 3.2 기하와 계산

115. Inner product spaces; the Cauchy–Schwarz inequality
116. Orthogonality; Gram–Schmidt; QR decomposition
117. Orthogonal projection; least squares
118. ⭐ The Riesz representation theorem in finite dimensions
119. ⭐ The adjoint operator
120. Self-adjoint, unitary, and normal operators
121. ⭐ The finite-dimensional spectral theorem
122. Positive operators; square roots; Cholesky decomposition
123. ⭐ Singular value decomposition; polar decomposition
124. Low-rank approximation; the Eckart–Young theorem
125. Quadratic forms; Sylvester's law of inertia
126. Matrix norms; the condition number
127. ⭐ The matrix exponential
128. ⭐ Nonnegative matrices; the Perron–Frobenius theorem
129. The numerical range and the field of values
     - 🔓 **Crouzeix의 추측**
130. ⭐ Tensor products and multilinear maps
131. ⭐ Exterior algebra; the wedge product; orientation and volume forms

---

# 제4부 — 거리공간과 일반위상

*(132–165)*

## 4.1 거리공간

132. Metric spaces; examples from earlier parts
133. Open and closed sets; closure, interior, boundary
134. Convergence and continuity in metric spaces
135. Completeness; completion of a metric space
136. ⭐ The contraction principle in general metric spaces 🔁 (81장)
137. ⭐ The Baire category theorem
138. Applications of Baire category 🔁 (45장)
139. Total boundedness
140. ⭐ Compactness: three equivalent formulations
141. Continuous maps on compact sets; uniform continuity
142. Connectedness and path-connectedness
143. Lipschitz, Hölder, and moduli of continuity
144. Hausdorff distance; the hyperspace of compact sets

## 4.2 일반위상

145. Topological spaces; bases and subbases
146. Continuous maps and homeomorphisms
147. The subspace topology
148. Product and box topologies
149. ⭐ Tychonoff's theorem 🔁 (2장)
150. The quotient topology; adjunction spaces
151. Nets and filters
152. Countability axioms; separability
153. Separation axioms
154. Hausdorff spaces
155. Regularity and normality
156. ⭐ Urysohn's lemma
157. ⭐ The Tietze extension theorem
158. The Urysohn metrization theorem
159. The Nagata–Smirnov metrization theorem
160. Local compactness; the one-point compactification
161. The Stone–Čech compactification
162. ⭐ Paracompactness; partitions of unity
163. ⭐ The uniform topology on C(X); the compact-open topology
164. ⭐ The Arzelà–Ascoli theorem in general form 🔁 (82장)
165. ⭐ The Stone–Weierstrass theorem, real and complex 🔁 (83장)

---

# 제5부 — 다변수미적분학과 다양체

*(166–217)*

## 5.1 ℝⁿ에의 특수화

166. ℝⁿ; norms and their equivalence
167. ⭐ Compactness in ℝⁿ: Heine–Borel revisited 🔁 (140장)
168. Connectedness and convexity in ℝⁿ

## 5.2 미분

169. Limits and continuity in several variables
170. Partial derivatives and their pathologies
171. ⭐ The Fréchet derivative; the Jacobian matrix
172. The Gâteaux derivative
173. The chain rule; directional derivatives; the gradient
174. The mean value inequality; Taylor's theorem in several variables
175. The Hessian; classification of critical points
176. ⭐ The inverse function theorem 🔁 (81장)
177. ⭐ The implicit function theorem
178. The rank theorem; immersions and submersions
179. Lagrange multipliers
180. The Morse lemma
181. Sard's theorem
182. ⭐ The Whitney extension theorem
     - 🔓 Whitney 문제군의 정량적 형태
183. Convex analysis in ℝⁿ; separating hyperplanes; the subdifferential
184. The Legendre–Fenchel transform
185. Brouwer's fixed point theorem (analytic proof)

## 5.3 다중적분

186. Jordan content; the multiple Riemann integral
187. Fubini's theorem for Riemann integrals
188. ⭐ The change of variables theorem
189. Improper multiple integrals; polar and spherical coordinates

## 5.4 벡터해석

190. Curves; arc length; curvature
191. Line integrals; vector fields; conservative fields and potentials
192. Surfaces; surface integrals; flux
193. Green's theorem in the plane
194. The divergence theorem and the classical Stokes theorem in ℝ³
195. ⭐ Closed versus exact: the angle form on the punctured plane

## 5.5 다양체와 미분형식

196. ⭐ Smooth manifolds: charts and atlases 🔁 (154, 162장)
     - 🔓 매끄러운 4차원 푸앵카레 추측
197. Smooth maps; the tangent space; the differential
198. Submanifolds; the regular value theorem
199. Immersions and embeddings; the Whitney embedding theorem
200. Vector fields, flows, and the Lie bracket
201. Partitions of unity on manifolds 🔁 (162장)
202. ⭐ Differential forms
203. The wedge product 🔁 (131장)
204. ⭐ The exterior derivative
205. Pullback of differential forms
206. Orientation; manifolds with boundary
207. ⭐ Integration of forms on manifolds
208. ⭐ Stokes' theorem
209. Recovery of Green, divergence, and classical Stokes 🔁 (193–194장)
210. Chain complexes and cohomology: the minimal algebraic setup
211. ⭐ de Rham cohomology
212. The Poincaré lemma
213. ⭐ The angle form revisited: H¹ of the punctured plane 🔁 (195장)
214. Computations: cohomology of spheres and tori
215. The Mayer–Vietoris sequence for de Rham cohomology
216. Degree theory via differential forms
217. ⭐ The Frobenius theorem; integrable distributions

---

# 제6부 — 측도론과 Lᵖ 공간

*(218–274)*

## 6.1 측도론

218. The failure of the Riemann integral 🔁 (74장)
219. Algebras and σ-algebras
220. ⭐ Dynkin's π–λ theorem; the monotone class theorem
221. Borel sets; the Borel hierarchy
222. Measures; continuity from above and below
223. Outer measures; Carathéodory's criterion
224. ⭐ The Carathéodory extension theorem
225. Construction of Lebesgue measure on ℝⁿ
226. Regularity of Lebesgue measure
227. ⭐ Non-measurable sets: the Vitali construction 🔁 (2장)
228. The Banach–Tarski paradox ⚪
229. Measurable functions
230. ⭐ Approximation by simple functions
231. The Lebesgue integral of nonnegative functions
232. ⭐ The monotone convergence theorem
233. ⭐ Fatou's lemma
234. The integral of general measurable functions
235. ⭐ The dominated convergence theorem
236. Comparison with the Riemann integral 🔁 (62장)
237. Null sets; completion of a measure
238. ⭐ Egorov's theorem
239. ⭐ Lusin's theorem
240. Convergence in measure
241. ⭐ Product measures; the Tonelli and Fubini theorems
242. Counterexamples to Fubini's theorem
243. Signed measures; the Hahn and Jordan decompositions 🔁 (65장)
244. Absolute continuity and mutual singularity of measures
245. ⭐ The Radon–Nikodym theorem
246. The Lebesgue decomposition theorem
247. Absolutely continuous functions
248. ⭐ The fundamental theorem of calculus for the Lebesgue integral
249. The Hardy–Littlewood maximal function
250. The Vitali covering lemma
251. ⭐ The Lebesgue differentiation theorem 🔁 (57장)
252. Lebesgue points; the density theorem
253. ⭐ The Riesz representation theorem for C₀(X)* 🔁 (160장)
254. Weak-* and vague convergence of measures
255. ⭐ Helly's selection theorem; tightness on ℝ
256. Analytic sets; measurable selection theorems

## 6.2 Lᵖ 공간

257. Lᵖ spaces; the Hölder and Minkowski inequalities
258. ⭐ The Riesz–Fischer theorem
259. Density of simple and continuous functions in Lᵖ
260. Duality: (Lᵖ)* = L^q
261. L^∞ and the essential supremum
262. Relations among modes of convergence
263. ⭐ Uniform integrability; the Vitali convergence theorem
264. The Dunford–Pettis theorem
265. ⭐ Convolution; Young's inequality
266. ⭐ Approximate identities and mollification
267. Separability and reflexivity of Lᵖ

## 6.3 보간 이론

268. ⭐ The Riesz–Thorin interpolation theorem
269. ⭐ The Marcinkiewicz interpolation theorem; weak-type estimates
270. Complex interpolation: the Calderón method
271. Real interpolation: the K-method
272. Interpolation spaces; the reiteration theorem
273. ⭐ The Bochner integral; vector-valued Lᵖ spaces
274. The Pettis integral; the Radon–Nikodym property

---

# 제7부 — 복소해석 I

*(275–302)*

275. The topology of the complex plane; domains
276. ⭐ Complex differentiability; the Cauchy–Riemann equations
277. Harmonic functions; harmonic conjugates
278. Conformality of holomorphic maps
279. Elementary functions
280. ⭐ The logarithm; branches and branch cuts 🔁 (95장) — *여전히 미해결*
281. Complex powers and multivaluedness
282. Contour integration
283. ⭐ The Cauchy–Goursat theorem (convex and star-shaped domains)
284. Primitives and path independence
285. ⭐ The Cauchy integral formula
286. Higher derivatives; Cauchy estimates
287. Morera's theorem
288. ⭐ Liouville's theorem; the fundamental theorem of algebra
289. The Schwarz lemma
290. The maximum modulus principle
291. The Phragmén–Lindelöf principle
292. Taylor expansion of holomorphic functions
293. Isolated zeros; the identity theorem
294. ⭐ Laurent series
295. Classification of isolated singularities
296. The Casorati–Weierstrass theorem
297. ⭐ The residue theorem
298. Evaluation of real integrals by residues
299. Summation of series by residues
300. ⭐ The winding number by integration; the argument principle 🔁 (195장)
301. Rouché's theorem; the open mapping theorem
302. Automorphisms of the disc; the Schwarz–Pick lemma
     - 🔓 **Sendov의 추측**; Smale의 평균값 추측

---

# 제8부 — 함수해석

*(303–351)*

## 8.1 바나흐 공간

303. Normed spaces; Banach spaces
304. Bounded linear operators; B(X,Y)
305. Finite-dimensional normed spaces; Riesz's lemma
306. ⭐ The Hahn–Banach theorem, analytic form 🔁 (3장)
307. The Hahn–Banach theorem, geometric form; separation of convex sets
308. Dual spaces: explicit computations 🔁 (245장)
309. The bidual; reflexivity
310. Quotient spaces; complemented subspaces
     - 🔓 보충부분공간 문제; 분리가능 몫 문제
311. ⭐ The uniform boundedness principle 🔁 (137장)
312. ⭐ The open mapping theorem
313. ⭐ The closed graph theorem
314. ⭐ The closed range theorem
315. Applications: divergence of Fourier series; a priori estimates 🔁 (90장)
316. Weak and weak-* topologies
317. ⭐ The Banach–Alaoglu theorem 🔁 (149장)
318. The Eberlein–Šmulian theorem
319. James' theorem
320. Extreme points; the Krein–Milman theorem
321. Choquet theory ⚪
322. Schauder bases
323. Topological vector spaces; locally convex spaces; seminorms
324. Fréchet spaces; inductive limits
325. Hahn–Banach in locally convex spaces; the bipolar theorem
326. The Bishop–Phelps theorem
327. The Schauder and Tychonoff fixed point theorems 🔁 (185장)
328. Monotone operators; the Browder–Minty theorem
329. Leray–Schauder degree theory 🔁 (216장)

## 8.2 힐베르트 공간과 컴팩트 작용소

330. Hilbert spaces; the parallelogram law
331. ⭐ The projection theorem; orthogonal decomposition
332. Orthonormal sets; Bessel's inequality; Parseval's identity
333. Orthonormal bases; classification of Hilbert spaces
334. ⭐ The Riesz representation theorem 🔁 (118장)
335. Adjoints in Hilbert space
336. Self-adjoint, unitary, normal, and positive operators
337. Orthogonal projections as operators
338. Spectrum and resolvent 🔁 (288장)
339. The spectral radius formula 🔁 (294장)
340. ⭐ Compact operators
341. Approximation by finite-rank operators
342. Riesz–Schauder theory
343. ⭐ The Fredholm alternative
344. ⭐ The Calkin algebra; Atkinson's theorem
345. ⭐ The Fredholm index; homotopy invariance and stability
346. ⭐ Essential spectrum; Weyl's theorem on compact perturbations
347. ⭐ The spectral theorem for compact self-adjoint operators
348. Hilbert–Schmidt operators; integral kernels
349. Trace class operators; Lidskii's theorem
350. Frames and Riesz bases; the Kadison–Singer problem
351. The invariant subspace problem
     - 🔓 **불변부분공간 문제**

---

# 제9부 — 작용소론과 스펙트럼 이론

*(352–377)*

352. Rings, ideals, and quotient rings (algebraic preliminaries)
353. ⭐ Banach algebras; invertibility; the spectrum
354. The Gelfand–Mazur theorem; the spectral radius formula 🔁 (288, 294장)
355. ⭐ Holomorphic functional calculus 🔁 (297장)
356. ⭐ Maximal ideals and the Gelfand transform
357. Commutative Banach algebras; Wiener's lemma 🔁 (88, 165장)
358. ⭐ C*-algebras; the Gelfand–Naimark theorem
359. ⭐ Continuous functional calculus
360. Positivity; states; the GNS construction
361. Projection-valued measures
362. ⭐ The spectral theorem for bounded normal operators
363. Borel functional calculus
364. The multiplication operator model
365. Spectral multiplicity; unitary equivalence
366. Unbounded operators; closed and closable operators
367. Symmetric versus self-adjoint operators; the Cayley transform
368. Deficiency indices; self-adjoint extensions
369. ⭐ The spectral theorem for unbounded self-adjoint operators
370. ⭐ Stone's theorem on one-parameter unitary groups
371. ⭐ Strongly continuous semigroups; the Hille–Yosida theorem
372. Analytic semigroups; fractional powers of operators 🔁 (270장)
373. Perturbation theory; the Kato–Rellich theorem 🔁 (346장)
374. ⭐ Operator topologies; the double commutant theorem
375. ⭐ Factors; traces; the type I/II/III classification
376. The hyperfinite II₁ factor
377. Free group factors; the link to free probability
     - 🔓 자유군 인자 동형 문제 L(F₂) ≅ L(F₃)

---

# 제10부 — 대수적 위상수학

*(378–426)*

## 10.1 호모토피와 기본군

378. Homotopy of maps and paths
379. ⭐ The fundamental group
380. Change of basepoint; functoriality
381. Homotopy equivalence; deformation retracts
382. ⭐ π₁(S¹) ≅ ℤ
383. ⭐ The winding number, homotopically 🔁 (195, 213, 300장)
384. The Brouwer fixed point theorem in dimension two; the fundamental theorem of algebra
385. Van Kampen's theorem
386. ⭐ Covering spaces; the unique lifting property
387. ⭐ Path lifting and homotopy lifting
388. ⭐ The lifting criterion — *95장과 280장의 답*
389. The universal cover; the deck transformation group
390. Classification of covering spaces
391. ⭐ Classification of surfaces; genus; the Euler characteristic

## 10.2 호몰로지

392. Simplicial complexes; simplicial homology
393. ⭐ Singular homology: the singular chain complex
394. Chain maps and chain homotopies 🔁 (210장)
395. ⭐ Homotopy invariance of homology
396. Reduced homology; relative homology
397. ⭐ The long exact sequence of a pair; the snake lemma
398. ⭐ The excision theorem
399. ⭐ The Mayer–Vietoris sequence 🔁 (215장)
400. The Eilenberg–Steenrod axioms; uniqueness of homology
401. Computations: spheres, tori, projective spaces 🔁 (214장)
402. Degree of maps Sⁿ → Sⁿ; local degree 🔁 (216장)
403. The Hopf theorem
404. CW complexes; cellular homology
405. Euler characteristic and Betti numbers; the Lefschetz fixed point theorem 🔁 (391장)
406. Homology with coefficients; Tor; the universal coefficient theorem
407. The Künneth formula
408. ⭐ The Jordan curve theorem
409. ⭐ Invariance of domain; Brouwer's theorem in all dimensions 🔁 (198장)
410. ⭐ The Borsuk–Ulam theorem; the ham sandwich theorem

## 10.3 코호몰로지와 쌍대성

411. ⭐ Singular cohomology; contravariance 🔁 (205장)
412. The universal coefficient theorem for cohomology; Ext
413. ⭐ The cup product; the cohomology ring 🔁 (203장)
414. Computations: cohomology rings of spheres, tori, ℂPⁿ
415. The cap product
416. Orientation of manifolds; the fundamental class 🔁 (206장)
417. ⭐ Poincaré duality
418. The intersection form; signature
419. Alexander and Lefschetz duality
420. ⭐ The de Rham theorem as a ring isomorphism 🔁 (208, 211장)
421. ⭐ Vector bundles; characteristic classes: a topological introduction

## 10.4 호모토피론

422. Higher homotopy groups πₙ(X)
423. Relative homotopy groups; the long exact sequence
424. Fibrations; the homotopy lifting property; the exact sequence of a fibration
425. The Hurewicz theorem; Whitehead's theorem
426. The Hopf fibration; homotopy groups of spheres ⚪

---

# 제11부 — 복소해석 II

*(427–486)*

## 11.1 대역 이론과 등각사상

427. ⭐ Chains and cycles; the homology form of Cauchy's theorem 🔁 (213, 393장)
428. The homotopy form of Cauchy's theorem 🔁 (395장)
429. ⭐ Equivalent characterizations of simple connectivity 🔁 (379장)
430. The global residue theorem
431. ⭐ Normal families; Montel's theorem 🔁 (164장)
432. Zalcman's lemma and the rescaling principle
433. Hurwitz's theorem
434. ⭐ The Riemann mapping theorem
435. Carathéodory's boundary extension theorem; prime ends
436. The Schwarz–Christoffel transformation
437. Canonical forms for multiply connected domains
438. Extremal length and conformal modulus
439. The Poisson integral formula
440. Subharmonic functions
441. ⭐ Harnack's inequality and Harnack's principle for harmonic functions
442. ⭐ Perron's method and the Dirichlet problem
443. Green's functions; harmonic measure; capacity
444. ⭐ Infinite products; the Weierstrass factorization theorem
445. The Mittag-Leffler theorem
446. Jensen's formula; order and genus of entire functions
447. ⭐ The Hadamard factorization theorem
448. Bloch, Landau, and Schottky theorems
449. The modular function λ 🔁 (389장)
450. ⭐ Picard's little and great theorems
451. Nevanlinna theory: the first and second main theorems
452. ⭐ Runge's theorem
453. Mergelyan's theorem
454. Analytic capacity; the Painlevé problem
455. ⭐ Analytic continuation; function elements; the monodromy theorem 🔁 (387장)

## 11.2 하디 공간과 재생핵

456. Hardy spaces H^p on the disc 🔁 (제6부)
457. Boundary values; Fatou's theorem
458. Blaschke products
459. The Nevanlinna class; inner and outer functions
460. ⭐ The canonical factorization theorem
461. ⭐ Beurling's theorem on invariant subspaces 🔁 (351장)
462. Carleson measures
463. The corona theorem
     - 🔓 **다원판·구에서의 코로나 문제**
464. Toeplitz and Hankel operators; the Nehari and AAK theorems ⚪
465. Bergman spaces
466. Reproducing kernel Hilbert spaces 🔁 (334, 465장)

## 11.3 단엽함수론

467. Univalent functions; the class S
468. ⭐ The area theorem; Koebe's one-quarter theorem
469. Distortion and growth theorems
470. The Bieberbach conjecture and de Branges' theorem
471. ⭐ The Loewner differential equation
472. ⭐ Quasiconformal mappings; the Beltrami equation; the measurable Riemann mapping theorem
     - 🔓 **Brennan의 추측**

## 11.4 리만 곡면

473. Riemann surfaces: definitions and examples
474. The surfaces of log z and √z 🔁 (280장) — *95장 완결*
475. Holomorphic maps; degree; ramification 🔁 (402장)
476. The Riemann–Hurwitz formula 🔁 (405장)
477. Meromorphic functions on compact surfaces
478. Holomorphic and meromorphic differentials
479. ⭐ Homology bases and period matrices 🔁 (391, 417–418장)
480. ⭐ The uniformization theorem
481. Fuchsian groups; hyperbolic geometry of the disc
482. ⭐ Divisors; the Riemann–Roch theorem via periods
483. Abel's theorem; the Jacobi inversion problem
484. Elliptic functions; the Weierstrass ℘-function
485. The modular curve; SL₂(ℤ)
486. Teichmüller theory (survey) ⚪

---

# 제12부 — 푸리에 해석

*(487–515)*

487. Fourier series with the Lebesgue integral 🔁 (88장)
488. The Dirichlet kernel; pointwise convergence criteria
489. The Gibbs phenomenon
490. Divergence: du Bois-Reymond and Kolmogorov examples
491. ⭐ Fejér's theorem
492. Abel summability; the Poisson kernel 🔁 (439장)
493. ⭐ L² theory; completeness of the trigonometric system 🔁 (333장)
494. The Carleson–Hunt theorem
495. ⭐ Weyl's equidistribution theorem; uniform distribution mod 1
     - 🔓 3/2 거듭제곱의 균등분포 (Mahler의 Z-수 문제)
496. Convolution and approximate identities on the torus
497. ⭐ The Fourier transform on L¹(ℝⁿ)
498. The Riemann–Lebesgue lemma
499. The inversion theorem; the Gaussian and self-duality
500. ⭐ The Plancherel theorem
501. ⭐ Bochner's theorem; positive-definite functions
502. ⭐ The Schwartz space
503. The Poisson summation formula
504. ⭐ Uncertainty principles: Heisenberg, Hardy, Beurling
505. ⭐ The Paley–Wiener theorems 🔁 (291, 447장)
506. The Hausdorff–Young inequality 🔁 (268장)
507. Fourier multipliers
508. Sobolev spaces via the Fourier transform
509. Besov and Triebel–Lizorkin spaces 🔁 (271장)
510. Time-frequency analysis; the Gabor transform
     - 🔓 **HRT 추측** — 4개 점에서도 미해결
511. Fourier uniqueness pairs; Radchenko–Viazovska interpolation 🔁 (485장)
512. ⭐ Sphere packing and modular forms; the Viazovska construction 🔁 (485장)
     - 🔓 8, 24차원 외의 최적 구 채우기
513. The discrete and fast Fourier transform
514. The sampling theorem; band-limited functions
515. The Laplace and Mellin transforms; Wiener's Tauberian theorem
     - 🔓 **Fuglede의 스펙트럼 집합 추측**

---

# 제13부 — 조화해석

*(516–548)*

## 13.1 특이적분과 실변수 방법

516. Maximal functions revisited; covering lemmas 🔁 (249장)
517. ⭐ The Calderón–Zygmund decomposition
518. ⭐ The Hilbert transform 🔁 (제11.2절)
519. Conjugate functions; the M. Riesz theorem
520. ⭐ Singular integral operators
521. The Riesz transforms
522. The T(1) and T(b) theorems
523. ⭐ Littlewood–Paley theory
524. Multiplier theorems: Mikhlin and Hörmander
525. ⭐ BMO; the John–Nirenberg inequality
526. Real Hardy spaces H^p(ℝⁿ); atomic decomposition
527. ⭐ The Fefferman duality theorem
528. Muckenhoupt A_p weights; the A₂ theorem

## 13.2 진동적분과 제한 이론

529. Oscillatory integrals; stationary phase
530. Van der Corput lemmas
531. ⭐ Restriction and extension estimates; the Stein–Tomas theorem
     - 🔓 **제한 추측** — n ≥ 3에서 미해결
532. Bochner–Riesz means
     - 🔓 **Bochner–Riesz 추측** — n ≥ 3에서 미해결
533. ⭐ Besicovitch sets; the Kakeya problem
     - 🔓 **Kakeya 집합 추측** — 3차원은 Wang–Zahl(2025)로 해결, **n ≥ 4는 미해결**
534. Local smoothing for the wave equation
     - 🔓 **국소 평활화 추측**
535. ⭐ Decoupling theory
536. Applications of decoupling: Vinogradov's mean value theorem
537. Sum-product phenomena; the polynomial Freiman–Ruzsa theorem
     - 🔓 **Erdős–Szemerédi 합–곱 추측**

## 13.3 군 위의 조화해석과 근사

538. ⭐ Haar measure on locally compact groups
539. ⭐ Pontryagin duality — *푸리에 변환의 정체*
540. Representations of compact groups; the Peter–Weyl theorem
541. ⭐ Unitary representations of noncompact groups; SL(2,ℝ)
542. Principal series and discrete series
543. Induced representations; Mackey theory
544. ⭐ The Plancherel formula for SL(2,ℝ)
545. Spherical harmonics
546. Wavelets and multiresolution analysis 🔁 (523장)
547. Approximation theory; Chebyshev systems 🔁 (83장)
548. Superposition; the Kolmogorov–Arnold representation theorem
     - 🔓 **힐베르트 13번 문제의 해석적 형태**

---

# 제14부 — 기하측도론

*(549–571)*

549. ⭐ Hausdorff measure and Hausdorff dimension
550. Minkowski, box, and packing dimension
551. Frostman's lemma; energy and capacity 🔁 (443장)
552. Self-similar sets; the open set condition 🔁 (44장)
553. Densities; the Besicovitch differentiation theorem
554. ⭐ Rectifiable sets; approximate tangent planes
555. ⭐ The Besicovitch structure theorem
556. ⭐ Blow-ups and tangent measures
557. Preiss' theorem on densities and rectifiability
558. ⭐ The Marstrand projection theorem
559. Distance sets
     - 🔓 **Falconer 거리집합 추측**
560. Slicing and intersection theorems
     - 🔓 Furstenberg 교차 문제의 정량적 형태
561. ⭐ Uniform rectifiability (David–Semmes)
562. ⭐ Jones' traveling salesman theorem; β-numbers
563. Analytic capacity and rectifiability 🔁 (454, 561–562장)
564. The area and coarea formulas
565. Sets of finite perimeter; BV functions
566. Currents; the compactness theorem
567. ⭐ Varifolds; first variation and stationarity
568. ⭐ The Allard regularity theorem
569. Plateau's problem; minimal surfaces; regularity theory
     - 🔓 고여차원 면적최소화 흐름의 정칙성
570. ⭐ Isoperimetric inequalities; the Brunn–Minkowski inequality
     - 🔓 **Mahler의 부피곱 추측**
571. Fractal measures; Fourier dimension
     - 🔓 **Erdős 닮음 문제**

---

# 제15부 — 상미분방정식

*(572–593)*

572. First-order equations: separable, exact, integrating factors
573. Initial value problems as integral equations
574. ⭐ The Picard–Lindelöf theorem 🔁 (81장)
575. ⭐ The Peano existence theorem 🔁 (82장)
576. Non-uniqueness; Osgood's criterion
577. Maximal solutions; continuation; blow-up
578. Dependence on initial conditions and parameters
579. ⭐ Grönwall's inequality
580. Linear systems; the fundamental matrix
581. ⭐ Constant coefficients; the matrix exponential 🔁 (127장)
582. Variation of parameters; Duhamel's principle
583. Floquet theory
584. Higher-order linear equations; the Wronskian
585. Series solutions; ordinary and regular singular points
586. ⭐ The Frobenius method
587. Bessel, Legendre, Hermite, and hypergeometric functions
588. Monodromy of linear ODEs; the Riemann–Hilbert problem 🔁 (455장)
589. Boundary value problems; Green's functions for ODEs
590. ⭐ Sturm–Liouville theory 🔁 (347장)
591. Sturm comparison and oscillation theory
592. Volterra and Fredholm integral equations 🔁 (343장)
593. Phase plane analysis; Lyapunov stability; the Poincaré–Bendixson theorem
     - 평면을 벗어난 정성이론은 제20부에서 (에르고딕 이론을 갖춘 뒤)
     - 🔓 **힐베르트의 16번 문제**

---

# 제16부 — 분포이론과 소볼레프 공간

*(594–615)*

594. Test functions and the topology on 𝒟(Ω) 🔁 (324장)
595. ⭐ Distributions: definition and basic examples
596. Differentiation of distributions
597. Support and singular support
598. Compactly supported distributions
599. Convolution of distributions; regularization
600. ⭐ Tempered distributions
601. ⭐ The Fourier transform of tempered distributions 🔁 (500장)
602. Structure theorems for distributions
603. ⭐ Fundamental solutions
604. The Malgrange–Ehrenpreis theorem
605. Hypoellipticity
606. ⭐ The wavefront set: definition and computation
607. ⭐ Sobolev spaces W^{k,p} and H^s 🔁 (508장)
608. Density and extension theorems 🔁 (182장)
609. ⭐ Sobolev embedding theorems
610. Morrey's inequality
611. ⭐ The Rellich–Kondrachov compactness theorem
612. The trace theorem
613. Poincaré and Friedrichs inequalities
614. Gagliardo–Nirenberg inequalities
615. Sobolev spaces on manifolds 🔁 (201장)

---

# 제17부 — 편미분방정식과 최적수송

*(616–670)*

## 17.1 편미분방정식

616. Classification; well-posedness in the sense of Hadamard
617. ⭐ The Cauchy–Kovalevskaya theorem 🔁 (86장)
618. Holmgren's uniqueness theorem
619. ⭐ First-order equations; the method of characteristics
620. Conservation laws; shocks; entropy solutions
621. Hamilton–Jacobi equations; viscosity solutions
622. Second-order linear equations; the elliptic–parabolic–hyperbolic trichotomy
623. ⭐ Laplace's equation; the mean value property 🔁 (277장)
624. ⭐ The maximum principle; Harnack's inequality 🔁 (441장)
625. Poisson's equation; the Newtonian potential
626. Green's functions; the Poisson kernel 🔁 (443장)
627. Perron's method revisited 🔁 (442장)
628. Capacity; the Wiener criterion for boundary regularity
629. ⭐ The heat equation; the fundamental solution
630. Smoothing; the parabolic maximum principle
631. Duhamel's principle for evolution equations 🔁 (371장)
632. ⭐ The wave equation; d'Alembert's formula
633. Kirchhoff's formula; Huygens' principle; the method of descent
634. Energy methods; domains of dependence; uniqueness
635. ⭐ Symmetric hyperbolic systems; energy estimates
636. Hyperbolic systems: finite propagation speed and well-posedness
637. Separation of variables; eigenfunction expansions 🔁 (590장)
638. ⭐ Weak solutions; variational formulation
639. ⭐ The Lax–Milgram theorem
640. ⭐ Gårding's inequality; coercivity of elliptic forms
641. ⭐ The Galerkin method; existence for evolution equations
642. Existence theory for elliptic equations 🔁 (343장)
643. Schauder estimates
644. Calderón–Zygmund (Lᵖ) estimates 🔁 (520장)
645. ⭐ De Giorgi–Nash–Moser theory
646. Parabolic regularity; the parabolic Harnack inequality
647. ⭐ Homogenization: the periodic setting; G- and H-convergence
648. Homogenization: stochastic and quantitative theory
649. Unique continuation; Carleman estimates
     - 🔓 **Landis의 추측** (2차원은 해결)
650. Eigenvalue problems; the min–max principle
651. ⭐ The direct method in the calculus of variations
652. Euler–Lagrange equations; Γ-convergence
653. The mountain pass theorem; critical point theory
654. ⭐ Fully nonlinear equations; the Monge–Ampère equation
655. ⭐ Caffarelli's regularity theory for Monge–Ampère
656. ⭐ Strichartz estimates; dispersive equations 🔁 (531장)
657. Well-posedness for nonlinear Schrödinger and wave equations
     - 🔓 임계·초임계 영역에서의 대역 적정성
658. ⭐ Convex integration; the Nash–Kuiper theorem and the h-principle
659. ⭐ The Nash–Moser inverse function theorem 🔁 (176장)
660. Non-uniqueness for the Euler equations; the Onsager conjecture
     - 🔓 3차원 오일러 방정식의 특이점 형성; 난류의 Kolmogorov 이론
661. Free boundary problems; the obstacle problem
662. The Navier–Stokes equations; Leray–Hopf solutions; partial regularity
     - 🔓 **나비에–스토크스 존재성과 매끄러움** (밀레니엄 문제)
     - 🔓 **양–밀스 존재성과 질량 간극** (밀레니엄 문제)
     - 🔓 볼츠만 방정식의 대역 정칙성

## 17.2 최적수송

663. ⭐ The Monge and Kantorovich problems
664. Kantorovich duality; c-concavity; cyclical monotonicity
665. ⭐ Brenier's theorem; polar factorization 🔁 (184장)
666. The Monge–Ampère equation in optimal transport 🔁 (654장)
667. Regularity of optimal maps; the Ma–Trudinger–Wang condition 🔁 (655장)
     - 🔓 일반 비용함수에 대한 정칙성의 최적 조건
668. ⭐ Wasserstein spaces: completeness, tightness, geodesics, displacement convexity
669. Gradient flows in Wasserstein space; the JKO scheme 🔁 (630장)
670. Otto calculus; the formal Riemannian structure

---

# 제18부 — 확률론과 확률해석

*(671–756)*

## 18.1 확률론

671. Probability spaces; random variables 🔁 (제6.1절)
672. Distribution functions; pushforward measures
673. ⭐ Independence; π–λ criteria 🔁 (220장)
674. Infinite product spaces
675. ⭐ The Kolmogorov extension theorem
676. Expectation; moments; Jensen's inequality
677. The Markov and Chebyshev inequalities
678. Uniform integrability in probability 🔁 (263장)
679. Modes of convergence
680. ⭐ The Borel–Cantelli lemmas
681. ⭐ The weak law of large numbers
682. Kolmogorov's inequality; the three-series theorem
683. ⭐ The strong law of large numbers
684. Zero-one laws: Kolmogorov, Hewitt–Savage
685. Weak convergence; the portmanteau theorem 🔁 (255장)
686. ⭐ Tightness; Prokhorov's theorem 🔁 (317장)
687. ⭐ The Skorokhod representation theorem
688. ⭐ Characteristic functions 🔁 (497, 501장)
689. The Lévy continuity theorem; inversion formulas
690. ⭐ The central limit theorem
691. The Lindeberg–Feller condition; triangular arrays
692. Berry–Esseen bounds
693. Stein's method
694. Poisson approximation
695. ⭐ Infinitely divisible laws; the Lévy–Khintchine formula
696. Stable laws; domains of attraction
697. The law of the iterated logarithm
698. Concentration inequalities: Chernoff, Hoeffding, Azuma
699. McDiarmid's inequality; the bounded differences method
700. ⭐ Gaussian concentration; the Borell–TIS inequality
701. ⭐ Large deviations: Cramér's theorem
702. Sanov's theorem; relative entropy 🔁 (245장)
703. Varadhan's lemma; the large deviation principle
704. Exchangeability; de Finetti's theorem
705. ⭐ Conditional expectation 🔁 (245장)
706. Regular conditional probability; disintegration 🔁 (256장)
707. Filtrations; stopping times
708. ⭐ Martingales; the optional stopping theorem
709. Doob's maximal and Lᵖ inequalities
710. ⭐ The Burkholder–Davis–Gundy inequalities
711. ⭐ Martingale convergence; the Doob–Meyer decomposition

## 18.2 확률과정과 확률해석

712. Markov chains; recurrence and transience 🔁 (128장)
713. Stationary distributions; the ergodic theorem for chains
714. Coupling; mixing times; spectral gaps
715. ⭐ Branching processes; Galton–Watson trees
716. The Poisson process; renewal theory
717. Lévy processes 🔁 (695장)
718. Continuous-time Markov processes; generators 🔁 (371장)
719. ⭐ Construction of Brownian motion
720. The Kolmogorov continuity criterion
721. Path properties: quadratic variation, nowhere differentiability
722. Lévy's modulus of continuity
723. The Markov and strong Markov properties; the reflection principle
724. ⭐ Donsker's invariance principle
725. Gaussian processes; Dudley's entropy bound
726. Empirical processes; Glivenko–Cantelli and Donsker classes
727. ⭐ The Itô integral
728. The Itô isometry
729. ⭐ Itô's formula
730. Local martingales and semimartingales 🔁 (710장)
731. General stochastic integration
732. Local time; Tanaka's formula
733. ⭐ Girsanov's theorem
734. ⭐ The martingale representation theorem
735. Stochastic differential equations: existence and uniqueness 🔁 (136장)
736. Weak solutions; the martingale problem
737. Diffusion processes; infinitesimal generators
738. ⭐ The Feynman–Kac formula 🔁 (629장)
739. Kolmogorov forward and backward equations; Fokker–Planck 🔁 (670장)
740. Dirichlet forms; symmetric Markov processes 🔁 (638장)
741. Malliavin calculus; Hörmander's theorem ⚪
742. Rough paths; regularity structures; singular SPDEs
     - 🔓 **KPZ 보편성**

## 18.3 슈뢰딩거 작용소와 랜덤 스펙트럼

743. ⭐ Schrödinger operators; essential spectrum; bound states 🔁 (346, 369, 607장)
744. Scattering theory ⚪
745. Random Schrödinger operators; the Anderson model
746. Ergodicity of the spectrum; the integrated density of states
747. Lifshitz tails; the low-energy regime
748. ⭐ Anderson localization: multiscale analysis
749. The fractional moment method; the delocalization regime
     - 🔓 **확장상태 추측**

## 18.4 랜덤 행렬과 확률적 기하

750. ⭐ Random matrices: Wigner's semicircle law
751. The Marchenko–Pastur law; sample covariance matrices
752. ⭐ Eigenvalue spacings; the Tracy–Widom law
     - 🔓 알려진 대칭 클래스 밖의 보편성
753. Free probability; free convolution; asymptotic freeness 🔁 (375–377장)
754. Percolation; critical phenomena
     - 🔓 3차원 등각불변성; 임계지수의 존재성
755. Self-avoiding walks
     - 🔓 ℤ² 위의 연결상수; 스케일링 극한
756. ⭐ Schramm–Loewner evolution; conformal invariance 🔁 (471장)

---

# 제19부 — 에르고딕 이론

*(757–776)*

757. Measure-preserving transformations
758. ⭐ The Poincaré recurrence theorem
759. Ergodicity; unique ergodicity 🔁 (495장)
760. ⭐ The ergodic decomposition theorem
761. ⭐ Birkhoff's pointwise ergodic theorem
762. The von Neumann mean ergodic theorem 🔁 (331장)
763. Mixing properties and their hierarchy
764. Kingman's subadditive ergodic theorem
765. ⭐ Rokhlin's lemma
766. ⭐ Entropy; the Kolmogorov–Sinai invariant
767. Krieger's generator theorem
768. The Shannon–McMillan–Breiman theorem
769. The Ornstein isomorphism theorem
770. ⭐ Topological dynamics; topological entropy
771. ⭐ The variational principle
772. Spectral theory of dynamical systems 🔁 (362장)
773. Furstenberg's multiple recurrence; Szemerédi's theorem
774. The Oseledets multiplicative ergodic theorem
775. Homogeneous dynamics; Ratner's theorems 🔁 (481, 541–544장)
     - 🔓 **Furstenberg의 ×2 ×3 추측**; **Littlewood의 추측**
776. Möbius disjointness; the Chowla conjecture
     - 🔓 **Sarnak의 추측**; **Chowla 추측**

---

# 제20부 — 미분동역학계

*(777–791)*

593장에서 끊긴 정성이론을 잇고, 774장 오세레데츠를 페신 이론으로 연결합니다.

777. Flows and diffeomorphisms; topological conjugacy
778. Hyperbolic fixed points; ⭐ the Hartman–Grobman theorem
779. ⭐ Stable and unstable manifolds
780. Hyperbolic sets; the shadowing lemma
781. ⭐ Anosov diffeomorphisms and flows
782. Axiom A; the spectral decomposition theorem
783. Markov partitions; symbolic dynamics 🔁 (770장)
784. Structural stability and the Ω-stability theorem
785. ⭐ SRB measures 🔁 (761장)
786. ⭐ Thermodynamic formalism; pressure and Gibbs states 🔁 (771장)
787. ⭐ Lyapunov exponents; Pesin theory 🔁 (774장)
788. Bifurcation theory: saddle-node, Hopf, period-doubling
789. Renormalization and universality
790. ⭐ KAM theory; small divisors and invariant tori
791. Arnold diffusion (survey) ⚪

---

# 제21부 — 점근기하해석

*(792–808)*

792. ⭐ John's ellipsoid theorem
793. Convex bodies; the isotropic position and the isotropic constant 🔁 (570장)
794. Log-concave measures; the Prékopa–Leindler inequality
795. Borell's lemma; functional forms of Brunn–Minkowski
796. ⭐ The Blaschke–Santaló inequality
     - 🔓 **Mahler의 부피곱 추측** — 역방향 부등식
797. ⭐ Concentration on the sphere; Lévy's isoperimetric inequality 🔁 (700장)
798. ⭐ Dvoretzky's theorem; almost-spherical sections
799. Milman's quotient-of-subspace theorem; the ℓ-position
800. ⭐ Milman's reverse Brunn–Minkowski inequality; M-position
801. Type and cotype; the Maurey–Pisier theorem
802. ⭐ Generic chaining; Talagrand's majorizing measures 🔁 (725장)
803. Isoperimetry for log-concave measures; the Cheeger constant
804. The thin-shell (variance) conjecture
805. ⭐ Bourgain's slicing (hyperplane) conjecture
     - Klartag–Lehec(2024–25)가 Guan의 부등식을 이용해 긍정적으로 해결
806. ⭐ Eldan's stochastic localization 🔁 (729, 733장)
807. The KLS conjecture
     - 🔓 **KLS 추측** — 여전히 미해결
808. Mixing of random walks in convex bodies; algorithmic sampling

---

# 제22부 — 다변수복소해석

*(809–824)*

809. Holomorphic functions of several variables
810. Power series; Reinhardt domains
811. ⭐ The Weierstrass preparation and division theorems
812. Local rings of holomorphic functions; Noetherian and UFD properties
813. ⭐ The Hartogs extension phenomenon 🔁 (295장) — *일변수와의 결정적 차이*
814. Domains of holomorphy
815. Holomorphic convexity
816. Plurisubharmonic functions 🔁 (440장)
817. ⭐ Pseudoconvexity; the Levi problem
818. ⭐ The ∂̄-equation
819. ⭐ Hörmander's L² estimates 🔁 (제16부)
820. Solution of the Levi problem by L² methods
821. CR structures; the tangential operator ∂̄_b
822. ⭐ Kohn's subelliptic estimates; the ∂̄-Neumann problem
823. The Bergman kernel and metric 🔁 (465–466장)
824. Proper holomorphic maps; rigidity
     - 🔓 **야코비안 추측**; S⁶ 위의 복소구조 존재성

---

# 제23부 — 복소동역학

*(825–840)*

825. Iteration of rational maps
826. ⭐ Fatou and Julia sets 🔁 (431장)
827. Periodic points and their classification
828. ⭐ Classification of Fatou components
829. Local normal forms: Böttcher, Koenigs, Leau–Fatou
830. Linearization; small divisors; the Brjuno condition 🔁 (790장)
831. The Mandelbrot set; hyperbolic components
     - 🔓 **MLC**; **쌍곡성의 조밀성** (Fatou의 추측)
832. Quasiconformal surgery 🔁 (472장)
833. ⭐ Sullivan's no-wandering-domain theorem
834. ⭐ Holomorphic motions; the λ-lemma
835. Mañé–Sad–Sullivan; structural stability in holomorphic families 🔁 (784장)
836. Polynomial-like maps; the Douady–Hubbard theory
837. Renormalization; Feigenbaum universality 🔁 (789장)
838. Dimension of Julia sets; thermodynamic formalism 🔁 (786장)
839. Measures of maximal entropy 🔁 (771장)
840. Transcendental dynamics; escaping sets
     - 🔓 **Eremenko의 추측**

---

# 제24부 — 해석적 정수론

*(841–863)*

841. Arithmetic functions; Dirichlet convolution; Möbius inversion
842. Dirichlet series; abscissas of convergence 🔁 (제2.1절)
843. ⭐ The Riemann zeta function; the Euler product
844. ⭐ Analytic continuation and the functional equation 🔁 (455장)
845. The Hadamard product for ξ(s) 🔁 (447장)
846. Zero-free regions
847. ⭐ The prime number theorem via contour integration
848. The explicit formula
849. Tauberian proofs: Wiener–Ikehara and Newman 🔁 (515장)
850. Dirichlet characters; L-functions
851. ⭐ Dirichlet's theorem on primes in arithmetic progressions
852. Siegel zeros; effectivity
853. Moments of the zeta function
854. Montgomery's pair correlation; random matrix statistics 🔁 (752장)
     - 🔓 **쌍상관 추측**
855. Zeros on the critical line; Hardy's theorem
     - 🔓 **리만 가설** (밀레니엄 문제); **린델뢰프 가설**
856. Lattice point problems; the Gauss circle and Dirichlet divisor problems
     - 🔓 **가우스 원 문제**와 **디리클레 약수 문제**
857. The circle method; Waring's problem 🔁 (536장)
858. Sieve methods; the large sieve
     - 🔓 **쌍둥이 소수 추측**; **골드바흐 추측**
859. ⭐ The Bombieri–Vinogradov theorem — *GRH의 평균적 대체물*
860. Exponential sums; Weyl differencing 🔁 (495장)
861. Mahler measure; Lehmer's problem
     - 🔓 **Lehmer의 문제**
862. Modular forms and L-functions 🔁 (485장)
863. ⭐ The Selberg trace formula 🔁 (369, 481, 544장)
     - 🔓 **일반화 리만 가설**

---

# 제25부 — 다양체 위의 해석학

*(864–927)*

## 25.1 리만 기하와 스펙트럼

864. Riemannian metrics; length, distance, volume
865. Connections; the Levi-Civita connection
866. Geodesics; the exponential map; normal coordinates
867. ⭐ The first and second variation formulas
868. Jacobi fields; conjugate points
869. The Hopf–Rinow theorem
870. Comparison theorems: Rauch, Bishop–Gromov
871. ⭐ The Bonnet–Myers and Synge theorems
872. ⭐ The Cartan–Hadamard theorem
873. ⭐ The Laplace–Beltrami operator
874. Integration by parts on manifolds; Green's identities; essential self-adjointness
875. The Hodge star; the codifferential
876. ⭐ Hodge theory and harmonic forms 🔁 (211, 420장)
877. ⭐ The Bochner technique; Weitzenböck formulas
878. ⭐ The heat kernel on a Riemannian manifold 🔁 (629장)
879. ⭐ The spectrum of the Laplacian on compact manifolds 🔁 (369장)
880. Weyl's law via the heat trace
881. Isoperimetric and Sobolev inequalities on manifolds; the Cheeger constant 🔁 (803장)
882. Eigenvalue estimates: Lichnerowicz, Cheng, Faber–Krahn
883. Nodal sets and nodal domains; Courant's theorem
     - 🔓 **Yau의 마디집합 추측**
884. Isospectrality; "can one hear the shape of a drum?"
     - 🔓 볼록 평면영역에서는 미해결
885. Eigenfunction concentration; L^p estimates
     - 🔓 **Berry의 무작위파동 추측**; **Hot spots 추측**; Pólya의 고유값 추측
886. ⭐ Ricci curvature bounds via transport; the CD(K,N) condition 🔁 (668, 870장)
887. Analysis on metric measure spaces; Cheeger's theorem; Gromov–Hausdorff limits

## 25.2 특성류와 지표정리

이 로드맵의 여러 갈래가 한 점에서 만나는 절입니다.

888. ⭐ Vector bundles; connections and curvature 🔁 (421장)
889. ⭐ Chern–Weil theory
890. ⭐ Chern classes; Pontryagin classes; the Euler class 🔁 (413–414장)
891. The Gauss–Bonnet theorem
892. ⭐ The Chern–Gauss–Bonnet theorem 🔁 (405장)
893. Clifford algebras; spin structures
894. ⭐ Dirac operators; the Lichnerowicz formula 🔁 (877장)
895. ⭐ The McKean–Singer formula; heat kernel asymptotics 🔁 (878장)
896. ⭐ **The Atiyah–Singer index theorem** 🔁 (345, 417, 420, 876장)

## 25.3 기하해석

897. Harmonic maps; the energy functional 🔁 (651장)
898. ⭐ The Eells–Sampson theorem
899. Bochner formulas for harmonic maps 🔁 (877장)
900. ⭐ The Yamabe problem; the Yamabe invariant
901. Minimal surfaces in Riemannian manifolds; curvature estimates 🔁 (569장)
902. The positive mass theorem (Schoen–Yau) ⚪
903. Ricci flow: short-time existence and Hamilton's theorem (survey)
904. Perelman's entropy and geometrization (survey) ⚪ 🔁 (887장)

## 25.4 심플렉틱 기하와 미시국소해석

606장(wavefront set), 880장(Weyl 법칙), 885장(고유함수 집중)이 실은 여접다발 $T^*M$ 위의 이야기라는 것을 밝히는 절입니다.

905. Symplectic vector spaces; the linear symplectic group
906. Symplectic manifolds; Darboux's theorem
907. ⭐ The cotangent bundle as a symplectic manifold
908. ⭐ Hamiltonian vector fields; the Poisson bracket
909. Hamiltonian flows; Liouville's theorem
910. ⭐ Integrable systems; the Arnold–Liouville theorem 🔁 (217, 790장)
911. Lagrangian submanifolds; generating functions
912. ⭐ Moment maps; symmetry and symplectic reduction
913. Symplectic capacities; Gromov's non-squeezing theorem
     - 🔓 정량적 심플렉틱 기하의 용량 문제; **아널드 추측**의 축퇴 경우
914. ⭐ Pseudodifferential operators: symbols and quantization 🔁 (601장)
915. Symbolic calculus: composition, adjoints, asymptotic expansion
916. Ellipticity; parametrices; microlocal regularity 🔁 (345장)
917. ⭐ The wavefront set on the cotangent bundle 🔁 (606장)
918. ⭐ Propagation of singularities; Hörmander's theorem
919. Fourier integral operators
920. The wave group; the Hadamard parametrix
921. ⭐ Semiclassical analysis; the ħ → 0 limit 🔁 (529장)
922. Egorov's theorem; the classical–quantum correspondence
923. ⭐ Weyl asymptotics via the wave trace; Duistermaat–Guillemin 🔁 (880장)
924. Semiclassical measures; defect measures
925. ⭐ Quantum ergodicity; Shnirelman's theorem 🔁 (761, 885장)
926. Quantum unique ergodicity; entropy methods 🔁 (766장)
     - 🔓 **QUE** — 일반 음곡률 다양체에서 미해결
927. Trace formulas: Selberg and Gutzwiller 🔁 (863장)
     - 🔓 Gutzwiller 대각합 공식의 엄밀화; 양자 카오스의 스펙트럼 통계

---

# 제26부 — 에필로그: 계산과 결정 가능성

*(928–929)*

16장에서 열어둔 질문으로 돌아옵니다.

928. Differential Galois theory; Liouville's theorem on elementary integrals
929. Transcendence theory; the Risch algorithm and decidability 🔁 (16, 34장)
     - 🔓 **Schanuel의 추측**

---

# 부록 A — v9에서 바뀐 것

## 추가된 13챕터

| 챕터 | 위치 | 왜 필요한가 |
|---|---|---|
| 61 로그·지수의 적분 구성 | 제2.4절 | FTC 직후의 첫 응용. 지금까지 22장에서 $e$만 다루고 구성이 없었음 |
| 128 Perron–Frobenius | 제3.2절 | 712–714장 마르코프 연쇄 정상분포·스펙트럼 간극의 유한차원 원형 |
| 255 헬리 선택정리 | 제6.1절 | 685–686장 포트만토·프로호로프의 1차원 원형 |
| 314 폐치역 정리 | 제8.1절 | 642장 타원형 존재이론, 818장 $\bar\partial$ 방정식에서 사용 |
| 410 보르숙–울람·햄샌드위치 | 제10.2절 | 408–409장과 함께 호몰로지 대표 응용 3종 |
| 441 하르낙 원리 | 제11.1절 | 442장 페론 방법 증명의 핵심 도구 |
| 556 접측도와 blow-up | 제14부 | 557장 Preiss 정리의 증명 도구 |
| 640 Gårding 부등식 | 제17.1절 | 639장 락스–밀그램의 실제 적용에 필요 |
| 641 Galerkin 근사 | 제17.1절 | 진화방정식 존재 증명의 표준 방법 |
| 710 BDG 부등식 | 제18.1절 | 727–731장 확률적분의 $L^p$ 추정, 742장 러프 패스 |
| 760 에르고딕 분해정리 | 제19부 | 785장 SRB, 786장 깁스 상태의 전제 |
| 867 제1·제2 변분 공식 | 제25.1절 | 868장 야코비장, 871장 보네–마이어스의 증명 도구 |
| 912 모멘트 사상과 축소 | 제25.4절 | 심플렉틱 기하의 필수 항목. 910장 적분가능계와 짝 |

## 조정 3건

| 조정 | 내용 |
|---|---|
| 79장 이동 | 적분기호 아래 미분을 제2.5절(균등수렴)로 이동. 증명에 77장이 필요한데 이전에는 앞에 있었음 |
| 83·165장 | 바이어슈트라스 근사와 스톤–바이어슈트라스에 복소 버전 명시. 357장 위너 보조정리, 539장 폰트랴긴 쌍대성의 도구 |
| 668장 확장 | Wasserstein 공간에 완비성·타이트니스 추가. 669장 JKO 도식의 각 단계가 최소화 문제라 필요 |
| 217장 ⚪ 제거 | 프로베니우스 정리는 910장 아르놀드–리우빌 증명에 쓰임 |

## 소소한 추가

75장(수치적분)은 ⚪로 남겼습니다. 73장 오일러–매클로린의 자연스러운 응용이라 한 챕터 값은 합니다.

---

# 부록 B — 지표정리로 수렴하는 것들

896장이 이 로드맵의 최대 수렴점입니다.

| 선행 | 역할 |
|---|---|
| 211·420장 드람 코호몰로지·드람 정리 | 특성류의 미분형식 표현 |
| 345장 프레드홀름 지표 | 좌변 $\operatorname{ind}(D)$ |
| 405장 오일러 지표 | 가우스–보네의 위상적 좌변 |
| 413–414장 컵곱·코호몰로지 환 | 천 지표 $\mathrm{ch}(E)$의 곱 구조 |
| 417장 푸앵카레 쌍대성 | 우변 적분의 정당화 |
| 421·888장 벡터다발과 접속 | 대상의 정의 |
| 876장 호지 이론 | $\ker D$의 조화적 해석 |
| 877장 보흐너–바이첸뵈크 | 리히네로비츠 공식(894장) |
| 878장 열핵 | 맥킨–싱어 방법(895장) |
| 880장 Weyl 법칙 | 열 대각합 점근의 짝 |

$$\operatorname{ind}(D) = \int_M \hat A(M)\,\mathrm{ch}(E)$$

---

# 부록 C — 심어둘 복선

| 심는 곳 | 닫는 곳 |
|---|---|
| 2장 (선택공리) | 100장, 149장, 227장, 306장 |
| 16장 (괴델) | **929장** — *전체를 감싸는 수미상관* |
| 74장 (극한·적분 교환 실패) | 235장 |
| 81·82장 (축소사상·아르첼라–아스콜리) | 136장, 164장, 176장, 574–575장, 735장 |
| 86장 (실해석적 함수) | 617장 (Cauchy–Kovalevskaya) |
| 95장 (복소로그) | 280장 → 388장 → 455장 → 474장 |
| 128장 (Perron–Frobenius) | 712–714장 (마르코프 연쇄) |
| 176장 (역함수정리) | 659장 (Nash–Moser) |
| 195장 (각형식) | 213장, 300장, 383장, 427장 |
| 198장 (정칙값 정리) | 409장 (영역불변정리) |
| 203·207–208장 (쐐기곱·스토크스) | 413장, 417장, 420장 |
| 216장 (미분형식 도수) | 329장, 402장 |
| 217장 (프로베니우스) | 910장 (아르놀드–리우빌) |
| 255장 (헬리) | 685–686장 (포트만토·프로호로프) |
| 288·294·297장 (리우빌·로랑·유수) | 338–339장, 354–355장 |
| 295장 (고립특이점) | 813장 (하르톡스) |
| 343장 (프레드홀름 대안) | 344–346장 → **896장** |
| 347장 (컴팩트 자기수반) | 590장, 637장 |
| 351장 (불변부분공간 문제) | 461장 (뵈를링) |
| 371장 (힐레–요시다) | 631장, 718장 |
| 375–377장 (vN 대수) | 753장 (자유확률) |
| 391장 (곡면 분류) | 479장, 482장 |
| 441장 (하르낙 원리) | 442장, 624장 |
| 471장 (로에브너) | 756장 (SLE) |
| 501장 (Bochner) | 688–689장 (특성함수·레비 연속성) |
| 541–544장 (SL(2,ℝ) 표현론) | 775장 (Ratner), 863장 (셀버그), 926장 (QUE) |
| 570장 (브룬–민코프스키) | 792–796장 |
| 606장 (wavefront set) | 917–918장 |
| 629장 (열방정식) | 738장 (파인만–칵), 878장 (열핵) |
| 654장 (몬주–암페르) | 666–667장 |
| 710장 (BDG) | 730–731장 (확률적분의 $L^p$ 이론) |
| 760장 (에르고딕 분해) | 785–786장 (SRB·깁스 상태) |
| 770–771장 (위상엔트로피·변분원리) | 786장, 838–839장 |
| 774장 (오세레데츠) | 787장 (페신 이론) |
| 790장 (KAM) | 830장 (Brjuno), 910장 (아르놀드–리우빌) |
| 867장 (변분 공식) | 868장, 871–872장 |
| 880장 (Weyl 법칙 주항) | 923장 |

---

# 부록 D — 난제 접근성 순위

**진입장벽 낮음**

| 문제 | 위치 |
|---|---|
| Crouzeix의 추측 | 129장 |
| Sendov의 추측 | 302장 |
| HRT 추측 | 510장 |
| 힐베르트 13번 (해석적) | 548장 |
| Mahler의 부피곱 추측 | 570, 796장 |
| Erdős 닮음 문제 | 571장 |
| 가우스 원 문제 | 856장 |
| Lehmer의 문제 | 861장 |

**중간**

| 문제 | 위치 | 선행 |
|---|---|---|
| Kakeya 추측 (n ≥ 4) | 533장 | 제13–14부 |
| Falconer 거리집합 추측 | 559장 | 제14부 |
| 힐베르트 16번 문제 | 593장 | 제15, 20부 |
| Landis의 추측 | 649장 | 제17부 |
| 확장상태 추측 | 749장 | 제9, 18부 |
| **KLS 추측** | 807장 | 제18, 21부 |
| MLC | 831장 | 제23부 |
| 불변부분공간 문제 | 351장 | 제8, 11.2절 |
| 쌍상관 추측 | 854장 | 제18.4절, 제24부 |
| Hot spots 추측 | 885장 | 제17, 25.1절 |
| 볼록영역 등스펙트럼성 | 884장 | 제25.1절 |
| Berry의 무작위파동 추측 | 885장 | 제25부 |
| QUE | 926장 | 제25.4절 |

**밀레니엄급**

- 나비에–스토크스 정칙성 (662장)
- 리만 가설 (855장)
- 양–밀스 질량 간극 (662장)

---

# 부록 E — 점검 이력

| 순회 | 새 챕터 | 성격 |
|---|---|---|
| 1차 | 78 | 파트·절 규모의 공백 |
| 2차 | 12 | 단일 정리 누락 |
| 3차 (증명 관점) | 8 | 증명 도구 — 자연 발생으로 처리 |
| 4차 | 1 | BDG 부등식 |
| 5차 | 0 | 기존 챕터 내 서술로 해결 |

수렴 완료. **929챕터.**
