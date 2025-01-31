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