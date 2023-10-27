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


#####
# 1 - MÉTHODE INCOMPLÈTE DE RÉSOLUTION 
#####
# 1.1 - PREMIÈRE ÉTAPE
####

# Implémentation de structure 
class Matrix : 
  # Initialisation 
  def __init__(self, width, height, colored=[]) : 
    self.N = width
    self.M = height
    self.board = np.zeros((width,height)) # N : width, M : height
    for (x,y) in colored : 
      self.board[x][y] = 1

  def show(self) : 
    print("================================")
    print("Current Board {}x{}".format(self.N,self.M))
    print("================================")
    print(self.board)

  def colorier(self, s, j, i=0) : 
    """
    Colorier la ligne `i` à partir du colonne `j` un bloc de longueur `s`
    """
    if s==0 : print("Warning : no cell colored, color array NULL"); return
    if s+j>self.M : print("Warning : Impossible to colorize the bloc of {} from j.".format(s)); return
    else : 
      for cell in range(j, j+s) : 
        self.board[i][cell] = 1
    

  #####
  # Q1.4
  #####
  def T(self, j, l, i=0, s=[]) : 
    
    # Vérification de conformité
    if np.sum(s)>self.M : return True
    if l>len(s) : return False

    if l==0 : return False
    
    if j<=s[l-1]-1 : 
      return True 

    else : 
      if self.board[i][j]==0 : 
        
      return True if self.board[i][j]==0 else T(j-s[l-1], l-1, i)