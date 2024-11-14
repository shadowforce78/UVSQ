# Thème contrôle 1
	Arithmétique :
		Ex1 : Congruence
		Ex2 : Cherchez l'intrus
		Ex3 : Division Euclidienne
		Ex4 : Congruence + puissance + reste
		Ex5 : Sans reccurence
		Ex7 : Congruences + puissance
	
	Logique élémentaire :
			Ex9 : Table de vérité
			Ex12 : Evaluer = V/F
			Ex13b : Evaluer avec table

## Loi de Morgan

p|q|$\bar p$|$\bar q$|(p+$\bar q$)|($\bar p$+q)|p=q|(p+$\bar q$)($\bar p$+q)
	---|---|---|---|---|---|---|---
	0|0|1|1|1|1|1|1
	0|1|1|0|0|1|0|0
	1|0|0|1|1|0|0|0
	1|1|0|0|1|1|1|1


| a   | b   | $\overline a$ | $\overline b$ | a+b | $\overline{a+b}$ | $\overline{a} \overline b$ | ab  | $\overline{ab}$ | $\overline a$+$\bar b$ |
| --- | --- | ------------- | ------------- | --- | ---------------- | -------------------------- | --- | --------------- | ---------------------- |
| 0   | 0   | 1             | 1             | 0   | 1                | 1                          | 0   | 1               | 1                      |
| 0   | 1   | 1             | 0             | 1   | 0                | 0                          | 0   | 1               | 1                      |
| 1   | 0   | 0             | 1             | 1   | 0                | 0                          | 0   | 1               | 1                      |
| 1   | 1   | 0             | 0             | 1   | 0                | 0                          | 1   | 0               | 0                      |

## Distributivité

ou = +
ou exclusif = $\oplus$ (un seul des deux doit être vrai)
et = .
a implique b = $a \implies b$ (si a = 0 alors vrai, si a = 1 et que b = 0 alors faux)

	a+bc = (a+b).(a+c)

| a b c | b.c | a+bc | a+b | a+c | (a+b).(a+c) |
| ----- | --- | ---- | --- | --- | ----------- |
| 0 0 0 | 0   | 0    | 0   | 0   | 0           |
| 0 0 1 | 0   | 0    | 0   | 1   | 0           |
| 0 1 0 | 0   | 0    | 1   | 0   | 0           |
| 0 1 1 | 1   | 1    | 1   | 1   | 1           |
| 1 0 0 | 0   | 1    | 1   | 1   | 1           |
| 1 0 1 | 0   | 1    | 1   | 1   | 1           |
| 1 1 0 | 0   | 1    | 1   | 1   | 1           |
| 1 1 1 | 1   | 1    | 1   | 1   | 1           |

D'après la table, a+bc = (a+b).(a+c)

Exercice 12 :

Une semaine compte 7 jours ET un mois compte 24 heures : Faux
Une semaine compte 7 jours OU un mois compte 24 heures : Vrai
Une semaine compte 7 jours ET un jour compte 24 heures : Vrai
Si 2 est un diviseur de 6, ALORS 3 est un diviseur de 39 : Vrai
Si 7 est plus grand que 3, alors 4 est plus petit que $\dfrac {\pi}{2}$ : Faux
Si le carré d'un nombre réel est strictement négatif, alors 3 + 2 = 5 : Vrai
Si votre enseignant de TD est Brad Pitt, alors $5 \geq 12$ : Vrai
On pose : 
	e  = "je m'entraine"
	p = "je progresse"
	s = "je suis souffrant"
Donc P = ($e \implies p$ ) et ($s \oplus{e}$ ) et $\overline s$ $\implies p$

