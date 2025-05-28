
## Exercice 2
### a)
**Énoncé :**  
Déterminer la raison $r$ de la suite arithmétique (un)(u_n), définie pour tout n∈Nn \in \mathbb{N}, sachant que :

$u_0 = 3 \quad \text{et} \quad u_5 = 96$ 

**Solution :**  
On sait que dans une suite arithmétique, chaque terme s’exprime en fonction du premier terme u0u_0 et de la raison rr de la manière suivante :

$u_n = u_0 + n \cdot r$ 

En particulier, pour $n=5$, on a :

$u5=u0+5$ 

On remplace $u_0$ et $u_5$ par leurs valeurs connues :

$96 = 3 + 5r$

On résout l’équation :

$5r=96−3=93$
$5r = 96 - 3 = 93$ 
$r=935r = \frac{93}{5}$ 
$r=18,6$

**Conclusion :**  
La raison $r$ de la suite arithmétique est $\boxed{18{,}6}$.



### b)

**Énoncé :**  
Déterminer la raison qq de la suite géométrique $(u_n)$, définie pour tout $n \in \mathbb{N}$, sachant que :

u0=3etu5=96u_0 = 3 \quad \text{et} \quad u_5 = 96

**Solution :**  
Dans une suite géométrique, chaque terme s’exprime en fonction du premier terme u0u_0 et de la raison qq de la manière suivante :

un=u0⋅qnu_n = u_0 \cdot q^n

En particulier, pour n=5n = 5, on a :

u5=u0⋅q5u_5 = u_0 \cdot q^5

On remplace u0u_0 et u5u_5 par leurs valeurs connues :

96=3⋅q596 = 3 \cdot q^5

On résout cette équation :

q5=963=32q^5 = \frac{96}{3} = 32 q=325q = \sqrt[5]{32} q=2q = 2

**Conclusion :**  
La raison qq de la suite géométrique est **$\boxed{2}$**.

---

## Exercice 3

**a) Déterminer le réel \( k \)**

On a la suite $((u_n)_{n \in \mathbb{N}})$ définie par :
$[ u_0 = -1 ]$ 
$[ u_{n+1} = \frac{\sqrt{3}}{2} u_n - \frac{1}{2} ]$

On définit une nouvelle suite $((v_n)_{n \in \mathbb{N}})$ par :
$[ v_n = u_n + k ]$
où $((v_n))$ est une suite géométrique de raison $( \frac{\sqrt{3}}{2} )$.

**Étape 1 : Exprimer $( v_{n+1} )$ de deux manières**

1. **En utilisant la définition de $( v_n )$ :**
   $[ v_{n+1} = u_{n+1} + k = \frac{\sqrt{3}}{2} u_n - \frac{1}{2} + k ]$

2. **Comme suite géométrique :**
   $[ v_{n+1} = \frac{\sqrt{3}}{2} v_n = \frac{\sqrt{3}}{2} (u_n + k) ]$

**Étape 2 : Égaliser les deux expressions de $( v_{n+1} )$**
$[ \frac{\sqrt{3}}{2} u_n - \frac{1}{2} + k = \frac{\sqrt{3}}{2} u_n + \frac{\sqrt{3}}{2} k ]$

Simplifions :
$[ -\frac{1}{2} + k = \frac{\sqrt{3}}{2} k ]$
$[ k - \frac{\sqrt{3}}{2} k = \frac{1}{2}]$
$[ k \left(1 - \frac{\sqrt{3}}{2}\right) = \frac{1}{2} ]$
$[ k = \frac{\frac{1}{2}}{1 - \frac{\sqrt{3}}{2}} = \frac{1}{2 - \sqrt{3}} ]$ 

Rationalisons le dénominateur :
$[ k = \frac{1}{2 - \sqrt{3}} \times \frac{2 + \sqrt{3}}{2 + \sqrt{3}} = \frac{2 + \sqrt{3}}{(2)^2 - (\sqrt{3})^2} = \frac{2 + \sqrt{3}}{4 - 3} = 2 + \sqrt{3} ]$

**Réponse :**
$[ \boxed{k = 2 + \sqrt{3}} ]$

---

