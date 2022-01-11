# -*- coding: utf-8 -*- 

from flask import Flask, render_template, jsonify
import random
import json 

app = Flask(__name__)

with open("frases/pt-br/frases_motivacionais.json", encoding='utf-8') as json_open:
    frases_motivacionais = json.load(json_open)

with open("frases/pt-br/frases_religiosas.json", encoding='utf-8') as json_open:
    frases_religiosas = json.load(json_open)

@app.route('/')
def home():  
    return render_template('index.html')
    
@app.route('/frases_motivacionais')
def Frases_motivacionais():
    escolhe_frase_motivacional = random.choice(frases_motivacionais['frases'])
    return jsonify(escolhe_frase_motivacional) 

@app.route('/frases_religiosas')
def Frases_religiosas():
    escolhe_frase_religiosa = random.choice(frases_religiosas['frases'])
    return jsonify(escolhe_frase_religiosa)

if __name__ == "__main__":
    app.run(host='0.0.0.0')