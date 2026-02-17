"""
tests.py

Student-facing unit tests for the "Array Inversion Analysis (Disorder Metric)" problem.


What we test here:
1) The provided sample case (mixed values with duplicates).
2) Already-sorted input (should yield 0 inversions).
3) Reverse-sorted input (should yield the maximum inversions n*(n-1)/2).
4) Duplicates + negatives (checks that duplicates do NOT count as inversions).
5) Large input performance sanity check.
"""

import unittest
import solution


class TestProgram(unittest.TestCase):

    def test_case_1_sample_mixed_with_duplicates(self):
        """Sample case: verifies correctness on a typical mixed array with duplicates."""
        arr = [2, 3, 3, 1, 9, 5, 6]
        expected = 5
        self.assertEqual(solution.count_inversions(arr), expected)

    def test_case_2_already_sorted(self):
        """Edge case: already sorted array has 0 inversions."""
        arr = [1, 2, 3, 4, 5]
        expected = 0
        self.assertEqual(solution.count_inversions(arr), expected)

    def test_case_3_reverse_sorted_max_inversions(self):
        """
        Edge case: reverse-sorted array has the maximum inversions.
        For n=5, maximum inversions = 5*4/2 = 10.
        """
        arr = [5, 4, 3, 2, 1]
        expected = 10
        self.assertEqual(solution.count_inversions(arr), expected)

    def test_case_4_negatives_and_duplicates(self):
        """
        Edge case: includes negatives and duplicates.
        Duplicates do NOT count as inversions because the comparison is strict ( > ).

        Array: [-1, -1, -2, 0]
        Inversions:
          index 0 (-1) > index 2 (-2)
          index 1 (-1) > index 2 (-2)
        Total = 2
        """
        arr = [-1, -1, -2, 0]
        expected = 2
        self.assertEqual(solution.count_inversions(arr), expected)

    def test_case_5_large_input_performance(self):
        """
        Performance sanity check.

        We create a reverse-sorted array of size 2000.
        The expected number of inversions is n*(n-1)/2.

        This test ensures:
        - The algorithm handles larger inputs correctly.
        - The solution is not O(n^2) (which would be noticeably slow here).
        """
        n = 2000
        arr = list(range(n, 0, -1))  # reverse sorted
        expected = n * (n - 1) // 2
        self.assertEqual(solution.count_inversions(arr), expected)


if __name__ == "__main__":
    unittest.main()
