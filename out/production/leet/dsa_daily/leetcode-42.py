# Fri 11 Aug 2023 @11:38PM

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


# Example 1:

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.


# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9


# Constraints:

# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        ff, wl, res = [], 0, 0
        for i in range(len(height)):
            h = height[i]
            ff.append(max(0, wl - h))
            wl = max(h, wl)
        wl = 0
        for i in range(-1, -len(height)-1, -1):
            h = height[i]
            res += min(ff[i], max(0, wl - h))
            wl = max(h, wl)
        return res
