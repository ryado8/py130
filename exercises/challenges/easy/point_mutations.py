"""
P
Given two strings representing DNA, count the number of differences between them.
If one strand is shorter than another, only check for diferences up to the length of shorter strand.

E
A constructor accepts a DNA strand string argument.
A method accepts second DNA strand string and returns difference.

D
input: string
output: integer

A
constructor
- accept a DNA strand string argument

hamming_distance method
1. get the shorter length string. initialize a count to 0
2. iterate idx in range(length)
3. check if chars are different at idx for both strings
    - if True, increment counter by 1
4. return counter
"""
class DNA:
    def __init__(self, strand):
        self.strand = strand

    def hamming_distance(self, other):
        counter = 0
        if not (self.strand and other):
            return counter

        for char1, char2 in zip(self.strand, other):
            if char1 != char2:
                counter += 1

        return counter

