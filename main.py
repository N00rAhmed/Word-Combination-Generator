from flask import Flask, render_template, request, json
import os
from collections import Counter

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

        userInputSet = set(Counter(letterinput.lower()))

        userInputArray = []
        for k in letterinput:
            userInputArray.append(k.lower())
        characterCount = Counter(userInputArray)
        print(characterCount)


        # data = json.load(open('./english-words.json'))

        # Dynamically determine the path to the JSON file
        script_dir = os.path.dirname(os.path.realpath(__file__))
        json_file_path = os.path.join(script_dir, './english-words.json')

        # Load the JSON file
        with open(json_file_path, 'r') as f:
            data = json.load(f)

        
        # with open('./english-words.json') as f:
        #     data = json.load(f)
        

        wordsMatch = []

        # words_array = ["apple", "banana", "cherry", "elderberry", "tea", "eat", "ate", "date", "add"]
        
        wordCount = 0
        
        for i in data:
            outputCharacterCounter = Counter(i)

            if set(i).issubset(userInputSet) and characterCount >= outputCharacterCounter:
                wordsMatch.append(i)
                
                wordCount = len(wordsMatch)
                print("word count: " + str(wordCount)) 
                # print("i(json): {}, characterCount(Input): {}, outputCharacterCount(Output): {}".format(i, characterCount, outputCharacterCounter))


        return render_template('wordMaker.html', wordsMatch=wordsMatch, wordCount=wordCount)


    return render_template('wordMaker.html')



if  __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    # app.run(debug=True)

