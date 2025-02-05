Seulement 4 semaines 

1h de CM (3 ou 4)
1h30 de TD en dédoublé
1h30 de TP en salle machine (R)

1 DS en fin de module
? 1 participation de SAé ?



## Statistique descriptives

1) Histoire et étymologie
	1) (Latin) Status => état
	2) (Italien) Statistira => 1700
	3) (Allemand) Statistite => 1750
	4) (Anglais) Political Arithmetic => 1750

2) Contexte :
	1)  ![[Drawing 2025-01-23 11.18.18.excalidraw]]
3) Vocabulaire
	1) <u>Population</u> : L'ensemble des évènements sur lequel on mène une étude 
	2) <u>Individue</u> : Un individu est un membre d'une population
		1) <u>Charactères</u> : Partie spécifique d'un individue
			1) Si on fait une étude sur un seul charactère, alors on fait une étude statistique a une <u>variable</u> 
				1) Cette variable peut avoir <u>plusieurs valeurs</u> que l'on appel : <u>modalité</u>,
				2) modalité discrète => variable discrète : (x1, x2, x3)
				4) modalité constante => variable continue : ([x1,x2[,[x3, x4[.....) 
4) Notations
	1) Charactères (variables) : x, y, z
	2) Modalités (valeurs de variables) : x=(x1, x2, x3, x4........)
		1) x = c(x1, x2, x3, x4.....) (Collection)
		2) Effectives associé a chaque modalité : 

| x   | n   |
| --- | --- |
| x1  | n1  |
| x2  | n2  |
| x3  | n3  |
| ... | ... |

N = $\sum_{i=1}^{P} n_i$ effectif total
$n_i$ => fréquence marginales $f_i = \dfrac{n_i}{N}$ 
$\boxed{\sum^{P}_{i=1} f_i=1 = \sum^{P}_{i=1} = \dfrac{1}{N} \sum^{P}_{i=1} n_i = \dfrac{1}{N} \times N = 1}$ Démonstration 

5) Indicateurs de positions 
	1) Mode
	2) Médiane
	3) Moyenne arithmétique
		1) Mode : 
			1) Le mode d'une série statistique est la valeur ou les valeurs de la variables qui possède l'effectif ou la fréquence le plus élevé 
			2) Exemple : ![[Drawing 2025-01-23 11.44.51.excalidraw]]
		2) Médiane : 
			1) Une valeur du caractère tel que 50% des valeurs de la variables sont inferieures à m et 50% des valeurs sont supérieures à m
			2) Supposons que x et trié en ordre croissant,
				1) Si N est pair $m=\dfrac{x_{\dfrac{N}{2}}+x_{\dfrac{N}{2}+1}}{2}$ 
				2) Si N est impair $m=x_{\dfrac{N+1}{2}}$ 
			3) Exemple : 

| x   | 7   | 8   | 9   | 10  | 12  | 14  | 17  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| n   | 1   | 2   | 3   | 5   | 5   | 3   | 2   |
				N = 21 N est impair donc $x_{14}=10=m$ 
			3) Moyenne arithmétique :
				1) $\bar{x} = \dfrac{1}{N} \sum^{P}_{i=1} n_i;x_i = \sum^{P}_{i=1}f_i;x_i$  


<u>Propriété</u>: $y=ax+b \ ;  a\in b; \ b\in \mathbb{R}$   
$\bar{y}=a\bar{x} +b$ 

R = $x=c(2,4,3,7,8)$
$y=2\times x+3$
$y=c(2\times 2+3, 4\times 2+3,....)$ 

= $$\bar{y}= a\dfrac{1}{N} \sum_{i=1}^{P}n_i x_i +b\dfrac{1}{N} \sum_{i=1}^{P}n_i$$
$y=x-\bar{x}$
6) Indicateurs de dispersion 
	1) Etendue 
		1) e = max(x)-min(x)
	2) Ecart interquartile
		1) Quartile : Quartile 1 avant la médiane, Quartile 3 après la médiane
		2) $e = Q_3-Q_1$ 
		3) ![[Drawing 2025-01-30 11.20.39.excalidraw]]
	3) Variance et écart type
		1) $var(x) = \sigma ^2x = \dfrac{1}{N}\sum_{i=1}^{P}n_i(x_i-\bar{x})^2$  
		2) $\sigma x=\sqrt{\sigma^2x}=\sqrt{var(x)}$ 
		3) Propriétés : $$ \sigma ^2x = \dfrac{1}{N}\sum_{i=1}^{P}n_i(x_i-\bar{x})^2 = \dfrac{1}{N}\sum_{i=1}^{P}n_i x_i^2-(\bar{x})^2 $$ 
	

#### Exercice 1

| 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  | 12  | 14  | 16  | 18  | $x_i$                            |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------- |
| 1   | 2   | 2   | 4   | 5   | 6   | 8   | 9   | 6   | 5   | 1   | 1   | $n_i$                            |
| 1   | 3   | 5   | 9   | 14  | 20  | 28  | 37  | 43  | 48  | 49  | 50  | Effectifs cumulé croissant (ECC) |
Il y a 12 modalités
Il y a 50 individu (N=50) (pair)

Médiane :  $\dfrac{25^{ème}note+26^{ème}note}{2} =\dfrac{10+10}{2} = 10$
Remarque : si N=51 (impaire), Médiane = $26^{ème} Note$ 
Q1 = 13ème note ($\dfrac{N}{2}=25$ est impaire)
Q1 = 8

Q2 = 10

Q3 = médiane des notes de 26 à 50
Q3 = 38ème note
Q3 = 12


Ecart interquartile e = Q3-Q1 = 12-8 = 4
![[Drawing 2025-01-30 15.09.37.excalidraw]]


#### Exercice 2

| 1   | 2   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  | 12  | 14  | 16  | 18  | 19  | $x_i$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
| 1   | 3   | 1   | 2   | 2   | 4   | 5   | 6   | 10  | 11  | 6   | 5   | 1   | 1   | 2   | $n_i$ |
| 1   | 4   | 5   | 7   | 9   | 13  | 18  | 24  | 34  | 45  | 51  | 56  | 57  | 58  | 60  | ECC   |

Il y a 15 modalités
Il y a 60 individu (N=60=pair)
Médiane = $\dfrac{30^{ème}note+31^{ème}note}{2} = \dfrac{10+10}{2}=10$ 
Q1 = $\dfrac{N}{2} =30^{ème} note =\dfrac{15^{ème}note+16^{ème}note}{2} =\dfrac{8+8}{2}=8$ 
Q1 = 8

Q3 = $\dfrac{45^{ème}note+46^{ème}note}{2}=\dfrac{11+12}{2}=11,5$ 
Q3 = 11,5

Ecart interquartile e = Q3-Q1 = 11,5 - 8 = 3,5


#### Exercice 4