| e   | p   | s   | $\overline s$ | $e \implies p$ | $s \oplus e$ | ($e \implies p$) . ($s \oplus e$) . $\overline s$ | [] $\implies p$ |
| --- | --- | --- | ------------- | -------------- | ------------ | ------------------------------------------------- | --------------- |
| 0   | 0   | 0   | 1             | 1              | 0            | 0                                                 | 1               |
| 0   | 0   | 1   | 0             | 1              | 1            | 0                                                 | 1               |
| 0   | 1   | 0   | 1             | 1              | 0            | 0                                                 | 1               |
| 0   | 1   | 1   | 0             | 1              | 1            | 0                                                 | 1               |
| 1   | 0   | 0   | 1             | 0              | 1            | 0                                                 | 1               |
| 1   | 0   | 1   | 0             | 0              | 0            | 0                                                 | 1               |
| 1   | 1   | 0   | 1             | 1              | 1            | 1                                                 | 1               |
| 1   | 1   | 1   | 0             | 1              | 0            | 0                                                 | 1               |
Donc vrai

Exercice 13 : 

(( $p \implies q$ ) p ) $\implies q$
$\overline p \implies (p \implies q)$
($p \implies q) p \overline q$ 


$p \oplus q$ =? $\overline{p <===> q}$

| p   | q   | $p \oplus q$ | p<===>q | $\overline{p<===>q}$ |
| --- | --- | ------------ | ------- | -------------------- |
| 0   | 0   | 0            | 1       | 0                    |
| 0   | 1   | 1            | 0       | 1                    |
| 1   | 0   | 1            | 0       | 1                    |
| 1   | 1   | 0            | 1       | 0                    |
d'après la table, $p \oplus q$ est bien égale a $\overline{p <===> q}$ 


| p   | q   | $\overline p$ | $\overline q$ | pq  | $p \implies q$ | pq <===> p | $\overline q \implies \overline p$ |
| --- | --- | ------------- | ------------- | --- | -------------- | ---------- | ---------------------------------- |
| 0   | 0   | 1             | 1             | 0   | 1              | 1          | 1                                  |
| 0   | 1   | 1             | 0             | 0   | 1              | 1          | 1                                  |
| 1   | 0   | 0             | 1             | 0   | 0              | 0          | 0                                  |
| 1   | 1   | 0             | 0             | 1   | 1              | 1          | 1                                  |

d'après la table, ces trois forme son bien tautologiques

P+Q = $\overline{\overline{P+Q}}$ = $\overline{\overline{P} . \overline{Q}}$ = $\overline{P} \uparrow \overline{Q}$ = $(P\uparrow P)\uparrow (Q\uparrow Q)$ 

$P\implies Q$ = $\overline P + Q$
		= $\overline{\overline{\overline{P}+Q}}$
		= $\overline{P + \overline {Q}}$
		= $P \uparrow \overline Q$
		= $P \uparrow (Q\uparrow Q)$

$P \Leftrightarrow Q$ = PQ + $\overline {P} .\overline {Q}$ 
		= $\overline{\overline{PQ + \overline{P}\overline{Q}}}$ 
		= $\overline{\overline{PQ}\overline{P}.\overline{Q}}$ 
		= $\overline{PQ}\uparrow \overline{\overline{P}.\overline{Q}}$
		=  $(P\uparrow Q)\uparrow (\overline{P}\uparrow \overline{Q})$
		= $(P\uparrow Q)\uparrow ((P\uparrow P)\uparrow (Q \uparrow Q))$

	$P\oplus{Q} = \overline{P\Leftrightarrow Q}$ 

$\overline{P} = \overline{P+P} = P\downarrow P$
$PQ = \overline{\overline{PQ}} = \overline{\overline{P}+\overline{Q}} = \overline{P}\downarrow \overline{Q} = (P\downarrow P)\downarrow (Q\downarrow Q)$
$P+Q = \overline{\overline{P+Q}} = \overline{P\downarrow Q} = (P\downarrow Q)\downarrow (P\downarrow Q)$
$P\implies Q = \overline{P} + Q = \overline{\overline{\overline{P}+Q}} = \overline{\overline{P}\downarrow Q}= \overline{(P\downarrow Q) \downarrow Q} = ((P\downarrow P)\downarrow Q) \downarrow ((P\downarrow P) \downarrow Q)$ 
$P \Leftrightarrow Q = \overline{P\oplus Q} = \overline{P\overline{Q} + \overline{P} Q} = (\overline{\overline{P\overline{Q}}})\downarrow(\overline{\overline{\overline{P}Q}}) = (\overline{P}\downarrow Q)\downarrow  (P \downarrow \overline{Q})$ 


