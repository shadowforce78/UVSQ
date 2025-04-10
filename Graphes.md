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

### Exercice 6

![[Drawing 2025-04-02 14.04.12.excalidraw]]
### Exercice 7 :  
Graphe orienté $D = (V, A)$ avec $V = [0 ; 99]$ et pour $v, w$ distincts :  
$$ vw \in A \iff (w \equiv v + 10 \mod 100 \quad \text{ou} \quad w = v^2 + 1) $$  

**Analyse :**  
- **Arcs $w \equiv v + 10 \mod 100$** : Crée 10 cycles de longueur 10 (e.g., $0 \rightarrow 10 \rightarrow \dots \rightarrow 90 \rightarrow 0$).  
- **Arcs $w = v^2 + 1$** : Liens non linéaires dépendants de $v^2$. Par exemple, $0 \rightarrow 1$, $1 \rightarrow 2$, $2 \rightarrow 5$, etc.  

**Structure :** Combinaison de cycles (première règle) et d'arbres/chaînes (deuxième règle).  

---

### Exercice 8 :  
Graphe non orienté où chaque sommet est de degré 2.  

**Composantes connexes :**  
- Chaque composante est un **cycle** (simple ou multiple).  
- Raison : Un graphe 2-régulier est une union disjointe de cycles.  

**Exemple :**  
- Un triangle ($C_3$), un carré ($C_4$), etc., ou plusieurs cycles disjoints.  

---

### Exercice 9 :  
Soit $G = (V, E)$ et $\bar{G} = (V, \bar{E})$ son complémentaire.  

1. **$G$ connexe $\Rightarrow$ $\bar{G}$ non connexe ?**  
   - **Non.** Contre-exemple : $G = P_3$ (chemin à 3 sommets).  
     - $\bar{G}$ est connexe (sommet central relié aux autres).  
   - **Cas particulier :** Si $G$ est complet ($K_n$), $\bar{G}$ est vide (non connexe pour $n \geq 2$).  

2. **$G$ non connexe $\Rightarrow$ $\bar{G}$ connexe ?**  
   - **Oui**, sauf si $G$ est une union disjointe de deux cliques complètes.  
   - **Preuve :** Soit $G$ non connexe avec composantes $C_1, C_2, \dots$. Pour $u \in C_1$, $v \in C_2$, l'arête $uv \notin E$ donc $uv \in \bar{E}$. Ainsi, $\bar{G}$ relie toutes les composantes.  
   - **Exception :** $G = K_n \sqcup K_m$ (alors $\bar{G}$ est deux cliques disjointes).  

**Conclusion :**  
- $G$ connexe $\nRightarrow$ $\bar{G}$ non connexe.  
- $G$ non connexe $\Rightarrow$ $\bar{G}$ connexe (sauf cas spécifique).  

# TD 4

## Exercice 6

#### **Graphe de précédence :**
- **Sommets** : \( T_1 \) à \( T_8 \).
- **Arcs** (contraintes) :
  - \( T_5 \to T_2 \), \( T_5 \to T_6 \), \( T_5 \to T_4 \), \( T_5 \to T_8 \),
  - \( T_6 \to T_1 \), \( T_6 \to T_4 \),
  - \( T_8 \to T_1 \),
  - \( T_2 \to T_3 \), \( T_4 \to T_3 \), \( T_4 \to T_8 \),
  - \( T_1 \to T_7 \).

#### **Ordre topologique possible :**
1. **Sources initiales** : \( T_5 \) (seule tâche sans prédécesseur).
2. **Étapes** :
   - Retirer \( T_5 \) → nouvelles sources : \( T_6 \), \( T_2 \), \( T_4 \), \( T_8 \).
   - Retirer \( T_6 \) → nouvelles sources : \( T_2 \), \( T_4 \), \( T_8 \).
   - Retirer \( T_2 \) → \( T_4 \), \( T_8 \) restent.
   - Retirer \( T_4 \) → \( T_8 \), \( T_3 \) deviennent sources.
   - Retirer \( T_8 \) → \( T_1 \), \( T_3 \) restent.
   - Retirer \( T_1 \) → \( T_3 \), \( T_7 \) restent.
   - Retirer \( T_3 \), puis \( T_7 \).

#### **Solution :**
Un ordre valide est :  
**\( T_5, T_6, T_2, T_4, T_8, T_1, T_3, T_7 \)**.  

**Validation** : Toutes les contraintes sont respectées (ex: \( T_5 \) avant \( T_6 \), \( T_6 \) avant \( T_1 \), etc.).


![[Drawing 2025-04-10 14.51.29.excalidraw]]

## *Diagramme de Hasse*

![[Drawing 2025-04-10 15.17.26.excalidraw]] 