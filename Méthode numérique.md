
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

**b) Exprimer \( u_n \) en fonction de \( n \) et déterminer sa limite**

**Étape 1 : Exprimer \( v_n \) en fonction de \( n \)**

La suite \((v_n)\) est géométrique de raison \( \frac{\sqrt{3}}{2} \) et de premier terme :
\[ v_0 = u_0 + k = -1 + (2 + \sqrt{3}) = 1 + \sqrt{3} \]

Ainsi :
\[ v_n = v_0 \left( \frac{\sqrt{3}}{2} \right)^n = (1 + \sqrt{3}) \left( \frac{\sqrt{3}}{2} \right)^n \]

**Étape 2 : Exprimer \( u_n \) en fonction de \( v_n \)**
\[ u_n = v_n - k = (1 + \sqrt{3}) \left( \frac{\sqrt{3}}{2} \right)^n - (2 + \sqrt{3}) \]

**Étape 3 : Calculer la limite de \( u_n \) quand \( n \to +\infty \)**

On sait que \( \left| \frac{\sqrt{3}}{2} \right| \approx 0.866 < 1 \), donc :
\[ \lim_{n \to +\infty} \left( \frac{\sqrt{3}}{2} \right)^n = 0 \]

Ainsi :
\[ \lim_{n \to +\infty} u_n = 0 - (2 + \sqrt{3}) = - (2 + \sqrt{3}) \]

**Réponses :**
- Expression de \( u_n \) :
  \[ \boxed{u_n = (1 + \sqrt{3}) \left( \frac{\sqrt{3}}{2} \right)^n - (2 + \sqrt{3})} \]

- Limite de \( u_n \) :
  \[ \boxed{\lim_{n \to +\infty} u_n = - (2 + \sqrt{3})} \]