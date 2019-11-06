#!/usr/bin/python3
import os, json
from flask import Flask
app = Flask('test')

@app.route('/')
def index():
    return 'ok'

@app.route('/disk')
def disk():
    stat = os.statvfs('/')
    free = stat.f_bavail * stat.f_bsize
    r = {'free': free}
    return json.dumps(r)

app.run(debug=True)

