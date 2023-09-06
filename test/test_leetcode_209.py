from typing import List
from leetcode_209 import Solution
import pytest


@pytest.mark.parametrize("target, nums, expected_output", [
    (7, [2, 3, 1, 2, 4, 3], 2),
    (4, [1, 4, 4], 1),
    (11, [1, 1, 1, 1, 1, 1, 1, 1], 0)
])
def test_minSubArrayLen(target: int, nums: List[int], expected_output: int):
    solution = Solution()
    result = solution.minSubArrayLen(target, nums)
    assert result == expected_output
