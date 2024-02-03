# main/main.py

from flask import Flask, render_template

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


@app.route('/wordmaker')
def wordMaker():
    return render_template('wordMaker.html')


if  __name__ == "__main__":
    app.run(debug=True)