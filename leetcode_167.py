# Fri 1 Sep 2023 @12:42PM

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.


# Example 1:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].


# Example 2:

# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].


# Example 3:

# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].


# Constraints:

# 2 <= numbers.length <= 3 * 104
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000
# The tests are generated such that there is exactly one solution.

from typing import List, Optional


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Find two numbers in the 1-indexed list that add up to the target.

        Args:
            numbers (List[int]): A list of integers.
            target (int): The target sum to find.

        Returns:
            List[int]: A list of two indices of the numbers in the list that add up to the target.

        Example:
            solution = Solution()
            result = solution.twoSum([2, 7, 11, 15], 9)
            # Returns [1, 2] because numbers[1] + numbers[2] = 7 + 2 = 9.
        """
        diff = {}  # Dictionary to store differences and their corresponding indices.

        for i, n in enumerate(numbers):
            # Calculate the difference between the target and the current number.
            complement = target - n

            # Check if the complement exists in the dictionary.
            if complement in diff:
                # Return the indices of the two numbers that add up to the target.
                return [diff[complement], i + 1]

            # Store the current number's index plus 1 in the dictionary with its complement as the key.
            diff[n] = i + 1
