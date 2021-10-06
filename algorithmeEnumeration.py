# -*- coding: utf-8 -*-
"""
Created on Sun May  9 17:48:18 2021

@author: User
"""

import datetime
import random
import copy

class Train :
  """Classe qui représente objet Train
     Parametres :
     nom : string
     sens : string
     horaire : datetime.time"""

  def __init__(self,num,nom,sens,horaire,type_t):
    self.num=num
    self.nom = nom
    self.sens = sens
    self.horaire = horaire
    self.type_t = type_t

# Initialisation objets

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

import itertools
from itertools import combinations
from itertools import permutations


def enumeration(liste_train_depart,liste_train_arrivee,taille):
    #enum pour nb_depart=nb_arrivee

    temp1_l=[]
    temp2_l=[]
    temp3_l=[]
    count = 0
    liste_return=[]#toutes les possibilités

    list_fin=[]#meilleure possibilité en changeant depart
    list_fin2=[] #meilleure possibilité en changeant arrivee
    # produit cartesien des 2 listes
    prod = list(itertools.product(liste_train_arrivee,liste_train_depart))

    # permutation du produit des 2 listes
    permut_prod = list(itertools.permutations(prod, taille))


    # parcours de la liste afin de convertir tuples en liste
    for x in range(len(permut_prod)):
        for y in range(len(permut_prod[x])):
            temp1_l = list(permut_prod[x][y])
            temp2_l.append((temp1_l[0]))
            temp2_l.append(temp1_l[1])
            count+=1
            if count==taille:
                count=0
                temp3_l.append(temp2_l)
                temp2_l=[]

    # parcours des permutations afin d'enlever
    # les combinaisons qu'on n'a pas besoin (duplicats)
    for x in range(len(temp3_l)):
        temp3_l_set = set(temp3_l[x])
        if len(temp3_l_set)==len(temp3_l[x]):
            liste_return.append(temp3_l[x])


    liste_return2 = copy.deepcopy(liste_return)

    #calculer pénalités pour chaque liste possible en changeant depart
    penalites=10000
    nv_penalites=0 #valeur temporaire
    #nbre approximatif de trains de chaque type
    nb_m=(len(liste_train))/6
    nb_l=(len(liste_train))/3
    nb_b=(len(liste_train))/2

    for x in range(len(liste_return)):
        nv_penalites=0
        m_modif=0
        l_modif=0
        b_modif=0
        for y in range(len(liste_return[x])):
            if(liste_return[x][y].sens=="depart"): #ici on ne modifie que les trains au départ
                if((liste_return[x][y].horaire)!=(liste_return[x][y-1].horaire)):
                    if(liste_return[x][y].type_t=="m"):
                        nv_penalites=nv_penalites+3
                        m_modif=m_modif+1
                    elif(liste_return[x][y].type_t=="l"):
                        nv_penalites=nv_penalites+2
                        l_modif=l_modif+1
                    elif(liste_return[x][y].type_t=="b"):
                        nv_penalites=nv_penalites+1
                        b_modif=b_modif+1
        #ajouter penalites liees a la densite du traffic
        if(m_modif>nb_m):
            nv_penalites=nv_penalites+3
        elif(m_modif>0.75*nb_m):
            nv_penalites=nv_penalites+2
        elif(m_modif>0.5*nb_m):
            nv_penalites=nv_penalites+1
        if(l_modif>nb_l):
            nv_penalites=nv_penalites+3
        elif(l_modif>0.75*nb_l):
            nv_penalites=nv_penalites+2
        elif(l_modif>0.5*nb_l):
            nv_penalites=nv_penalites+1
        if(b_modif>nb_b):
            nv_penalites=nv_penalites+3
        elif(b_modif>0.75*nb_b):
            nv_penalites=nv_penalites+2
        elif(b_modif>0.5*nb_b):
            nv_penalites=nv_penalites+1
       #si liste meilleure que l'actuelle meilleure liste
        if(nv_penalites<penalites):
            penalites=nv_penalites
            list_fin[:]=[]
            for a in range(len(liste_return[x])):
                list_fin.append(liste_return[x][a])

    #changer horaires
    nb_economies=0
    trains_changes=[]
    for a in range(len(list_fin)):
        if(list_fin[a].sens=="depart"):
            if((list_fin[a].horaire)!=(list_fin[a-1].horaire)):
                nb_economies=nb_economies+1
                list_fin[a].horaire=list_fin[a-1].horaire
                trains_changes.append(list_fin[a])

    #calculer pénalités pour chaque liste possible en changeant arrivees
    penalites2=1000
    for x in range(len(liste_return2)):
        nv_penalites2=0
        m_modif=0
        l_modif=0
        b_modif=0
        for y in range(len(liste_return2[x])):
            if(liste_return2[x][y].sens=="arrivee"): #ici on ne modifie que les trains a l'arrivee
                if((liste_return2[x][y].horaire)!=(liste_return2[x][y+1].horaire)):
                    if(liste_return2[x][y].type_t=="m"):
                        nv_penalites2=nv_penalites2+3
                        m_modif=m_modif+1
                    elif(liste_return2[x][y].type_t=="l"):
                        nv_penalites2=nv_penalites2+2
                        l_modif=l_modif+1
                    elif(liste_return2[x][y].type_t=="b"):
                        nv_penalites2=nv_penalites2+1
                        b_modif=b_modif+1
        if(m_modif>nb_m):
            nv_penalites2=nv_penalites2+3
        elif(m_modif>0.75*nb_m):
            nv_penalites2=nv_penalites2+2
        elif(m_modif>0.5*nb_m):
            nv_penalites2=nv_penalites2+1
        if(l_modif>nb_l):
            nv_penalites2=nv_penalites2+3
        elif(l_modif>0.75*nb_l):
            nv_penalites2=nv_penalites2+2
        elif(l_modif>0.5*nb_l):
            nv_penalites2=nv_penalites2+1
        if(b_modif>nb_b):
            nv_penalites2=nv_penalites2+3
        elif(b_modif>0.75*nb_b):
            nv_penalites2=nv_penalites2+2
        elif(b_modif>0.5*nb_b):
            nv_penalites2=nv_penalites2+1
       #si liste meilleure que l'actuelle meilleure liste
        if(nv_penalites2<penalites2):
            penalites2=nv_penalites2
            list_fin2[:]=[]
            for a in range(len(liste_return2[x])):
                list_fin2.append(liste_return2[x][a])

    #changer horaires
    nb_economies2=0
    trains_changes2=[]
    for a in range(len(list_fin2)):
        if(list_fin2[a].sens=="arrivee"):
            if((list_fin2[a].horaire)!=(list_fin2[a+1].horaire)):
                nb_economies2=nb_economies2+1
                list_fin2[a].horaire=list_fin2[a+1].horaire
                trains_changes2.append(list_fin2[a])

    #il y a deux possibilites, meilleure liste en changeant depart et meilleure liste en changeant arrivees
    #garder celle qui a le moins de penalites et faire les affichages correspondants
    if(penalites<=penalites2):
        print(" ")
        print("pénalités : ",penalites)
        print(" ")
        print("Trains à modifier :")
        for x in range(len(trains_changes2)):
            print(trains_changes[x].num,trains_changes[x].nom,trains_changes[x].horaire)
    else:
        print(" ")
        print("pénalités : ",penalites2)
        print(" ")
        print("Trains à modifier :")
        for x in range(len(trains_changes2)):
            print(trains_changes2[x].num,trains_changes2[x].nom,trains_changes2[x].horaire)

    print(" ")
    return list_fin

#demander a l'utilisateur de choisir le nombre de trains
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

#generer liste de trains
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

taille=nb_trains_entree//2
ex = enumeration(liste_train_depart,liste_train_arrivee,taille)

#afficher trains apres changements
print("HORAIRES TRAINS")
for x in range(len(ex)):
   print(ex[x].nom,ex[x].horaire)
