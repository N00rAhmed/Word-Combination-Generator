import unittest
import sys
import os
from bs4 import BeautifulSoup
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import app, wordMaker


class TestWordMaker(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()


    def test_word_maker_get(self):
        response = self.client.get('/wordmaker')
        self.assertEqual(response.status_code, 200)


    def test_word_maker(self):
        with self.app.test_request_context('/wordmaker', method='POST', data={'letterinput': 'apple'}):
            response = wordMaker()
            # Note: You might need to adjust this part based on how you're returning the response
            # For example, if you're returning a template with a list of words, you might need to parse the response
            # to check if 'apple' is in the list of words.
            self.assertIn('apple', response, 200)


    def test_word_count(self):
        response = self.client.post('/wordmaker', data={'letterinput': 'apple'})
        self.assertEqual(response.status_code, 200)
        
        soup = BeautifulSoup(response.data, 'html.parser')
        word_count_element = soup.find('div', id='word-count')
        if word_count_element is not None:
            # Extract the numeric part of the string and convert it to an integer
            word_count_text = word_count_element.text.split(':')[1].strip()
            word_count = int(word_count_text)
            self.assertEqual(word_count, 17)
        else:
            self.fail("Word count element not found in the response.")




if __name__ == '__main__':
    unittest.main()
