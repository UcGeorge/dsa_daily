# Sun 30 Jul 2023 @8:58PM

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


# Example 1:

# Input: nums = [3,2,3]
# Output: 3


# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2


# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109


# Follow-up: Could you solve the problem in linear time and in O(1) space?

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Find the majority element in the given list of integers using the Boyer-Moore Algorithm.

        The Boyer-Moore Algorithm is an efficient algorithm to find the majority element in a list,
        which is an element that appears more than ⌊n/2⌋ times (where n is the length of the list).

        Algorithm Steps:
        1. Initialize two variables, 'res' and 'count', to None and 0 respectively.
        2. Iterate through each element 'n' in the list 'nums'.
        3. If 'count' is 0, set 'res' to 'n' and 'count' to 1.
           - This step sets a new potential majority candidate when the count becomes zero.
        4. If 'count' is not 0, increment 'count' by 1 if 'n' is equal to 'res', otherwise decrement 'count' by 1.
           - This step essentially cancels out pairs of different elements, preserving the majority element.
        5. Return 'res' as the majority element found.

        Note:
        - The Boyer-Moore Algorithm guarantees that if there exists a majority element in the list,
          the 'res' variable will contain that element by the end of the iteration.

        Parameters:
        nums (List[int]): A list of integers.

        Returns:
        int: The majority element in the given list 'nums'.
        """
        res, count = None, 0
        for n in nums:
            count += 1 if n == res else -1
            if count < 0:
                res, count = n, 1
        return res
