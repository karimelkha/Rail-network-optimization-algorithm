# -*- coding: utf-8 -*-
"""
Created on Sun May  9 17:48:18 2021

@author: DAUSSY Lorette, EL KHARROUBI Karim
"""

import datetime
import random

class Train : 

  # initialisation parametres 
  def __init__(self,num,nom,sens,horaire,type_t):
    self.num = num
    self.nom = nom
    self.sens = sens
    self.horaire = horaire
    self.type_t = type_t
  
  # surcharge opérateur pour tri liste train
  def __lt__(self, other):
        return self.horaire < other.horaire

# generateur liste de train
def generateurTrain(nb_train):
    gares=["Paris","Strasbourg","Nice","Marseille","Lilles","Nantes","Nancy","Lyon","Bordeaux","Toulouse","Rennes","Perpignan","Annecy"]
    d = []
    temp=True
    numero=1
    for x in range(0,nb_train,1):
        if temp == True:
            temp=False
            t=Train(numero," ","arrivee",datetime.timedelta(hours=round(5+(18/nb_train)*x),minutes=random.randint(1, 60))," ")
        else:
            temp=True
            t=Train(numero," ","depart",datetime.timedelta(hours=round(5+(18/nb_train)*x),minutes=random.randint(1, 60))," ")
        r=random.randint(1, 6)
        # random pour avoir environ les pourcentages des trains entre banlieue,grandes lignes et marchandise
        if  r== 1 :
            t.type_t="m"
        elif r>3:
            t.type_t="b"
        else:
            t.type_t="l"
        m=random.randint(0,12)
        t.nom=gares[m]
        d.append(t)
        numero=numero+1
    return d

# fonction pour faire choix echange par type de train
def countTypeTrain(type_train_arrivee,type_train_depart,count_m,count_l,count_b):
    echange_ok=False
    # arbre avec combinaisons des paires d'echange par type
    if type_train_arrivee=="m" and type_train_depart=="m":
               # si on n'a pas change plus de la moitie des trains de m (marchandise)
               if count_m+2 <= len(2*liste_train_depart)/100*(17/2) :
                   count_m+=2
                   echange_ok=True
               else:
                   # sinon on ne fait pas le changement
                   echange_ok=False
              
                   
    elif type_train_arrivee=="m" and type_train_depart=="l":
               if count_m+1 <= len(2*liste_train_depart)/100*(17/2) and count_l+1 <= len(liste_train_depart)/100*(28/2) :
                   count_m+=1
                   count_l+=1
                   echange_ok=True
               else:
                   # sinon on ne fait pas le changement
                   echange_ok=False
                   
    elif type_train_arrivee=="m" and type_train_depart=="b":
               if count_m+1 <= len(2*liste_train_depart)/100*(17/2) and count_b+1 <= len(liste_train_depart)/100*(55/2) :
                   count_m+=1
                   count_b+=1
                   echange_ok=True
               else:
                   # sinon on ne fait pas le changement
                   echange_ok=False
                   
    elif type_train_arrivee=="b" and type_train_depart=="m":
               if count_b+1 <= len(2*liste_train_depart)/100*(55/2) and count_m+1 <= len(liste_train_depart)/100*(17/2) :
                   count_m+=1
                   count_b+=1
                   echange_ok=True
               else:
                   # sinon on ne fait pas le changement
                   echange_ok=False

    elif type_train_arrivee=="b" and type_train_depart=="l":
               if count_b+1 <= len(2*liste_train_depart)/100*(55/2) and count_l+1 <= len(liste_train_depart)/100*(28/2) :
                   count_m+=1
                   count_l+=1
                   echange_ok=True
               else:
                   # sinon on ne fait pas le changement
                   echange_ok=False
      
    elif type_train_arrivee=="b" and type_train_depart=="b":
               if count_b+2 <= len(2*liste_train_depart)/100*(55/2) :
                   count_b+=2
                   echange_ok=True
               else:
                   # sinon on ne fait pas le changement
                   echange_ok=False
          
    elif type_train_arrivee=="l" and type_train_depart=="m":
               if count_l+1 <= len(2*liste_train_depart)/100*(28/2) and count_m+1 <= len(liste_train_depart)/100*(17/2) :
                   count_l+=1
                   count_m+=1
                   echange_ok=True
               else:
                   # sinon on ne fait pas le changement
                   echange_ok=False
          
    elif type_train_arrivee=="l" and type_train_depart=="l":
               if count_l+2 <= len(2*liste_train_depart)/100*(28/2) :
                   count_l+=2
                   echange_ok=True
               else:
                   # sinon on ne fait pas le changement
                   echange_ok=False
                   
    elif type_train_arrivee=="l" and type_train_depart=="b":
               if count_l+1 <= len(2*liste_train_depart)/100*(28/2) and count_b+1 <= len(liste_train_depart)/100*(55/2):
                   count_l+=2
                   echange_ok=True
               else:
                   # sinon on ne fait pas le changement
                   echange_ok=False
                   
    return echange_ok,count_m,count_l,count_b