### Exercice 18

| x   | y   | z   | f(x;y;z) | g(x;y;z) | min terme de F                           | min terme de G                |
| --- | --- | --- | -------- | -------- | ---------------------------------------- | ----------------------------- |
| 0   | 0   | 0   | 1        | 0        | $\overline{X};\overline{Y};\overline{X}$ |                               |
| 0   | 0   | 1   | 1        | 1        | $\overline{X};\overline{Y};Z$            | $\overline{X};\overline{Y};Z$ |
| 0   | 1   | 0   | 0        | 0        |                                          |                               |
| 0   | 1   | 1   | 0        | 1        |                                          | $\overline{X};Y;Z$            |
| 1   | 0   | 0   | 1        | 0        | $X;\overline{Y};\overline{Z}$            |                               |
| 1   | 0   | 1   | 0        | 0        |                                          |                               |
| 1   | 1   | 0   | 1        | 0        | $X;Y;\overline{Z}$                       |                               |
| 1   | 1   | 1   | 1        | 1        | $X;Y;Z$                                  | $X;Y;Z$                       |

### Exercice 19
$x\oplus{y}$ = $\overline{x}y+x\overline{y}$ = FnD
	 = $\overline{xy+\overline{xy}}$
	 = $\overline{xy}.\overline{\overline{x}\overline{y}}$
	 = $(\overline{x}+\overline{y})(x+y)$ FnC (2 Max Terms)

### Exercice 20

g(a;b;c) = $abc+ab\overline{c}+\overline{a}bc+\overline{a}\overline{b}c+\overline{a}\overline{b}\overline{c}$ = $\overline{a}\overline{b}+bc$


|                | $\overline{a}\overline{b}$ | $\overline{a}b$ | $ab$ | $a\overline{b}$ |
| -------------- | -------------------------- | --------------- | ---- | --------------- |
| $\overline{c}$ | X                          |                 | X    |                 |
| $c$            | X                          | X               | X    |                 |



h(a;b;c) = $ab\overline c\overline d+a\overline bcd+a\overline b\overline cd+\overline abc\overline d+\overline ab\overline c\overline d+\overline a\overline bcd+\overline a\overline b\overline cd$

|                          | $\overline a\overline b$ | $\overline ab$ | $ab$ | $a\overline b$ |
| ------------------------ | ------------------------ | -------------- | ---- | -------------- |
| $\overline c\overline d$ |                          | X              | X    |                |
| $\overline cd$           | X                        |                |      | X              |
| $cd$                     | X                        |                |      | X              |
| $c\overline d$           |                          | X              |      |                |

$S = [(pq)\implies{(\overline{q}r)}]\implies{[(p+q)\implies{\overline q}]}$ 
$S = pqr + pq\overline{r}+\overline{p}q\overline{r}+p\overline{q}r+\overline{p}\overline{q}r+p\overline{q}\overline{r}+\overline{p}\overline{q}\overline{r}$


|                | $\overline{p}.\overline{q}$ | $\overline{p}q$ | $pq$ | $p\overline{q}$ |
| -------------- | --------------------------- | --------------- | ---- | --------------- |
| $\overline{r}$ | X                           | X               | X    | X               |
| $r$            | X                           |                 | X    | X               |

D'après le diagramme 
$S = p + \overline q + \overline r$ (FnC)


# Les Ensembles

### Exercice 24
Soit \( E = \{1, 2, 3, 4, 5, 6, 7, 8\} \), \( A = \{1, 2, 3, 4, 5\} \) et \( B = \{1, 3, 5, 7\} \)

1. **Complémentaire de A dans E** :
   $\overline{A} = E \setminus A = \{6, 7, 8\}$

2. **Complémentaire de B dans E** :
   $\overline{B} = E \setminus B = \{2, 4, 6, 8\}$

3. **Intersection de A et B** :
   $A \cap B = \{1, 3, 5\}$

