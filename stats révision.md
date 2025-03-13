# **Fiche de Révision - Statistiques** 📊  

## **I. Statistiques Descriptives**  

### **1. Définitions de base**  
- **Population** : Ensemble étudié.  
- **Individu** : Un élément de la population.  
- **Caractère** : Propriété mesurée sur un individu.  
  - **Quantitatif** : Nombre (ex : âge).  
  - **Qualitatif** : Catégorie (ex : couleur des yeux).  
  - **Discret** : Valeurs isolées (ex : nombre d’enfants).  
  - **Continu** : Intervalle de valeurs (ex : taille).  
- **Modalités** : Différentes valeurs possibles d’un caractère.  

### **2. Notations**  
| Variable       | Notation              |
| -------------- | --------------------- |
| Caractère      | $x$                   |
| Modalités      | $x_1, x_2, …$         |
| Effectifs      | $n_1, n_2, …$         |
| Effectif total | $N = \sum n_i$        |
| Fréquence      | $f_i = \frac{n_i}{N}$ |

### **3. Indicateurs de Position**  
- **Mode** : Valeur la plus fréquente.  
- **Médiane** : Valeur séparant la population en deux groupes égaux.  
  - Si $N$ impair : $m = x_{\frac{N+1}{2}}$.  
  - Si $N$ pair : $m = \frac{x_{\frac{N}{2}} + x_{\frac{N}{2}+1}}{2}$.  
- **Moyenne** :  
  $$\bar{x} = \frac{1}{N} \sum n_i x_i$$

### **4. Indicateurs de Dispersion**  
- **Étendue** : $e = \max(x) - \min(x)$.  
- **Écart interquartile** : $Q_3 - Q_1$.  
- **Variance** :  
  $$\sigma^2 = \frac{1}{N} \sum n_i (x_i - \bar{x})^2$$
- **Écart-type** :  
  $$\sigma = \sqrt{\sigma^2}$$

---

## **II. Statistiques à Deux Variables**  

### **1. Covariance et Corrélation**  
- **Covariance** :  
  $$cov(x, y) = \frac{1}{N} \sum (x_i - \bar{x}) (y_i - \bar{y})$$
- **Coefficient de corrélation** :  
  $$r = \frac{cov(x, y)}{\sigma_x \sigma_y}, \quad -1 \leq r \leq 1$$
  - $r > 0$ : Corrélation positive  
  - $r < 0$ : Corrélation négative  
  - $r = 0$ : Pas de corrélation  

### **2. Droite de régression (Méthode des Moindres Carrés)**  
Équation de la droite :  
  $$y = m x + p$$
- **Pente** :  
  $$m = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2}$$
- **Ordonnée à l'origine** :  
  $$p = \bar{y} - m \bar{x}$$

---

## **III. Formules Importantes**  
- **Variance** :  
  $$\sigma^2 = E(x^2) - \bar{x}^2$$
- **Moyenne harmonique** :  
  $$H = \frac{N}{\sum \frac{n_i}{x_i}}$$
- **Covariance si $y = ax + b$** :  
  $$cov(x, y) = a \sigma_x^2$$