# fonction pour trier listes trains par plage horaire
def triParHeure(liste_train_depart,liste_train_arrivee):
    
    l_5h,l_6h,l_7h,l_8h,l_9h,l_10h,l_11h,l_12h = [],[],[],[],[],[],[],[]
    l_13h,l_14h,l_15h,l_16h,l_17h,l_18h,l_19h = [],[],[],[],[],[],[]
    l_20h,l_21h,l_22h,l_23h = [],[],[],[]
    for x in range(len(liste_train_depart)):
            
        if liste_train_arrivee[x].horaire >= datetime.timedelta(hours=5) and liste_train_arrivee[x].horaire < datetime.timedelta(hours=6) :
            l_5h.append(liste_train_arrivee[x])
        elif liste_train_arrivee[x].horaire >= datetime.timedelta(hours=6) and liste_train_arrivee[x].horaire < datetime.timedelta(hours=7) :
            l_6h.append(liste_train_arrivee[x])
        elif liste_train_arrivee[x].horaire >= datetime.timedelta(hours=7) and liste_train_arrivee[x].horaire < datetime.timedelta(hours=8) :
            l_7h.append(liste_train_arrivee[x])
        elif liste_train_arrivee[x].horaire >= datetime.timedelta(hours=8) and liste_train_arrivee[x].horaire < datetime.timedelta(hours=9) :
            l_8h.append(liste_train_arrivee[x])
        elif liste_train_arrivee[x].horaire >= datetime.timedelta(hours=9) and liste_train_arrivee[x].horaire < datetime.timedelta(hours=10) :
            l_9h.append(liste_train_arrivee[x])
        elif liste_train_arrivee[x].horaire >= datetime.timedelta(hours=10) and liste_train_arrivee[x].horaire < datetime.timedelta(hours=11) :
            l_10h.append(liste_train_arrivee[x])
        elif liste_train_arrivee[x].horaire >= datetime.timedelta(hours=11) and liste_train_arrivee[x].horaire < datetime.timedelta(hours=12) :
            l_11h.append(liste_train_arrivee[x])
        elif liste_train_arrivee[x].horaire >= datetime.timedelta(hours=12) and liste_train_arrivee[x].horaire < datetime.timedelta(hours=13) :
            l_12h.append(liste_train_arrivee[x])
        elif liste_train_arrivee[x].horaire >= datetime.timedelta(hours=13) and liste_train_arrivee[x].horaire < datetime.timedelta(hours=14) :
            l_13h.append(liste_train_arrivee[x])
        elif liste_train_arrivee[x].horaire >= datetime.timedelta(hours=14) and liste_train_arrivee[x].horaire < datetime.timedelta(hours=15) :
            l_14h.append(liste_train_arrivee[x])
        elif liste_train_arrivee[x].horaire >= datetime.timedelta(hours=15) and liste_train_arrivee[x].horaire < datetime.timedelta(hours=16) :
            l_15h.append(liste_train_arrivee[x])
        elif liste_train_arrivee[x].horaire >= datetime.timedelta(hours=16) and liste_train_arrivee[x].horaire < datetime.timedelta(hours=17) :
            l_16h.append(liste_train_arrivee[x])
        elif liste_train_arrivee[x].horaire >= datetime.timedelta(hours=17) and liste_train_arrivee[x].horaire < datetime.timedelta(hours=18) :
            l_17h.append(liste_train_arrivee[x])
        elif liste_train_arrivee[x].horaire >= datetime.timedelta(hours=18) and liste_train_arrivee[x].horaire < datetime.timedelta(hours=19) :
            l_18h.append(liste_train_arrivee[x])
        elif liste_train_arrivee[x].horaire >= datetime.timedelta(hours=19) and liste_train_arrivee[x].horaire < datetime.timedelta(hours=20) :
            l_19h.append(liste_train_arrivee[x])
        elif liste_train_arrivee[x].horaire >= datetime.timedelta(hours=20) and liste_train_arrivee[x].horaire < datetime.timedelta(hours=21) :
            l_20h.append(liste_train_arrivee[x])
        elif liste_train_arrivee[x].horaire >= datetime.timedelta(hours=21) and liste_train_arrivee[x].horaire < datetime.timedelta(hours=22) :
            l_21h.append(liste_train_arrivee[x])
        elif liste_train_arrivee[x].horaire >= datetime.timedelta(hours=22) and liste_train_arrivee[x].horaire < datetime.timedelta(hours=23) :
            l_22h.append(liste_train_arrivee[x])
        else:
            l_23h.append(liste_train_arrivee[x])
            
        if liste_train_depart[x].horaire >= datetime.timedelta(hours=5) and liste_train_depart[x].horaire < datetime.timedelta(hours=6) :
            l_5h.append(liste_train_depart[x])
        elif liste_train_depart[x].horaire >= datetime.timedelta(hours=6) and liste_train_depart[x].horaire < datetime.timedelta(hours=7) :
            l_6h.append(liste_train_depart[x])
        elif liste_train_depart[x].horaire >= datetime.timedelta(hours=7) and liste_train_depart[x].horaire < datetime.timedelta(hours=8) :
            l_7h.append(liste_train_depart[x])
        elif liste_train_depart[x].horaire >= datetime.timedelta(hours=8) and liste_train_depart[x].horaire < datetime.timedelta(hours=9) :
            l_8h.append(liste_train_depart[x])
        elif liste_train_depart[x].horaire >= datetime.timedelta(hours=9) and liste_train_depart[x].horaire < datetime.timedelta(hours=10) :
            l_9h.append(liste_train_depart[x])
        elif liste_train_depart[x].horaire >= datetime.timedelta(hours=10) and liste_train_depart[x].horaire < datetime.timedelta(hours=11) :
            l_10h.append(liste_train_depart[x])
        elif liste_train_depart[x].horaire >= datetime.timedelta(hours=11) and liste_train_depart[x].horaire < datetime.timedelta(hours=12) :
            l_11h.append(liste_train_depart[x])
        elif liste_train_depart[x].horaire >= datetime.timedelta(hours=12) and liste_train_depart[x].horaire < datetime.timedelta(hours=13) :
            l_12h.append(liste_train_depart[x])
        elif liste_train_depart[x].horaire >= datetime.timedelta(hours=13) and liste_train_depart[x].horaire < datetime.timedelta(hours=14) :
            l_13h.append(liste_train_depart[x])
        elif liste_train_depart[x].horaire >= datetime.timedelta(hours=14) and liste_train_depart[x].horaire < datetime.timedelta(hours=15) :
            l_14h.append(liste_train_depart[x])
        elif liste_train_depart[x].horaire >= datetime.timedelta(hours=15) and liste_train_depart[x].horaire < datetime.timedelta(hours=16) :
            l_15h.append(liste_train_depart[x])
        elif liste_train_depart[x].horaire >= datetime.timedelta(hours=16) and liste_train_depart[x].horaire < datetime.timedelta(hours=17) :
            l_16h.append(liste_train_depart[x])
        elif liste_train_depart[x].horaire >= datetime.timedelta(hours=17) and liste_train_depart[x].horaire < datetime.timedelta(hours=18) :
            l_17h.append(liste_train_depart[x])
        elif liste_train_depart[x].horaire >= datetime.timedelta(hours=18) and liste_train_depart[x].horaire < datetime.timedelta(hours=19) :
            l_18h.append(liste_train_depart[x])
        elif liste_train_depart[x].horaire >= datetime.timedelta(hours=19) and liste_train_depart[x].horaire < datetime.timedelta(hours=20) :
            l_19h.append(liste_train_depart[x])
        elif liste_train_depart[x].horaire >= datetime.timedelta(hours=20) and liste_train_depart[x].horaire < datetime.timedelta(hours=21) :
            l_20h.append(liste_train_depart[x])
        elif liste_train_depart[x].horaire >= datetime.timedelta(hours=21) and liste_train_depart[x].horaire < datetime.timedelta(hours=22) :
            l_21h.append(liste_train_depart[x])
        elif liste_train_depart[x].horaire >= datetime.timedelta(hours=22) and liste_train_depart[x].horaire < datetime.timedelta(hours=23) :
            l_22h.append(liste_train_depart[x])
        else:
            l_23h.append(liste_train_depart[x])
            
    return l_5h,l_6h,l_7h,l_8h,l_9h,l_10h,l_11h,l_12h,l_13h,l_14h,l_15h,l_16h,l_17h,l_18h,l_19h,l_20h,l_21h,l_22h,l_23h        
  
