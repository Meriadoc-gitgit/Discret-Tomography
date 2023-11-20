###############
# INFORMATION DE BINOMES
###############
# Hoang Thuy Duong VU | 21110221
# Halimatou DIALLO | 21114613
##############

# Import necessary libraries
import numpy as np

 
###############
# COLORATION DES LIGNES ET COLONNES 
###############
from itertools import combinations

def CalculPossibititesConstant(current_line, bloc, length) : 
  n_groups = len(bloc)
  n_empty = length-2*n_groups+1
  opts = combinations(range(n_groups+n_empty), n_groups)

  possible_placement = set()
  glob = []
  for p in opts : 
    total = np.max(p) + np.sum(bloc)
    if total<=length : 
      possible_placement.add(p)
      
  possible_placement = list(possible_placement)
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
  
  if len(glob)==0 : 
    return False, []

  finalist = []
  for i in range(length) : 
    tmp = [glob[k][i] for k in range(len(glob))]
    if tmp==[0]*len(glob) : 
      finalist.append(0)  
    elif tmp==[1]*len(glob) : 
      finalist.append(1)
    else : 
      finalist.append(-1)

  return True, finalist
