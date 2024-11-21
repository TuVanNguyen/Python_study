"""
Class implementation of fractions to demonstrate how to set up a class in python
"""


def gcd(m, n):
    """
    Helper functions don't need to access class members, so they reside outside of classes.
    This function finds the greatest common divisor using Euclid's Algorithm.
    Args:
        m (int): 1st number
        n (int): 2nd number

    Returns:
        (int): the greatest common divisor for m and n
    """
    while m % n != 0:
        old_m = m
        old_n = n

        m = old_n
        n = old_m % old_n
    return n


class Fraction:
    def __init__(self, num: int, den: int):
        """
        Constructor to initialize class members
        Args:
            num (int): numerator
            den (int): denominator
        """
        self.num = num
        self.den = den

    def __str__(self):
        """
        Overriding built-in class methods
        Returns:
            (str): Fraction represented as string
        """
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other):
        new_num = self.num * other.den + \
                 self.den * other.num
        new_den = self.den * other.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __eq__(self, other):
        """
        Checks for deep equality between the fraction with an other fraction
        Args:
            other (Fraction): another fraction to compare to
        Returns:
            (bool): whether the fraction has the same value as the other fraction
        """
        num1 = self.num * other.den
        num2 = other.num * self.den

        return num1 == num2

    def __gt__(self, other):
        return (self.num/self.den) > (other.num/other.den)

    def __lt__(self, other):
        return (self.num/self.den) < (other.num/other.den)


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(2, 3)
    print(x)
    print(x + y)
    print(x == y)
    print(x * y)
    print(x / y)
    print(x > y)
    print (x < y)