# fonction pour faire echange horaires
def choixEchange(l_h,count_m,count_l,count_b,liste_return):
    
    for x in range(0,len(l_h),2):
        # l_h[x]  -> train_arrivee
        # l_h[x+1]-> train_depart
        if l_h[x].horaire+datetime.timedelta(minutes=5) >= l_h[x+1].horaire or l_h[x].horaire-datetime.timedelta(minutes=5) <= l_h[x+1].horaire : 
           type_train_arrivee = l_h[x].type_t
           type_train_depart = l_h[x+1].type_t
           echange_ok,count_m,count_l,count_b = countTypeTrain(type_train_arrivee,type_train_depart,count_m,count_l,count_b)
           if echange_ok == True : 
               # alors on peut faire la modification d'horaire
               l_h[x].horaire = l_h[x+1].horaire
               liste_return.append(l_h[x])
               liste_return.append(l_h[x+1])
           else:
                # sinon on ne fait pas le changement
                liste_return.append(l_h[x])
                liste_return.append(l_h[x+1])
        else:
            # sinon on ne fait pas le changement
            liste_return.append(l_h[x])
            liste_return.append(l_h[x+1])
            
    
    return liste_return,count_m,count_l,count_b
    
  
# algo heuristique  
def algoHeuristique(liste_train_depart,liste_train_arrivee):
    # initialisation des variables
    l_5h,l_6h,l_7h,l_8h,l_9h,l_10h,l_11h,l_12h = [],[],[],[],[],[],[],[]
    l_13h,l_14h,l_15h,l_16h,l_17h,l_18h,l_19h = [],[],[],[],[],[],[]
    l_20h,l_21h,l_22h,l_23h = [],[],[],[]
    liste_return=[]
    count_m,count_b,count_l=0,0,0
    x_5h,x_6h,x_7h,x_8h,x_9h,x_10h,x_11h,x_12h = False,False,False,False,False,False,False,False
    x_13h,x_14h,x_15h,x_16h,x_17h,x_18h,x_19h = False,False,False,False,False,False,False
    x_20h,x_21h,x_22h,x_23h = False,False,False,False
    
    # Appel de fonction pour trier les horaires par plage horaire 5h/23h
    l_5h,l_6h,l_7h,l_8h,l_9h,l_10h,l_11h,l_12h,l_13h,l_14h,l_15h,l_16h,l_17h,l_18h,l_19h,l_20h,l_21h,l_22h,l_23h = triParHeure(liste_train_depart,liste_train_arrivee)

    # Arbre if pour changer liste en nombre pair si impair
    if len(l_5h) % 2 != 0:
        train_5h_enleve = l_5h[-1]
        l_5h.pop()
        x_5h=True
    if len(l_6h) % 2 != 0:
        train_6h_enleve = l_6h[-1]
        l_6h.pop()
        x_6h=True
    if len(l_7h) % 2 != 0:
        train_7h_enleve = l_7h[-1]
        l_7h.pop()
        x_7h=True
    if len(l_8h) % 2 != 0:
        train_8h_enleve = l_8h[-1]
        l_8h.pop()
        x_8h=True
    if len(l_9h) % 2 != 0:
        train_9h_enleve = l_9h[-1]
        l_9h.pop()
        x_9h=True
    if len(l_10h) % 2 != 0:
        train_10h_enleve = l_10h[-1]
        l_10h.pop()
        x_10h=True
    if len(l_11h) % 2 != 0:
        train_11h_enleve = l_11h[-1]
        l_11h.pop()
        x_11h=True
    if len(l_12h) % 2 != 0:
        train_12h_enleve = l_12h[-1]
        l_12h.pop()
        x_12h=True
    if len(l_13h) % 2 != 0:
        train_13h_enleve = l_13h[-1]
        l_13h.pop()
        x_13h=True
    if len(l_14h) % 2 != 0:
        train_14h_enleve = l_14h[-1]
        l_14h.pop()
        x_14h=True
    if len(l_15h) % 2 != 0:
        train_15h_enleve = l_15h[-1]
        l_15h.pop()
        x_15h=True
    if len(l_16h) % 2 != 0:
        train_16h_enleve = l_16h[-1]
        l_16h.pop()
        x_16h=True
    if len(l_17h) % 2 != 0:
        train_17h_enleve = l_17h[-1]
        l_17h.pop()
        x_17h=True
    if len(l_18h) % 2 != 0:
        train_18h_enleve = l_18h[-1]
        l_18h.pop()
        x_18h=True
    if len(l_19h) % 2 != 0:
        train_19h_enleve = l_19h[-1]
        l_19h.pop()
        x_19h=True
    if len(l_20h) % 2 != 0:
        train_20h_enleve = l_20h[-1]
        l_20h.pop()
        x_20h=True
    if len(l_21h) % 2 != 0:
        train_21h_enleve = l_21h[-1]
        l_21h.pop()
        x_21h=True
    if len(l_22h) % 2 != 0:
        train_22h_enleve = l_22h[-1]
        l_22h.pop()
        x_22h=True
    if len(l_23h) % 2 != 0:
        train_23h_enleve = l_23h[-1]
        l_23h.pop()
        x_23h=True
        
    # appel de fonction pour faire le choix de l'echange horaires par plage horaire
    liste_return,count_m,count_l,count_b = choixEchange(l_5h,count_m,count_l,count_b,liste_return)
           
    if x_5h==True :
        liste_return.append(train_5h_enleve)
    
    liste_return,count_m,count_l,count_b = choixEchange(l_6h,count_m,count_l,count_b,liste_return)

    if x_6h==True :
        liste_return.append(train_6h_enleve)           

    liste_return,count_m,count_l,count_b = choixEchange(l_7h,count_m,count_l,count_b,liste_return)
           
    if x_7h==True :
        liste_return.append(train_7h_enleve)
        
    liste_return,count_m,count_l,count_b = choixEchange(l_8h,count_m,count_l,count_b,liste_return)

    if x_8h==True :
        liste_return.append(train_8h_enleve)
        
    liste_return,count_m,count_l,count_b = choixEchange(l_9h,count_m,count_l,count_b,liste_return)

    if x_9h==True :
        liste_return.append(train_9h_enleve)
        
    liste_return,count_m,count_l,count_b = choixEchange(l_10h,count_m,count_l,count_b,liste_return)

    if x_10h==True :
        liste_return.append(train_10h_enleve)
           
    liste_return,count_m,count_l,count_b = choixEchange(l_11h,count_m,count_l,count_b,liste_return)

    if x_11h==True :
        liste_return.append(train_11h_enleve)
           
    liste_return,count_m,count_l,count_b = choixEchange(l_12h,count_m,count_l,count_b,liste_return)

    if x_12h==True :
        liste_return.append(train_12h_enleve)
           
    liste_return,count_m,count_l,count_b = choixEchange(l_13h,count_m,count_l,count_b,liste_return)

    if x_13h==True:
        liste_return.append(train_13h_enleve)
           
    liste_return,count_m,count_l,count_b = choixEchange(l_14h,count_m,count_l,count_b,liste_return)

    if x_14h==True :
        liste_return.append(train_14h_enleve)
        
    liste_return,count_m,count_l,count_b = choixEchange(l_15h,count_m,count_l,count_b,liste_return)

    if x_15h==True :
        liste_return.append(train_15h_enleve)
           
    liste_return,count_m,count_l,count_b = choixEchange(l_16h,count_m,count_l,count_b,liste_return)

    if x_16h==True:
        liste_return.append(train_16h_enleve)
        
    liste_return,count_m,count_l,count_b = choixEchange(l_17h,count_m,count_l,count_b,liste_return)

    if x_17h==True:
        liste_return.append(train_17h_enleve)
           
    liste_return,count_m,count_l,count_b = choixEchange(l_18h,count_m,count_l,count_b,liste_return)

    if x_18h==True:
        liste_return.append(train_18h_enleve)
        
    liste_return,count_m,count_l,count_b = choixEchange(l_19h,count_m,count_l,count_b,liste_return)

    if x_19h==True:
        liste_return.append(train_19h_enleve)
           
    liste_return,count_m,count_l,count_b = choixEchange(l_20h,count_m,count_l,count_b,liste_return)
           
    if x_20h==True:
        liste_return.append(train_20h_enleve)      
        
    liste_return,count_m,count_l,count_b = choixEchange(l_21h,count_m,count_l,count_b,liste_return)

    if x_21h==True:
        liste_return.append(train_21h_enleve)
           
    liste_return,count_m,count_l,count_b = choixEchange(l_22h,count_m,count_l,count_b,liste_return)

    if x_22h==True:
        liste_return.append(train_22h_enleve)
           
    liste_return,count_m,count_l,count_b = choixEchange(l_23h,count_m,count_l,count_b,liste_return)
    
    if x_23h==True:
        liste_return.append(train_23h_enleve)        
    
    return liste_return

