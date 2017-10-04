from flask import Flask
import os, json

app = Flask('test')

@app.route('/')
def index():
    return('bonjour, vous etes sur la page dacceuil')

@app.route('/disk')
def disk():
    dsk = 1
    d = make_summary()
    return jsonify(d)


app.run(debug=True)