**b) Exprimer $( u_n )$ en fonction de $( n )$ et déterminer sa limite**

**Étape 1 : Exprimer $( v_n )$ en fonction de $( n )$**

La suite $(v_n)$ est géométrique de raison $( \frac{\sqrt{3}}{2} )$ et de premier terme :
$[ v_0 = u_0 + k = -1 + (2 + \sqrt{3}) = 1 + \sqrt{3} ]$ 

Ainsi :
$[ v_n = v_0 \left( \frac{\sqrt{3}}{2} \right)^n = (1 + \sqrt{3}) \left( \frac{\sqrt{3}}{2} \right)^n ]$

**Étape 2 : Exprimer \( u_n \) en fonction de \( v_n \)**
$[ u_n = v_n - k = (1 + \sqrt{3}) \left( \frac{\sqrt{3}}{2} \right)^n - (2 + \sqrt{3}) ]$

**Étape 3 : Calculer la limite de \( u_n \) quand \( n \to +\infty \)**

On sait que $( \left| \frac{\sqrt{3}}{2} \right| \approx 0.866 < 1 )$, donc :
$[ \lim_{n \to +\infty} \left( \frac{\sqrt{3}}{2} \right)^n = 0 ]$

Ainsi :
$\lim_{n \to +\infty} u_n = 0 - (2 + \sqrt{3}) = - (2 + \sqrt{3})$

**Réponses :**
- Expression de $( u_n )$ :
  $\boxed{u_n = (1 + \sqrt{3}) \left( \frac{\sqrt{3}}{2} \right)^n - (2 + \sqrt{3})}$

- Limite de $( u_n )$ :
  $\boxed{\lim_{n \to +\infty} u_n = - (2 + \sqrt{3})}$ 

![[Pasted image 20250521144019.png]]![[Pasted image 20250521144027.png]]![[Pasted image 20250521144034.png]]![[Pasted image 20250521144045.png]]![[Pasted image 20250521144056.png]]![[Pasted image 20250521144104.png]]![[Pasted image 20250521144123.png]]![[Pasted image 20250521144130.png]]![[Pasted image 20250521144144.png]]


## Exercice 10

![[Pasted image 20250522134036.png]]
![[Pasted image 20250522134046.png]]
![[Pasted image 20250522134057.png]]
![[Pasted image 20250522134106.png]]
![[Pasted image 20250522134117.png]]
![[Pasted image 20250522134131.png]]

## Exercice 12
Pour déterminer la dérivée d'ordre $N$ (où $N$ est un entier naturel) de la fonction inverse définie sur $\mathbb{R}^* = \mathbb{R} \setminus \{0\}$ par :

$$
f(x) = \frac{1}{x}
$$

nous allons procéder par récurrence.

### **Calcul des premières dérivées :**

1. **Dérivée première ($N = 1$) :**
   $$
   f'(x) = -\frac{1}{x^2}
   $$
   On peut aussi écrire :
   $$
   f'(x) = (-1)^1 \cdot \frac{1!}{x^{2}}
   $$

2. **Dérivée seconde ($N = 2$) :**
   $$
   f''(x) = \frac{2}{x^3}
   $$
   Ou :
   $$
   f''(x) = (-1)^2 \cdot \frac{2!}{x^{3}}
   $$

3. **Dérivée troisième ($N = 3$) :**
   $$
   f'''(x) = -\frac{6}{x^4}
   $$
   Ou :
   $$
   f'''(x) = (-1)^3 \cdot \frac{3!}{x^{4}}
   $$

### **Hypothèse de récurrence :**

Supposons que pour un certain entier $N \geq 1$, la dérivée $N$-ième de $f$ est donnée par :

$$
f^{(N)}(x) = (-1)^N \cdot \frac{N!}{x^{N+1}}
$$

### **Étape de récurrence :**

Dérivons $f^{(N)}(x)$ pour obtenir $f^{(N+1)}(x)$ :

$$
f^{(N+1)}(x) = \frac{d}{dx} \left( f^{(N)}(x) \right) = \frac{d}{dx} \left( (-1)^N \cdot \frac{N!}{x^{N+1}} \right)
$$

En utilisant la règle de dérivation des puissances :

