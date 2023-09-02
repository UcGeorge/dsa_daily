from typing import List
from leetcode_11 import Solution
import pytest


@pytest.mark.parametrize("height, expected_output", [
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ([1, 1], 1),
])
def test_maxArea(height: List[int], expected_output: List[int]):
    solution = Solution()
    result = solution.maxArea(height)
    assert result == expected_output
