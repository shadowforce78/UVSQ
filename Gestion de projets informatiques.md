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

## Exemple 3

| Taches                                      | Durée en jours | Prédécesseurs | Niveau |
| ------------------------------------------- | -------------- | ------------- | ------ |
| A - Acceptation des plans                   | 4              |               | 1      |
| B - Préparation du terrain                  | 2              |               | 1      |
| C - Commande de matériaux                   | 1              | A             | 2      |
| D - Creusage des fondations                 | 1              | A,B           | 2      |
| E - Commande des portes et fenêtres         | 2              | A             | 2      |
| F - Livraison de matériaux                  | 2              | C             | 3      |
| G - Coulage des fondations                  | 2              | D,F           | 4      |
| H - Livraison des portes et fenêtres        | 10             | E             | 3      |
| I - Pose des murs, de la charpente, du toit | 4              | G             | 5      |
| J - Mise en place des portes et fenêtres    | 1              | H,I           | 6      |
![[Drawing 2025-02-03 11.26.56.excalidraw]]
Chemin critique : A -> E -> H -> J


# TD2

| A   |      | 1   | 1   |
| --- | ---- | --- | --- |
| B   | A    | 2   | 1   |
| C   | A    | 2   | 1   |
| D   | K, B | 3   | 1   |
| E   | C, B | 3   | 1   |
| F   | H    | 6   | 1   |
| G   | I    | 4   | 1   |
| H   | G    | 5   | 1   |
| I   | B, J | 3   | 1   |
| J   |      | 1   | 1   |
| K   | J    | 2   | 1   |
| L   | E, G | 5   | 1   |


![[Drawing 2025-02-10 11.24.38.excalidraw]]

# TD3

## App 1


| Taches | Prédécesseur | Durée (semaine) | Cout planifié (k€) |
| ------ | ------------ | --------------- | ------------------ |
| A      |              | 2               | 5                  |
| B      | A            | 6               | 12                 |
| C      | A            | 5               | 10                 |
| D      | C            | 3               | 9                  |
|        |              | Total :         | 36                 |

![[Drawing 2025-02-14 11.47.04.excalidraw]] 


| semaines     | 1    | 2   | 3   | 4    | 5    | 6   | 7   | 8   | 9   | 10  | $\sum$ Total (k€) |
| ------------ | ---- | --- | --- | ---- | ---- | --- | --- | --- | --- | --- | ----------------- |
| A            | 2.5  | 2.5 |     |      |      |     |     |     |     |     | 5                 |
| B            |      |     | 2   | 2    | 2    | 2   | 2   | 2   |     |     | 12                |
| C            |      |     | 2   | 2    | 2    | 2   | 2   |     |     |     | 10                |
| D            |      |     |     |      |      |     |     | 3   | 3   | 3   | 9                 |
| VP           | 2.5  | 5   | 9   | 13   | 17   | 21  | 25  | 30  | 33  | 36  | 36 = BAA          |
| CR           | 3    | 5   | 8   | 14   | 18   |     |     |     |     |     |                   |
| VA           | (1)  | (2) | (3) | (4)  | (5)  |     |     |     |     |     |                   |
| ED = VA - VP | -0.5 | 0   | +1  | +0.2 | -0.4 |     |     |     |     |     |                   |
| EC = VA - CR | -1   | 0   | +2  |      |      |     |     |     |     |     |                   |

(1) = 40% X 5 = 2 
(2) = 100% X 5 = 5
(3) = 100% X 5 + 25% X 12 + 20% X 10 = 5 + 3 + 2 = 10
(4) = 100% X 5 + 35% X 12 + 40% X 10 = 5 + 4.2 + 4 = 13.2
(5) = 100% X 5 + 55% X 12 + 50% X 10 = 5 + 6.6 + 5 = 16.6

BAA = Budget a l'achèvement (Planifié)
VP = Valeur planifié
ED = Ecart de délai
EC = Ecart de cout


| Tâche | Semaine        | 1        | 2         | 3        | 4        | 5        |
| ----- | -------------- | -------- | --------- | -------- | -------- | -------- |
| A     | Réel % achevée | 3<br>40% | 2<br>100% |          |          |          |
| B     | Réel % achevée |          |           | 1<br>25% | 4<br>35% | 2<br>55% |
| C     | Réel % achevée |          |           | 2<br>20% | 2<br>40% | 2<br>50% |

Finir semaine 5 : 
	J'ai prévu de dépenser 17k€ ($VP_5$)
	J'ai réellement dépensé 18k€ ($CR_5$) 
	Compte tenu du travail technique réellement effectué, j'aurais dû dépenser 16.6k€ ($VA_5$)
	