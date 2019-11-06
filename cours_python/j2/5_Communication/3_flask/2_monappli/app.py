# apt-get install python3-flask
# ou: pip3 install flask

from flask import Flask, render_template
from googlesearch import get_google_result
from t4a import gettab
import json
from pprint import pprint

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Saluuuuuut!!'

@app.route('/search/<keyword>')
def search_google(keyword):
    links = get_google_result(keyword)
    # return json.dumps(links)
    return render_template('googlesearch.html', links=links)

@app.route('/tab/<keyword>')
def search_tab(keyword):
    return gettab(keyword)

if __name__ == '__main__':
    app.run()

