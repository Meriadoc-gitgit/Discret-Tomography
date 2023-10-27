|nom|choix du sommet dans la bordure|comp|appli|
|-|-|-|-|
|parcours generique|quelconque|$O(n+m)$|detection de composantes connexes/fortement connexes|
|parcours en largeur|sommet adjacent au 1er sommet ouvert|$O(n+m)$|arborescence des plus courts chemin en nb d'arêtes (arcs)|
|parcours en profondeur|sommet adj au dernier sommet ouvert|$O(n+m)$|détection de circuit + ordre topologique|
|algo de Dijsktra|sommet avec la + petite valeur d; <br>d(x) : longueur d'un plus court chemin entre la racine et x <br>(d(x) : distance entre la racine et x)|tas : $O((n+m)\log n)$ <br>sans tas : $O(n^2)$|arborescence des plus courts chemins quand les couts des arcs sont >=0|
|Algo de Prim|d(x) : distance entre x et un sommet de l'arbre|$O(m\log n)$ <br>ou $O(n^2)$|arbre couvrant de cout minimum|
