"""
P
To be a valid triangle, each side length must be greater than 0.
To be a valid triangle, the sum of the lengths of any two sides must be greater than the length of the remaining side.
An equilateral triangle has three sides of equal length.
An isosceles triangle has exactly two sides of the equal length.
A scalene triangle has three sides of unequal length (no two sides have equal length).

E
raise an exception if any side length <= 0 in constructor
raise an exception if the sum of two sides <= third side
need a method `kind` that returns a string describing type of triangle

D
input: 3 numbers (integers or floats)
output: string

A
constructor
1. initialize a list that contains the three argument values to `sides`
2. use a helper method `is_invalid_triangle` to check if any element is <= 0, or sum of any two sides is <= third side.
raise an exception if method returns True

kind
1. if all three sides are equal, return equilateral
2. if any two sides are equal, return isosceles
3. return scalene
"""

class Triangle:
    def __init__(self, a, b, c):
        self.sides = [a, b, c]
        if self.is_invalid():
            raise ValueError

    @property
    def kind(self):
        if self.is_equilateral():
            return "equilateral"
        elif self.is_isosceles():
            return "isosceles"
        else:
            return "scalene"

    def is_equilateral(self):
        return len(set(self.sides)) == 1

    def is_isosceles(self):
        return len(set(self.sides)) == 2

    def is_invalid(self):
        shortest, mid, longest = sorted(self.sides)

        return any(side <= 0 for side in self.sides) or (shortest + mid <= longest)

