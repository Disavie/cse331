import unittest
from solution import next_greater_element


class TestNextGreaterElement(unittest.TestCase):
    def test_case_1(self):
        nums = [2, 5, -3, -4, 6, 7, 2]
        expected = [5, 6, 6, 6, 7, -1, 5]

        self.assertEqual(next_greater_element(nums), expected)

    def test_case_2(self):
        nums = [1, 1, 1]
        expected = [-1, -1, -1]  # All equal, no greater element exists

        self.assertEqual(next_greater_element(nums), expected)


if __name__ == "__main__":
    unittest.main()
