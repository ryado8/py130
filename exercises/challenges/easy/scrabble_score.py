"""
P
Given a string, return an integer that represents the score of the combined letters.

E
invalid words should return a score of 0
words are case-insensitive

D
input: string
output: integer
intermediate: dictionary for score conversion

A
- initialize `score_dict` and assign to dictionary for score conversions. if input has non-alpha chars, return 0. iterate through lowercased
chars of input. iterate through keys of dictionary and return key that contains char. Find value of that key and add to score. Return score
after iterating through all chars.

1. initialize `score_dict` and assign to dictionary for score conversions, initialize `total` to 0
2. if input string is not alpha, return total
3. iterate through lowercased chars of input string
4. iterate through dictionary items
    - if char is in key, increment `total` by value
5. return `total`
"""


class Scrabble:
    SCORE_DICT = {
        "aeioulnrst": 1,
        "dg": 2,
        "bcmp": 3,
        "fhvwy": 4,
        "k": 5,
        "jx": 8,
        "qz": 10,
    }

    def __init__(self, word):
        self.word = word if word else ""

    @classmethod
    def calculate_score(cls, word):
        return cls(word).score()

    def score(self):
        total = 0

        valid_chars = [char for char in self.word if char.isalpha()]

        for char in valid_chars:
            for key, value in Scrabble.SCORE_DICT.items():
                if char.lower() in key:
                    total += value
                    break

        return total