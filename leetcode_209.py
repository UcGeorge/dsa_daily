# Wed 6 Sep 2023 @01:17AM

# Given an array of positive integers nums and a positive integer target, return the minimal length of a
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.


# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.


# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1


# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0


# Constraints:

# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104


# Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Find the minimum length of a contiguous subarray of which the sum is greater than or equal to the target.

        Args:
            target (int): The target sum.
            nums (List[int]): A list of integers.

        Returns:
            int: The minimum length of the subarray, or 0 if no such subarray exists.

        Example:
            >>> solution = Solution()
            >>> solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
            2
        """
        l = r = 0
        lr_sum = nums[0]
        min_len = 0

        while r < len(nums) and l <= r:
            if lr_sum < target:
                r += 1
                if r < len(nums):
                    lr_sum += nums[r]
                continue

            min_len = (min(min_len, r - l + 1) * int(bool(min_len))
                       ) + ((r - l + 1) * int(not bool(min_len)))
            lr_sum -= nums[l]
            l += 1
        return min_len
