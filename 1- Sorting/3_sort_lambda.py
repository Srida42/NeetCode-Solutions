"""Implement the following functions:

sort_words(words: List[str]) -> List[str] - This function accepts a list of words and returns a new list of words sorted based on their length, in descending order. Use a lambda function to sort the words by their length.

sort_numbers(numbers: List[int]) -> List[int] - This function accepts a list of numbers and returns a new list of numbers sorted based on their absolute value, in ascending order. Use a lambda function to sort the numbers by their absolute value."""

from typing import List


def sort_words(words: List[str]) -> List[str]:
    return sorted(words, key=lambda x: len(x), reverse=True)


def sort_numbers(numbers: List[int]) -> List[int]:
    return sorted(numbers, key=lambda x: abs(x))


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))