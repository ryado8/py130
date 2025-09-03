"""
P
Given an integer year, convert to roman numeral equivalent string.

E
I -> 1
V -> 5
X -> 10
L -> 50
C -> 100
D -> 500
M -> 1000
3000 is the max we will account for

D
input: integer
output: string
intermediate: collection for conversions between integer and roman numeral

A
- Create `numeric_conversion` collection in descending order. iterate through the values of collection and check if the input
integer is >= value. if True, calculate how many times you can multiply the value before being greater than the input integer.
multiply letter equivalent by number of times multiplied and append to a result string. if the multiplying value is 4, append current
letter and previous letter and append to string. subtract the input integer by multiplied value and repeat until the input integer becomes 0.

1. create a list of tuples with value to roman numeral char in descending order and assign to `numeric_conversion`.
2. initialize a `result` to empty string
3. iterate through `numeric_conversion`
    1. if input integer is >= value, assign `count` to the max value that value can be multipied while being less or equal to input.
    2. reassign input % value to input
4. return `result`
"""


class RomanNumeral:
    NUMERIC_CONVERSION = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    def __init__(self, num):
        self.num = num

    def to_roman(self):
        result = ''
        number = self.num

        for value, roman in RomanNumeral.NUMERIC_CONVERSION:
            count = int(number / value)
            result += (roman * count)
            number %= value

        return result