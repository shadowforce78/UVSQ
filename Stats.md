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


## Statistique a 2 variables
Cf snap


Méthode des mendré carré 

$S = \sum(M_iP_i)^2$ 
$y = m x_i + P$
$S = \sum^{n}_{i=1}(mx_i +p -y_i)^2$ 
$= \sum^{n}_{i=1}((mx_i -y_i)+p)^2$ 
$=\sum^{n}_{i=1}((mx_i)^2+2p(mx_i -y_i)+p^2)$
$S(p)=A+2pB-np^2$ 
$p=\dfrac{-2B}{2n} = \dfrac{-B}{n}=\dfrac{\sum^{n}_{i=1}mx_i-y_i}{n}$
$\boxed{p=\bar{y}-m\bar{x}}$ 
Donc la droite de régression par la méthode des mendré carrés passe par le point moyen du nuage

$S=\sum^{n}_{i=1}mx_i +p -y_i^2$ 
$S=\sum^{n}_{i=1}(mx_i + \bar{y}-m\bar{x}-y_i)^2$ 
$S=\sum^{n}_{i=1}(m(x_i+\bar{y})-(y_i-\bar{y}))$ 
$\boxed{n=\dfrac{\sum^{n}_{i=1}(x_i-\bar{x})(y_i-\bar{y})}{\sum^{n}_{i=1}(x_i-\bar{x})^2}}$ 

Covariance de x et y= $cov(x,y) = \sigma_{xy}=\dfrac{1}{n}\sum^{n}_{i=1}(x_i-\bar{x})(y_i-\bar{y})$ 
$\boxed{r=\dfrac{\sigma_{xy}}{\sigma_x \sigma_y}} => \boxed{-1 < r < 1}$  

Droite allométrique (Passe entre les deux droites)
$y=mx+p$
$|m|=\dfrac{\sigma_y}{\sigma_x}$
$m\sigma_{xy}>0$ 
$p=\bar{y}-m\bar{x}$ 


## Exercice 5)

| $x_i$ | 2   | 3   | 4   | 6   |
| ----- | --- | --- | --- | --- |
| $n_i$ | 2   | 4   | 1   | 1   |
| $N$   | 2   | 6   | 7   | 8   |

| $y_i$ | 3   | 4   | 6   | 7   |
| ----- | --- | --- | --- | --- |
| $n_i$ | 1   | 2   | 2   | 1   |
| $N$   | 1   | 3   | 5   | 6   |



$M_x \ \ N = 8$ (pair) 
Donc $M_x = \dfrac{4^{ème}+5^{ème}}{2} = \dfrac{3+3}{2}=3$ 

$M_y \ \ N = 6$ (pair)
Donc $M_y = \dfrac{3^{ème}+4^{ème}}{2} = \dfrac{4+6}{2}=5$ 

$S_x(a) = \sum^{P}_{i=1} n_i |a-x_i|=2|a-2|+4|a-3|+1|a-4|+1|a-6|$ 
Si $a =< 2  \ \ S_x(a) = 2(2-a)+4(3-a)+(4-a)+(6-a) =-8a+26$
Si $a\in]2;3] \ \ S_x(a)=2(a-2)+4(3-a)+(4-a)+(6-a)=-4a+18$
Si $a\in]3;4] \ \ S_x(a)=2(a-2)+4(a-3)+(4-a)+(6-a)=4a-6$ 
Si $a\in]4;6] \ \ S_x(a) = 2(a-2)+4(a-3)+(a-4)+(6-a)=6a-14$
Si $a>6 \ \ S_x(a)=2(a-2)+4(a-3)+(a-4)+(a-6)=8a-26$ 

![[Pasted image 20250213151408.png]]

$S_x(a)$ est min lorsqu'on choisit $a=M_x$ la médiane
Alors : $\dfrac{1}{N}S_x(a=M_x)$ est la moyenne des valeurs absolue d'écart par rapport à la médiane 
C'est un indicateur de dispersion

Moyennes :
$\bar x = \dfrac{1}{N} \sum^{P}_{n=i}n_ix_i=\dfrac{1}{8}(2\times 2 +4\times 3 +1 \times 4 +1 \times 6)=\dfrac{26}{8}=\dfrac{13}{4}=3.25$
$\bar y= 5$ (à la maison)

$\Gamma_x(a)=\sum^{4}_{i=1}n_i(a-x_i)^2$ 
	$=\sum^{P}_{i=1}n_i(a^2-2a x_i+x_i^2)$
	$=a^2\sum^{P}_{i=1}-2a\sum^{P}_{i=1}n_ix_i+\sum^P_{i=1}n_ix_i^2$ 
$\Gamma_x(a)=Na^2-2N\bar x a + N E(x^2)$	 

