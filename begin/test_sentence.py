"""
fixture usage
"""

import pytest
from sentence import Sentence

@pytest.fixture
def example_sentence():
    return Sentence("Hello World!")

def test_letter_count(example_sentence):
    assert example_sentence.letter_count() == 12

def test_word_count(example_sentence):
    assert example_sentence.word_count() == 2

def test_upper(example_sentence):
    assert example_sentence.upper() == "HELLO WORLD!"
