Voici une fiche de révision reprenant les points essentiels du document :

---

# Fiche de Révision : Statistiques Descriptives

## 1. Informations Pratiques
- **Durée du module :** 4 semaines  
- **Répartition horaire :**  
  - CM : 1h (3 à 4 séances)  
  - TD : 1h30 en doublé  
  - TP : 1h30 en salle machine (R)  
- **Évaluation :**  
  - 1 DS en fin de module  
  - Possiblement une participation de SAé

---

## 2. Statistiques Descriptives

### A. Histoire et Étymologie
- **Origine du terme :**  
  - Latin : *Status* (état)  
  - Italien : *Statistira* (vers 1700)  
  - Allemand : *Statistite* (vers 1750)  
  - Anglais : *Political Arithmetic* (vers 1750)

### B. Contexte et Représentations
- Le document mentionne des schémas/dessins illustrant certains concepts (par exemple, la répartition des effectifs ou le découpage en quartiles).

### C. Vocabulaire Fondamental
- **Population :** L’ensemble des événements ou individus étudiés.  
- **Individu :** Un membre de la population.  
- **Caractère (ou variable) :** Une caractéristique mesurée sur chaque individu.  
  - **Modalités :** Les différentes valeurs que peut prendre une variable.  
    - **Modalités discrètes** : (ex. x₁, x₂, x₃, …)  
    - **Modalités continues** : représentées par des intervalles (ex. [x₁, x₂[, [x₃, x₄[,…)

### D. Notations et Fréquences
- **Variables :** Souvent notées x, y, z.  
- **Modalités d’une variable :**  
  - On les note sous forme d’un vecteur : x = c(x₁, x₂, x₃, …)
- **Effectifs :**  
  - Pour chaque modalité xᵢ, on a un effectif nᵢ.
  - **Total des effectifs :** N = ∑₍ᵢ₌₁₎ᴾ nᵢ.
  - **Fréquence relative :** fᵢ = nᵢ/N, avec ∑₍ᵢ₌₁₎ᴾ fᵢ = 1.

### E. Indicateurs de Position
1. **Mode :**  
   - Valeur(s) de la variable ayant l’effectif le plus élevé.
2. **Médiane :**  
   - La valeur qui partage la distribution en deux parties égales.
   - Pour une série triée :  
     - Si N est pair :  
       m = (x[N/2] + x[N/2 + 1]) / 2  
     - Si N est impair :  
       m = x[(N + 1)/2]
3. **Moyenne arithmétique :**  
   - Formule :  
    $\bar{x} = \frac{1}{N}\sum_{i=1}^{P} n_i\,x_i$
   - **Propriété de linéarité :**  
     Pour y = a·x + b, on a  
     $\bar{y} = a\bar{x} + b$

### F. Indicateurs de Dispersion
1. **Étendue :**  
   - e = max(x) − min(x)
2. **Écart interquartile (IQR) :**  
   - Calculé à partir du 1er (Q₁) et du 3ème quartile (Q₃)  
   - IQR = Q₃ − Q₁
3. **Variance et Écart-type :**  
   - **Variance :**  
     $\text{var}(x) = \sigma^2_x = \frac{1}{N}\sum_{i=1}^{P} n_i\,(x_i-\bar{x})^2$ 
   - **Écart-type :**  
     $\sigma_x = \sqrt{\text{var}(x)}$
   - **Propriété alternative :**  
	   $\sigma^2_x = \frac{1}{N}\sum_{i=1}^{P} n_i\,x_i^2 - (\bar{x})^2$ 

---

## 3. Exemples et Exercices

### Exercice 1
- **Données :**  
  Une distribution avec 12 modalités, N = 50 individus (N pair).  
- **Calculs :**  
  - **Médiane :**  
    La 25ᵉ et 26ᵉ note sont utilisées :  
    $m = \frac{10 + 10}{2} = 10$
  - **Quartiles :**  
    - Q₁ = 8 (13ᵉ note)  
    - Q₃ = 12 (38ᵉ note)  
  - **Écart interquartile :**  
    IQR = 12 − 8 = 4

### Exercice 2
- **Données :**  
  Distribution avec 15 modalités, N = 60 individus (N pair).  
- **Calculs :**  
  - **Médiane :**  
    La 30ᵉ et 31ᵉ note :  
    $m = \frac{10 + 10}{2} = 10$
  - **Quartiles :**  
    - Q₁ = 8 (médiane de la première moitié, calculée sur la 15ᵉ et 16ᵉ note)  
    - Q₃ = 11,5 (médiane des notes 45ᵉ et 46ᵉ)
  - **Écart interquartile :**  
    IQR = 11,5 − 8 = 3,5

### Exercice 3
- (Les éléments de l'exercice 3 ne sont pas développés dans le document fourni.)

---

Cette fiche de révision reprend les concepts clés tels que présentés dans le document : notions de population, variables et modalités, calculs d’indicateurs de position (mode, médiane, moyenne) et de dispersion (étendue, IQR, variance, écart-type), ainsi que quelques exercices pratiques pour appliquer ces notions.  
N’hésitez pas à compléter par des schémas ou à refaire les calculs sur d’autres séries de données pour renforcer votre compréhension.