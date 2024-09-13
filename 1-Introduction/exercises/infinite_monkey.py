"""
Infinite Monkey Theorem: a monkey hitting random keys an infinite number of times
will eventually type a given text

Actually has applications in tech, such as brute force algorithms for password cracking

Exercise: create a function that will randomly generate strings and compare it to the goal string every 1000 tries
"""
from random import choice
from string import ascii_lowercase

goal_string = "methinks it is like a weasel"


def string_generator(strlen):
    """
    Args:
        strlen (int): length of desired string
    Returns:
        (str): randomly generated string of desired length
    """
    chars = ascii_lowercase + " "
    return "".join([choice(chars) for i in range(strlen)])


def score_string(goal, compare):
    """
    Scores two sets of strings
    Args:
        goal (str)
        compare (str)
    Returns:
        (int): the number of matching letters in the two strings
    """
    min_len = min(len(goal), len(compare))
    score = 0
    for i in range(min_len):
        score += 1 if goal[i] == compare[i] else 0
    return score


def hill_climbing_string_generator(old_string, score_array):
    """
    Generates a string replacing 1st unmatching char in old_string with random char
    Args:
        old_string (s):
        score_array (list): array where ith element is 1 for matching char and 0 for unmatching char
    Returns:
        (s): new string with first unmatching character replaced with random char

    """
    chars = ascii_lowercase + " "
    s_list = list(old_string)
    for i in range(len(old_string)):
        if score_array[i] == 0:
            s_list[i] = choice(chars)
            return "".join(s_list)


def hill_climbing_score(goal, compare):
    """
    Args:
        goal (str):
        compare (str):
    Returns:
        (list): an array where ith item is 1 if ith char in goal and compare match, else 0

    """
    return [1 if goal[i] == compare[i] else 0 for i in range(len(goal))]


def infinite_monkey(goal):
    """
    Iteratively generates strings randomly until it generates the goal string.
    Prints best string every 1000 tries
    Args:
        goal (str): string the program is trying to generated
    Return:
        None
    """
    best_string = ""
    best_score = 0
    iterations = 0
    random_string = ""
    while random_string != goal:
        iterations += 1
        random_string = string_generator(len(goal))
        score = score_string(goal, random_string)
        if score > best_score:
            best_score = score
            best_string = random_string
        if iterations % 1000 == 0:
            print(f"Best string in {iterations} iterations with score {best_score} out of {len(goal)}: {best_string}")

    print(f"Generated the string in {iterations} iterations")
    return


def hill_climbing_monkey(goal):
    """
    Uses a Hill-climbing algorithm to speed up the process of randomly generating the string matching goal.
    The hill-climbing algorithm means that the program will only replace 1 unmatching char
    with a random char for each iteration, so that the program can progressively generate strings closer to goal string
    with more iterations.
    Args:
        goal (str): string that function is trying to generate
    Returns:

    """
    best_string = ""
    best_score = [0 for i in range(len(goal))]
    iterations = 1
    random_string = string_generator(len(goal))
    score = best_score
    while random_string != goal:
        iterations += 1
        random_string = hill_climbing_string_generator(random_string, score)
        score = hill_climbing_score(goal, random_string)
    if sum(score) > sum(best_score):
        best_score = score
        best_string = random_string
    if iterations % 1000 == 0:
        print(f"Best string in {iterations} iterations with score {best_score} out of {len(goal)}: {best_string}")

    print(f"Generated the string in {iterations} iterations: {random_string}")
    return


if __name__ == "__main__":
    #infinite_monkey(goal=goal_string)
    hill_climbing_monkey(goal=goal_string)
