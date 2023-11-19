|0|0|0|0|0|0|0|
|-|-|-|-|-|-|-|
|2|3|**2**|3|3|3|2|
|5|5|5|5|5|5|5|
|3|3|3|3|3|3|3|
|4|4|4|4|4|4|4|


- Dimension : 5x7
- len(line) = 5
- len(col) = 7
- len(list_line_coloration) = 5
- len(list_col_coloration) = 7
- len(line_vertical) = 7
- len(col_horizontal) = 5
- M[1][2] = 2

```python
  # Colorer les cas restants en noir
  for n in range(N) : 
    for m in range(M) : 
      if Mtx[n][m]==-1 : 
        Mtx[n][m] = 1

        # Recopier les lignes et les colonnes apres la coloration supposee
        line = Mtx[n].copy()
        col = [Mtx[k][m] for k in range(N)]

        # Verifier la conformite
        P = T2(list_line[n], M-1, len(list_line[n]), line)  # pour ligne
        Q = T2(list_col[m], N-1, len(list_col[m]), col)    # pour colonnes

        # Imprimer pour verifier
        #print(P, line, Q, col)

        if not P or not Q : 
          Mtx[n][m] = -1

  # Colorer les cas restants en blanc
  for n in range(N) : 
    for m in range(M) : 
      if Mtx[n][m]==-1 : 
        Mtx[n][m] = 0

        # Recopier les lignes et les colonnes apres la coloration supposee
        line = Mtx[n].copy()
        col = [Mtx[k][m] for k in range(N)]

        # Verifier la conformite
        P = T2(list_line[n], M-1, len(list_line[n]), line)  # pour ligne
        Q = T2(list_col[m], N-1, len(list_col[m]), col)    # pour colonnes

        # Imprimer pour verifier
        #print(P, line, Q, col)

        if not P or not Q : 
          Mtx[n][m] = -1
```

Cần viết : 
- colorLigne
- colorCol