import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import wordMaker
import unittest
from flask import Flask, request

class TestWordMaker(unittest.TestCase):
    def setUp(self):
        # Create a test Flask app
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True

    def test_word_maker(self):
        with self.app.test_request_context('/', method='POST', data={'letterinput': 'apple'}):
            # Simulate a POST request with 'apple' as input
            response = wordMaker()
            # Assuming 'apple' is in the json data
            self.assertIn('apple', response)

if __name__ == '__main__':
    unittest.main()
