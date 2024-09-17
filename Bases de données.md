
Caractéristiques générales : 
	Un ensemble de donnée représentant une partie du monde réel, stocké, pouvant être interrogé et mis a jour, servant de support pour des applications

Un fichier texte peut par exemple servir de base de données
Il faut que le format soit connu défini par des Meta données (Dans un tableau ou chaque colonne a un nom)
Il faut que toutes les modifications doivent être faites avec un SGBD (système de gestion de base de données) : 
	- Oracle
	- SQL Server
	- MySQL
	- PostfreSQL
	- MongoDB
	- Etc...
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
	Un ensemble de logiciels système qui permet de :
		- Mettre en forme
		- Sauvegarder
		- Mettre a jour
		- Rechercher
	Efficacement dans une grande masse d'informations et entre plusieurs utilisateurs

Les données sont stockés dans des tableaux, ces tableau communique entre eux avec une valeur commune:

		Client : NumeroClient, Nom, Prenom, DateDeNaissance
		Compte : NumeroCompte, Solde, Type, NumeroClient
		
	NumeroClient, fait communiquer les deux tables

On utilise un schéma d'arbre binaire pour retrouver les données (gauche plus petit, droite plus grand) 
	Schéma1

L'accès se fait de différente manière, utilisateur ou administrateur, donc toutes les valeurs ne sont pas visible pour tous le monde (privilèges)

Création d'une interface/applications pour y intégrer notre SGBD


Fonctionnalités d'un SGBD
	- Gestion de données persistantes
	- Gestion de grandes quantités de données
	- Fiabilité des données
		- Cohérence et contraintes d'intégrité
		- Sureté du fonctionnement
			- Notion de transaction atomique
			- Techniques de sauvegarde et/ou journalisation
			- Procédure de reprise sur panne
		-Sécurité d'accès
			- Commandes d'autorisation
		-Partage et accès concurrents
			- Techniques de verrouillage
		-Interrogation : langage de requêtes
			- Déclaratifs et incomplet
			- Intégrations
			- Dysfonctionnements

Vision globale d'un BDD

	Schéma 2

Niveau conceptuel
	- Modèle hiérarchique (Structure de l'arbre, une valeur parent et plusieurs valeurs enfant)
	- Modèle réseau (Graphe orienté)
	- Modèle relationnel (Relation entre valeur dans des tableaux)

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

pour afficher un tableau complet on va exécuter : <code SQL> SELECT * FROM client </code>

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

1) Donner les numéros de comptes du client 2

<code>SELECT numC FROM COMPTE WHERE numeroClient=2 </code>

2) Donner les numéros des clients ayant un compte avec plus 1500€

<code>SELECT numeroClient FROM COMPTE WHERE solde > '1500'</code>

3) Donner les numéros de comptes et le client dont le solde est entre 600 et 4000€

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

Un relation r sur R est un ensemble de n-uplets sur R
	- R est appelé schéma de R, et noté sch(r)
	Exemple :
		t<sub>1</sub>(num) = 1                       t<sub>2</sub>(num)=2
		t<sub>1</sub>(nom)='Dupont'             t<sub>2</sub>(nom)='Durand'
		t<sub>2</sub>(prenom)='Jean'             t<sub>2</sub>(prenom)='Jacques'

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

Deux type de langages :
	- Langage fondé sur l'algèbre relationnelle
		- impératifs
	- Langage fondés sur le calcul relationnel
		- déclaratifs

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

A|B|C|D
-|---|---|---
1|1|3|3
1|1|4|4
2|2|3|3
2|2|4|4


- Renommage :
	changer le nom d'une table, d'une colonne