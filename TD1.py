## Importations

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime


#utilise impout pour date de debut et date de fin

#tableau = pd.read_csv(r"C:\Users\perso\Documents\GitHub\Projet_TD_EIVP\EIVP_KM.csv", sep = ";")
tableau = pd.read_csv(r"EIVP_KM.csv", sep = ";")

print(tableau)
saved_column = tableau.column_name


## Courbe

mycolomns = ['temp','humidity']
print(tableau[mycolomns])

plt.plot(tableau['sent_at'],tableau['noise'])
plt.show()

def min(liste):
	if len(liste)==1 or len(liste)==0:
		return 0
	a = liste[0]
	for i in range(1,len(liste)):
		if a >liste[i]:
			a = liste[i]
	return a

def max(liste):
	if len(liste)==1 or len(liste)==0:
		return 0
	a = liste[0]
	for i in range(1,len(liste))==0:
		if a < liste[i]:
			a = liste[i]
	return a


def moyenne(liste):
	if len(liste)== 0 or len(liste)==1:
		return 0
	a = 0
	for i in range(1,len(liste)):
		a+=liste(i)
	return a/len(liste)


def variance(liste):
	if len(liste)== 0 or len(liste)==1:
		return 0
	for i in range(1,len(liste)):
		a+= (liste[i]-moyenne(liste))**2
	return a/len(liste)

def ecartType(liste):
	return sqrt(variance(liste))


def quicksort(L):
    if L==[]:
        return L
    else :
        To=L[0]
        Tinf=[]
        Tsup=[]
        for x in L[1:]:
            if x<=To:
                Tinf.append(x)
            else:
                Tsup.append(x)
        return quicksort(Tinf)+[To]+quicksort(Tsup)

def medianne(liste):
	L = quicksort(liste)
	return L[len(liste)/2]

def humidex(temperature,humitité):
