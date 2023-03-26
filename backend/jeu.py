import random as r
import mots_dans_liste as listemots
import json


fichier = open('./data/dico_par_tailles.json', "r")
dictionnaire = json.load(fichier)

MOTS_TAILLE_UN = ["A", "B", "C","D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
MOTS_TAILLE_DEUX = listemots.get_list(2, dictionnaire)
MOTS_TAILLE_TROIS = listemots.get_list(3, dictionnaire)
MOTS_TAILLE_QUATRE = listemots.get_list(4, dictionnaire)
MOTS_TAILLE_CINQ = listemots.get_list(5, dictionnaire)
MOTS_TAILLE_SIX = listemots.get_list(6, dictionnaire)
MOTS_TAILLE_SEPT = listemots.get_list(7, dictionnaire)
MOTS_TAILLE_HUIT = listemots.get_list(8, dictionnaire)
MOTS_TAILLE_NEUF = listemots.get_list(9, dictionnaire)
MOTS_TAILLE_DIX = listemots.get_list(10, dictionnaire)
MOTS_TAILLE_ONZE = listemots.get_list(11, dictionnaire)
MOTS_TAILLE_DOUZE = listemots.get_list(12, dictionnaire)
MOTS_TAILLE_TREIZE = listemots.get_list(13, dictionnaire)
MOTS_TAILLE_QUATORZE = listemots.get_list(14, dictionnaire)


def choix(longueur : int) -> str:
    """
    Prend en argument un entier définissant la longueur du mot souhaité
    Renvoie un mot de type String aléatoirement suivant la taille du dictionnaire des mots de la taille souahité
    """
    if longueur == 1 : return MOTS_TAILLE_UN[r.randint(0,len(MOTS_TAILLE_UN)-1)]
    if longueur == 2 : return MOTS_TAILLE_DEUX[r.randint(0,len(MOTS_TAILLE_DEUX)-1)]
    if longueur == 3 : return MOTS_TAILLE_TROIS[r.randint(0,len(MOTS_TAILLE_TROIS)-1)]
    if longueur == 4 : return MOTS_TAILLE_QUATRE[r.randint(0,len(MOTS_TAILLE_QUATRE)-1)]
    if longueur == 5 : return MOTS_TAILLE_CINQ[r.randint(0,len(MOTS_TAILLE_CINQ)-1)]
    if longueur == 6 : return MOTS_TAILLE_SIX[r.randint(0,len(MOTS_TAILLE_SIX)-1)]
    if longueur == 7 : return MOTS_TAILLE_SEPT[r.randint(0,len(MOTS_TAILLE_SEPT)-1)]
    if longueur == 8 : return MOTS_TAILLE_HUIT[r.randint(0,len(MOTS_TAILLE_HUIT)-1)]
    if longueur == 9 : return MOTS_TAILLE_NEUF[r.randint(0,len(MOTS_TAILLE_NEUF)-1)]
    if longueur == 10 : return MOTS_TAILLE_DIX[r.randint(0,len(MOTS_TAILLE_DIX)-1)]
    if longueur == 11 : return MOTS_TAILLE_ONZE[r.randint(0,len(MOTS_TAILLE_ONZE)-1)]
    if longueur == 12 : return MOTS_TAILLE_DOUZE[r.randint(0,len(MOTS_TAILLE_DOUZE)-1)]
    if longueur == 13 : return MOTS_TAILLE_TREIZE[r.randint(0,len(MOTS_TAILLE_TREIZE)-1)]
    if longueur == 14 : return MOTS_TAILLE_QUATORZE[r.randint(0,len(MOTS_TAILLE_QUATORZE)-1)]
    else : return ""

def verif_dico(mot : str) -> bool :
    """
    Prend en argument un mot de type String et regarde si ce mot est dans le dictionnaire
    Renvoie un booléen suivant si le mot est dans le dictionnaire ou non
    """
    longueur = len(mot)
    if longueur == 1 : return mot in MOTS_TAILLE_UN
    if longueur == 2 : return mot in MOTS_TAILLE_DEUX
    if longueur == 3 : return mot in MOTS_TAILLE_TROIS
    if longueur == 4 : return mot in MOTS_TAILLE_QUATRE
    if longueur == 5 : return mot in MOTS_TAILLE_CINQ
    if longueur == 6 : return mot in MOTS_TAILLE_SIX
    if longueur == 7 : return mot in MOTS_TAILLE_SEPT
    if longueur == 8 : return mot in MOTS_TAILLE_HUIT
    if longueur == 9 : return mot in MOTS_TAILLE_NEUF
    if longueur == 10 : return mot in MOTS_TAILLE_DIX
    if longueur == 11 : return mot in MOTS_TAILLE_ONZE
    if longueur == 12 : return mot in MOTS_TAILLE_DOUZE
    if longueur == 13 : return mot in MOTS_TAILLE_TREIZE
    if longueur == 14 : return mot in MOTS_TAILLE_QUATORZE
    else : return False


def occurrence(mot : str) ->tuple:
    """
    Prend en argument un mot de type String
    Renvoie deux listes, la première liste comprend toutes les lettres du mot pris en argument sans doublon,
    la deuxième renvoie le nombre de fois que ces lettres apparaissent dans le mot 
    Pour un indice i donné l'occurence i de la deuxième liste correspond à la lettre i de la première liste 
    """
    lettre = []
    res = []
    for elt in mot:
        if elt not in lettre:
            lettre.append(elt)
    for i in range (len(lettre)):
        compt = 0
        for k in range (0,len(mot)):
            if mot[k]==lettre[i]:
                compt += 1
        res.append(compt)
    return lettre,res

def correction(a_trouve : str,proposition : str) -> list:
    """
    Prend en argument deux mots de type String, le premier étant le mot à trouver et le deuxième le mot proposé
    Renvoie une liste de couleur de type String list qui suit le raisonnement suivant :
     - vert : la lettre choisie est la bonne
     - bleu : la lettre est bien dans le mot mais n'est pas bien placée
     - noir : la lettre n'est pas dans le mot ou il n'y a plus d'occurence de cette lettre dans le mot
    """
    res = []
    if len(a_trouve) != len(proposition):
        return []
    lettre,occur = occurrence(a_trouve)                          #initialise la liste de lettre et des occurences associées
    rencontre = len(occur)*[0]                                   #initialise la liste qui permettra de compter les lettre étudiées
    res = len(a_trouve)*["N"]                                    #initialise la liste résultats avec seulement noir comme couleur
    for k in range (len(proposition)):                           #on parcours une première fois le mot proposé
        if a_trouve[k] == proposition[k]:
            ind = lettre.index(proposition[k])                   #on colore en vert chaque lettre qui est bien placée 
            rencontre[ind] += 1                                  #on incrémente d'un dans la liste d'étude toutes les lettres bonnes
            res[k] = "V"

    for j in range (len(proposition)):                           #on parcours une deuxième fois le mot proposé pour voir toutes les lettre mal placée
        if res[j] != "V" and (proposition[j] in a_trouve):       #si cette lettre est bien dans le mot mais mal placée on la colore en bleu
            ind = lettre.index(proposition[j])                   #sinon on la laisse noire
            if rencontre[ind]<occur[ind]:                        #la liste d'étude permet de ne pas colorer plus de lettre que nécéssaire
                rencontre[ind] += 1                              #si une lettre a été donné plus de fois qu'elle est présente dans le mot a trouver
                res[j] ="B"                                      #alors on laisse en noir les occurences supplémentaire pour le signaler au joueur 
    return res