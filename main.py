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
        


    words_array = ["eat", "tea"]
    error = "incorrect input"

    if request.method == 'POST':
        letterinput = request.form.get('letterinput')

        if letterinput in words_array:
            return render_template('wordMaker.html', words_array=words_array)
            
        # else:
        #     return render_template('wordMaker.html', error=error)


    return render_template('wordMaker.html')



if  __name__ == "__main__":
    app.run(debug=True)

