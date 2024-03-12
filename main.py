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
        


    words_array = ["eat", "tea", "ate", "we"]
    error = "incorrect input"

    if request.method == 'POST':
        letterinput = request.form.get('letterinput')

        if letterinput in words_array:
            return render_template('wordMaker.html', words_array=words_array)
        
        # potentially use for loop which iterate over each characrer in user input
        # and check against the array for valid characters 
        # (pseuso code) for char in letterinput:
        # print (char)

        # else:
        #     return render_template('wordMaker.html', error=error)

# make the logic work with current array first then move onto json file

    return render_template('wordMaker.html')



if  __name__ == "__main__":
    app.run(debug=True)

