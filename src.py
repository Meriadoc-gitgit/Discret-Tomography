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
  if L==len(L)*[0] : return True

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
        if L[i]==-1 : L[i] = 1
        elif L[i]==0 : return False
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
      if not (b0 or b1) : return False
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
        if L[i]==0 : return False
      if L[j-seq[l-1]]==1 : return False
      else : return T2(seq, j-seq[l-1]-1, l-1, L)
    else : return T2(seq, j-1, l, L)



#####
# 1.3 - PROPAGATION
####
from itertools import combinations

def possible_coloration(bloc, length) : 
  
  nb_bloc = len(bloc) 
  nb_bloc_useless = length - np.sum(bloc) - (len(bloc)-1)
  opts = combinations(range(nb_bloc+nb_bloc_useless), nb_bloc)
  
  possible_placement = []
  glob = []
  for p in opts :
    total = 0
    for i in range(len(bloc)) : 
      total += p[i]+bloc[i]
    if total<=length or length - len(bloc)==len(bloc)-1 : 
      possible_placement.append(p)
  
  for p in possible_placement : 
    L_res = []
    for i in range(len(bloc)) : 
      if i>=1 :  
        L_res += [0]*(p[i]-p[i-1])+[1]*bloc[i]
      else : 
        L_res += [0]*(p[i])+[1]*bloc[i]

    while len(L_res)<length : 
      L_res.append(0)
  
    glob.append(L_res)
  return glob


def colorLine(bloc, length) : 

  glob = possible_coloration(bloc, length)
  if len(glob)==1 : 
    return glob[0]

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

  glob = possible_coloration(bloc, length)
  list_glob = glob.copy()

  for i in range(len(list_glob)) : 
    for j in range(len(list_glob[i])) : 
      tmp = list_glob[i]
      if list_glob[i][j]!=current_line[j] and current_line[j] in [0,1] and list_glob[i] in glob: 
        glob.remove(tmp)

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



def Coloration(list_line, list_col, Mtx) :   
  N = len(Mtx)
  M = len(Mtx[0])
  A = copie_matrix(Mtx)
  # Pour lignes
  for i in range(N) : 
    colored = colorLine(list_line[i], M)
    Mtx[i] = colored
  
  # Pour colonnes
  for i in range(M) : 
    col = [A[k][i] for k in range(N)]
    colored = colorCol(list_col[i], col, N)
    if T2(list_col[i], N-1, len(list_col[i]), colored) : 
      for k in range(N) : 
        if A[k][i]==-1 :
          A[k][i] = colored[k]
          line = A[k].copy()
          if not T2(list_line[k], M-1, len(list_line[k]), line) : 
            A[k][i] = -1

  # Blend les 2 matrices
  for i in range(N) : 
    for j in range(M) : 
      if Mtx[i][j]!=A[i][j] and Mtx[i][j]==-1 : 
        Mtx[i][j] = A[i][j]
  
  # Colorier 1 dans les cas restants
  for i in range(N) : 
    for j in range(M) :
      if Mtx[i][j]==-1 : 
        Mtx[i][j] = 1 
        line = Mtx[i].copy()
        col = [Mtx[k][j] for k in range(N)] 
        P = T2(list_col[j], N-1, len(list_col[j]), col)
        Q = T2(list_line[i], M-1, len(list_line[i]), line)
        if not P or not Q : 
          Mtx[i][j] = -1

  # Fill the blank with 0
  for i in range(N) : 
    for j in range(M) :
      if Mtx[i][j]==-1 : 
        Mtx[i][j] = 0

  return Mtx