Donc : $\dfrac{\Gamma_x(a)}{N}=a^2-2\bar x a+E(x^2)$

Rappel : le trinôme $AX^2+BX+C$ (A>0)
	est min pour $X=-\dfrac{B}{2A}$
	$\Gamma_x(a)$ est min pour $a=-\dfrac{-2\bar x}{2}=\bar x$ 
	= var(x)

## Exercice 8)

$E(\dfrac{1}{x})$ 
$\boxed{H=\dfrac{1}{E(\dfrac{1}{x})}}=\dfrac{N}{\sum^P_{i=1}\dfrac{n_i}{x_i}}$


## Exercice 11)

Soit (y; n) la série statistique suivante 

| Caractère y | 101 | 102 | 103 | 104 | 105 | 106 |
| ----------- | --- | --- | --- | --- | --- | --- |
| effectif n  | 2   | 3   | 2   | 1   | 4   | 1   |

On donne les résultats suivants :
$\bar y = 103.38$
$\sigma^2_y = 2.7$

Soit (x; n) la série statistique suivante :


| Caractère x | 1   | 1.01 | 1.02 | 1.03 | 1.04 | 1.05 |
| ----------- | --- | ---- | ---- | ---- | ---- | ---- |
| effectif n  | 2   | 3    | 2    | 1    | 4    | 1    |

1) Déterminer deux réels a et b tels que $x=ay+b$
2) En déduire $\bar x$ et $\sigma^2_y$ 

- **Calcul de x̄ :**

- `x̄ = aȳ + b`
    
    - `x̄ = (0.01)(103.38) - 0.01`
    - `x̄ = 1.0338 - 0.01`
    - `x̄ = 1.0238`

- **Calcul de σ²ₓ :**

- `σ²ₓ = a²σ²ᵧ`
    
    - `σ²ₓ = (0.01)² (2.7)`
    - `σ²ₓ = (0.0001)(2.7)`
    - `σ²ₓ = 0.00027`



## Exercice 12)

Soit le nuage de points suivant : 

| x   | 1   | 2   | 3   | 4   | 5   | 6   |
| --- | --- | --- | --- | --- | --- | --- |
| y   | 2   | 4   | 3   | 5   | 3   | 4   |

1) Représenter le nuage de points
2) Déterminer l'équation de la droite de régression obtenue par la méthode de Mayer
3) Tracer la Droit de Mayer

## Exercice 13)

Soit $x;y$ une série statistique double 

1) Démontrer que : 
$cov(x,y)=\dfrac{1}{n}\sum^{i=n}_{i=1}(\bar x x_i)(\bar y -y_i) = \dfrac{1}{n}\sum^{i=n}_{i=i}x_i y_i - \bar x \bar y$ 
$$\begin{aligned}
cov(x,y) &= \frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y}) \\
&= \frac{1}{n} \sum_{i=1}^{n} (x_i y_i - x_i \bar{y} - \bar{x} y_i + \bar{x} \bar{y}) \\
&= \frac{1}{n} \left( \sum_{i=1}^{n} x_i y_i - \bar{y} \sum_{i=1}^{n} x_i - \bar{x} \sum_{i=1}^{n} y_i + \sum_{i=1}^{n} \bar{x} \bar{y} \right) \\
&= \frac{1}{n} \left( \sum_{i=1}^{n} x_i y_i - \bar{y} (n \bar{x}) - \bar{x} (n \bar{y}) + n \bar{x} \bar{y} \right) \\
&= \frac{1}{n} \left( \sum_{i=1}^{n} x_i y_i - n \bar{x} \bar{y} - n \bar{x} \bar{y} + n \bar{x} \bar{y} \right) \\
&= \frac{1}{n} \left( \sum_{i=1}^{n} x_i y_i - n \bar{x} \bar{y} \right) \\
&= \frac{1}{n} \sum_{i=1}^{n} x_i y_i - \bar{x} \bar{y}
\end{aligned}$$


1) Démontrer que si y = $ax+b$ alors $\sigma_{x,y}=a\sigma^2_x$ 

$$\begin{aligned}
\text{Si } y_i &= ax_i + b \text{, alors } \bar{y} = a\bar{x} + b \\
\sigma_{xy} &= \frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y}) \\
&= \frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})(ax_i + b - (a\bar{x} + b)) \\
&= \frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})(ax_i - a\bar{x}) \\
&= \frac{a}{n} \sum_{i=1}^{n} (x_i - \bar{x})(x_i - \bar{x}) \\
&= \frac{a}{n} \sum_{i=1}^{n} (x_i - \bar{x})^2 \\
&= a \sigma^2_x
\end{aligned}$$ 