# entree nombre trains
val=0
while val==0:
    entree = input ("Entrez un nombre pair: ")

    if (int(entree))%2==0:
        print("Création de ",entree," trains")
        val=1
    else:
        print("Ce n'est pas un nombre pair!")

val = int(entree)

nb_trains_entree=int(entree)

# generation simulation liste horaires
liste_train=generateurTrain(nb_trains_entree)

for x in range(len(liste_train)):
    print(liste_train[x].num,liste_train[x].nom,liste_train[x].horaire,liste_train[x].sens,liste_train[x].type_t)
print(" ")

liste_train_arrivee = []
for train in liste_train :
  if train.sens == "arrivee" :
    liste_train_arrivee.append(train)

liste_train_depart = []
for train in liste_train :
  if train.sens == "depart" :
    liste_train_depart.append(train)

liste_train_arrivee.sort()
liste_train_depart.sort()

ex = algoHeuristique(liste_train_depart,liste_train_arrivee)

# liste horaires modifiees
print("HORAIRES TRAINS")
for x in range(len(ex)):
   print(ex[x].nom,ex[x].horaire)

# bloc pour tester temps execution algorithme
# import time

# l_time = []
# temp=0
# axe_x = []
# for x in range(100,20000,100):
        # axe_x.append(x)
        # liste_train=generateurTrain(x)
        
        # liste_train_arrivee = []
        # for train in liste_train : 
          # if train.sens == "arrivee" :
            # liste_train_arrivee.append(train)
        
        # liste_train_depart = []
        # for train in liste_train : 
          # if train.sens == "depart" :
            # liste_train_depart.append(train)
            
        # liste_train_arrivee.sort()
        # liste_train_depart.sort()
        # print("cycle nb : {}".format(temp))
        # start = time.time()
        # d = algoOptimisePlageHoraire(liste_train_depart, liste_train_arrivee)
        # end = time.time()
        # l_time.append(end-start)
        # temp+=1
# for x in range(len(l_time)):
    # print(l_time[x])
    
# import matplotlib.pyplot as plt

    

# plt.plot(axe_x,l_time)
# plt.xlabel('Nombre de trains')
# plt.ylabel('Temps execution')
# plt.show()
