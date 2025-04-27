"""Challenge
Implement the following functions:

sort_words(words: List[str]) -> List[str] - This function accepts a list of words and returns a new list of words sorted in ascending order. Do not modify the original list.

sort_numbers(numbers: List[int]) -> List[int] - This function accepts a list of numbers and returns a new list of numbers sorted in descending order based on their absolute value. Do not modify the original list."""

from typing import List


def sort_words(words: List[str]) -> List[str]:
    return sorted(words)

def sort_numbers(numbers: List[int]) -> List[int]:
    return sorted(numbers, key=lambda x: abs(x), reverse=True)


# do not modify below this line
original_words = ["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]

print(original_words)
print(sort_words(original_words))

original_numbers = [1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]

print(original_numbers)
print(sort_numbers(original_numbers))