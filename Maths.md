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
et = .

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