from leetcode_392 import Solution
import pytest


@pytest.mark.parametrize("s, t, expected_output", [
    ("abc", "ahbgdc", True),
    ("axc", "ahbgdc", False),
    ("", "ahbgdc", True),
    ("abc", "", False),
])
def test_isSubsequence(s: str, t: str, expected_output: bool):
    solution = Solution()
    result = solution.isSubsequence(s, t)
    assert result == expected_output
