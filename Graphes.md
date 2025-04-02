# TD1

## Exercice 1
1) 
	1) G = ($V,E$)
	2) V = {$v_1,v_2,v_3,v_4,v_5$}
	3) E = {$v_1v_3,v_2v_3,v_4v_3,v_5v_3$}

## Exercice 2

1) ![[Drawing 2025-03-05 12.11.23.excalidraw]]
2) ![[Drawing 2025-03-05 12.13.10.excalidraw]]
3) ![[Drawing 2025-03-05 12.21.01.excalidraw]]

## Exercice 3

1) ![[Drawing 2025-03-05 12.28.47.excalidraw]]
2) ![[Drawing 2025-03-05 12.31.44.excalidraw]]
3) ![[Drawing 2025-03-05 12.36.06.excalidraw]]

## Exercice 4


![[Drawing 2025-03-05 13.00.42.excalidraw]]

1) Ordre, taille, degré
	1) Ordre = 8
	2) Taille = 12
	3) Degré :
		1) $\delta$(a) = 3
		2) $\delta$(b) = 4
		3) $\delta$(c) = 3
		4) $\delta$(d) = 4
		5) $\delta$(e) = 3
		6) $\delta$(f) = 2
		7) $\delta$(g) = 3
		8) $\delta$(h) = 2
		9) Total = 24
2) Déterminer un cycle, le plus court possible, passant par chaque sommets :
	1) a d c b f g h e a
	2) ![[Drawing 2025-03-05 13.02.59.excalidraw]] 

## Exercice 5

- 0<m<$\dfrac{n(n-1)}{2}$ 

## Exercice 6

Graphe de Brujin
![[Drawing 2025-03-05 13.18.13.excalidraw]]

## Exercice 7

$G = (V,E)$
$V=\{a,b,c,d,e\}$
Ordre $n = |V| = \binom{5}{2}=\dfrac{5!}{2!(5-2)!}= \dfrac{5\times4\times3\times2\times1}{2!\times3!}$ 

![[Drawing 2025-03-05 13.53.07.excalidraw]] 


# Quelques graphes classiques

## La chaîne a 6 sommets

![[Drawing 2025-03-06 13.37.19.excalidraw]]

## La chaîne a $n$ sommets

![[Drawing 2025-03-06 13.46.04.excalidraw]]

## Le cycle a 7 sommets

![[Drawing 2025-03-06 13.53.06.excalidraw]]

## Le cycle a n sommets 

![[Drawing 2025-03-06 13.58.04.excalidraw]]

## Le graphe complet à 5 sommets

![[Drawing 2025-03-06 14.05.06.excalidraw]]

## Le graphe complet à n sommets

![[Drawing 2025-03-06 14.09.29.excalidraw]]

## Le graphe biparti complet $K_{2,4}$ 

![[Drawing 2025-03-06 14.18.28.excalidraw]]

## Le graphe biparti complet $K_{p,q}$

![[Drawing 2025-03-06 14.24.16.excalidraw]]

## La grille 2D de côté 4

![[Drawing 2025-03-06 14.35.28.excalidraw]]



## Exercice 7
![[Drawing 2025-03-25 14.53.54.excalidraw]]

## Exercice 8

![[Drawing 2025-03-25 15.29.43.excalidraw]]

![[Drawing 2025-04-01 15.56.49.excalidraw]]
![[Drawing 2025-04-01 16.20.41.excalidraw]]
### Exercice 4

#### a) Connexité de $G$

**Preuve :**  
Supposons $G$ non connexe. Alors $G$ a deux composantes $C_1$ et $C_2$ d'ordres $n_1$ et $n_2$.  
Degré minimal $\geq n$ implique $n_1 \geq n + 1$ et $n_2 \geq n + 1$, donc $n_1 + n_2 \geq 2n + 2$. Contradiction avec $n_1 + n_2 = 2n$.  
**Conclusion :** $G$ est connexe.  

---

#### b) Diamètre $\leq 2$

**Preuve :**  
Pour deux sommets $u$ et $v$ :  
- Si adjacents : $d(u, v) = 1$.  
- Sinon, $|N(u) \cap N(v)| \geq 2$ (car $\delta_G \geq n$), donc $d(u, v) = 2$.  
**Conclusion :** diamètre $\leq 2$.  

### Exercice 5

#### a) Graphes 2-réguliers et 3-réguliers

**Ordre 4 :**
- 2-régulier : Carré (4-cycle $C_4$)
- 3-régulier : $K_4$ (graphe complet)

**Ordre 5 :**
- 2-régulier : Pentagone (5-cycle $C_5$)
- 3-régulier : N'existe pas (somme des degrés impaire)

---

#### b) Conditions sur $k$ et $n$

**Parité :**  
$\sum \text{deg} = kn$ doit être pair ⇒ $k$ et $n$ pas tous deux impairs.

**Connexité si $n - 2k - 2 < 0$ :**  
Preuve par l'absurde : si non connexe, une composante aurait $\leq k+1$ sommets ⇒ impossible car degré minimal $k$.

---

#### c) Complément d'un graphe régulier

**Preuve :**  
Si $G$ est $k$-régulier d'ordre $n$, chaque sommet de $\overline{G}$ a degré $(n-1) - k$ ⇒ $\overline{G}$ est $(n-k-1)$-régulier.

---

#### d) Graphe complémentaire $\overline{G}$

**Données :**  
$G$ 5-régulier d'ordre 12.

**Propriétés de $\overline{G}$ :**  
- Ordre : 12 (inchangé)
- Degré : $12 - 1 - 5 = 6$ ⇒ 6-régulier
- Taille : $\frac{12 \times 6}{2} = 36$ arêtes

