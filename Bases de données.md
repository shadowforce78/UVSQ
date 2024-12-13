Caractéristiques générales :
Un ensemble de donnée représentant une partie du monde réel, stocké, pouvant être interrogé et mis a jour, servant de support pour des applications

Un fichier texte peut par exemple servir de base de données
Il faut que le format soit connu défini par des Meta données (Dans un tableau ou chaque colonne a un nom)
Il faut que toutes les modifications doivent être faites avec un SGBD (système de gestion de base de données) : - Oracle - SQL Server - MySQL - PostfreSQL - MongoDB - Etc...
Toutes les modifications sont contrôlé par des transactions (vérifier l'intégrité des données):

    	```
    	c1=input(print('Compte 1 (a débiter)'))
    	c2=input(print('Compte 2 (a créditer)'))
    	m=input(print('Montant a transferer'))

    	solde(c1)=solde(c1)-m
    	solde(c2)=solde(c2)+m
    	```

    Si il y a un pb, la donnée m peut etre perdu

Système de gestion de base de données (SGBD) :
Un ensemble de logiciels système qui permet de : - Mettre en forme - Sauvegarder - Mettre a jour - Rechercher
Efficacement dans une grande masse d'informations et entre plusieurs utilisateurs

Les données sont stockés dans des tableaux, ces tableau communique entre eux avec une valeur commune:

    	Client : NumeroClient, Nom, Prenom, DateDeNaissance
    	Compte : NumeroCompte, Solde, Type, NumeroClient

    NumeroClient, fait communiquer les deux tables

On utilise un schéma d'arbre binaire pour retrouver les données (gauche plus petit, droite plus grand)
Schéma1

L'accès se fait de différente manière, utilisateur ou administrateur, donc toutes les valeurs ne sont pas visible pour tous le monde (privilèges)

Création d'une interface/applications pour y intégrer notre SGBD

Fonctionnalités d'un SGBD - Gestion de données persistantes - Gestion de grandes quantités de données - Fiabilité des données - Cohérence et contraintes d'intégrité - Sureté du fonctionnement - Notion de transaction atomique - Techniques de sauvegarde et/ou journalisation - Procédure de reprise sur panne
-Sécurité d'accès - Commandes d'autorisation
-Partage et accès concurrents - Techniques de verrouillage
-Interrogation : langage de requêtes - Déclaratifs et incomplet - Intégrations - Dysfonctionnements

Vision globale d'un BDD

    Schéma 2

Niveau conceptuel - Modèle hiérarchique (Structure de l'arbre, une valeur parent et plusieurs valeurs enfant) - Modèle réseau (Graphe orienté) - Modèle relationnel (Relation entre valeur dans des tableaux)

    - Nouveaux modèles :
    	- Modèle orienté objets (fichier vidéo, audio, géographique...)

# Bases de données relationnelles

- toutes les données sont dans des tableaux

exemples :

client :

| numero | nom    | prenom | date     |
| ------ | ------ | ------ | -------- |
| 1      | Dupont | Jacqes | 01/01/01 |
| 2      | Durand | Jean   | 03/05/99 |
| 3      | Martin | Pierre | 07/12/02 |

client = nom du tableau
les colonnes sont appelés ATTRIBUTS
les lignes sont les données

nous utiliserons SQL (Sub Query Language)
langage de requêtes déclaratif, différent des langages impératifs (C, Python, Java...)

exemples :
si je cherche la date de naissance du client 2 :

<code SQL>SELECT 'date' FROM client WHERE 'numero'=2</code>

# Syntaxe partielle de l'interrogation

<code> SELECT </code> + le nom de la donnée que l'on veut afficher ou des calculs (`* pour toutes les colonnes`)
<code> FROM </code>+ le nom de la table
<code> WHERE </code>+ conditions filtrage pour retrouvé la donnée (`optionnel`)

pour afficher un tableau complet on va exécuter : <code SQL> SELECT \* FROM client </code>

pour les conditions du <code>WHERE</code>:

- comparaisons (=, <, >, =<, >=)
- combinaisons (<code>AND, OR, NOT</code>)

COMPTE

| numC | numeroClient | type | solde |
| ---- | ------------ | ---- | ----- |
| 142  | 2            | CC   | 800   |
| 533  | 1            | CC   | 500   |
| 244  | 2            | LA   | 10000 |
| 202  | 4            | LA   | 2000  |

1. Donner les numéros de comptes du client 2

<code>SELECT numC FROM COMPTE WHERE numeroClient=2 </code>

2. Donner les numéros des clients ayant un compte avec plus 1500€

<code>SELECT numeroClient FROM COMPTE WHERE solde > '1500'</code>

3. Donner les numéros de comptes et le client dont le solde est entre 600 et 4000€

```sql
SELECT numC, numeroClient FROM COMPTE WHERE solde BETWEEN '600' AND '4000'
```

# Comment créer une base de donnée conceptuelle ?

Définition :
Un ensemble d'attributs
Un ensemble de domaines (ou type, ou valeurs)
Un ensemble de nom de tables

Schéma de relation

Schéma de relation R : ensemble fini de la forme
R = {A<sub>1</sub>:dom(A<sub>1</sub>),...,A<sub>n</sub>:dom(A<sub>n</sub>)}
où A<sub>i</sub> est un attribut et dom(A<sub>i</sub>) le domaine de A<sub>i</sub> noté R={A<sub>1</sub>,.....,A<sub>n</sub>}
N-uplets et relation

Exemple :

```sql
	R = {num:integer;nom:varchar(20);prenom:varchar(30)}
```

Un n-uplet t sur R est une fonction qui associe à chaque attribut de A<sub>i</sub> de R une valeur de son domaine dom(A<sub>i</sub>)

Un relation r sur R est un ensemble de n-uplets sur R - R est appelé schéma de R, et noté sch(r)
Exemple :
t<sub>1</sub>(num) = 1 t<sub>2</sub>(num)=2
t<sub>1</sub>(nom)='Dupont' t<sub>2</sub>(nom)='Durand'
t<sub>2</sub>(prenom)='Jean' t<sub>2</sub>(prenom)='Jacques'

## Relation :

r<sub>1</sub>={t<sub>1</sub>,t<sub>2</sub>}
r<sub>1</sub>={
(1,'Dupont','Jean')
(2,'Durand','Jacques')
}

r<sub>2</sub>={t<sub>1</sub>}
r<sub>3</sub>={NULL}

Un schéma de base de données S est un ensemble fini de tables, où chaque table T est associée à un schéma de relation sch(T)
Un attribut peut appartenir a plusieurs tables
Plusieurs tables peuvent avoir le même schéma

```sql
S = {
		client(num:int;nom:varchar(20);prenom:varchar(30));
		compte(numcompte:int;type:varchar(10);solde:float;numclient:int);
	}
```

Soit S = {T1,....,Tn}. Une base de données $\delta$ sur S est une fonction qui associe à chaque table Ti une relation finie $\delta$(Ti) sur sch(Ti)

Exemple :

```sql
	$\delta$(client) = {(1,'Dupont','Jean';(2,'Durand','Jacques'))}
	$\delta$(compte) = {(42,'cc',380.20,1);(56,'LA',2000,2)}
```

client :

| num | nom    | prenom  |
| --- | ------ | ------- |
| 1   | Dupont | Jean    |
| 2   | Durand | Jacques |

compte :

| numcompte | type | solde  | numclient |
| --------- | :--: | :----: | --------- |
| 42        |  cc  | 380.20 | 1         |
| 56        |  la  |  2000  | 2         |

# 2. Mis a jour

- Insertion
- Modification
- Suppression
  d'un ou plusieurs n-uplets dans une relation donnée

> Pas de difficulté au niveau conceptuel

# 3. Consultation

Deux type de langages : - Langage fondé sur l'algèbre relationnelle - impératifs - Langage fondés sur le calcul relationnel - déclaratifs

Il existe 6 opérations :

- Union :
  argument : 2 relations r et s
  telles que sch(r)=sch(s)

  résultat : une relation r $\cup$ s telle que :
  sch(r $\cup$ s) = sch(r)
  r $\cup$ s = {t | t $\in$ r ou t $\in$ s}

- Différence :
  argument : 2 relations r et s
  telles que sch(r)=sch(s)

  résultat : une relation r - s telle que :
  sch(r-s)=sch(r)
  r-s = {t | t $\in$ r }

- Projection
  argument : une relation r et un ensemble d'attribut X tel que X $\subseteq$ sch(r)

  résultat : une relation $\pi$<sub>x</sub>(r) telle que:
  sch($\pi$<sub>x</sub>(r)) = X
  ou t(X) est la projection de t sur X

- Sélection :
  comparaison basé sur des égalités, on peut les combiner avec des conjonctions, (ou, ... et ....)
  (le WHERE en SQL)

- Produit :
  produit cartésien, il ne faut pas qu'il y est des lignes commun, toutes les lignes d'une table combinée a toutes les lignes d'une autre tables

| A   | B   |
| --- | --- |
| 1   | 1   |
| 2   | 2   |

| C   | D   |
| --- | --- |
| 3   | 3   |
| 4   | 4   |

r<sub>1</sub> X r<sub>2</sub>

| A   | B   | C   | D   |
| --- | --- | --- | --- |
| 1   | 1   | 3   | 3   |
| 1   | 1   | 4   | 4   |
| 2   | 2   | 3   | 3   |
| 2   | 2   | 4   | 4   |

- Renommage :
  changer le nom d'une table, d'une colonne

# Algèbre relationnelle

## 6 opérations,

<div id="symbole">les symboles</div>
Union : U
Différence : -
Projection : $\pi$
Sélection : $\sigma$ 
Produit : x
Renommage : $\rho$

Ensemble R

ABC = Schéma de relation
B, C ou D = attributs
l'ensemble est constitué de n-uplets

Ensemble R

| A   | B   | C   |
| --- | --- | --- |
| a   | b   | c   |
| a'  | b   | c   |
| a   | b'  | c   |

Ensemble A

| B   | C   | D   |
| --- | --- | --- |
| b   | c   | d   |
| b   | c'  | d'  |
| b'  | c'  | d'  |

$\pi$<sub>BC</sub>(r) =

| B     | C     |
| ----- | ----- |
| b     | c     |
| ~~b~~ | ~~c~~ |
| b'    | c     |

Projection sur BC de la relation r
On ne sélectionne que les lignes B et C

$\sigma$<sub>A=a'</sub>(r) =

| A   | B   | C   |
| --- | --- | --- |
| a'  | b   | c   |

Sélection dans r par rapport à A = a'
On en sélectionne que la ligne qui remplie la condition A = a'

^ = et
v = ou
\> = non

$\sigma$<sub>B=b ^ > D=d'</sub>(A) =

| B   | C   | D   |
| --- | --- | --- |
| b   | c   | d   |

Sélection dans A par rapport a B = b et D ne pas être égale a d'
On sélectionne la ligne qui remplie la condition B = b' et qui ne remplie pas D = d'

r U A = IMPOSSIBLE, car sch(r) != sch(A)

$\pi$<sub>BC</sub>(r) $\cup$ $\pi$<sub>BC</sub>(A) =

| B   | C   |
| --- | --- |
| b   | c   |
| b'  | c   |

| B   | C   |
| --- | --- |
| b   | c   |
| b   | c'  |
| b'  | c'  |

Donc :

| B   | C   |
| --- | --- |
| b   | c   |
| b'  | c   |
| b   | c'  |
| b'  | c'  |

$\pi$<sub>BC</sub>(r) - $\pi$<sub>BC</sub>(A) =

| B   | C   |
| --- | --- |
| b'  | c   |

# Produit cartésien :

$\mathbb{N}$² = $\mathbb{N}*\mathbb{N}$

$\rho$<sub>B->E</sub>(r) =

| A   | E   | C   |
| --- | --- | --- |
| a   | b   | c   |
| a'  | b   | c   |
| a   | b'  | c   |

$\rho$<sub>B->r.B(r) ET C->r.C(r)</sub> X $\rho$<sub>B->A.B(A) ET C->A.C(A)</sub>

| A   | r.B | r.C | A.B | A.C | D   |
| --- | --- | --- | --- | --- | --- |
| a   | b   | c   | b   | c   | d   |
| a   | b   | c   | b   | c'  | d'  |
| a   | b   | c   | b'  | c'  | d'  |
| a'  | b   | c   | b   | c   | d   |
| a'  | b   | c   | b   | c'  | d'  |
| a'  | b   | c   | b'  | c'  | d'  |
| a   | b'  | c   | b   | c   | d   |
| a   | b'  | c   | b   | c'  | d'  |
| a   | b'  | c   | b'  | c'  | d'  |

```sql
select ename from emp where job="manager"
```

$\pi$<sub>ename</sub>($\sigma$<sub>job="manager"</sub>(emp))

# Le langage SQL

    Mot clés -> en majuscule GRAS
    Paramètres -> entre chevrons (ex: <table>)
    Optionnel -> entre crochet (ex: [a])
    Alternatives de syntaxes -> entre accolades séparés de barres (ex: { a | b })

Exemple :

```sql
SELECT nom, prenom, note FROM Etudiant, Resultat WHERE note > 10 AND Etudiant.num=Resultat.num;
```

Etape 1 : produit des tables Etudiant et Résultat
Etape 2 : Filtrage des lignes (note > 10 et numéro étudiant = numéro résultat)
Etape 3 : On projette sur les colonnes du SELECT (nom, prénom, note)

# TD voir <a href="#symbole">symbole</a>

3 tables,
filme(titre, realisateur, acteur)
seance(numsalle, titre, horaires)
produit(titre, producteur)

1. Donner les titres des films réalisé par Coppola ?
   $\pi$<sub>titre</sub>($\sigma$<sub>realisateur='Coppola'</sub>(film))
2. Où peut-on voir le film 'le parrain' ?
   $\pi$<sub>numsalle</sub>($\sigma$<sub>titre='le parrain'</sub>(seance))

3. Où et a quelle heure peut-on voir le film 'le parrain' ?
   $\pi$<sub>numsalle, horaires</sub>($\sigma$<sub>titre='le parrain'</sub>(seance))

# Interrogation des données (syntaxe partielle)

```
SELECT <liste de colonnes dont on cherche la valeur>
FROM <liste de tables dans lesquelles on sélectionne ces colonnes>
[ WHERE <condition de sélection>]
```

Table Élève

| num | idcours | note |
| --- | ------- | ---- |
| 1   | BD      | 14   |
| 2   | BD      | 16   |
| 3   | BD      | 12   |
| 1   | Algo    | 10   |
| 2   | Algo    | 12   |
| 3   | Algo    | 8    |
| 1   | BDA     | 4    |
| 2   | BDA     | 8    |
| 3   | BDA     | 12   |

Table Cours

| idcours | nom | coef | prof |
| ------- | --- | ---- | ---- |
| BD      | n1  | 4    | YL   |
| Algo    | n2  | 3    | DA   |
| BDA     | n3  | 4    | YL   |

Quels sont les noms des cours de YL dont la moyenne est supérieure à 10 classés par ordre décroissant de la moyenne ?

```sql
SELECT nom as nomDuCours
FROM cours, eleve
WHERE cours.idcours = eleve.idcours AND prof = 'YL'
GROUP BY nom HAVING AVG(note) >= 10
ORDER BY AVG(note) DESC;
```

Donner les notes de l'élève 1 avec les noms et coef des cours

```sql
SELECT note, note, coef
FROM cours, eleve
WHERE eleve.idcours = cours.idcours AND num = 1;
```

Donner les noms des cours où il n'y a pas de note < 10

```sql
SELECT nom
FROM cours
WHERE idcours NOT IN (
	SELECT idcours
	FROM eleve
	WHERE note<10
)
```

```sql
SELECT nom
FROM cours
WHERE NOT EXISTS (
	SELECT *
	FROM eleve
	WHERE note < 10 AND cours.idcours = eleve.idcours
)
```

```sql
ETUDIANT(num;nom;prenom;fromation)
RESULTAT(num;idcours;note)
COURS(idcours;intitulé;ceof;responsable)
```

1. Donner les noms et prénoms des étudiants du BUT INFO
   select nom,prenom from etudiant where formation = "but info"
   $\pi_{\text{nom, prenom}} (\sigma_{\text{formation} = \text{"but info"}} (\text{etudiant}))$

2. Donner les noms, prenoms des etudiant de but info qui ont moins de 10 en BD (idcours)
   select nom, prenom from etudiant, resultat where note > 10 and idcours ="BD"
   $\pi_{\text{nom, prenom}} (\sigma_{\text{note} > 10 \land \text{idcours} = "BD"} (\text{etudiant} \times \text{resultat}))$

3. Donner les noms et prenom des étudiants de but info dont toutes les notes sont >= 10
   SELECT nom, prenom FROM ETUDIANT WHERE formation = 'but info' AND NOT EXISTS (SELECT \* FROM RESULTAT WHERE num = num AND note < 10)
   $\pi_{\text{nom, prenom}} \left( \sigma_{\text{formation} = \text{"but info"}} \left( \text{ETUDIANT} \right) \div \pi_{\text{idcours}} \left( \sigma_{\text{note} \geq 10} \left( \text{RESULTAT} \right) \right) \right)$

# 3 Conception de schéma de base de données

## Introduction à la conception

Le schéma change rarement
Importance du choix initial de regroupement des attributs
Respect de certains critères

Processus appelé conception de schéma
Description d'une d'application $\rightarrow$ un "bon" schéma

## Description d'une application

- Attributs : caractéristiques pertinentes des informations (nom, departement, numero....)
- Univers : ensemble des attributs
- Les liens sémantiques entre attributs, appelés dépendances de données
  - Décrivent des propriétés que doivent satisfaire les données
  - Imposent des restrictions sur les bases possibles
  - Peuvent être considérées comme des contraintes d'intégrité

## Description du processus

Définition de l'univers U
De l'ensembles des dépendances F
Décomposition successives de U par rapport a F
Un ou plusieurs schéma de BD
Décomposition de U : tout ensemble S = {R1,...,Rn} de schéma de relation tel que U <1<i<nRi = U
S est un schéma de base de données

# Conceptions Entités/Associations

## Entités : classe d'objets ou d'indications

    ex : client, produit, etudiant, cours etc...

## Associations : classe des liaisons entre les entités

    ex : client, commante, produit
    		(enités) <= Associations => (entités)

## Attributs : caractéristiques des entités ou associations

    ex : client : nom, prenom, adresse, tel, email, etc...
    		(entité) : (attributs)

## Clé d'une entités : un attributs (ou un ensemble d'attributs) qui permette d'identifier les objets de l'entité

    remarque : souvent on ajoute un attribut comme identifié, numéro ou code

## Cardinalité d'un couple Entité/Association

couple d'entité (x, y) tel que

- x est le nombre minimale d'utilisation de l'association pour chaque objet de l'entité
- y est le nombre maximale d'utilisation de l'association pour chaque objet de l'entité
  ex : client commente produit
  client <=> commente = (0, N)
  produit <=> commente = (0, N)

|  client  |                | produit   |
| :------: | :------------: | --------- |
| idclient | \<=commente=\> | idProduit |
|   nomC   |    dateComm    | nomP      |
| prenomC  |      text      | desc      |
|  emailC  |      note      | prix      |

client (0, 4)
produit (0, 4)
Modèle Conceptuel de Données (MCP)

### Exemple :

Exo 1 : On a des chefs cuisiniers dont on connais les infos (nom,prenom,adresse,telephone,restaurant) qui preparent des plats (nomPlat, naturePlat(entrée desert), originePlat, ingrédients(nom,quantité,nature,origine))
![[Exo1bd.svg]]

Exo 2 : Base de donnée de forum, catégorie, sous catégorie, utilisateurs, message, réponses, 
![[Exo2bd.svg]]

Exo 3 : Base de donnée d'une bibliothèque
![[Exo3bd.svg]]
![[basedonnée13-12-24]]
```sql
CREATE TABLE Utilisateurs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom_utilisateur VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    mot_de_passe VARCHAR(255) NOT NULL,
    date_inscription DATE NOT NULL
);

CREATE TABLE Groupes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    description TEXT,
    date_creation DATE NOT NULL
);

CREATE TABLE Messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    contenu TEXT NOT NULL,
    date_publication DATETIME NOT NULL,
    utilisateur_id INT NOT NULL,
    groupe_id INT NOT NULL,
    FOREIGN KEY (utilisateur_id) REFERENCES Utilisateurs(id) ON DELETE CASCADE,
    FOREIGN KEY (groupe_id) REFERENCES Groupes(id) ON DELETE CASCADE
);

CREATE TABLE Utilisateurs_Groupes (
    utilisateur_id INT NOT NULL,
    groupe_id INT NOT NULL,
    PRIMARY KEY (utilisateur_id, groupe_id),
    FOREIGN KEY (utilisateur_id) REFERENCES Utilisateurs(id) ON DELETE CASCADE,
    FOREIGN KEY (groupe_id) REFERENCES Groupes(id) ON DELETE CASCADE
);

-- Exemple d'ajout de rôles spécifiques (administrateur et modérateur)
CREATE TABLE Roles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom_role VARCHAR(20) NOT NULL
);

INSERT INTO Roles (nom_role) VALUES ('Administrateur'), ('Modérateur'), ('Utilisateur');

CREATE TABLE Utilisateurs_Roles (
    utilisateur_id INT NOT NULL,
    role_id INT NOT NULL,
    PRIMARY KEY (utilisateur_id, role_id),
    FOREIGN KEY (utilisateur_id) REFERENCES Utilisateurs(id) ON DELETE CASCADE,
    FOREIGN KEY (role_id) REFERENCES Roles(id) ON DELETE CASCADE
);```
