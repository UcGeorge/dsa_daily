# Tue 15 Aug 2023 @6:57PM

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"


# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        for i in range(len(strs[0])):
            for s in strs:
                try:
                    if s[i] != strs[0][i]:
                        return lcp
                except IndexError:
                    return lcp
            lcp = lcp + strs[0][i]
        return lcp
