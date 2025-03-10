
---

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

|Variable|Notation|
|---|---|
|Caractère|xx|
|Modalités|x1,x2,…x_1, x_2, \dots|
|Effectifs|n1,n2,…n_1, n_2, \dots|
|Effectif total|N=∑niN = \sum n_i|
|Fréquence|fi=niNf_i = \frac{n_i}{N}|

### **3. Indicateurs de Position**

- **Mode** : Valeur la plus fréquente.
- **Médiane** : Valeur séparant la population en deux groupes égaux.
    - Si NN impair : m=xN+12m = x_{\frac{N+1}{2}}.
    - Si NN pair : m=xN2+xN2+12m = \frac{x_{\frac{N}{2}} + x_{\frac{N}{2}+1}}{2}.
- **Moyenne** : xˉ=1N∑nixi\bar{x} = \frac{1}{N} \sum n_i x_i.

### **4. Indicateurs de Dispersion**

- **Étendue** : e=max⁡(x)−min⁡(x)e = \max(x) - \min(x).
- **Écart interquartile** : Q3−Q1Q_3 - Q_1.
- **Variance** : σ2=1N∑ni(xi−xˉ)2\sigma^2 = \frac{1}{N} \sum n_i (x_i - \bar{x})^2.
- **Écart-type** : σ=σ2\sigma = \sqrt{\sigma^2}.

---

## **II. Statistiques à Deux Variables**

### **1. Covariance et Corrélation**

- **Covariance** : cov(x,y)=1N∑(xi−xˉ)(yi−yˉ)cov(x, y) = \frac{1}{N} \sum (x_i - \bar{x}) (y_i - \bar{y})
- **Coefficient de corrélation** : r=cov(x,y)σxσy,−1≤r≤1r = \frac{cov(x, y)}{\sigma_x \sigma_y}, \quad -1 \leq r \leq 1
    - r>0r > 0 : Corrélation positive
    - r<0r < 0 : Corrélation négative
    - r=0r = 0 : Pas de corrélation

### **2. Droite de régression (Méthode des Moindres Carrés)**

Équation de la droite :

y=mx+py = m x + p

- **Pente** : m=∑(xi−xˉ)(yi−yˉ)∑(xi−xˉ)2m = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2}
- **Ordonnée à l'origine** : p=yˉ−mxˉp = \bar{y} - m \bar{x}

---

## **III. Formules Importantes**

- **Variance** : σ2=E(x2)−xˉ2\sigma^2 = E(x^2) - \bar{x}^2.
- **Moyenne harmonique** : H=N∑nixiH = \frac{N}{\sum \frac{n_i}{x_i}}
- **Covariance si y=ax+by = ax + b** : cov(x,y)=aσx2cov(x, y) = a \sigma_x^2