$$
f^{(N+1)}(x) = (-1)^N \cdot N! \cdot \frac{d}{dx} \left( x^{-(N+1)} \right) = (-1)^N \cdot N! \cdot \left( -(N+1) \cdot x^{-(N+2)} \right)
$$

Simplifions :

$$
f^{(N+1)}(x) = (-1)^{N+1} \cdot (N+1)! \cdot \frac{1}{x^{N+2}}
$$

Ce qui correspond bien à la formule générale pour $N+1$.

### **Conclusion :**

Par récurrence, nous avons montré que pour tout entier naturel $N$, la dérivée $N$-ième de $f(x) = \frac{1}{x}$ est :

$$
\boxed{f^{(N)}(x) = (-1)^N \cdot \frac{N!}{x^{N+1}}}
$$

où $N!$ désigne la factorielle de $N$.


# 📘 Exercice 13 – Approche de √5 par une suite

## a) Étude de la suite définie par :  
On considère la fonction réelle définie par :

> ∀ x ∈ ℝ₊*,  
> **f(x) = ½ (x + 5/x)**

et la suite réelle (uₙ)ₙ∈ℕ définie par :

> u₀ = 1  
> ∀ n ∈ ℕ, **uₙ₊₁ = ½ (uₙ + 5/uₙ)**

---

### 🔹 (i) Calcul des premiers termes :  
On calcule u₁, u₂ et u₃ :

- u₀ = 1  
- u₁ = ½ (1 + 5/1) = ½ (6) = **3**  
- u₂ = ½ (3 + 5/3) = ½ (3 + 1.666...) = ½ (4.666...) ≈ **2.333...**  
- u₃ = ½ (2.333... + 5/2.333...)  
   → approx 5 / 2.333... ≈ 2.1429  
   → u₃ ≈ ½ (2.333 + 2.1429) ≈ ½ (4.4759) ≈ **2.23795**

---

### 🔹 (ii) Montrer :  
> uₙ₊₁ = ((uₙ - √5)²)/(2uₙ) + √5

On part de :

> uₙ₊₁ = ½ (uₙ + 5/uₙ)

Écrivons 5 comme (√5)² :

> uₙ₊₁ = ½ (uₙ + (√5)²/uₙ) = ½ [(uₙ² + 5) / uₙ]  
> ⇒ uₙ₊₁ = (uₙ² + 5) / (2uₙ)

Or :

> (uₙ - √5)² = uₙ² - 2√5·uₙ + 5  
⇒ ((uₙ - √5)²)/(2uₙ) = (uₙ² - 2√5·uₙ + 5) / (2uₙ)

Donc :

> ((uₙ - √5)²)/(2uₙ) + √5 = (uₙ² + 5) / (2uₙ) = uₙ₊₁ ✔️

---

### 🔹 (iii) Montrer que :  
> ∀ n ∈ ℕ, uₙ > 0  
> ⇒ en déduire ∀ n ∈ ℕ*, uₙ > √5

Par récurrence :

- Initialisation : u₀ = 1 > 0
- Hérédité : si uₙ > 0, alors 5/uₙ > 0, donc uₙ₊₁ = ½ (uₙ + 5/uₙ) > 0

Donc ∀ n ∈ ℕ, uₙ > 0 ✔️

Ensuite, on utilise l’expression trouvée en (ii) :

> uₙ₊₁ = ((uₙ - √5)²)/(2uₙ) + √5

Or ((uₙ - √5)²)/(2uₙ) > 0 donc uₙ₊₁ > √5 ✔️

---

### 🔹 (iv) Montrer que :  
> 0 < (uₙ - √5)/(2uₙ) < ½  
> ⇒ en déduire : uₙ₊₁ - √5 < uₙ - √5

On sait que :

> uₙ₊₁ - √5 = ((uₙ - √5)²)/(2uₙ)

On pose **εₙ = uₙ - √5**, donc :

> uₙ₊₁ - √5 = (εₙ²) / (2uₙ)

Puisque uₙ > √5 ⇒ uₙ > 0, donc :

> 0 < εₙ² / (2uₙ) < εₙ  
⇒ uₙ₊₁ - √5 < uₙ - √5 ✔️

