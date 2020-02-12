from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/jwnas')
def jwnas():
    return render_template('jwnas.html')

@app.route('/cwnas')
def cwnas():
    return render_template('cwnas.html')

@app.route('/info')
def info():
    return 'this web is made by CWHa, The handsome'

@app.route('/secret')
def secret():
    return render_template('easteregg.html')

app.run(host='0.0.0.0')
