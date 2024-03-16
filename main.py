# main/main.py
import os

from flask import Flask, render_template, request, json, url_for
import requests

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


@app.route("/footer")
def footer():
    return render_template('footer.html')


@app.route('/wordmaker', methods=['GET', 'POST'])

def wordMaker():
        


    if request.method == 'POST':
        letterinput = request.form.get('letterinput')

        userInputSet = set(letterinput)

        words_array = ["apple", "banana", "cherry", "date", "elderberry", "tea", "eat", "ate"]
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        json_url = os.path.join(SITE_ROOT, "english-words.json")

        # if letterinput.lower() in words_array:
        #     return render_template('wordMaker.html', words_array=words_array)
        wordsMatch = []
        for i in words_array:
            if set(i).issubset(userInputSet):
                wordsMatch.append(i)

        return render_template('wordMaker.html', wordsMatch=wordsMatch)


        # for i in letterinput:
        #     if i in str(words_array):
        #         return render_template('wordMaker.html', words_array=words_array)


# maybe now try conencting to words api instead of json file ?
# make the logic work with current array first then move onto json file

    return render_template('wordMaker.html')



if  __name__ == "__main__":
    app.run(debug=True)

