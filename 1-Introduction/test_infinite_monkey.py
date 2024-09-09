"""
Infinite Monkey Theorem: a monkey hitting random keys an infinite number of times
will eventually type a given text

Actually has applications in tech, such as brute force algorithms for password cracking

Exercise: create a function that will randomly generate strings and compare it to the goal string every 1000 tries
"""
from random import choice
from string import ascii_lowercase

goal_string = "methinks it is like a weasel"

def string_generator(len):
    """
    Args:
        len (str): length of desired string
    Returns:
        (str): randomly generated string of desired length
    """
    chars = ascii_lowercase + " "
    return "".join([choice(chars) for i in range(len)])

def score_string(goal, compare):
    """
    Scores two sets of strings
    Args:
        goal (str)
        compare (str)
    Returns:
        (float): the percent of matching letters in the two strings
    """
    min_len = min(len(goal), len(compare))
    max_len = max(len(goal), len(compare))
    score = 0
    for i in range(min_len):
        score += 1 if goal[i] == compare[i] else 0
    return score/max_len
def infinite_monkey(goal):
    """
    Iteratively generates strings randomly until it generates the goal string
    """
    for i in range(1000):

    return

def hillclimbing_monkey():
    return

def test_monkey():
