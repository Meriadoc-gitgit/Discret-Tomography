#####
# INFORMATION DE BINOMES
#####
# Hoang Thuy Duong VU | 21110221
# Halimatou DIALLO | 21114613
####


####
# UN PROBLÈME DE TOMOGRAPHIE DISCRÈTE
####


# Import necessary libraries
import numpy as np

# Define constant width x length
M = 15


#####
# 1 - MÉTHODE INCOMPLÈTE DE RÉSOLUTION 
#####
# 1.1 - PREMIÈRE ÉTAPE
####

def T(seq, j, l, L=M*[0]) : 
  """
  Paramètre : 
    L : ligne considérée de longueur M de zéros par défaut
    seq : séquence s considérer pour la coloration
    j : le nombre de cases on a besoin de colorier
    l : index l indiquant l'index courant de seq, dont l premiers blocs de la ligne 
  Retourne 0 si c'est possible de colorier et 1 sinon
  """

  # Cas de base l=0
  if l==0: 
    for i in range(j+1) : 
      if L[i]==True : return False
    return True

  # Cas 2a
  elif j<seq[l-1]-1 : return False

  # Cas 2b
  elif j==seq[l-1]-1 : 
    for i in range(j+1) : 
      if L[i]==False : return False
    return True

  # Cas 2c
  elif j>seq[l-1]-1 : 
    if L[j]==1 : 
      for i in range(j-seq[l-1]+1,j) : 
        if L[i]==False : return False
      if L[j-seq[l-1]]==True : return False
      else : return T(seq, j-seq[l-1]-1, l-1, L)
    else : return T(seq, j-1, l, L)


#####
# 1.2 - GÉNÉRALISATION
####
def T2(seq, j, l, L=M*[0]) : 
  """
  Paramètre : 
    L : ligne considérée de longueur M de zéros par défaut
    seq : séquence s considérer pour la coloration
    j : le nombre de cases on a besoin de colorier
    l : index l indiquant l'index courant de seq, dont l premiers blocs de la ligne 
  Retourne 0 si c'est possible de colorier et 1 sinon
  """
  if L==len(L)*[0] : 
    return True

  # Cas de base l=0
  if l==0: 
    for i in range(j+1) : 
      if L[i]==1 : return False
    return True

  # Cas 2a
  elif j<seq[l-1]-1 : return False

  # Cas 2b
  elif j==seq[l-1]-1 : 
    if l==1 : 
      for i in range(j+1) : 
        if L[i]==0 : return False
      return True
    else : 
      return T2(seq, j-1, l, L)
  # Cas 2c
  elif j>seq[l-1]-1 : 
    if L[j]==-1 : 
      tmp0 = L[0:j]+[0]
      #print(tmp0)
      tmp1 = L[0:j]+[1]
      #print(tmp1)
      b0 = T2(seq, j, l, tmp0)
      b1 = T2(seq, j, l, tmp1)
      #print(tmp0, tmp1, L)
      if not (b0 or b1) : 
        return False

      elif not b0 and b1 : 
        for i in range(j+1) : 
          L[i] = tmp1[i]
        return True

      elif b0 and not b1 : 
        for i in range(j+1) : 
          L[i] = tmp0[i]
        return True
      
      else : 
        for i in range(j+1) : 
          if tmp0[i]==tmp1[i] : 
            L[i] = tmp1[i]
        return True
    
    elif L[j]==1 : 
      for i in range(j-seq[l-1]+1,j) : 
        if L[i]==0 : 
          return False
        
      if L[j-seq[l-1]]==1 : 
        return False
      
      else : 
        return T2(seq, j-seq[l-1]-1, l-1, L)
    else : 
      return T2(seq, j-1, l, L)



#####
# 1.3 - PROPAGATION
####
from itertools import combinations

def possible_coloration(bloc, current_line, length) : 
  nb_bloc = len(bloc)
  nb_bloc_useless = length - np.sum(bloc) - (len(bloc)-1)
  opts = combinations(range(nb_bloc+nb_bloc_useless), nb_bloc)

  possible_placement = []
  glob = []

  for p in opts : 
    total = 0
    for i in range(len(bloc)) : 
      total+=p[i]+bloc[i]

    if total<=length+1 : 
      possible_placement.append(p)


  for p in possible_placement : 
    L_res = []
    for i in range(len(bloc)) : 
      if i>=1 : 
        L_res += [0]*(p[i]-p[i-1])+[1]*bloc[i]
      else : 
        L_res += [0]*(p[i])+[1]*bloc[i]
    
    if len(L_res)<length : 
      L_res += [0]*(length-len(L_res))

    glob.append(L_res)

  tmp1 = current_line.copy()
  tmp2 = current_line.copy()
  for i in range(length) : 
    if current_line[i]==-1 : 
      tmp1[i] = 1
      tmp2[i] = 0
  
  for g in glob : 
    if g==tmp1 or g==tmp2 : 
      return [g]

  return glob

  


def colorLine(bloc, current_line, length) : 
  glob = possible_coloration(bloc, current_line, length)
  if len(glob)==1 : 
    return glob[0]
  list_glob = glob.copy()

  for i in range(len(list_glob)) : 
    for j in range(len(list_glob[i])) : 
      tmp = list_glob[i].copy()
      if list_glob[i][j]!=current_line[j] and current_line[j] in [0,1] and list_glob[i] in glob: 
        glob.remove(tmp)

  if len(glob)==0 : 
    return [-1]*length
  res = glob[0]
  L = [-1]*length
  for i in range(length) : 
    col = [glob[k][i] for k in range(len(glob))]
    if np.sum(col)==len(glob) : 
      L[i] = 1
    elif np.sum(col)==0 : 
      L[i] = 0
  return L



