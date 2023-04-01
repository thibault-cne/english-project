from flask import Flask, render_template
import random as rd

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

    with open("static/fun_facts") as f:
        fun_facts = f.readlines()
        fun_fact = fun_facts[rd.randint(0, len(fun_facts)-1)]
    return render_template('fun_fact.html', fun_fact_content=fun_fact)


@app.route("/random_word")
def random_word():
    with open("static/words") as f:
        words = f.readlines()
        random_word = words[rd.randint(0, len(words)-1)]
        
    return render_template('random_word.html', random_word_content=random_word)