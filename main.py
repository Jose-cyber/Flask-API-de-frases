# -*- coding: utf-8 -*- 

from flask import Flask, render_template, jsonify
import random
import json 

app = Flask(__name__)

with open("frases/frases_motivacionais.json", encoding='utf-8') as json_open:
    dados = json.load(json_open)

@app.route('/')
def home():  
    return render_template('index.html')
    
@app.route('/frases_motivacionais')
def phrases():
    generate = random.choice(dados['frases'])
    return jsonify(generate) 

if __name__ == "__main__":
    app.run(host='0.0.0.0')