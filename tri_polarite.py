from collections import OrderedDict

liste_un = [0 for i in range(0,28)]
liste_deux = [0 for i in range(0,28)]
liste_trois = [0 for i in range(0,28)]
liste_quatre = [0 for i in range(0,28)]
liste_cinq = [0 for i in range(0,28)]
liste_six = [0 for i in range(0,28)]
liste_sept = [0 for i in range(0,28)]
liste_huit = [0 for i in range(0,28)]
liste_neuf = [0 for i in range(0,28)]
liste_dix = [0 for i in range(0,28)]
liste_onze = [0 for i in range(0,28)]
liste_douze = [0 for i in range(0,28)]
liste_treize = [0 for i in range(0,28)]
liste_quatorze = [0 for i in range(0,28)]
liste_quinze = [0 for i in range(0,28)]
liste_seize = [0 for i in range(0,28)]
liste_dixsept = [0 for i in range(0,28)]
liste_dixhuit = [0 for i in range(0,28)]
liste_dixneuf = [0 for i in range(0,28)]
liste_vingt = [0 for i in range(0,28)]
liste_vingtun = [0 for i in range(0,28)]
liste_vingtdeux = [0 for i in range(0,28)]
liste_vingttrois = [0 for i in range(0,28)]
liste_vingtquatre = [0 for i in range(0,28)]
liste_vingtcinq = [0 for i in range(0,28)]
liste_vingtsix = [0 for i in range(0,28)] # on cree les 26 listes qui vont comprendre les mots de taille 1 à 26 

Alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"] #on cree l'alphabet
listes = [liste_un, liste_deux, liste_trois, liste_quatre, liste_cinq, liste_six, liste_sept, liste_huit, liste_neuf, liste_dix, liste_onze, liste_douze, liste_treize, liste_quatorze, liste_quinze, liste_seize, liste_dixsept, liste_dixhuit, liste_dixneuf, liste_vingt, liste_vingtun, liste_vingtdeux, liste_vingttrois, liste_vingtquatre, liste_vingtcinq, liste_vingtsix]
#on met les listes dans un liste pour faciliter tout les programmes qui suivront (faire une boucle "for" au lieu de faire 26 "if")

ftest = open('src/data/pli07.txt','r')
lines = ftest.readlines() #on recupère le dictionnaire dans lines

nombre_lignes = 78854 #nombre de lignes

def lettres() :
    nb_mots = 0
    for i in range(0,nombre_lignes+1) : 
        nb_mots += 1 
        line = lines[i].rstrip()
        for a in range(0,26) : 
            if len(line) == a+1 : # on regarde la taille du mot
                listes[a][27] += 1 #alors on met en 27eme place dans le tableau "+1" (pour compter le nombre de mot de chaque taille)
                for j in line : #on parcourt le mot
                    for k in range(0,26) : #on regarde que lettre est en position k
                        if j == Alphabet[k] :
                            listes[a][k] += 1 #on ajoute 1 a la position "i" pour la lettre "i" (si il y a un A alors on rajoute 1 a la case 0, 1 a la case 1 pour B etc...)
                            listes[a][26] += 1 #on met en position 26 le nombre de lettre qu'il y a dans les mots de taille a
    return nb_mots #on renvoie le nombre de mot (pour s'assurer de ne pas en oublier)

lettres()


def ratio() : 
    for i in range(0,26) :
        for a in range(0,26) : #le 26 de taille mot
            if listes[a][26] != 0 :
                listes[a][i] = round(listes[a][i] / listes[a][26],4) #on fais le ratio du nombre de "A" par le nombre de lettre pour avoir le %age de A, pareil pour B etc...

ratio()


def montre_les_listes() : #on print les listes qui ont en position 0 le %age de la lettre A dans les mots de taille k, puis en position 1 pour B etc...
    res = 0
    for i in listes :
        for j in range(0, len(i)-2) :
            i[j] = (round(i[j]*100,8)) 
        print(sum(i) - i[26] - i[27])
        print(i)
        res += i[27] 
        print(res)

