from flask import Flask, redirect, render_template, session, request, g
from flask_session import Session
from jeu import choix,verif_dico,correction
import sqlite3
from auxiliaire import moyenne_nombre_coups, moyenne_taille_mots, get_chart

app = Flask(__name__)
app.config["SECRET_KEY"]="madllefkhlkhe"
app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]='filesystem'
Session()

### Variables gloables ###
DATABASE = 'donnees.db'

Error_dict = {
    0 : "Erreur test",
    1 : "Erreur de connexion",
    2 : "Erreur de type d'entrée",
    666 : "Erreur inexistante"
}

### FONCTIONS BASE DE DONNÉES

def get_db():
    """
    Connexion à la base de données
    """
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    """
    déconnexion propre de la base de données
    """
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def definition_parametres():
    """
    création de la table parametre dans la bd
    """

    db = get_db()
    c = db.cursor()
    compteur = 1

    c.execute("DROP TABLE parametre")
    c.execute("CREATE TABLE parametre (id_parametre INTEGER PRIMARY KEY NOT NULL, nb_coups INTEGER(20) NOT NULL, nb_lettres INTEGER NOT NULL)")
 
    for i in range(1, 16):
        for j in range(1, 16):
            c.execute("INSERT INTO parametre VALUES ("+ str(compteur) + "," + str(i) + "," + str(j) + ")")
            compteur += 1

    db.commit()
    return None


### routes ###

@app.route("/")
def index():
    definition_parametres()
    if not session.get("nb"):                               # vérification des paramètres de base
        session["nb"] = 6                                   # si absence on complète avec des valeurs par défaut
    if not session.get("taille"):
        session["taille"] = 5
    if not session.get("darkmode"):
        session["darkmode"] = "ON"
    if not session.get("connected"):
        session["connected"]=False
    if not session.get("parametre"):
        session["parametre"]=80                             #id de la bd correspondant au cas (5, 6)
       
    return render_template('index.html', connected=session["connected"], darkmode=session["darkmode"])

