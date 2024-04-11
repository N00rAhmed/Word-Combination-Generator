import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# import main # Import the main module to ensure routes are registered
# from flask import Flask
# import unittest
from main import app, wordMaker # Import the Flask app instance and the wordMaker function
import unittest



class TestWordMaker(unittest.TestCase):
    def setUp(self):
        # Create a test Flask app
        self.app = app #use flask app instance from main.py
        self.app.config['TESTING'] = True

    def test_word_maker(self):
        with self.app.test_request_context('/', method='POST', data={'letterinput': 'apple'}):
            # Simulate a POST request with 'apple' as input
            response = wordMaker() # Use the wordMaker function from the main module
            # Assuming 'apple' is in the json data
            # Note: You might need to adjust this part based on how you're returning the response
            # For example, if you're returning a template with a list of words, you might need to parse the response
            # to check if 'apple' is in the list of words.
            self.assertIn('apple', response)

if __name__ == '__main__':
    unittest.main()
