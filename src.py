###############
# INFORMATION DE BINOMES
###############
# Hoang Thuy Duong VU | 21110221
# Halimatou DIALLO | 21114613
##############

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt



def coloring_chain(L, seq, j, l) : 
  if l==0 : 
    for i in range(j+1) : 
      if L[i]==1 : return False
    for i in range(j+1) : 
      if L[i]==-1 : L[i] = 0
    return True

  elif j<seq[l-1]-1 : return False
  elif j==seq[l-1]-1 :
    if l==1 : 
      for i in range(j+1) : 
        if L[i]==0 : return False
      for i in range(j+1) : 
        if L[i]==-1 : L[i] = 1 
      return True
    else : return False
  
  else : 
    if L[j]==0 : return coloring_chain(L, seq, j-1, l)
    elif L[j]==1 : 
      if L[j-seq[l-1]]==1 : return False

      for i in range(j-seq[l-1]+1, j) : 
        if L[i]==0 : return False

      if L[j-seq[l-1]]==-1 : L[j-seq[l-1]] = 0
      for i in range(j-seq[l-1]+1, j) : 
        if L[i]==-1 : L[i] = 1
      return coloring_chain(L, seq, j-seq[l-1]-1, l-1)
    else : 
      hypo0 = L[:j] + [0]
      hypo1 = L[:j] + [1]
      P = coloring_chain(hypo0, seq, j, l)
      Q = coloring_chain(hypo1, seq, j, l)
      if not (P or Q) : return False 
      elif not Q : 
        for i in range(j+1) : 
          if L[i]!=hypo0[i] : L[i] = hypo0[i]
      elif not P : 
        for i in range(j+1) : 
          if L[i]!=hypo1[i] : L[i] = hypo1[i]
      else : 
        for i in range(j) : 
          if hypo0[i]==hypo1[i] and L[i]!=hypo0[i] :
            L[i] = hypo0[i]
      return True


# Pour lire un fichier
def read_file(file_name):
  count = 0
  res = 0
  global_list = []
  with open(file_name, 'r') as file:
    for line in file : 
      if line=="#\n" : 
        res = count
      else : 
        count+=1
        numbers = list(map(int, line.split()))
        if len(numbers)==0 : 
          global_list.append([0])
        else : global_list.append(numbers)

  first_half_list = global_list[:res]
  second_half_list = global_list[res:]
      
  return first_half_list, second_half_list


def CopierMatrice(Matrix) : 
  N = len(Matrix)
  M = len(Matrix[0])
  A = [0*M]*N
  for n in range(N) : 
    A[n] = Matrix[n].copy()

  return A
 


def is_finish(Matrix) : 
  N = len(Matrix)
  M = len(Matrix[0])
  list_neg = [Matrix[i][j] for i in range(N) for j in range(M) if Matrix[i][j]==-1]

  return True if len(list_neg)==0 else False


def ColoreLigne(Matrix, index, sequence) : 
  """
  Paramètre : 
    Matrix : matrice à traiter
    index : indice de la ligne à traiter
    sequence : séquence de bloc à colorer sur chaque ligne `current_line`
  Retoure `True` si la matrice est finie de colorer et `False` sinon, avec la matrice déjà traiter
  """
  M = len(Matrix[0])
  line = Matrix[index]

  tmp = line.copy()

  ok = coloring_chain(line, sequence, M-1, len(sequence))
  #print("coloring_chain: ok", ok, line, sequence, M-1, len(sequence))

  newCol = []
  for m in range(M) : 
    if tmp[m]!=line[m] : 
      newCol.append(m)

  return ok, Matrix, newCol



# Fonction facultative pour mieux metter à jour la nouvelle colonne
def changeCol(Matrix, index, col) : 
  N = len(Matrix)
  for n in range(N) : 
    line = Matrix[n].copy()
    line[index] = col[n]
    Matrix[n] = line.copy()
  return Matrix

def getCol(Matrix, index) : 
  N = len(Matrix)
  col = [Matrix[k][index] for k in range(N)]
  return col

def EmptyCounter(Matrix) : 
  N = len(Matrix)
  M = len(Matrix[0])
  L = [Matrix[n][m] for n in range(N) for m in range(M) if Matrix[n][m]==-1]
  return len(L)



def ColoreColonne(Matrix, index, sequence) : 
  """
  Paramètre : 
    Matrix : matrice à traiter
    index : indice de la colonne à traiter
    sequence : séquence de bloc à colorer sur chaque colonne `current_line`
  Retoure `True` si la matrice est finie de colorer et `False` sinon, avec la matrice déjà traiter
  """
  N = len(Matrix)
  M = len(Matrix[0])

  col = getCol(Matrix, index)
  tmp = col.copy()
  
  ok = coloring_chain(col, sequence, N-1, len(sequence))

  newLine = []
  for n in range(N) : 
    if tmp[n]!=col[n] : 
      newLine.append(n)

  Matrix = changeCol(Matrix, index, col)
    
  return ok, Matrix, newLine





def COLORATION(Matrix, list_line, list_col) : 
  A = CopierMatrice(Matrix)
  N = len(Matrix)
  M = len(Matrix[0])

  lines = [A[n] for n in range(N) if -1 in A[n]]
  cols = [getCol(A, i) for i in range(M) if -1 in getCol(A, i)]

  empty = 0

  ok1, ok2 = False, False
  while lines!=[] or cols!=[]: 
    empty = EmptyCounter(A)
    for line in range(N) : 
      l = A[line].copy()
      ok, A, newCol = ColoreLigne(A, line, list_line[line])
      if not ok : return False, [[-1]*M]*N
      lines.remove(l) if l in lines else lines
      New = [getCol(Matrix, index) for index in newCol]
      cols+=New 

    for col in range(M) : 
      c = getCol(Matrix, col)
      ok, A, newLine = ColoreColonne(A, col, list_col[col])
      if not ok : return False, [[-1]*M]*N
      cols.remove(c) if c in cols else cols
      New = [A[index] for index in newLine]
      lines+=New
    print(EmptyCounter(A)==empty)
    if EmptyCounter(A)==empty : 
      break


  if is_finish(A) : 
    return True, A 
  else : 
    return -1, A

def show(Matrix) : 
  plt.matshow(Matrix)