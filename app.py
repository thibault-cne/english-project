from flask import Flask, render_template, redirect, session, request
from flask_cors import CORS
import random as rd
from flask_session import *


### LOAD DATAS ###

en_words = []
fr_words = []
fun_fact = []

with open("static/words") as f:
    en_words = f.readlines()
    for i in range(len(en_words)):
        en_words[i] = en_words[i].rstrip()

with open("static/words_fr") as f:
    fr_words = f.readlines()
    for i in range(len(fr_words)):
        fr_words[i] = fr_words[i].rstrip()

with open("static/fun_facts") as f:
    fun_facts = f.readlines()
    for i in range(len(fun_facts)):
        fun_facts[i] = fun_facts[i].rstrip()


current_TORF = False

### FLASK APP ###


app = Flask(__name__)
app.config["SECRET_KEY"]="madllefkhlkhe"
app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]='filesystem'
app.config['CORS_HEADERS'] = 'Content-Type,Authorization'
app.config["SESSION_COOKIE_SAMESITE"] = "None"
app.config["SESSION_COOKIE_SECURE"] = True

Session(app)

CORS(app, origins=["http://localhost:5173"], headers=['Content-Type'], expose_headers=['Access-Control-Allow-Origin'], supports_credentials=True) 

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

        return {"status": "playing", "en_word":en_word, "fr_word":fr_word, "e":e, "score": session["score"], "total":session["total"]}
    else:
        current_TORF = False
        j = rd.randint(0, len(en_words)-1)
        while j == i:
            j = rd.randint(0, len(en_words)-1)
        en_word = en_words[j]   
        fr_word = fr_words[i]
        
        return {"status": "playing", "en_word":en_word, "fr_word":fr_word, "e":e, "score": session["score"], "total":session["total"]}
    

@app.route("/TORF_EXAM_True")
def TORF_EXAM_True():
    session["total"] += 1
    if current_TORF:
        session["score"] += 1
        if session["total"] == 10:
            return redirect("/TORF_EXAM_END")

        return redirect("/TORF_EXAM")    
    else:
        if session["total"] == 10:
            return redirect("/TORF_EXAM_END")
        return redirect("/TORF_EXAM")   
    
@app.route("/TORF_EXAM_False")
def TORF_EXAM_False():
    session["total"] += 1
    if current_TORF:
        if session["total"] == 10:
            return redirect("/TORF_EXAM_END")
        return redirect("/TORF_EXAM")   
    else:
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

    return {"status": "end", "score": s, "total": t}

@app.route("/disorder")
def disorder():
    i = rd.randint(0, len(en_words)-1)

    session["disorder"] = i

    en_words_disorder = (en_words[i])
    tmp = []
    for el in en_words_disorder:
        tmp.append(el)

    rd.shuffle(tmp)

    en_words_disorder = ""
    for el in tmp:
        en_words_disorder += el

    return {"permutated_word": en_words_disorder}

@app.route("/verif_word")
def verif_word():
    word = request.args.get("word")
    print(word)
    print(en_words[session["disorder"]])
    if word == en_words[session["disorder"]]:
        return {"status": "won"}
    else:
        return {"status": "lost"}


### TODO : QCM choisir 4 mots.



    
if __name__ == "__main__":
    app.run(debug = True, port=5454)