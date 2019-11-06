#!/usr/bin/python3
from flask import Flask
app = Flask('test')

@app.route('/hello/<string:nom>/<int:age>')
def index(nom='inconnu', age=0):
    return "salut %s, bon anniv pour tes %s an(s)" % (nom, age)

app.run(debug=True)

