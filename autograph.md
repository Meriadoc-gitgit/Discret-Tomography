# Méthode incomplète de résolution
## Première étape 
Considérons une ligne $l_i$ dont la séquence associée est $(s_1,s_2...s_k)$.
>**Objectif** : déterminer s'il existe un coloriage possible de la ligne avec cette séquence. 

$$T(j,l)(j=0,...M, l=1,...k)$$
vrai s'il est possible de colorier les $j+1$ premières cases $(i,0), (i,1)...(i,j)$ de la ligne $l_i$, avec la sous-séquence $(s_1,...s_l)$ des premières blocs de la ligne $l_i$.

#### Question 1
Si on a calculé tous les $T(j,l)$, pour savoir s'il est possible de colorier la ligne $l_i$ entière avec la séquence entière : 

On vérifie si :
- tous les blocs $l$ de la ligne $l_i$ ont respectivement une longueur de $s_l$ cases noires consécutifs, 
- et les cases blanches respectent également la séparation d'un case blanche entre chaque bloc, alors la ligne $l_i$ peut être correctement coloriée en fonction de la séquence complète. 

Considérons l'algorithme qui procède par récurrence en distinguant les 3 cas possibles :
1. Cas $l=0$