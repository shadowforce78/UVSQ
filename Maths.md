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