taille_un = [50.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 50.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2, 2]
taille_deux = [9.9, 2.48, 5.45, 3.47, 7.92, 2.48, 1.98, 4.46, 6.44, 2.48, 1.98, 2.48, 3.47, 5.94, 7.43, 4.46, 0.99, 2.97, 5.45, 3.47, 6.93, 4.95, 0.5, 0.99, 0.0, 0.99, 202, 101]
taille_trois = [9.5, 3.56, 5.34, 3.66, 9.25, 3.05, 2.49, 1.88, 7.42, 0.36, 0.91, 4.32, 4.22, 3.81, 6.96, 5.23, 0.46, 4.98, 5.95, 5.89, 4.98, 2.13, 0.51, 0.81, 1.17, 1.17, 1968, 656]
taille_quatre = [11.29, 2.21, 3.9, 2.62, 13.07, 2.33, 2.3, 1.54, 7.92, 0.69, 1.26, 4.95, 3.48, 4.32, 7.31, 3.41, 0.13, 6.73, 5.41, 4.99, 5.59, 1.54, 0.3, 0.91, 1.12, 0.66, 6688, 1672]
taille_cinq = [10.46, 3.0, 3.77, 2.47, 15.94, 1.72, 2.36, 1.57, 7.11, 0.52, 0.62, 5.35, 2.92, 5.59, 6.56, 2.95, 0.26, 7.85, 4.88, 5.42, 4.99, 1.63, 0.11, 0.57, 0.89, 0.48, 20035, 4007]
taille_six = [10.16, 2.58, 4.08, 2.64, 16.24, 1.62, 2.35, 1.61, 7.23, 0.35, 0.41, 4.99, 2.86, 5.88, 6.05, 2.71, 0.44, 9.0, 4.65, 5.66, 5.23, 1.43, 0.08, 0.55, 0.79, 0.4, 42876, 7146]
taille_sept = [9.89, 2.32, 4.19, 2.52, 16.71, 1.59, 2.25, 1.55, 7.41, 0.3, 0.26, 5.04, 2.76, 6.3, 5.6, 2.63, 0.48, 9.09, 4.76, 6.33, 5.19, 1.27, 0.08, 0.59, 0.57, 0.31, 70196, 10028]
taille_huit = [9.59, 1.97, 4.05, 2.53, 16.34, 1.58, 2.19, 1.51, 7.94, 0.23, 0.21, 4.96, 2.78, 6.91, 5.64, 2.67, 0.59, 8.97, 4.92, 6.8, 5.03, 1.18, 0.07, 0.53, 0.62, 0.19, 93256, 11657]
taille_neuf = [9.43, 1.8, 4.01, 2.47, 15.84, 1.45, 2.08, 1.52, 8.43, 0.18, 0.15, 4.84, 2.95, 7.44, 5.72, 2.67, 0.61, 8.52, 5.22, 7.42, 4.78, 1.14, 0.06, 0.51, 0.62, 0.15, 105327, 11703]
taille_dix = [9.01, 1.61, 4.16, 2.46, 15.2, 1.24, 1.92, 1.63, 8.83, 0.15, 0.11, 4.85, 3.14, 7.89, 6.18, 2.88, 0.69, 8.04, 5.53, 7.71, 4.52, 1.03, 0.04, 0.47, 0.59, 0.12, 98259, 9826]
taille_onze = [8.87, 1.55, 4.28, 2.26, 14.63, 1.18, 1.8, 1.62, 9.41, 0.15, 0.11, 4.82, 3.29, 8.05, 6.58, 2.82, 0.7, 7.62, 5.78, 8.05, 4.32, 0.96, 0.04, 0.44, 0.59, 0.1, 83765, 7615]
taille_douze = [8.45, 1.49, 4.31, 2.1, 14.42, 1.01, 1.67, 1.72, 9.74, 0.11, 0.07, 4.77, 3.42, 8.34, 6.79, 2.84, 0.84, 7.56, 6.13, 8.08, 4.2, 0.89, 0.03, 0.36, 0.57, 0.1, 65099, 5425]
taille_treize = [8.24, 1.42, 4.53, 1.98, 13.93, 1.0, 1.57, 1.75, 10.28, 0.11, 0.07, 4.55, 3.45, 8.32, 6.78, 2.75, 0.89, 7.5, 6.62, 8.29, 4.06, 0.83, 0.02, 0.35, 0.63, 0.09, 47333, 3641]
taille_quatorze = [8.0, 1.27, 4.38, 2.17, 14.09, 0.97, 1.33, 1.71, 10.35, 0.08, 0.05, 4.5, 3.66, 8.47, 6.96, 2.72, 0.96, 7.24, 6.65, 8.47, 4.13, 0.79, 0.02, 0.35, 0.59, 0.08, 31906, 2279]
taille_quinze = [7.9, 1.25, 4.37, 1.92, 13.97, 0.95, 1.36, 1.7, 10.33, 0.1, 0.05, 4.35, 3.7, 8.44, 7.13, 2.78, 0.83, 7.39, 6.94, 8.74, 3.95, 0.75, 0.02, 0.37, 0.63, 0.07, 21045, 1403]
taille_seize = [7.26, 1.2, 4.3, 1.89, 14.27, 0.78, 1.29, 2.11, 10.46, 0.08, 0.05, 5.05, 3.78, 8.53, 7.21, 2.78, 0.89, 7.59, 6.46, 8.48, 3.76, 0.57, 0.02, 0.28, 0.84, 0.08, 12128, 758]
taille_dixsept = [7.28, 1.01, 4.43, 1.97, 13.58, 0.59, 1.45, 2.05, 10.4, 0.07, 0.01, 4.79, 3.83, 8.74, 7.56, 2.93, 0.67, 7.36, 7.41, 8.26, 3.83, 0.73, 0.03, 0.44, 0.55, 0.03, 7310, 430]
taille_dixhuit = [7.79, 0.85, 3.99, 2.01, 13.43, 0.69, 1.83, 1.7, 10.49, 0.08, 0.0, 5.22, 4.45, 8.95, 8.23, 3.22, 0.46, 7.28, 6.71, 8.08, 3.32, 0.49, 0.0, 0.23, 0.46, 0.05, 3888, 216]
taille_dixneuf = [6.99, 0.74, 4.67, 1.66, 14.13, 0.52, 1.55, 2.28, 9.35, 0.07, 0.07, 5.59, 3.64, 9.02, 7.66, 2.83, 0.44, 7.58, 7.07, 8.39, 3.64, 0.77, 0.0, 0.33, 0.96, 0.04, 2717, 143]
taille_vingt = [6.91, 0.37, 3.09, 1.62, 14.34, 0.59, 1.99, 1.76, 10.37, 0.0, 0.0, 5.44, 2.5, 9.78, 8.24, 2.5, 0.37, 7.57, 8.09, 8.82, 3.82, 0.74, 0.0, 0.22, 0.88, 0.0, 1360, 68]
taille_vingtun = [8.81, 1.62, 3.23, 2.34, 14.2, 0.54, 1.62, 2.16, 9.16, 0.0, 0.0, 6.11, 2.61, 8.09, 6.56, 1.71, 0.45, 8.45, 7.64, 7.73, 4.04, 1.35, 0.0, 0.63, 0.81, 0.18, 1113, 53] 
taille_vingtdeux = [7.02, 0.0, 3.16, 1.4, 14.04, 0.35, 2.81, 3.51, 7.02, 0.7, 0.0, 6.32, 1.75, 7.37, 9.47, 3.86, 0.0, 8.77, 6.67, 8.42, 4.21, 1.4, 0.0, 0.0, 1.75, 0.0, 285, 13]
taille_vingttrois = [8.7, 0.0, 4.35, 0.72, 17.39, 0.0, 2.9, 4.35, 7.97, 0.0, 0.0, 4.35, 1.45, 8.7, 5.07, 3.62, 0.0, 7.97, 7.97, 9.42, 3.62, 1.45, 0.0, 0.0, 0.0, 0.0, 138, 6]
taille_vingtquatre = [8.33, 0.0, 5.21, 2.08, 15.62, 0.0, 1.04, 4.17, 7.29, 2.08, 1.04, 0.0, 2.08, 7.29, 4.17, 2.08, 0.0, 9.38, 13.54, 9.38, 5.21, 0.0, 0.0, 0.0, 0.0, 0.0, 96, 4]
taille_vingtcinq = [8.0, 0.0, 6.0, 2.0, 12.0, 0.0, 2.0, 2.0, 10.0, 0.0, 0.0, 4.0, 2.0, 12.0, 6.0, 2.0, 0.0, 6.0, 10.0, 14.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 50, 2]
taille_vingtsix = [7.69, 0.0, 0.0, 0.0, 19.23, 0.0, 0.0, 7.69, 7.69, 0.0, 3.85, 0.0, 3.85, 3.85, 0.0, 3.85, 0.0, 7.69, 19.23, 7.69, 7.69, 0.0, 0.0, 0.0, 0.0, 0.0, 26, 1]
tailles = [taille_un, taille_deux, taille_trois, taille_quatre, taille_cinq, taille_six, taille_sept, taille_huit, taille_neuf, taille_dix, taille_onze, taille_douze, taille_treize, taille_quatorze, taille_quinze, taille_seize, taille_dixsept, taille_dixhuit, taille_dixneuf, taille_vingt, taille_vingtun, taille_vingtdeux, taille_vingttrois, taille_vingtquatre, taille_vingtcinq, taille_vingtsix]
#voici les listes, par exemple il y a 5.34% de C dans les mots de taille 3, et 6.91% de A dans les mots de taille 20
# tailles est la liste de toutes les listes, pour faciliter le traitement

def tri_poid() :
    d = dict() # on cree un dictionnaire, ou chaque mot (key) sera associe a son poid (somme de ses lettres*%age associe)
    for i in range(0,nombre_lignes+1) :
        line = lines[i].rstrip() 
        poid = 0
        for a in range(0,26) :
            for j in line :
                for k in range(0,len(Alphabet)) :
                    if j == Alphabet[k] :
                        poid += round(tailles[a][k],4)
        d[line] = poid #on associe donc a chaque mot son "poid", ou sa "polarite"

    d = OrderedDict(sorted(d.items(), key=lambda x: x[1])) # on trie le dictionnaire selon les poids de mots, pour avoir les mots avec les lettres les plus utilises tout en haut, et ceux avec les lettres moins utilisees tout en bas

    #print(len(d))

    return d 
    

fresult1 = open('src/data/mots_tries.txt', 'w')

def remplir_dicos() :
    mots = list(tri_poid()) # on met en liste les nouveaux mots, tries
    tl = len(mots)
    while tl > 0 :
        fresult1.write(f"{mots[tl-1]}\n") #on ecrit dans un nouveau fichier (mots_tries.txt) les mots, tries correctement 
        tl = tl - 1

remplir_dicos()