@app.route("/jeu", methods=["GET", "POST"])
def jeu():
    db = get_db()
    c = db.cursor()
    if request.method=="GET":
        c.execute("SELECT * FROM parametre WHERE id_parametre = "+str(session["parametre"]))
        parametres = c.fetchall()
        session["taille"] = parametres[0][2]               # récupération des informations dans la bd
        session["nb"] = parametres[0][1]

        session["mot"] = choix(session["taille"])           # choix d'un mot de la bonne taille

        # initialisation des variables necessaire au jeu
        session["victoire"] = False
        session["essai"] = 0
        session["message"] =""
        session["essais"] = ["NULL"]*session["nb"]
        session["couleurs"] = ["NNNNN"]*session["nb"]
        session["res"]=""
        session["fini"] = False

    if request.method=="POST":                              # si la première proposition a été faite
        
        mot = ""
        for i in range(session["taille"]):                  # récupération du mots à partir des différents textarea
            mot += request.form.get("Lettre"+str(i))
        mot = mot.upper()                                   #mise en majuscule pour coller à la liste de mot
        if len(mot) != session["taille"]:                   # si le mot n'est pas de la taille requise
            session["message"]="Word is too short"

        else:
            if not verif_dico(mot):                         #vérification de la présence du mot dans le dico
                session["message"]="This word is not in our dictionary" 
            else:
                res = correction(session["mot"], mot)
                if res == ["V"]*session["taille"]:          #vérification de la condition de victoire

                    # MAJ des variables importantes
                    session["message"]="You won ! The word was : "
                    session["victoire"] = True
                    session["couleurs"][session["essai"]] = "V"*session["taille"]
                    session["essais"][session["essai"]] = mot
                    session["res"] = session["mot"]
                    session["fini"] = True

                    if session.get("id"):                    # vérification de la connexion du joueur pour stocker son résultat dans la bd
                        session["id"] = session["id"]
                    else:
                        session["id"] = 0
                    
                    n = 0
                    while n < len(session["essais"]) and session["essais"][n] != "NULL": #compte le nombre de coup
                        n+=1
                    succes = ""
                    c.execute("SELECT * FROM statistiques WHERE id_joueur = "+str(session["id"])) #à chaque partie, on récupère les statistiques
                    stat = c.fetchall()

                    c.execute("SELECT * FROM succes WHERE id_joueur = "+str(session["id"])) # et on récupère les succès du joueur pour les mettre à jour
                    donnees = c.fetchall()
                    
                    if stat[0][2] + 1 >= 1:
                        succes += "succes1 = 1,"
                    else:
                        succes += "succes1 = 0,"    #suivant la situation on met true (le booléen true étant équivalant à 1) pour chaque succès
                                                    #dont la condition est vérifiée ou qui a déjà été réalisée
                    if stat[0][2] + 1 >= 100:    
                        succes += "succes2 = 1,"
                    else:
                        succes += "succes2 = 0,"
                    
                    if stat[0][2] + 1 >= 1000:
                        succes += "succes3 = 1,"
                    else:
                        succes += "succes3 = 0,"
                    
                    if n<=2 or donnees[0][4] == 1:
                        succes += "succes4 = 1"
                    else:
                        succes += "succes4 = 0"
                    
                    c.execute("UPDATE statistiques SET nb_parties ="+str(stat[0][1] +1 )+ " WHERE id_joueur = "+str(session["id"])) #met à jour le nombre de partie
                    c.execute("UPDATE statistiques SET nb_victoires ="+str(stat[0][2] +1)+ " WHERE id_joueur = "+str(session["id"]))#met à jour le nombre de victoire
                    c.execute("UPDATE succes SET "+succes+" WHERE id_joueur = "+str(session["id"]))  #met à jour les succès
                    db.commit()
                    
                    c.execute("SELECT MAX(id_partie) FROM partie")  #on récupère l'id le plus grand de la table partie
                    res = c.fetchall()
                    if res == [(None,)]:
                        res = [[0]]
                    
                    #on prépare insertion qui nous servira de requête d'abord en lui soumettant l'id de partie, l'id du joueur ainsi que l'id des paramètres
                    insertion = ""+str(res[0][0]+1)+","+str(session["id"])+","+str(session["parametre"])+","

                    #on ajoute à cela le booléen 1 (true) ou 0 (false)
                    if session["victoire"]:
                        insertion+="1,"
                    else:
                        insertion+="0,"

                    #le mot à trouver est également ajouté il sera utile pour l'affichage des différentes parties
                    insertion+=("'"+session["mot"]+"',")

                    #il faut alors compléter les différents coups donné par le joueur en complétant par NULL si jamais il sont inférieur à 15
                    for i in range(15):
                        if i <= session["nb"]-1:
                            if session["essais"][i]=='NULL':
                                if i != 14:
                                    insertion = insertion + "NULL" + ","                # ajoute une virgule si les 15 coups ne sont pas encore comptabilisé
                                else:
                                    insertion = insertion + "NULL"
                            else:
                                if i != 14:
                                    insertion = insertion +"'" +session["essais"][i] +"'"+ ","
                                else:
                                    insertion = insertion + "'" + session["essais"][i] +"'"
                        else:
                            if i != 14:
                                insertion = insertion + "NULL" + ","
                            else: 
                                insertion = insertion + "NULL"

                    
                    c.execute("INSERT INTO partie VALUES ("+insertion+")")          #ajoute les données de la partie joué dans la base de donnée
                    if session["id"] == 0:
                        session["id"] = None

                    db.commit()

                    
                else:
                    couleur =""
                    for i in range(len(res)):                                       #récupère le résultat du coup joué
                        couleur+= res[i]
                        
                    session["message"]=""
                    session["essais"][session["essai"]]=mot
                    session["couleurs"][session["essai"]] = couleur
                    session["essai"] += 1
   
            if session["essai"] == session["nb"]:                                   # vérification de la condition de défaite
                session["message"] = "You lost ! The word was : "
                session["res"] = session["mot"]
                session["fini"] = True

                if session.get("id"):                                               # vérification de la connexion de l'utilisateur pour le stockage dans la bd
                    session["id"] = session["id"]
                else:
                    session["id"] = 0
                
                c.execute("SELECT * FROM statistiques WHERE id_joueur = "+str(session["id"]))
                stat = c.fetchall()
                c.execute("UPDATE statistiques SET nb_parties ="+str(stat[0][1] +1 )+ " WHERE id_joueur = "+str(session["id"]))
                db.commit()    

                c.execute("SELECT MAX(id_partie) FROM partie")
                res = c.fetchall()
                
                if res == [(None,)]:                                                # si aucune partie n'a été jouée
                        res = [[0]]

                insertion = ""+str(res[0][0]+1)+","+str(session["id"])+","+str(session["parametre"])+"," # préparation des informations à insérer dans la bd
                if session["victoire"]:
                    insertion+="1,"
                else:
                    insertion+="0,"
            
                insertion+=("'"+session["mot"]+"',")
                for i in range(15):                                                 # mise au bon format pour insérer dans la bd
                    if i <= session["nb"]-1:
                        if session["essais"][i]=='NULL':
                            if i != 14:
                                insertion = insertion + "NULL" + ","
                            else:
                                insertion = insertion + "NULL"
                        else:
                            if i != 14:
                                insertion = insertion +"'" +session["essais"][i] +"'"+ ","
                            else:
                                insertion = insertion + "'" + session["essais"][i] +"'"
                    else:
                        if i != 14:
                            insertion = insertion + "NULL" + ","
                        else: 
                            insertion = insertion + "NULL"

                
                c.execute("INSERT INTO partie VALUES ("+insertion+")")              #ajoute les données de la partie joué dans la base de donnée
                if session["id"] == 0:
                    session["id"] = None
                db.commit()


    
    return render_template('game.html', connected=session["connected"], darkmode=session["darkmode"], taille=session["taille"],nb=session["nb"],parametres=session["parametre"], playable=session["essai"], message=session["message"], essais=session["essais"], victoire = session["victoire"], couleur=session["couleurs"], mot = session["res"], fini=session["fini"])


