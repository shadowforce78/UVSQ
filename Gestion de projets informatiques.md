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


| semaines     | 1    | 2   | 3   | 4    | 5    | 6                   | 7   | 8   | 9   | 10  | $\sum$ Total (k€) |
| ------------ | ---- | --- | --- | ---- | ---- | ------------------- | --- | --- | --- | --- | ----------------- |
| A            | 2.5  | 2.5 |     |      |      |                     |     |     |     |     | 5                 |
| B            |      |     | 2   | 2    | 2    | 2                   | 2   | 2   |     |     | 12                |
| C            |      |     | 2   | 2    | 2    | 2                   | 2   |     |     |     | 10                |
| D            |      |     |     |      |      |                     |     | 3   | 3   | 3   | 9                 |
| VP           | 2.5  | 5   | 9   | 13   | 17   | 21                  | 25  | 30  | 33  | 36  | 36 = BAA          |
| CR           | 3    | 5   | 8   | 14   | 18   |                     |     |     |     |     |                   |
| VA           | (1)  | (2) | (3) | (4)  | (5)  |                     |     |     |     |     |                   |
| ED = VA - VP | -0.5 | 0   | +1  | +0.2 | -0.4 | <= retard           |     |     |     |     |                   |
| EC = VA - CR | -1   | 0   | +2  | -0.8 | -1.4 | <= sur-consommation |     |     |     |     |                   |



(1) = 40% X 5 = 2 
(2) = 100% X 5 = 5
(3) = 100% X 5 + 25% X 12 + 20% X 10 = 5 + 3 + 2 = 10
(4) = 100% X 5 + 35% X 12 + 40% X 10 = 5 + 4.2 + 4 = 13.2
(5) = 100% X 5 + 55% X 12 + 50% X 10 = 5 + 6.6 + 5 = 16.6

BAA = Budget a l'achèvement (Planifié)
VP = Valeur planifié
ED = Ecart de délai
EC = Ecart de cout

Finir semaine 5 : 
	J'ai prévu de dépenser 17k€ ($VP_5$)
	J'ai réellement dépensé 18k€ ($CR_5$) 
	Compte tenu du travail technique réellement effectué, j'aurais dû dépenser 16.6k€ ($VA_5$)
	

| Tâche | Semaine        | 1        | 2         | 3        | 4        | 5        |
| ----- | -------------- | -------- | --------- | -------- | -------- | -------- |
| A     | Réel % achevée | 3<br>40% | 2<br>100% |          |          |          |
| B     | Réel % achevée |          |           | 1<br>25% | 4<br>35% | 2<br>55% |
| C     | Réel % achevée |          |           | 2<br>20% | 2<br>40% | 2<br>50% |

Prévision pour la fin de projet en semaine 5 :
	$PAA_5$ = $CR_5$ + ($BAA-VA_5$) = 18 + (36-16.6) = 37.4k€
	Sans nouveau incident sur le projet, je prévois en semaine 5 de terminer le projet avec un budget de 37.4k€ au lieu de 36k€ (=BAA) doit un dépassement budgétaire de +1.4k€, soit $\dfrac{1.4}{36}=$ 3.9%



# Analyse des coûts d'un projet

IO = Investissement initial du projet (cout du projet)
FTi = Flux de trésorerie généré par le projet et en année (= gain net du projet) 
a = taux d'actualisation
N = durée de vie du projet
VAN = Valeur actualisé Nette

VAN = -IO + $\dfrac{FTi}{1+a}+\dfrac{FTi}{(1+a)^2}+\dfrac{FTi}{(1+a)^3} + .... + \dfrac{FTi}{(1+a)^N}$ 
VAN = -IO + $\sum^{N}_{i=1}\dfrac{FTi}{(1+a)^i}$ 

Si VAN > 0, le projet est rentable

DRCI = Délai de récupération des capitaux investis

DRCI entre année 1 et 2
	A la fin de l'année 1 => il manque 18000€ (-85000+67000)
	Durant l'année 2 => le projet rapport 67000€, soit $\dfrac{67000}{365}$€/jour 
	$\dfrac{18000}{67000/365}=98.06$ 
	DRCI = 1 an et 99 jours <= on arrondie au jour suivant

Limite de la formule du calcul de DRCI
	On peut remettre en cause : 
		L'hypothèse selon laquelle le projet rapport des gains 365jour par an
		L'hypothèse selon laquelle les projet rapport des montants identiques chaque jour
		Le fait que les données ne se soient pas actualisées

# TD4

ROI = $\dfrac{moy(Benefice \ \ 3 \ \ années)}{Cout\ \ Du \ \ Projet}$ %

VAN = $-IO + \sum^{N}_{i=1}\dfrac{FTi}{(1+a)^i}$ 

1) Investissement = IO = 985k€ en 2020 (On ne compte pas les maintenances annuelle)
2) Exploitation = 42k€
3) Economie :
	1) **2021** : 415 000 + 9000 = 424 000 €
	2) **2022 et 2023** : 415 000 + 8 000 = **423 000 €** 
4) 
- **2021** : 424 000 - 42 000 = **382 000 €**
- **2022** : 423 000 - 42 000 = **381 000 €**
- **2023** : 423 000 - 42 000 = **381 000 €**

5) 
Le **flux de trésorerie annuel** correspond aux gains nets générés chaque année, en tenant compte de l’investissement initial en 2020 (**-985 000 €**).

