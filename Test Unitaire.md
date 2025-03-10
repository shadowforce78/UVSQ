# Opération qui calcule l'addition de deux nombres entier relatifs a et b

| Classe  | a   | b               | résultat attendu  |
| ------- | --- | --------------- | ----------------- |
| P1      | a>0 | b>0             | c=a+b>0           |
| P2      | a=0 | b>0             | c=b>0             |
| P3      | a>0 | b=0             | c=a>0             |
| P4      | a<0 | b<0             | c=a+b<0           |
| P5      | a=0 | b<0             | c=b<0             |
| P6      | a<0 | b=0             | c=a<0             |
| P7      | a=0 | b=0             | c=0               |
| P8      | a<0 | b>0 et \|a\|>b  | c=a+b<0           |
| P9      | a<0 | b>0 et \|a\|<b  | c=a+b>0           |
| P10     | a<0 | b>0 et \|a\|=0  | c=a+b=0           |
| P11     | a>0 | b<0 et a>\|b\|  | c=a+b>0           |

```mermaid

flowchart TD

    A{a > 0?} -->|Oui| B{b > 0?}
    A -->|Non| C{a = 0?}

    B -->|Oui| P1[P1: c = a + b > 0]
    B -->|Non| B1{b = 0?}

    B1 -->|Oui| P3[P3: c = a > 0]
    B1 -->|Non| P11[P11: Vérifier si a > b]

    C -->|Oui| D{b > 0?}
    C -->|Non| E{b > 0?}

    D -->|Oui| P2[P2: c = b > 0]
    D -->|Non| D1{b = 0?}

    D1 -->|Oui| P7[P7: c = 0]
    D1 -->|Non| P5[P5: c < 0]

    E -->|Oui| E1{Vérifier a et b}
    E -->|Non| E2{b = 0?}

    E1 -->|Oui| P8[P8: c < 0]
    E1 -->|Non| P9[P9: c > 0]
    E1 -->|Cas égalité| P10[P10: c = 0]

    E2 -->|Oui| P6[P6: c < 0]
    E2 -->|Non| P4[P4: c < 0]


```

# Opération qui calcule la soustraction de deux nombres entiers relatifs a et b

| Classe | a   | b   | résultat attendu  |
| ------ | --- | --- | ----------------- |
| P1     | a>0 | b>0 | c = a-b>0         |
| P2     | a=0 | b>0 | c = -b<0          |
| P3     | a>0 | b=0 | c = a>0           |
| P4     | a<0 | b<0 | c = a-b<0         |
| P5     | a=0 | b<0 | c = -b>0          |
| P6     | a<0 | b=0 | c = a<0           |
| P7     | a=0 | b=0 | c = 0             |
| P8     | a<0 | b>0 | c = a-b<0         |
| P9     | a>0 | b<0 | c = a-b>0         |

```mermaid

flowchart TD

    A{a > 0?} -->|Oui| B{b > 0?}

    A -->|Non| C{a = 0?}

    B -->|Oui| P1[P1: c=a-b>0]

    B -->|Non| B1{b = 0?}

    B1 -->|Oui| P3[P3: c=a>0]

    B1 -->|Non| P9[P9: c=a-b>0]

    C -->|Oui| D{b > 0?}

    C -->|Non| E{b > 0?}

    D -->|Oui| P2[P2: c=-b<0]

    D -->|Non| D1{b = 0?}

    D1 -->|Oui| P7[P7: c=0]

    D1 -->|Non| P5[P5: c=-b>0]

    E -->|Oui| P8[P8: c=a-b<0]

    E -->|Non| E2{b = 0?}

    E2 -->|Oui| P6[P6: c=a<0]

    E2 -->|Non| P4[P4: c=a-b<0]

```

# Opération qui calcule la multiplication de deux nombres entiers relatifs a et b

| Classe | a   | b   | résultat attendu   |
| ------ | --- | --- | ------------------ |
| P1     | a>0 | b>0 | c = a\*b>0         |
| P2     | a=0 | b>0 | c = 0              |
| P3     | a>0 | b=0 | c = 0              |
| P4     | a<0 | b<0 | c = a\*b>0         |
| P5     | a=0 | b<0 | c = 0              |
| P6     | a<0 | b=0 | c = 0              |
| P7     | a=0 | b=0 | c = 0              |
| P8     | a<0 | b>0 | c = a\*b<0         |
| P9     | a>0 | b<0 | c = a\*b<0         |

```mermaid

flowchart TD

    A{a = 0?} -->|Oui| P0[P2/P5/P7: c=0]

    A -->|Non| B{a > 0?}

    B -->|Oui| C{b = 0?}

    B -->|Non| D{b = 0?}

    C -->|Oui| P3[P3: c=0]

    C -->|Non| E{b > 0?}

    E -->|Oui| P1[P1: c=a*b>0]

    E -->|Non| P9[P9: c=a*b<0]

    D -->|Oui| P6[P6: c=0]

    D -->|Non| F{b > 0?}

    F -->|Oui| P8[P8: c=a*b<0]

    F -->|Non| P4[P4: c=a*b>0]

```

# Opération qui calcule la division de deux nombres entiers relatifs a et b

| Classe | a   | b   | résultat attendu  |
| ------ | --- | --- | ----------------- |
| P1     | a>0 | b>0 | c = a/b>0         |
| P2     | a=0 | b>0 | c = 0             |
| P3     | a>0 | b=0 | c = erreur        |
| P4     | a<0 | b<0 | c = a/b>0         |
| P5     | a=0 | b<0 | c = 0             |
| P6     | a<0 | b=0 | c = erreur        |
| P7     | a=0 | b=0 | c = erreur        |
| P8     | a<0 | b>0 | c = a/b<0         |
| P9     | a>0 | b<0 | c = a/b<0         |


```mermaid

flowchart TD

    Z{b = 0?} -->|Oui| Err[P3/P6/P7: c=erreur]

    Z -->|Non| A{a = 0?}

    A -->|Oui| B{b > 0?}

    A -->|Non| C{a > 0?}

    B -->|Oui| P2[P2: c=0]

    B -->|Non| P5[P5: c=0]

    C -->|Oui| D{b > 0?}

    C -->|Non| E{b > 0?}

    D -->|Oui| P1[P1: c=a/b>0]

    D -->|Non| P9[P9: c=a/b<0]

    E -->|Oui| P8[P8: c=a/b<0]

    E -->|Non| P4[P4: c=a/b>0]

```

