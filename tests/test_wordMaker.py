import unittest

import sys
import os
import json
from bs4 import BeautifulSoup

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# import main # Import the main module to ensure routes are registered
# from flask import Flask
# import unittest
from main import app, wordMaker # Import the Flask app instance and the wordMaker function



class TestWordMaker(unittest.TestCase):
    def setUp(self):
        # Create a test Flask app
        self.app = app #use flask app instance from main.py
        self.app.config['TESTING'] = True
        self.client = self.app.test_client() # Define the client attribute here

    def test_word_maker_get(self):
        response = self.client.get('/wordmaker')
        self.assertEqual(response.status_code, 200)
        # Additional assertions can be made here, such as checking the content of the response


    def test_word_maker(self):
        with self.app.test_request_context('/wordmaker', method='POST', data={'letterinput': 'apple'}):
            # Simulate a POST request with 'apple' as input
            response = wordMaker() # Use the wordMaker function from the main module
            # Assuming 'apple' is in the json data
            # Note: You might need to adjust this part based on how you're returning the response
            # For example, if you're returning a template with a list of words, you might need to parse the response
            # to check if 'apple' is in the list of words.
            self.assertIn('apple', response, 200)


    def test_word_count(self):
        response = self.client.post('/wordmaker', data={'letterinput': 'apple'})
        self.assertEqual(response.status_code, 200)
        
        soup = BeautifulSoup(response.data, 'html.parser')
        word_count_element = soup.find('div', id='word-count') # Adjust based on your actual template
        if word_count_element is not None:
            # Extract the numeric part of the string and convert it to an integer
            word_count_text = word_count_element.text.split(':')[1].strip()
            word_count = int(word_count_text)
            self.assertEqual(word_count, 17) # Adjust based on the expected word count for 'apple'
        else:
            self.fail("Word count element not found in the response.")


    # def test_word_count(self):
    # #     # Define a list of words to test
    #     wordsMatch = ['hello', 'world']
    # #     # Call the wordMaker function with the list of words
    #     wordCount = wordMaker(wordsMatch)
    # #     # Assert that the word count is as expected
    #     self.assertEqual(wordCount, 2)


if __name__ == '__main__':
    unittest.main()