La suite des erreurs εₙ est donc strictement décroissante.

---

### 🔹 (v) Nature de la suite (uₙ) et sa limite :

- On a montré que uₙ > √5 pour tout n
- Et que uₙ₊₁ < uₙ ⇒ suite décroissante et minorée

Donc :

> ✅ La suite (uₙ) est **strictement décroissante** et **minorée par √5**,  
> donc elle est **convergente**.  
> ✅ De plus, lim (uₙ - √5) = 0  
> 	⇒ lim uₙ = √5 ✔️

---

## b) Généralisation (remplacer 1 et 5 par u₀ > 0 et a > 0)

Soit :

> u₀ > 0  
> uₙ₊₁ = ½ (uₙ + a/uₙ)

Même raisonnement :

- uₙ₊₁ = ((uₙ - √a)²)/(2uₙ) + √a  
- uₙ > 0 ⇒ uₙ > √a  
- Suite décroissante et minorée par √a  
- Donc lim uₙ = √a ✔️

---

## c) 💻 Programme Python – Affichage des 20 premières valeurs de (uₙ - √5)

```python
import math

# Paramètres
u = 1  # u0
a = 5  # valeur à approcher
sqrt_a = math.sqrt(a)

# Calcul et affichage des 20 premières valeurs
print(f"{'n':>3} | {'u_n':>12} | {'u_n - √5':>12}")
print("-" * 35)

for n in range(20):
    diff = u - sqrt_a
    print(f"{n:>3} | {u:>12.8f} | {diff:>12.8f}")
    u = 0.5 * (u + a / u)

```


# Exercice 6 : Étude de suites récurrentes

## Énoncé

Soit la suite $(u_n)_{n\in\mathbb{N}}$ définie par : $\begin{cases} u_0 = 1 \ \forall n \in \mathbb{N}, u_{n+1} = 2 + \frac{3}{u_n} \end{cases}$

---

## a) Expression de $u_{n+2}$ en fonction de $u_n$

**Calcul :** $$u_{n+2} = 2 + \frac{3}{u_{n+1}}$$

En substituant l'expression de $u_{n+1}$ : $$u_{n+2} = 2 + \frac{3}{2 + \frac{3}{u_n}}$$

**Simplification du dénominateur :** $$2 + \frac{3}{u_n} = \frac{2u_n + 3}{u_n}$$

Donc : $$u_{n+2} = 2 + \frac{3}{\frac{2u_n + 3}{u_n}} = 2 + \frac{3u_n}{2u_n + 3}$$

**Réduction au même dénominateur :** $$u_{n+2} = \frac{2(2u_n + 3) + 3u_n}{2u_n + 3} = \frac{4u_n + 6 + 3u_n}{2u_n + 3}$$

$$\boxed{u_{n+2} = \frac{7u_n + 6}{2u_n + 3}}$$

---

## b) Étude des suites extraites et monotonie

### Définition des suites extraites

- $(v_n)_{n\in\mathbb{N}}$ : $v_n = u_{2n}$ (termes de rang pair)
- $(w_n)_{n\in\mathbb{N}}$ : $w_n = u_{2n+1}$ (termes de rang impair)

### Calcul des premiers termes

**Pour $(u_n)$ :**

- $u_0 = 1$
- $u_1 = 2 + \frac{3}{1} = 5$
- $u_2 = 2 + \frac{3}{5} = \frac{13}{5} = 2,6$
- $u_3 = 2 + \frac{3}{\frac{13}{5}} = 2 + \frac{15}{13} = \frac{41}{13} \approx 3,15$
- $u_4 = 2 + \frac{3}{\frac{41}{13}} = 2 + \frac{39}{41} = \frac{121}{41} \approx 2,95$

**Pour les suites extraites :**

- $(v_n)$ : $v_0 = u_0 = 1$, $v_1 = u_2 = \frac{13}{5}$, $v_2 = u_4 = \frac{121}{41}$
- $(w_n)$ : $w_0 = u_1 = 5$, $w_1 = u_3 = \frac{41}{13}$

### Étude de la monotonie

**Pour $(v_n)$ :** $$v_{n+1} = u_{2(n+1)} = u_{2n+2} = \frac{7u_{2n} + 6}{2u_{2n} + 3} = \frac{7v_n + 6}{2v_n + 3}$$

