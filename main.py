# main/main.py

from flask import Flask, render_template
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


@app.route('/wordmaker', methods=['GET'])
def wordMaker():
    
    api_url = "https://api.dictionaryapi.dev/api/v2/entries/en/mango"

    try:
        response = requests.get(api_url)
        response_data = json.loads(response.text)
        formatted_data = json.dumps(response_data, indent=4)
        return render_template('wordMaker.html', data=formatted_data)

    except Exception as e:
        return render_template('wordMaker.html', error=str(e))



if  __name__ == "__main__":
    app.run(debug=True)