@app.route("/erreur/<f>")
def erreur(f):
    try:
        NB=int(f)                                                   # vérification du type du numéro de l'erreur
    except:
        return redirect("/erreur/666")

    if not NB in Error_dict:                                        # vérification que l'erreur existe
        return redirect("/erreur/666")

    DESC = Error_dict[NB]
    return render_template('error.html', connected=session["connected"],darkmode=session["darkmode"], NB=NB, DESC=DESC)

@app.route("/connexion", methods=["POST", "GET"])
def connexion():
    db = get_db()
    c = db.cursor()

    if session["connected"]:            #vérifie que le joueur est bien connecté
        return redirect("/profil")

    if request.method == "POST":
        pseudo = request.form.get("pseudo")                   #récupère le pseudo et le mot de passe entré par l'utilisateur pour vérifié qu'il est bien dans la bse de donnée
        password = request.form.get("password")

        c.execute("SELECT id_joueur, darkmode FROM utilisateur WHERE pseudo LIKE '"+str(pseudo)+ "' AND mdp LIKE '"+str(password)+"'")
        res = c.fetchall()
        

        if res != [] and res[0][0] != 0:                      #si le pseudo et le mot de passe correspondent alors il est connecté et peut jouer
            session["connected"] = True
            id = res[0][0]
            session["id"] = id
            if res[0][1] == 1:
                session["darkmode"] = "ON"
            else:
                session["darkmode"] = "OFF"
            return redirect("/profil")

        else :                                                #sinon il est renvoyé vers une page d'erreur
            return redirect("/erreur/1")

    return render_template('login.html', connected=session["connected"], darkmode=session["darkmode"])

@app.route("/deconnexion")                                    # permet a l'utilisateur de se déconnecter
def deconnexion():

    session["nb"] = 6 
    session["taille"] = 5
    session["darkmode"] = "ON"
    session["connected"]=False
    session["parametre"]=80 
    session["id"] = None                                      # on remet l'ensemble des parametres à zéro
    return redirect("/")                                      # retour à l'accueil

