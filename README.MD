# Word Combination Generator

### Introduction
This Flask application is designed to take user input of random letters and generate all possible combinations of words using those letters.

### Tech Stack
##### Python | Flask | JavaScript | HTML/CSS

### Prerequisites
Please make sure you have the following installed on your machine:
```
pip install -r requirements.txt
```

### Run Application

```
flask --app main run
```

### Run App in Debug Mode

```
python main.py
```

### Docker
Download Docker Desktop for Mac or Windows. This solution uses Python3 and Flask.

### Build Command
Build the image, this may take some time. After your image is built, you can view your image in the Images tab in Docker Desktop.

```
docker build -t word-combination-generator .
```
The -t flag tags your image with a name, `word-combination-generator` in this case. And the `.` lets Docker know where it can find the Dockerfile.

### Run Command
To run the program type this command:

```
docker run -p 5000:5000 word-combination-generator
```

### Run Tests

```
cd tests 
```

```
python -m unittest test_wordMaker.py
```