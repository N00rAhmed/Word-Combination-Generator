# main/main.py

from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route("/nav")
def navigation():
    return render_template('nav.html')


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/wordmaker', methods=['GET', 'POST'])

def wordMaker():
        
    letterinput = ""

    if request.method == 'POST':
        letterinput = request.form['letterinput']

    elif request.method == "GET":
        letterinput = request.args.get('letterinput', '')

    # Check if the input is "acr" and display "car" accordingly
    if letterinput.lower() == 'acr':
        letterinput = 'car'
    
    return render_template('wordMaker.html', letterinput=letterinput)



if  __name__ == "__main__":
    app.run(debug=True)

