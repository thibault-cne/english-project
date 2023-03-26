def moyenne_nombre_coups(parties : list) -> float :
    """
        args    :   parties : list  ->  liste des parties correspondant à la requete SQL des parties gagnées

        retours :   float           -> moyenne des nombre de coups

        La fonction parcours les parties gagnées de l'utilisateur et compte le nombre de coups réalisés 
        pour gagner la patie. On en fait ensuite la moyenne.
    """
    if len(parties)==0:
        return(0)
    s=0
    for p in parties :
        cpt=0
        for i in range(5,20) :
            if p[i]!=None:
                cpt+=1
        s+=cpt
    return(s/len(parties))

def moyenne_taille_mots(mots : list) -> float:
    """
        args    :   mots : list  ->  liste des mots à chercher dans les parties jouées

        retours :   float        -> moyenne des nombre de coups

        La fonction parcours les parties de l'utilisateur et fait la moyenne des mots à trouver
    """
    if len(mots)==0:
        return(0)
    s=0
    for m in mots :
        s+=len(m[0])
    return(s/len(mots))

def get_chart(moyenne : float) -> str :
    """
        args    :   moyenne : float     ->  moyenne de victoire de l'utilisateur

        retours :   str                 ->  nom de l'image du pourcentage de victoire

        La fonction arrondie la moyenne pour trouver l'image la plus proche du pourcentage.
    """
    n=round(moyenne)
    filename = "../static/" + str(n) + "pourcent.png"
    return(filename)