4. **Union de A et B** :
   $A \cup B = \{1, 2, 3, 4, 5, 7\}$ 

5. **Différence de A par B** :
   $A \setminus B = \{2, 4\}$

6. **Différence de B par A** :
	$B \setminus A = \{7\}$

8. **Symétrie différence entre A et B** :
   $A \oplus B = (A \setminus B) \cup (B \setminus A) = \{2, 4, 7\}$


Pour rappel : $\overline{C}\cup{C} = E$ 


### Exercice 36

la fonction $f$ de E dans F est définie par $\forall x\in E, f(x) = x²$
Dans chaque cas, est elle une application, Injection, Surjection Bijection ?
a) E = F = $\mathbb{R}$ => Application
b) E = $\mathbb R$ et F = $\mathbb R$<sub>+</sub> => Application et Surjection
c) E = $\mathbb R$<sub>+</sub> et F = $\mathbb R$ => Pas une application
d) E = F = $\mathbb R$<sub>+</sub> => Application, Injection, Surjection et Bijection

### Exercice 41

$$A_{n}^{p}=\dfrac{n!}{(n-p)!}$$
$$C_{n}^{p}=\binom{n}{p}=\binom{n}{n-p}$$
	$$C_{n}^{p}=\binom{n}{p}=\dfrac{n!}{p!(n-p)!}$$


$A_{3}^{11}$ = $\dfrac{11!}{(11-3)!}$=$\dfrac{11!}{8!}$=$\dfrac{1*2*3*4*5*6*7*8*9*10*11}{1*2*3*4*5*6*7*8}$=$9*10*11$=990

$C_{11}^{8}$=$\dfrac{11!}{8!(11-8)!}$=$\dfrac{11!}{8!*3!}$=$\dfrac{11*10*9*8!}{8!*3!}$=$\dfrac{11*10*9}{3!}$=$\dfrac{990}{6}$=$165$ 

### Exercice 42

Six enfant font la course; il n'y a pas d'ex aequo. Combien y a t'il de classement possibles ?

$N = 6! = 1*2*3*4*5*6 = 36*25 = 720$
Il y a 720 classement possibles

### Exercice 43
Sept couverts sont disposés sur une table ronde.

a) De combien de façons peut-on disposer les sept convives ?
	Sur une table **non ronde** : 
		$N = 7! = 1*2*3*4*5*6*7 = 720*7 = 5040$
		Il y a 7! (5040) possibilité de disposer les couverts
	Sur une table **ronde** : 
		C'est pareil

b) Reprendre la question a) sachant que Monsieur Jecrains et Madame Ronchon ne doivent surtout pas être cote a côté

- Il faut faut faire un bloc de JC et R donc finalement il reste 6 places assises,
- Place JC = 7
- Place R = 4
- ça fait donc 6 places - les 2 places voisines = 4 possibilités
- il faut placer encore 5 convives : $5!$
$N = 7*4*5! = 7*4*120=3360$ 

### Exercice 44



