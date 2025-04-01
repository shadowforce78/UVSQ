# Résumé pour le DS de Graphes (R2.07)

---

## 📌 Sommaire
1. **Définitions de base**  
2. **Types de graphes**  
3. **Propriétés et théorèmes**  
4. **Exercices clés**  
5. **Concepts avancés**  
6. **Méthodes de preuve**  
7. **Exemples à retenir**  
8. **Astuces**  

---

## 1. 📚 Définitions de base
- **Graphe non orienté** : $G = (V, E)$  
  - $V$ : sommets, $E$ : arêtes (paires non ordonnées)  
- **Graphe orienté** : $D = (V, A)$  
  - $A$ : arcs (paires ordonnées)  
- **Degré d'un sommet** : Nombre d'arêtes incidentes  
  - En orienté : degré entrant ($deg⁻$) et sortant ($deg⁺$)  
- **Lemme des poignées de main** :  
  $$\sum_{v \in V} deg(v) = 2|E|$$  
  *Le nombre de sommets de degré impair est toujours pair*  

---

## 2. 🌐 Types de graphes
| Type                | Définition                                      | Exemple/Taille                          |     |     |     |                      |
| ------------------- | ----------------------------------------------- | --------------------------------------- | --- | --- | --- | -------------------- |
| **Complet $K_n$**   | Tous les sommets reliés                         | Taille : $\frac{n(n-1)}{2}$             |     |     |     |                      |
| **Biparti**         | $V = V_1 \cup V_2$, arêtes entre $V_1$ et $V_2$ | Graphe étoile, grille                   |     |     |     |                      |
| **Arbre**           | Connexe et sans cycle                           | $                                       | E   | =   | V   | - 1$                 |
| **Forêt**           | Union d'arbres                                  | $                                       | E   | =   | V   | - n$ (n composantes) |
| **Hypercube $H_n$** | Sommets = mots binaires de longueur $n$         | Arêtes entre mots à 1 bit de différence |     |     |     |                      |

---

## 3. 📏 Propriétés et théorèmes
- **Isomorphisme** : Bijection entre sommets préservant les arêtes  
- **Graphe complémentaire $\overline{G}$** :  
  - Mêmes sommets, arêtes inversées  
  - **Autocomplémentaire** : $G \simeq \overline{G}$  
    *Condition* : $|V| \equiv 0 \mod 4$ ou $1 \mod 4$  
- **Graphe de lignes $L(G)$** :  
  - Sommets = arêtes de $G$, adjacents si partagent un sommet dans $G$  
  - *Exemple* : $L(K_5) \simeq \overline{Peterson}$  

---

## 4. ✨ Exercices clés
### 🔹 Exercice 1 (TD2)  
*Problème* : 355 étudiants, chacun demande de l'aide à 5 autres. Montrer qu'un étudiant triche  
*Preuve* : Somme des degrés = $355 \times 5 = 1775$ (impair). Impossible (doit être pair)  

### 🔹 Exercice 4 (TD2)  
Montrer que $H_p$ est isomorphe à un sous-graphe de $H_q$ pour $p \leq q$  
*Idée* : Restreindre $H_q$ aux $p$ premières coordonnées  

### 🔹 Exercice 7 (TD2)  
*Théorème de Ramsey* : Tout graphe d'ordre $\geq 6$ contient un triangle ou un anti-triangle  

---

## 5. 🧠 Concepts avancés
- **Graphe cubique** : Tous les sommets de degré 3  
  - *Existe seulement si $|V|$ est pair*  
- **Théorème de Ramsey** :  
  - Dans un graphe suffisamment grand, présence forcée de sous-structures (cliques/stables)  

---

## 6. 🔍 Méthodes de preuve
- **Preuve par contradiction** :  
  - Ex : Un arbre ne peut avoir que des feuilles et degré 5 si $\sum deg(v) = 2|E|$  
- **Construction explicite** :  
  - Dessiner un graphe vérifiant des contraintes (ex : arbre avec 11 sommets)  

---

## 7. 🎯 Exemples à retenir
- **Graphe de Peterson** :  
  - 10 sommets, degré 3, régulier  
- **Hypercube $H_3$** :  
  - 8 sommets, 12 arêtes, degré 3  

---

## 8. 💡 Astuces
- **Isomorphismes** :  
  - Comparer les degrés, cycles, et voisinages  
- **Arbres** :  
  - Utiliser $|E| = |V| - 1$ et $\sum deg(v) = 2|V| - 2$  

---
