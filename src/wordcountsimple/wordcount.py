# wordcountsimple/wordcount.py
# wordcountsimple/word_counter.py
"""
Module for counting words in a given text.
"""

from collections import Counter
from typing import List

class WordCounter:
    """
    Class for counting words in a given text.
    """

    def __init__(self, text: str) -> None:
        """
        Initialize the WordCounter instance.

        Args:
        text (str): The input text to count words from.
        """
        self.text = text

    def count_words(self) -> dict:
        """
        Count the words in the input text.

        Returns:
        dict: A dictionary with words as keys and their counts as values.
        """
        words = self.text.split()
        word_counts = Counter(words)
        return dict(word_counts)

    def get_top_n_words(self, n: int) -> List[tuple]:
        """
        Get the top n words with their counts.

        Args:
        n (int): The number of top words to return.

        Returns:
        List[tuple]: A list of tuples containing the top n words and their counts.
        """
        word_counts = self.count_words()
        top_n_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:n]
        return top_n_words

if __name__ == "__main__":
    text = "This is a sample text. This text is for demonstration purposes."
    counter = WordCounter(text)
    print("Word counts:", counter.count_words())
    print("Top 3 words:", counter.get_top_n_words(3))