
### **1. Calcul des clés minimales (candidates) de R(ABCDE) avec F = {A → BC, CD → E, B → D, E → A}**

**Méthode :**  
Pour trouver les clés candidates, on cherche les ensembles minimaux d'attributs $( K )$ tels que $( K^+ = ABCDE )$.

1. **Calcul des fermetures :**
   - $( A^+ = A )$ → $( A → BC )$ ⇒ $( A^+ = ABC )$ → $( B → D )$ ⇒ $( A^+ = ABCD )$ → $( CD → E )$ ⇒ $( A^+ = ABCDE )$ ⇒ **A est une clé candidate**.
   - \( E^+ = E \) → \( E → A \) ⇒ \( E^+ = A^+ = ABCDE \) ⇒ **E est une clé candidate**.
   - \( CD^+ = CD \) → \( CD → E \) ⇒ \( CD^+ = CDE \) → \( E → A \) ⇒ \( CD^+ = ACDE \) → \( A → BC \) ⇒ \( CD^+ = ABCDE \) ⇒ **CD est une clé candidate**.
   - Test d'autres combinaisons (B, C, D, etc.) :
     - \( B^+ = B \) → \( B → D \) ⇒ \( B^+ = BD \) (ne couvre pas tout).
     - \( C^+ = C \) (ne couvre rien).
     - \( D^+ = D \) (ne couvre rien).
     - Aucune autre combinaison minimale ne ferme \( ABCDE \).

**Clés candidates :**  
✅ \( A \), \( E \), \( CD \).

---

### **2. Décomposition en R1(ABC) et R2(ADE) est-elle sans perte d’information (SPI) ?**

**Critère SPI :**  
Une décomposition $( {R_1, R_2} )$ est SPI si $( R_1 \cap R_2 \rightarrow R_1 )$ ou $( R_1 \cap R_2 \rightarrow R_2 )$.

- $( R_1 = ABC )$, $( R_2 = ADE )$.
- $( R_1 \cap R_2 = A )$.

On sait que $( A \rightarrow ABC )$ (car $( A \rightarrow BC \in F )$), donc $( R_1 \cap R_2 \rightarrow R_1 )$.  
**Conclusion :** La décomposition est SPI.

---

### **3. Cette décomposition est-elle sans perte de dépendances (SPD) ?**

**Définition :**  
Une décomposition est SPD si la fermeture des DF projetées sur $( R_1)$ et $( R_2 )$ est équivalente à $( F^+ )$.

- **Projection sur \( R_1(ABC) \) :**
  - $( F[ABC] = {A \rightarrow BC, B \rightarrow D})$ (mais $( D \notin ABC)$, donc seule $( A \rightarrow BC )$ est conservée).
- **Projection sur $( R_2(ADE) )$ :**
  - $( F[ADE] = \{E \rightarrow A, A \rightarrow BC\} )$ (mais $( B, C \notin ADE )$, donc seule $( E \rightarrow A )$ est conservée).

