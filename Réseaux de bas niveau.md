
# Réseau LAN 

## Définitions :

Un réseaux est constitué d’ordinateurs et d'éléments actifs reliés entre eux par les moyens de communication actuels

Éléments actif : équipement électronique qui permet de relier des machines dans un réseau 

Ordinateur : 
	1955 première apparition
	IBM France veut commercialiser un appareil qui s’appelait une tabulatrice et changer son nom pour qu'il soit plus vendeur
	Jacques Perret trouve le nom
	Le premier tableur : Microsoft Multiplan

Type de réseau : 
	- LAN (Local Area Network)
	- MAN (Metropolitan Area Network)
	- WAN (Wide Area Network)
	- Organisation différentes :
		- LAN : 
			- échelle : Entreprise, Bâtiment
			- nombre de machines : De l'ordre de 500
			- Petite DSI : Ingénieur / Technicien
			- Hardware : Ordinateur, switch, routeurs
			- Technologies : Ethernet (RJ45)
		- MAN :
			- échelle : Ville
			- nombre de machines : Plus de 1000
			- Plusieurs DSI : Ingénieur, Technicien, Fournisseur d'accès
			- Hardware : Ordinateur, switch, routeurs, Antennes, GSM
			- Technologies : Ethernet, Fibre
		- WAN :
			- échelle : Contient / Pays
			- nombre de machines 
			- Plusieurs fournisseur d'accès
			- Hébergeur
			- hardware : routeur, datacenter
			- technologies : GSM, fibre, antienne relais

- Topologie des LAN :
	![[Pasted image 20250325102838.png]]
	Topologie maillée : ![[Pasted image 20250325103632.png]]
Concept de réseau
![[Pasted image 20250325103921.png]]

# TD/TP 1

## Exercice 1

1) TCP / IP : 4 couches; OSI : 7 couche
![[Drawing 2025-03-28 08.40.53.excalidraw]]

2) Bus, Anneau, Etoiles, Arbre, Maillée
3) Un protocole est utilisé dans une communication de bout a bout pour établir une connexion entre deux système via un réseau
4) Il faudrait 45 liaison ($\dfrac{n(n-1)}{2}$) 
5) Le réseau Renater => Gros MAN ou petit WAN
Le réseau de l'UVSQ => Man<br>Le réseau de TC à Rambouillet => LAN<br>Le réseau du groupe Orange => WAN<br>Le réseau Amazon => WAN<br>Internet => Gros WAN

6) Ethernet (RJ45), Wifi, 4G, Bluetooth
## Exercice 2
1) ![[Drawing 2025-03-28 09.05.40.excalidraw]]C'est un domaine de diffusion, ce modèle ne peut gérer qu'une seul connexion a la fois, si deux station émette en même temps, le hub va planter, il y aura collision
2) Scénario : 
	1) Broadcast / Diffusion
	2) ![[Drawing 2025-03-28 09.20.35.excalidraw]]
## Exercice 5 :
![[Drawing 2025-03-28 09.57.56.excalidraw]]

|Adresse MAC|Port|
|---|---|
|st1|Port correspondant à st1|
|st2|Port correspondant à st2|
|st6|Port correspondant à st6|
|sw2|Port vers `sw2`|

| Adresse MAC | Port                     |
| ----------- | ------------------------ |
| st3         | Port correspondant à st3 |
| st4         | Port correspondant à st4 |
| st5         | Port correspondant à st5 |
| sw1         | Port vers `sw1`          |

## Exercice 7

![[Drawing 2025-03-28 10.06.34.excalidraw]]
**Tout le monde reçoit tout** → pas de confidentialité
**Bruit réseau infernal** → chaque machine reçoit des données qui ne la concernent pas.


## Exercice 8
![[Drawing 2025-03-28 10.10.05.excalidraw]]
Il faut activer le STP (Spanning Tree Protocol)

# Chapitre 3 : Couche liaison de données (2ème couche)

*Description*:
	Assurer un transfert fiable
		retransmission
		détection / correction des erreurs
		contrôle de flux
	la seconde couche est séparée en deux (LLC et MAC, ici on étudie MAC)
	
HDLC => Highlevel Data Link Control


# TP1 suite

Un VLAN permet de séparer un réseaux en sous réseaux de plusieurs machine a partir d'un seul switch
802.1q Pour la propagation de VLAN


CIDR => ClassLess Inter Domain Routing
Le slash de l'adresse ip correspond a son masque (127.0.0.1/24 et 24 bits de masque)


@IP = 192.168.1.1/23 => @MASK = 255.255.248.0


Identification avec MF pour prévenir de plusieurs packets, multiple de 8...

# Chapitre 4

Protocole TCP/IP

Transmission Control Protocol 
Septembre 1981

__Définition__ : TCP est un protocole de niveau transport en mode connecté chargé d'établir et  de maintenir une connexion entre 2 réseaux

# Exercice 10 (TD 1)

1) ![[Pasted image 20250507103531.png]]
$\boxed{\omega = 2\pi}$ C'est la pulsation
$T=\dfrac{2\pi}{\omega}$ 
Ici comme $\omega = 2\pi$ ici $T=1$

$f(t)=sin(t)$ est périodique de période $2\pi$ 
Car : $sin(t+2\pi) = sin(t)$   $\forall t \in \mathbb{R}$ 


2) ![[Pasted image 20250507103624.png]]
3) $S(t)=sin(\pi t)+sin(2\pi t)$
	1) La période du signal est : $T_0 = 2$ et $T_1 = 1$ 
		Donc $T = 2$ 

4) $S(t) = \dfrac{4}{3}sin(\pi t)$
	1) L'amplitude est de $\dfrac{4}{3}$
5) $S(t)=sin(2\pi t + \dfrac{\pi}{4})$ 
	1) La phase du signal est : $\dfrac{\pi}{4}$
6) $S(t)=sin(\dfrac{\pi}{4}t + \dfrac{\pi}{5})$
	1) La pulsation est : $\omega = \dfrac{\pi}{4}$ 
	2) $T=\dfrac{2\pi}{\omega}=\dfrac{2\pi}{\dfrac{\pi}{4}}=8$ 
	3) $f = \dfrac{1}{T} = \dfrac{1}{8}$ 

La fragmentation IP sert a envoie des données plus grosse que le réseaux lui même.


# Exercice 6 (TD 4)
LAN A :
@RSX 192.168.20.128/26
@PREMIERE 192.168.20.129/26
@BROADCAST 192.168.20.191/26
@DERNIERE 192.168.20.190/26

LAN B : 
@RSX 192.168.20.192/26
@PREMIERE 192.168.20.193/26
@BROADCAST 192.168.20.255
@DERNIERE 192.168.20.254

LAN C : 
@RSX 192.168.20.224/28
@PREMIERE 192.168.20.225
@BROADCAST 192.168.20.239
@DERNIERE 192.168.20.238

