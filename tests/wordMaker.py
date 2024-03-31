import unittest
from flask import Flask, request, json
from collections import Counter
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import wordMaker

class WordMakerTestCase(unittest.TestCase):
    @classmethod

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_word_maker_with_valid_input(self):

        expected_result = "Expected output here"

        response = self.client.post('/wordmaker', data={'letterinput': 'etad'})
        self.assertEqual(response.status_code, 200)
        # Assuming the response is JSON, you can assert the content like this:
        data = response.get_json()
        self.assertEqual(data['result'], expected_result)