**Problème :**  
- La DF $( CD \rightarrow E )$ est perdue (car $( CD )$ n'est pas incluse dans $( R_1 )$ ou $( R_2 )$).
- La DF $( B \rightarrow D )$ est perdue (car $( B )$ n'est pas dans $( R_2 )$).

**Conclusion :** La décomposition n'est pas SPD.

---

### **4. Contre-exemple pour la décomposition en R1(ABC) et R2(CDE) (non SPI)**

**Construction d'une instance \( r \) où la jointure crée des tuples fantômes :**

| A | B | C | D | E |
|---|---|---|---|---|
| a1| b1| c1| d1| e1| (original)
| a2| b2| c1| d2| e2| (original)

- **Projection sur \( R1(ABC) \):**
  - (a1, b1, c1)
  - (a2, b2, c1)
- **Projection sur \( R2(CDE) \):**
  - (c1, d1, e1)
  - (c1, d2, e2)

**Jointure naturelle :**  
- Combine (a1, b1, c1) avec (c1, d1, e1) → (a1, b1, c1, d1, e1) (correct).
- Combine (a1, b1, c1) avec (c1, d2, e2) → (a1, b1, c1, d2, e2) (**fantôme**).
- Combine (a2, b2, c1) avec (c1, d1, e1) → (a2, b2, c1, d1, e1) (**fantôme**).
- Combine (a2, b2, c1) avec (c1, d2, e2) → (a2, b2, c1, d2, e2) (correct).

**Résultat :**  
La jointure produit 4 tuples alors que \( r \) en avait 2 ⇒ **La décomposition n'est pas SPI**.

---

### **5. Preuve par l'algorithme de poursuite (Chase) que R1(ABC) et R2(CDE) n'est pas SPI**

**Principe :**  
On construit un tableau avec des variables distinctes pour les attributs non partagés et des symboles communs pour \( R_1 \cap R_2 \).

- **Attributs partagés :** \( C \).
- **Tableau initial :**

| A | B | C | D | E |
|---|---|---|---|---|
| a | b | c | d1| e1| (R1)
| a2| b2| c | d | e | (R2)

**Application des DF :**
1. \( A \rightarrow BC \) : Inapplicable (pas de conflit sur \( A \)).
2. \( CD \rightarrow E \) : Sur la 2ème ligne, \( C = c \), \( D = d \). Si \( CD \rightarrow E \), alors \( E \) doit être égal dans les deux lignes ⇒ **Échec** (pas de modification possible).

**Conclusion :**  
Le tableau final contient des symboles distincts ⇒ **La décomposition n'est pas SPI**.

---

### **6. Décomposition en 3NF, SPI et SPD**

**Méthode :**  
Utilisation de l'algorithme de synthèse (Bernstein) :
1. **Couverture minimale de \( F \) :**  
   - \( A \rightarrow B \), \( A \rightarrow C \), \( CD \rightarrow E \), \( B \rightarrow D \), \( E \rightarrow A \).
2. **Regroupement par DF :**  
   - \( R1(AB) \) (pour \( A \rightarrow B \)),  
   - \( R2(AC) \) (pour \( A \rightarrow C \)),  
   - \( R3(CDE) \) (pour \( CD \rightarrow E \)),  
   - \( R4(BD) \) (pour \( B \rightarrow D \)),  
   - \( R5(EA) \) (pour \( E \rightarrow A \)).  
3. **Élimination des redondances :**  
   - \( R1(ABC) \) (fusion de \( R1 \) et \( R2 \)),  
   - \( R3(CDE) \),  
   - \( R4(BD) \),  
   - \( R5(EA) \).  
4. **Ajout d'une clé candidate si nécessaire :**  
   - \( CD \) est déjà incluse dans \( R3 \).

**Décomposition finale :**  
✅ \( R1(ABC) \), \( R2(CDE) \), \( R3(BD) \), \( R4(EA) \).  
- **SPI** : Car couverture complète et préservation des DF.  
- **3NF** : Toutes les DF sont préservées et aucun attribut non-prime ne dépend transitivement d'une clé.

---

### **7. Décomposition en FNBC et SPI (2 relations)**

**Stratégie :**  
Choisir une clé candidate comme point de départ.  
- **Clé candidate :** \( A \).  
- **Dépendances violant la FNBC :**  
  - \( B \rightarrow D \) (car \( B \) n'est pas une super-clé).

**Décomposition :**  
1. \( R1(BD) \) (pour \( B \rightarrow D \)),  
2. \( R2(ABCE) \) (reste de la relation).  

**Vérification :**  
- \( R1(BD) \) est en FNBC (car \( B \rightarrow D \) avec \( B \) comme clé).  
- \( R2(ABCE) \) :  
  - \( A \rightarrow BCE \), \( E \rightarrow A \), \( CD \rightarrow E \) (mais \( C \) n'est pas seul).  
  - Nouvelle violation : \( CD \rightarrow E \) ⇒ Décomposer en \( R3(CDE) \) et \( R4(ABC) \).  

**Décomposition finale en 2 relations FNBC et SPI :**  
✅ \( R1(ABCE) \) et \( R2(BD) \) (mais cela ne préserve pas toutes les DF).  
**Alternative :**  
✅ \( R1(ABCD) \) et \( R2(ADE) \) (en utilisant \( A \) comme pivot).  

**Conclusion :**  
Une décomposition en 2 relations FNBC et SPI est difficile sans perdre des DF. Une solution possible est :  
- \( R1(ABC) \) (avec \( A \rightarrow BC \)),  
- \( R2(ADE) \) (avec \( E \rightarrow A \)),  
mais \( CD \rightarrow E \) est perdue. **Aucune décomposition en 2 relations ne préserve toutes les DF tout en étant FNBC et SPI.**  

--- 

### **Synthèse des réponses**
1. **Clés candidates :** \( A \), \( E \), \( CD \).  
2. **Décomposition \( \{ABC, ADE\} \) est SPI.**  
3. **Elle n'est pas SPD** (perte de \( CD \rightarrow E \) et \( B \rightarrow D \)).  
4. **Contre-exemple pour \( \{ABC, CDE\} \) :** Jointure crée des tuples fantômes.  
5. **Algorithme de poursuite confirme que \( \{ABC, CDE\} \) n'est pas SPI.**  
6. **Décomposition 3NF SPI et SPD :** \( \{ABC, CDE, BD, EA\} \).  
7. **Décomposition FNBC en 2 relations :** \( \{ABC, ADE\} \) est SPI mais pas SPD. Aucune solution en 2 relations ne satisfait FNBC + SPD.  