Étudions $v_{n+1} - v_n$ : $$v_{n+1} - v_n = \frac{7v_n + 6}{2v_n + 3} - v_n = \frac{7v_n + 6 - v_n(2v_n + 3)}{2v_n + 3}$$

$$= \frac{7v_n + 6 - 2v_n^2 - 3v_n}{2v_n + 3} = \frac{4v_n + 6 - 2v_n^2}{2v_n + 3}$$

$$= \frac{-2(v_n^2 - 2v_n - 3)}{2v_n + 3} = \frac{-2(v_n - 3)(v_n + 1)}{2v_n + 3}$$

**Analyse du signe :**

- Pour $v_n \in ]1, 3[$ : $(v_n - 3) < 0$ et $(v_n + 1) > 0$, donc $v_{n+1} - v_n > 0$
- $(v_n)$ est **croissante** sur l'intervalle $]1, 3[$

**Pour $(w_n)$ :** Par le même raisonnement : $$w_{n+1} - w_n = \frac{-2(w_n - 3)(w_n + 1)}{2w_n + 3}$$

- Pour $w_n \in ]3, 5]$ : $(w_n - 3) > 0$ et $(w_n + 1) > 0$, donc $w_{n+1} - w_n < 0$
- $(w_n)$ est **décroissante** sur l'intervalle $]3, 5]$

### Majoration et minoration

**Montrons par récurrence que $1 \leq v_n < 3$ :**

_Initialisation :_ $v_0 = 1$, donc $1 \leq v_0 < 3$ ✓

_Hérédité :_ Supposons $1 \leq v_n < 3$

- $v_{n+1} = \frac{7v_n + 6}{2v_n + 3}$
- Pour $v_n = 1$ : $v_{n+1} = \frac{13}{5} = 2,6 > 1$
- Pour $v_n \to 3^-$ : $v_{n+1} \to \frac{27}{9} = 3$
- La fonction $f(x) = \frac{7x + 6}{2x + 3}$ est croissante sur $[1, 3[$

Donc $1 < v_{n+1} < 3$ pour tout $n \geq 1$.

**Montrons par récurrence que $3 < w_n \leq 5$ :**

_Initialisation :_ $w_0 = 5$, donc $3 < w_0 \leq 5$ ✓

_Hérédité :_ Par un raisonnement similaire, on montre que $3 < w_{n+1} \leq 5$.

---

## c) Limites des suites

### Convergence des suites extraites

**Pour $(v_n)$ :**

- $(v_n)$ est croissante et majorée par 3
- Par le théorème de convergence monotone : $(v_n)$ converge

**Calcul de la limite :** Si $\lim_{n \to +\infty} v_n = \ell_v$, alors : $$\ell_v = \frac{7\ell_v + 6}{2\ell_v + 3}$$

$$\ell_v(2\ell_v + 3) = 7\ell_v + 6$$ $$2\ell_v^2 + 3\ell_v = 7\ell_v + 6$$ $$2\ell_v^2 - 4\ell_v - 6 = 0$$ $$\ell_v^2 - 2\ell_v - 3 = 0$$

**Résolution :** $(\ell_v - 3)(\ell_v + 1) = 0$

Donc $\ell_v = 3$ ou $\ell_v = -1$

Comme $v_n \geq 1 > -1$, on a $\boxed{\lim_{n \to +\infty} v_n = 3}$

**Pour $(w_n)$ :**

- $(w_n)$ est décroissante et minorée par 3
- Par le même calcul : $\boxed{\lim_{n \to +\infty} w_n = 3}$

### Conclusion pour $(u_n)$

Puisque :

- $\lim_{n \to +\infty} u_{2n} = \lim_{n \to +\infty} v_n = 3$
- $\lim_{n \to +\infty} u_{2n+1} = \lim_{n \to +\infty} w_n = 3$

**Théorème :** Si les suites extraites $(u_{2n})$ et $(u_{2n+1})$ convergent vers la même limite $\ell$, alors $(u_n)$ converge vers $\ell$.

$$\boxed{\lim_{n \to +\infty} u_n = 3}$$
