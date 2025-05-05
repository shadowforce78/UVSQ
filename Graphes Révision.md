# Fiche de Révision : Théorie des Graphes

---

## 1. Définitions de Base
- **Graphe** : Objet mathématique modélisant des relations entre éléments.
  - **Graphe orienté** : $D = (V, A)$ où $V$ = sommets, $A \subseteq V \times V$ = arcs.  
    *Exemple* : Réseau routier à sens unique.
  - **Graphe non orienté** : $G = (V, E)$ où $E$ = arêtes (paires non ordonnées).  
    *Exemple* : Réseau social (amis mutuels).

- **Ordre** : Nombre de sommets ($|V|$).
- **Taille** : Nombre d'arêtes/arcs ($|E|$ ou $|A|$).

---

## 2. Vocabulaire et Propriétés
- **Degré d'un sommet** :
  - **Non orienté** : Nombre d'arêtes incidentes ($\delta(v)$).  
    *Théorème* : $\sum \delta(v) = 2|E|$.
  - **Orienté** :
    - Degré entrant ($\delta^-(v)$).
    - Degré sortant ($\delta^+(v)$).

- **Voisinage** :
  - $N_G(v)$ = sommets adjacents à $v$.
  - Pour un graphe orienté :
    - Voisins sortants ($N^+(v)$).
    - Voisins entrants ($N^-(v)$).

---

## 3. Types de Graphes Classiques
- **Graphe complet $K_n$** : Tous les sommets sont reliés.
  - Taille : $\frac{n(n-1)}{2}$.
- **Cycle $C_n$** : Chaîne fermée sans répétition.
  - Degré constant = 2.
- **Arbre** : Graphe connexe sans cycle, taille = $n-1$.
- **Biparti complet $K_{p,q}$** : Deux ensembles de sommets, toutes les arêtes entre eux.

*Exemple* :
- $K_3$ (triangle) : 3 sommets, 3 arêtes.
- $C_4$ (carré) : 4 sommets, 4 arêtes.

---

## 4. Connexité
- **Non orienté** :
  - **Connexe** : Chemin entre toute paire de sommets.
  - **Composante connexe** : Sous-graphe connexe maximal.
- **Orienté** :
  - **Fortement connexe** : Chemins dans les deux sens entre toute paire.
  - **Composante fortement connexe (CFC)** : Sous-graphe maximal fortement connexe.

*Exemple* :
- Graphe non connexe : Deux triangles disjoints.
- Graphe fortement connexe : Cycle orienté.

---

## 5. Chaînes, Cycles, Chemins, Circuits
- **Chaîne** (non orienté) : Suite d'arêtes consécutives.
  - **Élémentaire** : Pas de sommet répété.
- **Cycle** : Chaîne fermée ($v_0 = v_k$).
- **Chemin** (orienté) : Suite d'arcs consécutifs.
- **Circuit** : Chemin fermé.

*Exemple* :
- Chaîne : $a-b-c-d$.
- Circuit : $a \to b \to c \to a$.

---

## 6. Parcours dans les Graphes
- **Parcours en largeur (BFS)** :
  - Utilise une file, calcule les distances depuis un sommet.
  - *Application* : Plus court chemin dans un graphe non pondéré.
- **Parcours en profondeur (DFS)** :
  - Utilise une pile, détection de cycles.

*Algorithme BFS* :
1. Initialiser une file avec le sommet de départ.
2. Marquer les sommets visités.
3. Pour chaque voisin, mettre à jour la distance.

---

## 7. Graphes Eulériens et Hamiltoniens
- **Eulérien** : Cycle passant par chaque arête une fois.
  - *Condition* : Tous les degrés pairs et graphe connexe.
- **Hamiltonien** : Cycle passant par chaque sommet une fois.
  - *Condition* : Aucune condition simple connue.

*Exemple* :
- Eulérien : Cycle $C_n$.
- Non eulérien : Graphe avec un sommet de degré impair.

---

## 8. Algorithmes et Applications
- **Tri topologique** : Ordonnancement de tâches (graphe sans circuit).
  - *Exemple* : $T_5 \to T_6 \to T_2 \to \dots$ (cf. TD4).
- **Graphes de précédence** : Modélisation de dépendances.

---

## 9. Exercices Types
1. **Calculer ordre/taille/degres** :
   - *Exemple* : Graphe $G = (V, E)$ avec $V = \{a, b, c\}$, $E = \{ab, bc\}$.
     - Ordre = 3, Taille = 2, $\delta(a)=1$, $\delta(b)=2$, $\delta(c)=1$.

2. **Détecter une CFC** :
   - Identifier les sommets mutuellement accessibles.

3. **Vérifier si eulérien** :
   - Compter les degrés et vérifier la connexité.

---

## 10. Formules Utiles
- Nombre maximal d'arêtes :
  - Non orienté : $\frac{n(n-1)}{2}$.
  - Orienté : $n(n-1)$.
- Somme des degrés :
  - Non orienté : $2|E|$.
  - Orienté : $\sum \delta^+(v) = \sum \delta^-(v) = |A|$.

---

### À Retenir
- Un graphe est un outil puissant pour modéliser des relations.
- La connexité et les parcours (BFS/DFS) sont fondamentaux.
- Les conditions pour les cycles eulériens/hamiltoniens sont classiques en examen.
