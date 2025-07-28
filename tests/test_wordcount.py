import sys, os, math
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
import pytest
from src.wordcountsimple.wordcount import WordCounter

def test_word_counter_init():
    text = "Sample text for testing"
    sut = WordCounter(text)
    assert sut.text == text

def test_count_words():
    text = "This is a sample text. This text is for demonstration purposes."
    sut = WordCounter(text)
    word_counts = sut.count_words()
    assert len(word_counts) == 10
    assert word_counts["This"] == 2
    assert word_counts["is"] == 2
    assert word_counts["a"] == 1
    assert word_counts["sample"] == 1
    assert word_counts["text"] == 2
    assert word_counts["for"] == 1
    assert word_counts["demonstration"] == 1
    assert word_counts["purposes"] == 1

def test_count_words_empty_text():
    text = ""
    sut = WordCounter(text)
    word_counts = sut.count_words()
    assert len(word_counts) == 0

def test_get_top_n_words():
    text = "This is a sample text. This text is for demonstration purposes."
    sut = WordCounter(text)
    top_n_words = sut.get_top_n_words(3)
    assert len(top_n_words) == 3
    assert top_n_words[0][0] == "This"
    assert top_n_words[0][1] == 2
    assert top_n_words[1][0] == "text"
    assert top_n_words[1][1] == 2
    assert top_n_words[2][0] == "is"
    assert top_n_words[2][1] == 2

def test_get_top_n_words_empty_text():
    text = ""
    sut = WordCounter(text)
    top_n_words = sut.get_top_n_words(3)
    assert len(top_n_words) == 0

def test_get_top_n_words_negative_n():
    text = "This is a sample text. This text is for demonstration purposes."
    sut = WordCounter(text)
    with pytest.raises(ValueError):
        sut.get_top_n_words(-1)

def test_get_top_n_words_zero_n():
    text = "This is a sample text. This text is for demonstration purposes."
    sut = WordCounter(text)
    top_n_words = sut.get_top_n_words(0)
    assert len(top_n_words) == 0