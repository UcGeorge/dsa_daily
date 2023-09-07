# Thu 7 Sep 2023 @011:77AM

# Given a string s, find the length of the longest
# substring
#  without repeating characters.


# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.


# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.


# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, uniq = 0, 0, set()
        max_uniq = 0
        while r < len(s) and l <= r:
            if s[r] in uniq:
                max_uniq = max(max_uniq, len(uniq))
                uniq.remove(s[l])
                l += 1
            else:
                uniq.add(s[r])
                r += 1
        return max(max_uniq, len(uniq))
