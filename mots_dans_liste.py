import json
import unicodedata


FILENAME = './data/word_jeu.txt'

def get_words_json (filename : str) -> dict :
    """
    Prend en argument l'adresse du fichier .txt contenant les mots 
    (un mot par ligne) et les mets dans un dictionnaire trié par taille
    La fonction retourne un dictionnaire.
    """
    fichier = open(filename, "r")
    Mots = fichier.read().splitlines()
    d={}
    for i in range(1,27):
        d["mots_taille_"+str(i)] = []
    for mot in Mots :
        if (mot not in d["mots_taille_"+str(len(mot))] and not ("<<" in mot  or "(" in mot or ")" in mot or "/" in mot or "\"" in mot or ">>" in mot or ":" in mot or "," in mot or ";" in mot)):
            d["mots_taille_"+str(len(mot))].append(mot)
    return(d)


#Creation du fichier json
"""d = get_words_json(FILENAME)
fichier = open('./data/dico_par_taille.json', "w")
json.dump(d, fichier)"""



def get_list(taille_mot : int, dico_json : dict) -> list :
    """
        args    :   taille_mot  :   int     -> taille des mots de la liste souhaitée
                    dico_json   :   dict    -> dictionnaire du fichier json
        returns :   L           :   list    -> liste des mots de taille souhaitée

        La fonction retourne la liste des mots de taille souhaitée à partir du dictionnaire
    """
    L = dico_json["mots_taille_" + str(taille_mot)]
    return(L)


#Lire un dictionnaire dans un fichier json : 
"""
import json
fichier = open('./data/dico_par_tailles.json', "r")
dictionnaire = json.load(fichier)
"""
#Acceder à la liste des mots de taille n
"""
mots_taille_n = dictionnaire['mots_taille_n']
"""
