| 128 | 64  | 32  | 16  | 8   | 4   | 2   | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 0   | 0   | 0   | 1   | 1   | 0   | 1   |

1011( <sub>2</sub> ) = 13( <sub>10</sub> )

BIT = Binary Digit
8 bits = octets = byte


| 128 | 64  | 32  | 16  | 8   | 4   | 2   | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 1   | 0   | 0   | 1   | 1   | 0   | 1   |
1011001( <sub>2</sub>) = 64 + 8 + 4 + 1 = 77( <sub>10</sub> )

Sur 2 bits on code 4 mots :

00 = 0(<sub>10</sub>)
01 = 1(<sub>10</sub>)
10 = 2(<sub>10</sub>)
11 = 3(<sub>10</sub>)

# Hexadecimal

0-F en base 16


D3E( <sub>16</sub> ) => 
	D(<sub>16</sub>) = 13(<sub>10</sub>) 
	3(<sub>16</sub>) = 3(<sub>10</sub>)
	E(<sub>16</sub>) = 14(<sub>10</sub>)

| 8   | 4   | 2   | 1   | 8   | 4   | 2   | 1   | 8   | 4   | 2   | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1   | 1   | 0   | 1   | 0   | 0   | 1   | 1   | 1   | 1   | 1   | 0   |

D3E(<sub>16</sub>) = 110100111110(<sub>2</sub>)

| Base 10 | Base 2 | Base 16 |
| ------- | ------ | ------- |
| 0       | 0000   | 0       |
| 1       | 0001   | 1       |
| 2       | 0010   | 2       |
| 3       | 0011   | 3       |
| 4       | 0100   | 4       |
| 5       | 0101   | 5       |
| 6       | 0110   | 6       |
| 7       | 0111   | 7       |
| 8       | 1000   | 8       |
| 9       | 1001   | 9       |
| 10      | 1010   | A       |
| 11      | 1011   | B       |
| 12      | 1100   | C       |
| 13      | 1101   | D       |
| 14      | 1110   | E       |
| 15      | 1111   | F       |

125(<sub>16</sub>) = 0001 0010 0101(<sub>2</sub>)

| 2048 | 1024 | 512 | 256 | 128 | 64  | 32  | 16  | 8   | 4   | 2   | 1   |
| ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0    | 0    | 0   | 1   | 0   | 0   | 1   | 0   | 0   | 1   | 0   | 1   |

125(<sub>16</sub>) = 256 + 32 + 4 + 1 = 288 + 5 = 293(<sub>10</sub>)

0xA5 + 0x8B = 0x130

0x5 + 0xB = 16 donc 0xF + 0x1
0xA + 0x8 = 18 donc 0xF + 0x3



| 32384 | 16192 | 8096 | 4048 | 2048 | 1024 | 512 | 256 | 128 | 64  | 32  | 16  | 8   | 4   | 2   | 1   |
| ----- | ----- | ---- | ---- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|       |       |      |      |      | 1    | 0   | 0   | 1   | 0   | 1   | 1   | 1   | 1   | 0   | 1   |

1024+128+32+16+8+4+1


Base 10 | Base 8
--|-
0|00
1|01
2|02
3|03
4|04
5|05
6|06
7|07
8|10
9|11
10|12
11|13
12|14
13|15
14|16
15|17
(16)|20
La base 8 (octal) sert notamment pour les droits Linux :

	RWX : Read Write Execute = 111<sub>(2)</sub> (1+2+4 = 7<sub>(10)</sub>)
Si on dit préciser les droits du propriétaire, du groupe et des autres, on utilise 3 fois : 
	RWX RWX RWX
	111   111   111<sub>(2)</sub> = 777<sub>(8)</sub>
Si on retire les droits d'exécution (X)
	110 110 110<sub>(2)</sub> = 666<sub>(8)</sub> 


### Sticky bit
	C'est le bit "t", on l'applique sur un repertoire
	Si tous les utilisateurs ont tous les droits sur le repertoire /temp,
	(rwx rwx rwx) ols peuvent tous créer des fichiers dans ce repertoire, 
	et ils peuvent supprimer les fichiers des autres utilisateurs
	Pour empecher cette suppression, on place le sticky bit

	mkidr ~/temp
	chmod 777 ~/temp
	chmod -t ~/temp

	pour verifier :
		ls -l ~/temp

### Umask
	La valeur umask définie les droits par défaut des futures fichiers et dossiers
	modifier unmask ne change pas les droits des fichiers et dossiers actuels
	la valeur de umask, donne le droits a retirer

	Pour les répertoires les droits sont : 777-044 = 733 = rwx-wx-wx
	Pour les fichiers les droits sont : 777-044 = 622 = rw-w-w

	Avant l'application du umask (ou unmask = 000)
	Pour les repertoires : 777
	Pour les fichiers : 666 (on retire les x)
	
	Avec le umask = 023
	Pour les repertoires : 754
	Pour les fichiers : 644
	Remarques, la commande umask 023 modifie les droits de maniere temporiare (le
	temps de la session) 