# Wed 30 Aug 2023 @5:45PM

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true


# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false


# Constraints:

# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.


# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Check if string 's' is a subsequence of string 't'.

        Args:
            s (str): The potential subsequence.
            t (str): The target string.

        Returns:
            bool: True if 's' is a subsequence of 't', False otherwise.
        """
        s_index = t_index = 0

        while s_index < len(s) and t_index < len(t):
            if s[s_index] == t[t_index]:
                s_index += 1
            t_index += 1

        return s_index == len(s)
