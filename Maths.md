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

