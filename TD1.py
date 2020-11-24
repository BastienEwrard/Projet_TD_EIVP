# Importations

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

# 2 lignes pour le csv, impossible de travailler à deux sur la même ligne, commentaire à déplacer

# tableau = pd.read_csv(r"C:\Users\perso\Documents\GitHub\Projet_TD_EIVP\EIVP_KM.csv", sep = ";")
tableau = pd.read_csv(r"EIVP_KM.csv", sep=";")
print(tableau)
##########
#print(tableau(sent_at))##########probleme######## qui est le meme pour le tout dernier programe
##########

## Courbe
##cette partie permet a l'utilisateur de selectione le capteur ainsi que la collone du tableau pour, par la suite effectuer les calcule  statistique et detecter les anomalies 
indice = input("donner l'indice du capteur (entre 1 et 6) :")
mycolomn = input('donner le nom de la colonne (temp, noise, humidity, co2, lum) :')
# indice = 1
# mycolomn = "temp"


liste = tableau.loc[(tableau["id"] == int(indice)), [mycolomn]]
liste = liste.values.tolist()

print(liste)

plt.plot(tableau.loc[(tableau["id"]== int(indice)),'sent_at'],liste)
plt.show()


# Fonctions statistiques

def min(liste):
    if len(liste) == 1 or len(liste) == 0: #on regarde si la liste est vide ou ne comporte que un elemeant dans de cas le resultat est trivial 
        return 0
    a = liste[0]
    for i in range(1, len(liste)): # on parcourt la liste en regardant a chaque fois si l'element et le plus grand ( ou le plus petit ) et on renvoie a la fin le max(ou le mon)
        if a > liste[i][0]:
            a = liste[i][0]
    return a


def max(liste):
    if len(liste) == 1 or len(liste) == 0:
        return 0
    a = liste[0]
    for i in range(1, len(liste)) == 0:
        if a < liste[i][0]:
            a = liste[i][0]
    return a


def moyenne(liste):
    if len(liste) == 0 or len(liste) == 1:
        return 0
    a = 0
    for i in range(1, len(liste)):
        a = a + liste[i][0]
    return a / len(liste)


def variance(liste):
    a = 0
    if len(liste) == 0 or len(liste) == 1:
        return 0
    for i in range(1, len(liste)):
        a = a + (liste[i][0] - moyenne(liste))**2
    return a / len(liste)


def ecartType(liste):
    return np.sqrt(variance(liste))


def quicksort(liste):
    if L == []:
        return L
    else:
        To = L[0]
        Tinf = []
        Tsup = []
        for x in L[1:]:
            if x <= To:
                Tinf.append(x)
            else:
                Tsup.append(x)
    return quicksort(Tinf) + [To] + quicksort(Tsup)


def medianne(liste):
    L = quicksort(liste)
    return L[len(liste) / 2]


def humidex(temperature, humidity):
    humidex = temperature + \
        (5 / 9) * (6.112 * (10 * (7.5 * (temperature / (237.7 + temperature))))
                   * (humidity / 100) - 10)
    return humidex

# calcule de l’indice de corrélation entre un couple de variables
# on a besoin de la variance ainsi que de la covariance pour calculer l'indide de persan


def covariance(X, Y):
    if len(X) != len(Y):
        return 0
    sum = 0
    moyX = moyenne(X)
    moyY = moyenne(Y)

    for i in range(len(X)):
        sum += ((X[i] - moyX) * (Y[i] - moyY))
    return sum / len(X)


def coefficient(X, Y):
    pr = covariance(X, Y) / sqrt(variance(X) * variance(Y))
    return pr
    plt.plot(X, sent_at)
    plt.plot(Y, sent_at)
    plt.title("graphique des deux courbes représentant les deux variables en fonction du temps, la valeur du coefficient de corrélation est : %i" % pr)
    plt.show()

# Recherche des anomalies

# anomalies = valeur manquantes, seuil de normalité, étude stat autour de la moyenne


def manquantes(liste):
    pos = []
    for i in range(0, len(liste)):
        if liste[i] == []:
            pos.append(i)
        elif liste[i][0] == 0 and liste[i + 1][0] == 0:
            pos.append(i)
            pos.append(i + 1)
    return pos


def anomalieStat(liste):
    pos = []
    m = moyenne(liste)
    e = ecartType(liste)
    for i in range(len(liste)):
        if liste[i][0] > m + 2 * e:
            pos.append(i)
    return pos


def anomalies(liste):
    pos = manquantes(liste) + anomalieStat(liste)
    if pos == []:
        return "pas d'anomalies détectées"
    else:
        return 'anomalies détectées', pos


# detecter si une valeur est aberente par exemple -30 °C ou plus 60°C a Paris

def anomaliesAberation(liste):
    pos = []
    time = []
    for i in range(len(liste)):
        if liste[i][0] > 20 or liste[i][0] < -30:
            pos.append(liste[i][0])
            time.append(sent_at[i])
    return [pos, time]

##########
# def afficherAnomalies(liste):
# 	anomalies=anomaliesAberation(liste)
# 	rang = len(anomalies[0])
# 	pos,time = anomalies[0],anomalies[1]
# 	for i in range(rang):
# 		plt.text(time[i], pos[i], r'Anomalie')
# 		plt.plot(tableau.loc[(tableau["id"]== int(indice)),'sent_at'],liste)
# 		print(time[i], pos[i])
# 		plt.show()


# afficherAnomalies(liste)
##########
