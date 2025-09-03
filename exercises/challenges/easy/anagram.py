"""
P
Given a string and a list of words, return a list with anagrams.

E
Case-insensitive
Anagrams must be same length and have same exact letters
A word is not an anagram of itself

D
input: string, list
ouput: list
intermediate: list to sort the characters

A
- create a helper method `sort_string` that converts input string to list of lowercased chars and returns list in ascending order.
pass in input string to `sort_string` and assign to `sorted_string`. iterate through the input list and pass word into `sort_string`.
if the returned list is equal to `sorted_string`, append word to `result` list. return `result` list

sort_string
takes in string and returns a list of lowercased chars sorted ascending

1. initialize `sorted_string` and assign to returned value of input string passed into `sort_string`
2. iterate through input list and pass word into `sort_string`
3. if returned list is equal to `sorted_string`, append word to `result` list
4. return `result`
"""


class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def _sort_string(self, word):
        return sorted([char.lower() for char in word])

    def match(self, lst):
        sorted_string = self._sort_string(self.word)

        return [
            word
            for word in lst
            if self._sort_string(word) == sorted_string
            and (self.word != word.lower())
        ]
