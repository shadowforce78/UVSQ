
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

<code>SELECT numC, numeroClient FROM COMPTE WHERE solde BETWEEN '600' AND '4000'</code>

