from flask import Flask, render_template, request, json

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

        userInputSet = set(letterinput.lower())

        # words_array = ["apple", "banana", "cherry", "date", "elderberry", "tea", "eat", "ate"]
        
        data = json.load(open('./english-words.json'))

        wordsMatch = []
        for i in data:
            if set(i).issubset(userInputSet):
                wordsMatch.append(i)

        return render_template('wordMaker.html', wordsMatch=wordsMatch)

# output is showing duplicate letters aswell which arent in the user input

# maybe now try conencting to words api instead of json file ?
# make the logic work with current array first then move onto json file

    return render_template('wordMaker.html')



if  __name__ == "__main__":
    app.run(debug=True)

