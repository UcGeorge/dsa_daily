# Mon 21 Aug 2023 @11:29PM

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.


# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.


# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.


# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.


import re
from typing import Any


class Solution:
    """
    A class that provides methods to check whether a given string is a palindrome.
    A palindrome is a string that reads the same forwards and backwards when ignoring non-alphanumeric characters.
    """

    def __init__(self) -> None:
        pass

    def _transform_string(self, s: str) -> str:
        """
        Transforms the input string by converting it to lowercase and removing non-alphanumeric characters.

        Args:
            s (str): The input string to be transformed.

        Returns:
            str: The transformed string.
        """
        lowercase_string = s.lower()
        alphanumeric_string = re.sub(r'[^a-z0-9]', '', lowercase_string)
        return alphanumeric_string

    def isPalindrome(self, s: str) -> bool:
        """
        Checks whether the input string is a palindrome when ignoring non-alphanumeric characters.

        Args:
            s (str): The input string to be checked.

        Returns:
            bool: True if the input string is a palindrome, False otherwise.

        Examples:
            >>> checker = PalindromeChecker()
            >>> checker.is_palindrome("A man, a plan, a canal, Panama")
            True
            >>> checker.is_palindrome("race a car")
            False
        """
        transformed_string = self._transform_string(s)
        left, right = 0, -1

        # Iterate through the transformed string while comparing characters from both ends
        while len(transformed_string) + right > left:
            if transformed_string[left] != transformed_string[right]:
                return False
            left += 1
            right = -1 - left

        return True