Formule du binôme de Newton : $$(a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k$$

Ici, \( a = x \), \( b = 1 \) et \( n = 6 \).

1. **Calcul des termes** :
   $(x+1)^6 = \sum_{k=0}^{6} \binom{6}{k} x^{6-k} \cdot 1^k$
   
2. **Développement complet** :
   $(x+1)^6 = x^6 + 6x^5 + 15x^4 + 20x^3 + 15x^2 + 6x + 1$
   


## Développement de $(2x - 3)^4$ 

Le développement est donné par :

$$(2x - 3)^4 = \sum_{k=0}^{4} \binom{4}{k} (2x)^{4-k} (-3)^k$$

1. **Premier terme** :  
   $\binom{4}{0} (2x)^4 (-3)^0 = 1 *(2x)^4* 1 = (2x)^4 = 16x^4$ 
   
1. **Deuxième terme** :  
   $\binom{4}{1} (2x)^3 (-3)^1 = 4 * (2x)^3 * (-3) = 4 * 8x^3 * (-3) = -96x^3$
   
1. **Troisième terme** :  
   $\binom{4}{2} (2x)^2 (-3)^2 = 6 * (2x)^2 * 9 = 6 * 4x^2 * 9 = 216x^2$

4. **Quatrième terme** :  
   $\binom{4}{3} (2x)^1 (-3)^3 = 4 * (2x) * (-27) = 4 * 2x * (-27) = -216x$

5. **Cinquième terme** :  
   $\binom{4}{4} (2x)^0 (-3)^4 = 1 * 1 * 81 = 81$ 

$$(2x - 3)^4 = 16x^4 - 96x^3 + 216x^2 - 216x + 81$$

### Triangle de Pascal

	$$ \begin{matrix} 
	& & & & & & & 1 & & & & & & &  \\
	& & & & & & 1 & & 1 & & & & & &  \\
	& & & & & 1 & & 2 & & 1 & & & & & \\
	& & & & 1 & & 3 & & 3 & & 1 & & & &  \\
	& & & 1 & & 4 & & 6 & & 4 & & 1 & & & \\
	& & 1 & & 5 & & 10 & & 10 & & 5 & & 1 & & \\
	& 1 & & 6 & & 15 & & 20 & & 15 & & 6 & & 1 &
	\end{matrix} $$

 $$
\begin{matrix} 
	& & & & & & & \binom{0}{0} & & & & & & &  \\
	& & & & & & \binom{1}{0} & & \binom{1}{1} & & & & & &  \\
	& & & & & \binom{2}{0} & & \binom{2}{1} & & \binom{2}{2} & & & & & \\
	& & & & \binom{3}{0} & & \binom{3}{1} & & \binom{3}{2} & & \binom{3}{3} & & & & \\
	& & & \binom{4}{0} & & \binom{4}{1} & & \binom{4}{2} & & \binom{4}{3} & & \binom{4}{4} & & & \\
	& & \binom{5}{0} & & \binom{5}{1} & & \binom{5}{2} & & \binom{5}{3} & & \binom{5}{4} & & \binom{5}{5} & & \\
	& \binom{6}{0} & & \binom{6}{1} & & \binom{6}{2} & & \binom{6}{3} & & \binom{6}{4} & & \binom{6}{5} & & \binom{6}{6} &
\end{matrix}
$$

## Exercice 45
## Partie a) : Considération des sous-ensembles

Soit $E$ un ensemble de cardinal $n$. Le nombre total de sous-ensembles de $E$ est donné par $2^n$, car chaque élément de $E$ peut soit appartenir, soit ne pas appartenir à un sous-ensemble.

Un sous-ensemble de $E$ peut être décrit par son cardinal $k$, c'est-à-dire par le nombre d'éléments qu'il contient. Le nombre de sous-ensembles de cardinal $k$ est donné par la combinaison $\binom{n}{k}$, qui représente le nombre de façons de choisir $k$ éléments parmi $n$.

Ainsi, le nombre total de sous-ensembles de $E$ peut être exprimé comme la somme des sous-ensembles de tous les cardinaux possibles :

$$
2^n = \sum_{k=0}^{n} \binom{n}{k}.
$$

### Partie b) : À l'aide de la formule du binôme de Newton

La formule du binôme de Newton nous donne l'expansion suivante pour tout $x$ et $y$ :

$$
(x + y)^n = \sum_{k=0}^{n} \binom{n}{k} x^{n-k} y^k.
$$

En prenant $x = 1$ et $y = 1$, on obtient :

$$
(1 + 1)^n = \sum_{k=0}^{n} \binom{n}{k} 1^{n-k} 1^k.
$$

Comme $1^{n-k} = 1$ et $1^k = 1$ pour tous les entiers $n$ et $k$, cela simplifie à :

$$
2^n = \sum_{k=0}^{n} \binom{n}{k}.
$$

Ainsi, nous avons montré que :

$$
2^n = \sum_{k=0}^{n} \binom{n}{k}.
$$

$$\sqrt{20} = \sqrt{4}*\sqrt{5} = 2\sqrt{5}$$ 
$$A = 5*\dfrac{13}{15}-7*\dfrac{6}{12} = \dfrac{65}{15}-\dfrac{7}{2}=\dfrac{130}{30}-\dfrac{105}{30} = \dfrac{130-105}{30} = \dfrac{5}{6}$$

$$B = {\sqrt{2}}^3(\sqrt{6}+\sqrt{10})=4\sqrt{3}+4\sqrt{5}$$
$$D=\dfrac{\sqrt{12}-5\sqrt{3}}{\sqrt{75}}=\dfrac{2\sqrt{3}-5\sqrt{3}}{\sqrt{75}}=\dfrac{-3}{5}$$ $$E=\dfrac{(\sqrt{5}-2)^2 + 2\sqrt{20}}{(\sqrt{7}-2)(\sqrt{7}+2)}=\dfrac{(\sqrt{5}​)^2−2×\sqrt{5}​×2+2^2+2×\sqrt{4×5}}{(\sqrt{7})^2-2^2}=\dfrac{9-4\sqrt{5}+4\sqrt{5}}{7-4}=\dfrac{9}{3}=3$$ 
$$F=\dfrac{\sqrt{3}}{2-\sqrt{3}}=\dfrac{\sqrt{3}(2+\sqrt{3})}{(2-\sqrt{3})(2+\sqrt{3})}=2\sqrt{3}+3$$


$$f(x)=(x+1)(2x+3)=2x^2+3x+2x+3=2x^2+5x+3$$
$$g(a;b;c)=(a+2b+c)(3a-b)$$
1. **Premier terme :** $(a \cdot (3a - b) = 3a^2 - ab)$
2. **Deuxième terme :**$(2b \cdot (3a - b) = 6ab - 2b^2)$
3. **Troisième terme :** $(c \cdot (3a - b) = 3ac - bc)$ 

$$g(a; b; c) = 3a^2 - ab + 6ab - 2b^2 + 3ac - bc$$
$$g(a; b; c) = 3a^2 + 5ab - 2b^2 + 3ac - bc$$
$$\begin{array}{c|c}
\text{Puissance} & \text{Coefficients binomiaux} \\
\hline
0 & 1 \\
1 & 1 \quad 1 \\
2 & 1 \quad 2 \quad 1 \\
3 & 1 \quad 3 \quad 3 \quad 1 \\
4 & 1 \quad 4 \quad 6 \quad 4 \quad 1 \\
5 & 1 \quad 5 \quad 10 \quad 10 \quad 5 \quad 1 \\
\end{array}$$
$$i(x)=(x-2)^5=(x - 2)^5 = \sum_{k=0}^{5} \binom{5}{k} x^{5-k} (-2)^k$$
K = 0 : $$\binom{5}{0}x^5(-2)^0=x^5 $$
K = 1 : $$\binom{5}{1}x^4(-2)^1=-10x^4 $$
K = 2 : $$\binom{5}{2}x^3(-2)^2=40x^3 $$
K = 3 : $$\binom{5}{3}x^2(-2)^3=-80x^2 $$
K = 4 : $$\binom{5}{4}x^1(-2)^4=80x $$
K = 5 : $$\binom{5}{5}x^0(-2)^5=-32 $$
$$i(x)=(x-2)^5 =x^5-10x^4+40x^3-80x^2+80x-32$$ 
$$ j(x) = (2\sqrt{2}-3)^2 = -12\sqrt{2}+17$$
	$$k(x)=(2\sqrt{x^2+3}-\sqrt{8})(\sqrt{x^2+3}+\sqrt{2})$$
- $a = 2\sqrt{x^2 + 3}$
- $b = \sqrt{8}$ 
$k(x) = \left( 2\sqrt{x^2 + 3} \right)^2 - (\sqrt{8})^2$
$\left( 2\sqrt{x^2 + 3} \right)^2 = 4(x^2 + 3) = 4x^2 + 12$
$(\sqrt{8})^2 = 8$
$k(x) = 4x^2 + 12 - 8$
$$k(x)=2x^2+2$$


$$f(t)=3t^2+6=3(t^2+2)$$ $$g(x)=4(x+1)-(x+1)^2=(x+1)(3-x)$$ 