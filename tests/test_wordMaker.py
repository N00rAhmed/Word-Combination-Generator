import pytest
from flask import Flask
from flask_testing import TestCase
from main import wordMaker

class TestWordMaker(TestCase):
    def create_app(self):
        wordMaker.config['TESTING'] = True
        return wordMaker
