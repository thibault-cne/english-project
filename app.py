from flask import Flask, render_template
import random as rd


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

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/lesson/<f>')
def hello(f):
    return render_template('lessons/lesson' +f+ '.html')

@app.route("/irregular_verbs")
def irregular_verbs():
    return render_template('irregular_verbs.html')


@app.route("/fun_fact")
def fun_fact():
    fun_fact = fun_facts[rd.randint(0, len(fun_facts)-1)]
    return render_template('fun_fact.html', fun_fact_content=fun_fact)


@app.route("/random_word")
def random_word():
    i = rd.randint(0, len(en_words)-1)

    en_word = en_words[i]
    fr_word = fr_words[i]

        
    return render_template('random_word.html', en_word=en_word, fr_word=fr_word)



@app.route("/TORF")
def TORF():
    i = rd.randint(0, len(en_words)-1)

    n = rd.randint(0, 1)
    if n == 0:
        global current_TORF
        current_TORF = True
        en_word = en_words[i]
        fr_word = fr_words[i]
        return render_template('TORF.html', en_word=en_word, fr_word=fr_word)
    else:
        current_TORF = False
        j = rd.randint(0, len(en_words)-1)
        while j == i:
            j = rd.randint(0, len(en_words)-1)
        en_word = en_words[j]   
        fr_word = fr_words[i]
        return render_template('TORF.html', en_word=fr_word, fr_word=en_word)
    


@app.route("/TORF_True")
def TORF_True():
    if current_TORF:
        return "you won !"
    else:
        return "you lost !"
    
@app.route("/TORF_False")
def TORF_False():
    if current_TORF:
        return "you lost !"
    else:
        return "you won !"
    