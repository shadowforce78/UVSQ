# 🧠 Suites - Corrections détaillées

> **Objectif** : comprendre et savoir reproduire chaque étape de raisonnement (définitions, méthode, calculs, justifications) pour être prêt·e au contrôle.

---

## Exercice 1 — Étude de suites explicites

### 1.a) $u_n = \dfrac{n}{n+1}$

**Domaine :** $n \in \mathbb{N}$

**Variation :**
$$
u_{n+1} - u_n = \frac{n+1}{n+2} - \frac{n}{n+1}
= \frac{(n+1)^2 - n(n+2)}{(n+2)(n+1)}
= \frac{1}{(n+2)(n+1)} > 0
$$
Donc la suite est **strictement croissante**.

**Borne supérieure :**  
$\forall n,\ u_n = \dfrac{n}{n+1} < 1$

**Conclusion :**  
Croissante et majorée ⇒ **converge**

**Limite :**
$$
\lim_{n \to \infty} \frac{n}{n+1} = 1
$$

---

### 1.c) $u_n = n - \sqrt{n^2 - n}$

**Domaine :** $n \geq 1$

**Encadrement et équivalent :**
- On sait que :
$$
\sqrt{n^2 - n} > n - 1 \Rightarrow u_n < 1
$$

- Et aussi :
$$
\sqrt{n^2 - n} = n\sqrt{1 - \frac{1}{n}} \sim n\left(1 - \frac{1}{2n}\right) = n - \frac{1}{2} \Rightarrow u_n \sim \frac{1}{2}
$$

- Calcul rigoureux :
$$
n - \sqrt{n^2 - n}
= \frac{n^2 - (n^2 - n)}{n + \sqrt{n^2 - n}}
= \frac{n}{n + \sqrt{n^2 - n}} > \frac{n}{2n} = \frac{1}{2}
$$

Donc :
$$
\frac{1}{2} < u_n < 1
$$

**Monotonie :**  
L’expression est décroissante (peut se prouver par récurrence si besoin).

**Conclusion :**  
Décroissante et minorée ⇒ **converge**

**Limite :**
$$
\lim_{n \to \infty} u_n = \frac{1}{2}
$$

---

### 1.d) $u_n = \frac{\sin(n^2)}{n}$

**Pas de variation évidente** (à cause des oscillations de $\sin(n^2)$)

**Encadrement :**
$$
-\frac{1}{n} \leq u_n \leq \frac{1}{n}
$$

**Conclusion :**  
Par le **théorème des gendarmes** :
$$
\lim_{n \to \infty} u_n = 0
$$

---

## Exercice 2 — Détermination des raisons

### 2.a) Suite arithmétique

Forme générale : $u_n = u_0 + n \cdot r$

Avec $u_3 = 3$, $u_5 = 96$ :

$$
u_5 - u_3 = 2r = 96 - 3 = 93 \Rightarrow r = \frac{93}{2} = 46{,}5
$$

---

### 2.b) Suite géométrique

Forme : $u_n = u_0 \cdot q^n$

Avec $u_3 = 3$, $u_5 = 96$ :

$$
\frac{u_5}{u_3} = \frac{u_0 q^5}{u_0 q^3} = q^2 = \frac{96}{3} = 32 \Rightarrow q = \sqrt{32} = 4\sqrt{2}
$$

---

## Exercice 8 — Somme d’une suite arithmétique

Formule de somme partielle :
$$
S_n = \sum_{k=0}^n u_k = (n+1)u_0 + \frac{n(n+1)}{2}r
$$

Avec $u_0 = 1 \Rightarrow u_n = 1 + nr$ :
$$
S_n = (n+1) + \frac{n(n+1)}{2}r
$$

### 8.a) Cas $r = -2$

$$
S_n = (n+1) - n(n+1) = (n+1)(1 - n) = -(n+1)(n-1)
$$

Donc $S_n \to -\infty$

### Cas $r = \frac{1}{4}$

$$
S_n = (n+1)\left(1 + \frac{n}{8}\right) \sim \frac{n^2}{8} \Rightarrow S_n \to +\infty
$$

### 8.b) Condition de convergence

Pour que $\sum u_n$ converge, il faut $\lim u_n = 0$

Mais ici $u_n = 1 + nr \not\to 0$ sauf si $r = 0$ et $u_0 = 0$  
Donc **diverge toujours**

---

## Exercice 9 — Somme d’une suite géométrique

Formule de somme géométrique :
$$
S_n = \sum_{k=0}^n q^k = \frac{1 - q^{n+1}}{1 - q} \quad (q \neq 1)
$$

### 9.a) Cas $q = -2$ ($|q| > 1$)

- $q^{n+1}$ diverge (en valeur absolue)
- Alternance ≠ convergence absolue ⇒ **diverge**

### Cas $q = \frac{1}{4}$ ($|q| < 1$)

$$
\lim_{n \to \infty} q^{n+1} = 0 \Rightarrow S_n \to \frac{1}{1 - q} = \frac{1}{1 - \frac{1}{4}} = \frac{4}{3}
$$

### 9.b) Condition de convergence

Une série géométrique converge **si et seulement si** $|q| < 1$

---

## Exercice 3 — Suite arithmético-géométrique

Donnée :
$$
u_0 = -1, \quad u_{n+1} = \frac{\sqrt{3}}{2}u_n - \frac{1}{2}
$$

### 1. Transformation

Posons $a = \frac{\sqrt{3}}{2}$, $b = -\frac{1}{2}$  
On cherche $k$ tel que $v_n = u_n - k$ soit géométrique :

$$
v_{n+1} = u_{n+1} - k = a u_n + b - k = a(v_n + k) + b - k = a v_n + (a k + b - k)
$$

On veut : $a v_n + (a k + b - k) = a v_n$  
Donc :
$$
a k + b - k = 0 \Rightarrow k(a - 1) = -b \Rightarrow k = \frac{-b}{a - 1}
= \frac{1/2}{\frac{\sqrt{3}}{2} - 1} = \frac{1}{\sqrt{3} - 2} = 2 + \sqrt{3}
$$

### 2. Formule explicite

$u_n = v_n + k$ avec :

- $v_0 = u_0 - k = -1 - (2 + \sqrt{3}) = -3 - \sqrt{3}$
- $v_{n+1} = a v_n \Rightarrow v_n = v_0 a^n$

Donc :
$$
u_n = v_n + k = (-3 - \sqrt{3})\left(\frac{\sqrt{3}}{2}\right)^n + (2 + \sqrt{3})
$$
