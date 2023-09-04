from typing import List
from leetcode_15 import Solution
import pytest


@pytest.mark.parametrize("nums, expected_output", [
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    ([0, 1, 1], []),
    ([0, 0, 0], [[0, 0, 0]])
])
def test_threeSum(nums: List[int], expected_output: List[List[int]]):
    solution = Solution()
    result = solution.threeSum(nums)
    assert result == expected_output
