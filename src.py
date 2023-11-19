###############
# INFORMATION DE BINOMES
###############
# Hoang Thuy Duong VU | 21110221
# Halimatou DIALLO | 21114613
##############

# Import necessary libraries
import numpy as np



###############
# VÉRIFICATION DE CONFORMITÉ
###############
def check_conformity(sequence, number_of_cases, active_index, line) : 
  """
  Paramètre : 
    sequence : séquence de bloc à colorer sur chaque ligne `line`
    number_of_cases (j) : nombre number_of_cases+1 des cases à colorier
    active_index (l) : indice active du bloc dans la liste `sequence` des blocs à colorier
    line : ligne à colorier
  Retoure `True` si c'est possible de colorier et `False` sinon
  """

  # Cas de base où l = 0
  if active_index==0 : 
    list_one = [i for i in line[0:number_of_cases+1] if i==1]
    #for i in range(number_of_cases+1) : 
      #if line[i]==1 : return False
    return True if len(list_one)==0 else False
  
  # Cas 2a : j < s[l]-1
  elif number_of_cases<sequence[active_index-1]-1 : return False

  # Cas 2b : j = s[l]-1
  elif number_of_cases==sequence[active_index-1]-1 : 
    if active_index==1 : 
      list_zero = [i for i in line[0:number_of_cases+1] if i==0]
      #for i in range(number_of_cases+1) : 
        #if line[i]==0 : return False
      return True if len(list_zero)==0 else False
    else : return check_conformity(sequence, number_of_cases-1, active_index, line)
  
  # Cas 2c : j > s[l]-1
  elif number_of_cases>sequence[active_index-1]-1 : 
    if line[number_of_cases]==-1 : 
      hypo0 = line[0:number_of_cases]+[0]
      hypo1 = line[0:number_of_cases]+[1]

      P = check_conformity(sequence, number_of_cases, active_index, hypo0)
      Q = check_conformity(sequence, number_of_cases, active_index, hypo1)

      # Cas 1 : si P et Q sont tous faux
      if not (P or Q) : return False

      # Cas 2 : si une entre les deux sont vrais
      elif not P and Q : 
        # P faux et Q vrai 
        line = hypo1+line[j:]
        return True

      elif P or not Q : 
        # P vrai et Q faux
        line = hypo0+line[j:]
        return True

      # Cas 3 : si P et Q sont tous vrais
      else : 
        for i in range(j+1) : 
          if hypo0[i]==hypo1[i] : 
            line[i] = hypo0[i]
        return True 

    elif line[number_of_cases]==1 : 
      # Vérifier si le bloc est bien colorié en noir
      for i in range(number_of_cases-sequence[active_index-1]+1, number_of_cases) : 
        if line[i]==0 : return False 

      # Vérifier si le case suivant du bloc est colorié différemment que celle du bloc
      if line[number_of_cases-sequence[active_index-1]]==1 : return False
      else : 
        return check_conformity(sequence, number_of_cases-sequence[active_index-1]-1, active_index-1, line)

    else : 
      return check_conformity(sequence, number_of_cases-1, active_index, line)




###############
# RECOPIER UNE MATRICE
###############
def CopierMatrice(Matrix) : 
  N = len(Matrix)
  M = len(Matrix[0])
  A = [0*M]*N
  for n in range(N) : 
    A[n] = Matrix[n].copy()

  return A
 
 
###############
# COLORATION DES LIGNES ET COLONNES 
###############
from itertools import combinations

def CalculPossibititesConstant(current_line, bloc, length) : 
  n_groups = len(bloc)
  n_empty = length-2*n_groups+1
  opts = combinations(range(n_groups+n_empty), n_groups)

  possible_placement = []
  glob = []

  for p in opts : 
    total = np.max(p) + np.sum(bloc)
    if total<=length : 
      possible_placement.append(p)
      
  for p in possible_placement : 
    sequence = []
    for i in range(n_groups) : 
      if i>=1 : 
        sequence+=[0]*(p[i]-p[i-1]) + [1]*bloc[i]
      else : sequence += [0]*p[i] + [1]*bloc[i]

    empty = length-len(sequence)
    sequence+=[0]*empty
    glob.append(sequence)

  list_glob = glob.copy()
  for possible in list_glob : 
    for i in range(length) : 
      if possible[i]!=-1 and current_line[i]!=-1 and current_line[i]!=possible[i] and possible in glob :
        glob.remove(possible)

  finalist = []
  for i in range(length) : 
    tmp = [glob[k][i] for k in range(len(glob))]
    if tmp==[0]*len(glob) : 
      finalist.append(0)  
    elif tmp==[1]*len(glob) : 
      finalist.append(1)
    else : 
      finalist.append(-1)

  return finalist



def is_finish(Matrix) : 
  N = len(Matrix)
  M = len(Matrix[0])
  list_neg = [Matrix[i][j] for i in range(N) for j in range(M) if Matrix[i][j]==-1]

  return True if len(list_neg)==0 else False

def ColoreLigne(Matrix, index, sequence, current_line) : 
  """
  Paramètre : 
    Matrix : matrice à traiter
    sequence : séquence de bloc à colorer sur chaque ligne `line`
    current_line : ligne à colorier
  Retoure `True` si c'est possible de colorier et `False` sinon
  """
  length = len(current_line)
  possible_coloration = CalculPossibititesConstant(current_line, sequence, length)
  Matrix[index] = possible_coloration.copy()

  return is_finish(Matrix), Matrix

def 
