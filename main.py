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
        


    if request.method == 'POST':
        letterinput = request.form.get('letterinput')

        userInputSet = set(letterinput)

        words_array = ["apple", "banana", "cherry", "date", "elderberry", "tea", "eat", "ate"]

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



# make the logic work with current array first then move onto json file

    return render_template('wordMaker.html')



if  __name__ == "__main__":
    app.run(debug=True)

