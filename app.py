
from flask import Flask, render_template
import random
from moje_programy.open_poem import open_poem
from moje_programy.character_wiki import character
app=Flask(__name__)

@app.route('/')
def index():
    text = open('dane/xd.txt').read()
    return render_template("index.html", text=text)

@app.route('/xd')
def xd():
    return render_template("xd.html")

@app.route('/flaga_dla_Ukrainy')
def zajecia():
    return render_template('flaga_dla_Ukrainy.html')

@app.route('/brudnopis')
def brudnopis():
    super_heroes= ['Bruce Lee', 'Kubuś Puchatek','Mikołaj Kopernik']
    chosen_hero = random.choice(super_heroes)
    description = character(chosen_hero).encode('utf-8').decode()
    poem_lines = open_poem()

    return render_template('brudnopis.html', hero=chosen_hero, description=description, poem_lines=poem_lines)

@app.route('/ciekawe_postacie')
def ciekawe_postacie():
    lista_ciekawych_postaci = []
    zmienna_python = 'abc'
    ciekawa_postac = character('Małysz')
    return render_template('ciekawe_postacie.html', zmienna=zmienna_python, ciekawa_postac=ciekawa_postac)         

if __name__=="__main__":
    app.run()
