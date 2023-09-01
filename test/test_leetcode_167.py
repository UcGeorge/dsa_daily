from typing import List
from leetcode_167 import Solution
import pytest


@pytest.mark.parametrize("numbers, target, expected_output", [
    ([2, 7, 11, 15], 9, [1, 2]),
    ([2, 3, 4], 6, [1, 3]),
    ([-1, 0], -1, [1, 2]),
])
def test_twoSum(numbers: List[int], target: int, expected_output: List[int]):
    solution = Solution()
    result = solution.twoSum(numbers, target)
    assert result == expected_output
