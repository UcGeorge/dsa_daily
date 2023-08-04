# Fri 4 Aug 2023 @10:27PM

# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

# 0 <= j <= nums[i] and
# i + j < n

# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].


# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.


# Example 2:

# Input: nums = [2,3,0,1,4]
# Output: 2


# Constraints:

# 1 <= nums.length <= 104
# 0 <= nums[i] <= 1000
# It's guaranteed that you can reach nums[n - 1].

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums) - 1
        min_i, min_diff = len(nums) - 1, 0
        for i in range(len(nums) - 2, -1, -1):
            n, gap = nums[i], len(nums) - i - 1
            diff = gap - n
            if diff < 0:
                diff = 0
            if diff <= min_diff:
                min_i, min_diff = i, diff
        return 1 + self.jump(nums[:min_i+1])

    def jump_optimised(self, nums: List[int]) -> int:
        res = 0
        l = r = 0
        while r < len(nums) - 1:
            f = 0
            for i in range(l, r + 1):
                f = max(f, i + nums[i])
            l, r = r + 1, f
            res += 1
        return res
