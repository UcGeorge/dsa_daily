# Mon 24 Jul 2023 @7:41PM

# A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.

# Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.


# Example 1:

# Input: s = "YazaAay"
# Output: "aAa"
# Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
# "aAa" is the longest nice substring.
# Example 2:

# Input: s = "Bb"
# Output: "Bb"
# Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.
# Example 3:

# Input: s = "c"
# Output: ""
# Explanation: There are no nice substrings.
 

# Constraints:

# 1 <= s.length <= 100
# s consists of uppercase and lowercase English letters.

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        isUppercase = lambda x: ord(x) in range(65, 91)
        changeCase = lambda x: chr(ord(x) + 32) if isUppercase(x) else chr(ord(x) - 32)

        def recur(string: str) -> str:
            if len(string) < 2: return ""
            for i, c in zip(range(len(string)), string):
                if not changeCase(c) in string:
                    left = recur(string[:i])
                    right = recur(string[i+1:])
                    return left if len(left) >= len(right) else right
            return string
        
        return recur(s)