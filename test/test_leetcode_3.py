from typing import List
from leetcode_3 import Solution
import pytest


@pytest.mark.parametrize("s, expected_output", [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
])
def test_lengthOfLongestSubstring(s: str, expected_output: int):
    solution = Solution()
    result = solution.lengthOfLongestSubstring(s)
    assert result == expected_output
