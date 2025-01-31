Cours basé sur ce [livre](https://www.google.fr/books/edition/L_essentiel_de_la_gestion_de_projet_2013/9rK-wAEACAAJ?hl=fr) 

Dans un WBS : Je vérifie bien que : 
	Au dernier niveau de l'arbre il n'y que des taches a l'infinitif (actions direct)
	Il y a une arborescence type "gestion de Projet"
	Mes types d'arborescence sont corrects (Idée relié a un parent, pas entre elle)


Exemple : ![[Voyage Pédagogique.png]] 
### Diagramme d'ordonnancement

- Les activités figurent en rectangles
- Les flèches représentent les liens
- Les ronds représentent des jalons = activité a durée nulle 

![[Drawing 2025-01-31 10.34.51.excalidraw]]

Les liens entre les taches représentent des contraintes 

## Exemple :


|            | Taches | Il faut avoir terminé | Durée en jours | Niveau |
| ---------- | ------ | --------------------- | -------------- | ------ |
| Pour faire | A      |                       | 3              | 1      |
|            | B      |                       | 12             | 1      |
|            | C      | A,B                   | 1              | 2      |
|            | D      | B                     | 6              | 2      |
|            | E      | C                     | 7              | 3      |
|            | F      | C,D                   | 3              | 3      |
|            | G      | F                     | 3              | 4      |

1) Construite le graphique d'ordonnancement 

![[Drawing 2025-01-31 10.37.53.excalidraw]]

2) Calculez pour chaque activité et pour le projet la date de début et de fin au plus tôt 
	1) Durée max (au plus tôt du projet) = 24 jours


Notion de marge et de tâches critiques :

Tache C : Peut être réalisée le jour 13,14,15,16,17 sans remettre en cause la durée minimale du projet 
	Le chef du projet a de la marge sur cette tâche, marge = 4 jours :
	(marge = 17_13j)

Tache E : Peut être réalisée le jour 14 au jour 18 
	marge = 18 - 14 ou 24-20 = 4 jours de marge

Tache F : Doit impérativement être réalisée le jour 19
	Pas de marge pour cette tâche = tâche critique (tâche qui retarde le jour max de fin)

Autres taches critique : B -> D -> F -> G = Chemin critique


## Exemple 2


| Nom des tâches                | Durée heures | Antécédents  | Niveau |
| ----------------------------- | ------------ | ------------ | ------ |
| T1 : Désinstaller ordinateurs | 3            |              | 1      |
| T2 : Déposer ancien vidéo     | 2            | T1           | 2      |
| T3 : Enlever le mobiler       | 5            | T1           | 2      |
| T4 : Déposer le tableau       | 3            | T1           | 2      |
| T5 : Peindre les murs         | 10           | T1;T3;T4     | 3      |
| T6 : Installer les bureaux    | 3            | T5           | 4      |
| T7 : Faire câblage            | 6            | T1;T6;T2;T11 | 5      |
| T8 : Installer vidéo          | 3            | T7           | 6      |
| T9 : Installer ordinateurs    | 8            | T7           | 6      |
| T10 : Installer tableaux      | 2            | T7           | 6      |
| T11 : Changement luminaire    | 4            | T2           | 3      |
![[Drawing 2025-01-31 11.26.42.excalidraw]] 
Chemin critique = T1 -> T3 -> T5 -> T6 -> T7 -> T9