@app.route("/profil")
def profil():

    if not session["connected"] :                             #vérifie que le joueur est bien connecté
        return redirect("/connexion")

    db = get_db()
    c = db.cursor()
    c.execute("SELECT * FROM utilisateur WHERE id_joueur ="+ str(session["id"]))    # récupère les données d'utilisateur
    utilisateur = c.fetchall()
    c.execute("SELECT * FROM partie WHERE id_joueur =" + str(session["id"]))        # récupère les parties de l'utilisateur
    parties = c.fetchall()
    coups = []
    for k in range(len(parties)):
        partie_coup = []                                                    #récupère les différents coup de l'utilisateur de chacune de ses parties 
        pas = 5
        while parties[k][pas] != None and pas != 16:
            partie_coup.append(parties[k][pas])
            pas += 1
        coups.append(partie_coup)
    c.execute("SELECT pr.* FROM parametre AS pr JOIN partie AS ps ON pr.id_parametre = ps.id_parametre WHERE id_joueur =" + str(session["id"])) #récupère les différents paramètres pour les différentes parties du joueur
    parametre = c.fetchall()
    c.execute("SELECT * FROM succes WHERE id_joueur =" + str(session["id"]))                #récupère les succès du joueur
    succes = c.fetchall()
    N = len(parties)


    c.execute("SELECT * FROM statistiques WHERE id_joueur =" + str(session["id"]))          #récupère les statistiques du joueur
    stat = c.fetchall()[0]
    nb_partie = stat[1]
    nb_victoire = stat[2]
    nb_defaite = nb_partie-nb_victoire
    c.execute("SELECT * FROM partie WHERE victoire=1 AND id_joueur =" + str(session["id"])) #récupère l'historique des parties où le joueur a gagné
    partie = c.fetchall()
    moyenne_nb_coups = round(moyenne_nombre_coups(partie),2)
    c.execute("SELECT a_trouve FROM partie WHERE id_joueur =" + str(session["id"]))         #récupère tous les mots que le joueur a du trouver au cours de ses parties
    mots=c.fetchall()
    m_taille_mots=round(moyenne_taille_mots(mots),2)
    if nb_partie == 0:                                                                      #récupère l'url du schéma statistique des parties du joueur
        filename_chart = get_chart(0)
    else:
        filename_chart = get_chart((100*nb_victoire)/nb_partie)

    return render_template('profile.html', connected=session["connected"], PSEUDO=utilisateur[0][1], url=utilisateur[0][4], darkmode=session["darkmode"],
    coups=coups,parties=parties,parametre=parametre, succes=succes,N=N, nombre_parties=nb_partie, nombre_victoires=nb_victoire, nombre_defaites=nb_defaite, 
    moyenne_nombre_coups=moyenne_nb_coups, moyenne_longueur=m_taille_mots, chart=filename_chart)



@app.route("/parametres", methods=["GET", "POST"])
def parametres():

    if request.method == "POST":                                #récupère les paramètres définis par l'utilisateur
        taille = request.form.get("length")
        nb = request.form.get("guess")
        darkmode = request.form.get("darkmode")

        if nb == "":
            nb = 6                                              #si des paramètres manquent, alors ils sont mis par défaut avec nombre de coup max égal 6
                                                                #et taille du mot égale a 5
        if taille == "":
            taille = 5

        try:
            taille = int(taille)
            nb = int(nb)
        
        except:
            return redirect("/erreur/2")

        
        session["taille"] = taille
        session["nb"] = nb

        db = get_db()
        c = db.cursor()

        if taille < 1 or taille > 14 :
            return redirect("/erreur/2")
        if nb < 1 or nb > 15 :
            return redirect("/erreur/2")                         #si jamais les paramètres rentrés n'existent pas renvoie une erreur

        c.execute("SELECT id_parametre FROM parametre WHERE nb_coups="+str(nb)+" AND nb_lettres="+str(taille))
        res = c.fetchall()

        session["parametre"] = res[0][0]

        if darkmode == None:                                    #change le mode de visionnage entre blanc ou noir
            session["darkmode"] = "OFF"
        else:
            session["darkmode"] = "ON"

        if session.get("id"):
            if darkmode == None:
                tmp = "0"
            else:
                tmp = "1"
            
            c.execute("UPDATE utilisateur SET darkmode = "+tmp + " WHERE id_joueur = "+str(session["id"])) #met a jour les données de l'utilisateur suivant le mode choisi
            db.commit()


        return redirect("/")


    return render_template("parameter.html", connected=session["connected"], darkmode=session["darkmode"])

@app.route("/replay/<f>")
def replay(f):                                                              #affiche le détails des coups joué lors d'une partie précise ou "f" est l'id de cette partie
    try:
        NB = int(f) 
    except:
        return redirect("/erreur/2")

    db = get_db()
    c = db.cursor()

    c.execute("SELECT * FROM partie WHERE id_partie = " + str(NB))          #récupère les données de la partie sélectionné
    res = c.fetchall()
    if res == [] or res == [(None,)]:
        return redirect("/erreur/2")

    parametres_id = res[0][2]
    victoire = res[0][3]
    mot = res[0][4]                                                         #répartit les différentes données entre 4 variables
    coups = res[0][5:]

    tmp = []
    couleur = []

    for i in range(len(coups)):
        if coups[i] == None:
            tmp.append("NULL")
        else:
            tmp.append(coups[i])
            couleur.append(correction(mot, coups[i]))
    
    coups = tmp
    c.execute("SELECT * FROM parametre WHERE id_parametre =" + str(parametres_id))          #récupère les paramètres liés a la partie  
    res = c.fetchall()
    nb = res[0][1]
    taille = res [0][2]
    return render_template("replay.html", message="Word : ", nb = nb, victoire = (victoire == 1), essais=coups, taille=taille,couleur=couleur, darkmode=session["darkmode"], mot = mot, connected=session["connected"])
app.run()