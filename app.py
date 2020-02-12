from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info')
def info():
    return 'this web is made by CWHa, The handsome'

@app.route('/secret')
def secret():
    return render_template('easteregg.html')