def colorCol(bloc, current_line, length) : 
  # Prendre current_line en tant que parametres vu qu'on colore les colonnes apres les lignes
  glob = possible_coloration(bloc, current_line, length)
  if len(glob)==1 : 
    return glob[0]
  list_glob = glob.copy()
  for i in range(len(list_glob)) : 
    for j in range(len(list_glob[i])) : 
      tmp = list_glob[i].copy()
      if list_glob[i][j]!=current_line[j] and current_line[j] in [0,1] and list_glob[i] in glob: 
        glob.remove(tmp)

  if len(glob)==0 : 
    return [-1]*length
  res = glob[0]
  L = [-1]*length
  for i in range(length) : 
    col = [glob[k][i] for k in range(len(glob))]
    if np.sum(col)==len(glob) : 
      L[i] = 1
    elif np.sum(col)==0 : 
      L[i] = 0
  return L




def copie_matrix(M) : 
  L = [[-1]*len(M[0])]*len(M)
  for i in range(len(M)) : 
    L[i] = M[i].copy()
  return L




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





def Coloration(list_line, list_col, Mtx) : 
  """
  Paramètre : 
    list_line : liste de listes d'indices à colorier sur les lignes
    list_colonnes : liste de listes d'indices à colorier sur les colonnes
    Mtx : matrice vide à colorier
  Retourne (ok, Mtx), avec ok vaut True si la matrice est totalement coloriée et False si non
  """
  # len(line) = N, len(col) = M
  N = len(Mtx)
  M = len(Mtx[0])

  # Colorer les cases constants par lignes
  for n in range(N) : 
    line = Mtx[n].copy()
    colored = colorLine(list_line[n], Mtx[n], M)
    Mtx[n] = colored
    for m in range(M) : 
      col = [Mtx[k][m] for k in range(N)]
      P = T2(list_line[n], M-1, len(list_line[n]), line)
      Q = T2(list_col[m], N-1, len(list_col[m]), col)
      if not P or not Q :
        Mtx[n][m] = -1


  #print(Mtx,"\n")  # Imprimer la matrice
  # Generer un duplicata du matrice
  A = copie_matrix(Mtx)
  # Colorer les cases constants par colonnes

  for m in range(M) : 
    # Recuperer les valeurs des colonnes m sur chaque ligne
    col = [A[k][m] for k in range(N)]
    colored = colorCol(list_col[m], col, N)
    
    P = T2(list_line[n], M-1, len(list_line[n]), line)
    Q = T2(list_col[m], N-1, len(list_col[m]), col)
    if Q : 
      for n in range(N) : 
        if A[n][m]==-1 : 
          A[n][m] = colored[n]
          line = A[n].copy()
          #print("line",n, line, T2(list_line[n], M-1, len(list_line[n]), line))

          if not P :
            A[n][m] = -1
  
  # Fusionner les 2 matrices
  for n in range(N) : 
    for m in range(M) : 
      if Mtx[n][m]!=A[n][m] and Mtx[n][m]==-1 : 
        Mtx[n][m] = A[n][m]

  #print(Mtx,"\n")  # Imprimer la matrice
  for n in range(N) : 
    for m in range(M) : 
      if Mtx[n][m]==-1 : return (-1, Mtx)

  return (True, Mtx)



def ColorationProgagee(Mtx, i, j, c, list_line, list_col) : 
  """
  Paramètre : 
    Mtx : une grille partiellement coloriée
    i, j : indice de la cases à colorier
    c : couleur, soit 0 ou 1
  Retourne (ok, Mtx), avec ok vaut True si la matrice est totalement coloriée et False si non
  """
  N = len(Mtx)
  M = len(Mtx[0])
  if Mtx[i][j]==-1 : 
    Mtx[i][j] = c 
    line = Mtx[i].copy()
    col = [Mtx[k][i] for k in range(N)]
    P = T2(list_line[i], M-1, len(list_line[i]), line)
    Q = T2(list_col[j], N-1, len(list_col[j]), col)

    print("P", P, "Q", Q)
    if not P or not Q : 
      print("ok", i,j,c)
      Mtx[i][j] = -1
    if P and Q : 
      ok, Mtx = Coloration(list_line, list_col, Mtx)

  for n in range(N) : 
    for m in range(M) : 
      if Mtx[n][m]==-1 : return (-1, Mtx)

  return True, Mtx


def EnumRec(Mtx, k, c, list_line, list_col) : 
  """
  Paramètre : 
    Mtx : une grille partiellement coloriée
    k : indice de case
    c : couleur, soit 0 ou 1
  Retourne 
  """
  S = set()
  # len(line) = N, len(col) = M
  N = len(Mtx)
  M = len(Mtx[0])
  for n in range(N) : 
    for m in range(M) : 
      if Mtx[n][m]==-1 : 
        S.add((n,m))

  for (i,j) in S : 
    B1, _ = ColorationProgagee(Mtx, i, j, 0, list_line, list_col)
    B2, _ = ColorationProgagee(Mtx, i, j, 1, list_line, list_col)
    P = B1 or B2
    if P : 
      return P, Mtx