#
## Exo1 
## Exo 2
- la densité d'un morceau de corde de longueur i est son prix au mètre p_i/i
- stratégie gloutonne : extraire de morceau de corde de densité maximale et recommencer tant qu'il reste de la corde

|i|1|2|3|4|
|-|-|-|-|-|
|p_i|1|5|8|9|
|p_i/i|1|2.5|2.67|2.25|

- la stratégie gloutonne conduit à découper la corde de n=4 mètres en deux morceaux de 1 et 3 mètres : ce qui procure un revenu total de 9
- pourtant on obtient un revenu de 10 en découpant la corde en deux morceaux de 2 mètres chacun

Le problème : déterminer le revenu de ventes maximal d'une corde de n mètres
-> Quelle est la sous-structure optimale dont on a besoin pour résoudre ce prob ? r(i) : le revenu maximal que l'on peut obtenie pour une corde de i mètres

-> caractériser cette sous structure optimal : r(i) - max_1<=j<=i{r(i-j) + p_j} avec r(0) = 0

-> le revenu de ventes maximal qu'on peut tirer d'une corde : r(n)


```txt
DécoupeCorde(p,b)
in : p[1...n] le tableau des prix et n la longueur de la corde
out : r(n) le revenu maximal qu'on peut tirer de la vente de la corde

r[0] = 0
pour i 1...n faire
  r[i] <- inf
  pour j 1...i faire
    r[i] <- max(r[i], r[i-j] + p[j])
  fin pour
fin pour

return r[n]
```
Complexité : $\Theta(n^2)$

```txt
DécoupeCorde(p,b)
in : p[1...n] le tableau des prix et n la longueur de la corde
out : la découpe optimale sous la forme d'une liste d'entiers L

L une liste vide
Soit t[1...n] un tableau qui fournit la longueur de morceaux découpés
r[0] = 0
pour i 1...n faire
  r[i] <- inf
  pour j 1...i faire
    si r[i]<r[i-j]+p[j] alors
      r[i]<-r[i-j]+p[j]
      t[i]<-j
    fin si
  fin pour
fin pour

i<-n 
tant que i!=0 faire 
  L.append(t[i])
  i<-i-t[i]
fin tant que

return r[n]
```

## Exo 3
On fournit la sous-structure optimale : opt(i) le cout minimum d'une séquence de i à n (avec 1<=i<=n)

opt  = 0

#photo
Complexité : $\Theta(n^2)$

## Exo 4 
## Exo 5