|                | 2020       | 2021      | 2022      | 2023      |
| -------------- | ---------  | --------- | --------- | --------- |
| **INVESTISSEMENT** |           |           |           |           |
| Salaire        | **-354 000** |           |           |           |
| Matériel       | **-89 000**  |           |           |           |
| Usine          | **-542 000** |           |           |           |
| **Total**      | **-985 000** |           |           |           |
| **EXPLOITATION** |           |           |           |           |
| Maintenance    |             | **-42 000** | **-42 000** | **-42 000** |
| Éco personnel  |             | **+415 000** | **+415 000** | **+415 000** |
| Éco matériel   |             | **+9 000**  | **+8 000**  | **+8 000**  |
| **Total**      | **-985 000** | **+382 000** | **+381 000** | **+381 000** |
| **Flux de trésorerie annuel (FT)** | **-985 000** | **+382 000** | **+381 000** | **+381 000** |


6) L'actualisation des flux de trésorerie permet de tenir compte de la **valeur temporelle de l'argent**. Un euro aujourd’hui vaut plus qu’un euro demain en raison de l’inflation et du coût d’opportunité. En actualisant les flux, on obtient une meilleure estimation de la rentabilité réelle du projet.

7) On actualise les flux de trésorerie avec un **taux d'actualisation de 6%** :
	### Formule : $$VAN = -IO + \sum^{N}_{i=1} \dfrac{FT_i}{(1+a)^i}$$ Avec : 
	- **\(IO\)** : Investissement initial (**985 000 €**) 
	- **\(N\)** : Nombre d'années d'exploitation (**3 ans**) 
	- **\(FT_i\)** : Flux de trésorerie de l’année \(i\) 
	- **\(a\)** : Taux d'actualisation (**6% soit 0,06**) 

	### Calcul détaillé : 
	#### Application de la formule : $$VAN = -985 000 + \dfrac{382 000}{(1,06)^1} + \dfrac{381 000}{(1,06)^2} + \dfrac{381 000}{(1,06)^3}$$ Développement des divisions : $$VAN = -985 000 + \dfrac{382 000}{1,06} + \dfrac{381 000}{1,1236} + \dfrac{381 000}{1,191}$$ Calcul des valeurs actualisées : $$VAN = -985 000 + 360 377 + 339 243 + 319 985$$ Addition des valeurs : $$VAN = -985 000 + 1 019 605$$ **Résultat final :** $$VAN = 34 605 €$$ 

8) Ce projet est-il rentable ?**

	Oui, car la **VAN est positive** (**34 605 €**). Cela signifie que le projet crée de la valeur et couvre les investissements initiaux.

---

9) Calcul du solde financier par année (hors actualisation)**

Cumul des flux de treˊsorerie=Somme des flux jusqu’aˋ l’anneˊe en cours\text{Cumul des flux de trésorerie} = \text{Somme des flux jusqu’à l’année en cours}Cumul des flux de treˊsorerie=Somme des flux jusqu’aˋ l’anneˊe en cours

| Année | Flux de trésorerie | Cumul des flux |
| ----- | ------------------ | -------------- |
| 2020  | **-985 000**       | **-985 000**   |
| 2021  | **+382 000**       | **-603 000**   |
| 2022  | **+381 000**       | **-222 000**   |
| 2023  | **+381 000**       | **+159 000**   |

👉 Le projet devient **bénéficiaire en 2023** (**+159 000 €**).  
👉 Sans actualisation, l’investissement est remboursé en **2 ans et quelques mois**.

---

10) Calcul du Délai de Récupération du Capital Investi (DRCI)**

Le **DRCI** est le moment où l’investissement initial est récupéré grâce aux gains d’exploitation.

- Après 2021, il reste **-603 000 €**.
- Après 2022, il reste **-222 000 €**.
- En 2023, on récupère **+381 000 €**, donc :

$\dfrac{222 000}{381 000} = 0,58 \text{ année}$ 

👉 **DRCI ≈ 2,58 ans (2 ans et environ 7 mois)**  
👉 Le projet est rentable en moins de **3 ans**, ce qui est un bon indicateur.

---

1) Le DRCI peut-il être un critère de rentabilité ?

Oui, le **Délai de Récupération du Capital Investi** est un bon indicateur pour voir **combien de temps** il faut pour récupérer l’investissement initial. Cependant, il **ne prend pas en compte la valeur temporelle de l’argent**, contrairement à la VAN.

Dans certains cas, un **DRCI court** peut être privilégié, mais pour une vraie évaluation financière, la VAN reste plus fiable.



## Application 1 : Rentabilité d'un logiciel de gestion


| Années | Dépense | Gains |
| ------ | :-----: | ----- |
| 0      |   700   | 0     |
| 1      |  1400   | 300   |
| 2      |  1300   | 1000  |
| 3      |  1150   | 2000  |
| 4      |   950   | 2500  |
| 5      |   900   | 3000  |
| 6      |  1000   | 3000  |
| 7      |  1500   | 3000  |
| Total  |  8900   | 14800 |


$$VAN = \sum \frac{(Gains - Dépenses)}{(1 + T)^t}$$ avec : 
- $( T = 4.5$%$= 0.045 )$
- ( t ) allant de 0 à 7


| Année | Dépenses (k€) | Gains (k€) | Flux Net (k€) | Valeur Actualisée (k€) |
| ----- | ------------- | ---------- | ------------- | ---------------------- |
| 0     | -700          | 0          | -700          | -700                   |
| 1     | -1 400        | 300        | -1 100        | -1 339.43              |
| 2     | -1 300        | 1 100      | -300          | -274.73                |
| 3     | -1 150        | 2 800      | 850           | 744.80                 |
| 4     | -950          | 2 500      | 1 550         | 1 300.17               |
| 5     | -900          | 3 000      | 2 100         | 1 687.39               |
| 6     | -1 000        | 3 000      | 2 000         | 1 538.46               |
| 7     | -1 000        | 3 000      | 1 500         | 1 473.64               |
