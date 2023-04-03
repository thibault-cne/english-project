from flask import Flask, render_template, redirect, session
from flask_cors import CORS
import random as rd
from flask_session import *


### LOAD DATAS ###

en_words = []
fr_words = []
fun_fact = []

with open("static/words") as f:
    en_words = f.readlines()

with open("static/words_fr") as f:
    fr_words = f.readlines()

with open("static/fun_facts") as f:
    fun_facts = f.readlines()


current_TORF = False

### FLASK APP ###


app = Flask(__name__)
app.config["SECRET_KEY"]="madllefkhlkhe"
app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]='filesystem'
Session()


CORS(app, ressources={r'/*': {'origins': '*'}})

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/lesson/<f>')
def hello(f):
    return render_template('lessons/lesson' +f+ '.html')

@app.route("/irregular_verbs")
def irregular_verbs():
    return render_template('irregular_verbs.html')


@app.route("/fun-fact")
def fun_fact():
    fun_fact = fun_facts[rd.randint(0, len(fun_facts)-1)]
    return {"fun_fact": fun_fact}


@app.route("/random_word")
def random_word():
    i = rd.randint(0, len(en_words)-1)

    en_word = en_words[i]
    fr_word = fr_words[i]

        
    return render_template('random_word.html', en_word=en_word, fr_word=fr_word)


@app.route("/TORF")
def TORF():
    i = rd.randint(0, len(en_words)-1)

    if not session.get("message") or session["message"][-1] != "\n":
        session["message"] = ""

    ### TODO : faire soit un système d'évaluation en reprenant ça soit on rajoute un compte de juste sur total

    e = rd.randint(0, 1)
    n = rd.randint(0, 1)
    if n == 0:
        global current_TORF
        current_TORF = True
        en_word = en_words[i]
        fr_word = fr_words[i]
        return {"en_word":en_word, "fr_word":fr_word}
    else:
        current_TORF = False
        j = rd.randint(0, len(en_words)-1)
        while j == i:
            j = rd.randint(0, len(en_words)-1)
        en_word = en_words[j]   
        fr_word = fr_words[i]
        return {"en_word":en_word, "fr_word":fr_word}
    


@app.route("/TORF_True")
def TORF_True():
    if current_TORF:
        return {"status": "won"}
    else:
        return {"status": "lost"}
    
@app.route("/TORF_False")
def TORF_False():
    if current_TORF:
        return {"status": "lost"}
    else:
        return {"status": "won"}
    




@app.route("/TORF_EXAM")
def TORF_EXAM():
    i = rd.randint(0, len(en_words)-1)

    if not session.get("message") or session["message"][-1] != "\n":
        session["message"] = ""

    if not session.get("score"):
        session["score"] = 0

    if not session.get("total"):
        session["total"] = 0

    e = rd.randint(0, 1)
    n = rd.randint(0, 1)
    if n == 0:
        global current_TORF
        current_TORF = True
        en_word = en_words[i]
        fr_word = fr_words[i]
        if (e==1):
            session["message"] += "Does the word " + en_word  + "is the english of " + fr_word + " ?"
        else:
            session["message"] += "Does the word " + fr_word  + "is the french of " + en_word + " ?"
        return render_template('TORF_EXAM.html', en_word=en_word, fr_word=fr_word, e=e, message=session["message"], score=session["score"], total=session["total"])
    else:
        current_TORF = False
        j = rd.randint(0, len(en_words)-1)
        while j == i:
            j = rd.randint(0, len(en_words)-1)
        en_word = en_words[j]   
        fr_word = fr_words[i]
        if (e==1):
            session["message"] += "Does the word " + en_word  + "is the english of " + fr_word + " ?"
        else:
            session["message"] += "Does the word " + fr_word  + "is the french of " + en_word + " ?"
        
        return render_template('TORF_EXAM.html', en_word=fr_word, fr_word=en_word, e=e, message=session["message"], score=session["score"], total=session["total"])
    

@app.route("/TORF_EXAM_True")
def TORF_EXAM_True():
    session["total"] += 1
    if current_TORF:
        session["message"] = "You won ! \n"
        session["score"] += 1
        if session["total"] == 10:
            return redirect("/TORF_EXAM_END")

        return redirect("/TORF_EXAM")    
    else:
        session["message"] = "You lost ! \n"
        if session["total"] == 10:
            return redirect("/TORF_EXAM_END")
        return redirect("/TORF_EXAM")   
    
@app.route("/TORF_EXAM_False")
def TORF_EXAM_False():
    session["total"] += 1
    if current_TORF:
        session["message"] = "You lost ! \n"
        if session["total"] == 10:
            return redirect("/TORF_EXAM_END")
        return redirect("/TORF_EXAM")   
    else:
        session["message"] = "You won ! \n"
        session["score"] += 1
        if session["total"] == 10:
            return redirect("/TORF_EXAM_END")
        return redirect("/TORF_EXAM")   
    
@app.route("/TORF_EXAM_END")
def TORF_EXAM_RESULT():
    s = session["score"]
    t = session["total"]
    session["score"] = 0
    session["total"] = 0

    return render_template('score.html', score=s, total=t)



### TODO : QCM choisir 4 mots.



    
if __name__ == "__main__":
    app.run(debug = True)