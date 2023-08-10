# Thu 10 Aug 2023 @10:34PM

# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

# You are giving candies to these children subjected to the following requirements:

# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.


# Example 1:

# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.


# Example 2:

# Input: ratings = [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
# The third child gets 1 candy because it satisfies the above two conditions.


# Constraints:

# n == ratings.length
# 1 <= n <= 2 * 104
# 0 <= ratings[i] <= 2 * 104

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        l2r = [1 for _ in ratings]
        r2l = [*l2r]
        for i in range(1, len(l2r)):
            if ratings[i] > ratings[i-1]:
                l2r[i] = l2r[i-1] + 1
        for i in range(-2, -len(r2l)-1, -1):
            if ratings[i] > ratings[i+1]:
                r2l[i] = r2l[i+1] + 1
        return sum([max(l2r[i], r2l[i]) for i in range(len(l2r))])
