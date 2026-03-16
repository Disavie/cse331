"""
Tests for compute_formula_tree. Import student submission as program.
"""
import unittest
import solution


def make_leaf(value):
    """Create a leaf node (no children)."""
    return solution.BinaryTree(value, None, None)


def tree(value, left, right):
    """Create an internal node with left and right subtrees."""
    return solution.BinaryTree(value, left, right)


class TestComputeFormulaTree(unittest.TestCase):
    """Test compute_formula_tree with valid formula trees."""

    def test_single_node(self):
        """Single-node tree returns the node's value."""
        t = make_leaf(7)
        self.assertEqual(solution.compute_formula_tree(t), 7)

    def test_single_node_zero(self):
        """Single node with value 0."""
        t = make_leaf(0)
        self.assertEqual(solution.compute_formula_tree(t), 0)

    def test_add_only(self):
        """Simple addition: 3 + 5 = 8."""
        t = tree(-1, make_leaf(3), make_leaf(5))
        self.assertEqual(solution.compute_formula_tree(t), 8)

    def test_sub_only(self):
        """Simple subtraction: 10 - 2 = 8."""
        t = tree(-2, make_leaf(10), make_leaf(2))
        self.assertEqual(solution.compute_formula_tree(t), 8)

    def test_mul_only(self):
        """Simple multiplication: 6 * 7 = 42."""
        t = tree(-4, make_leaf(6), make_leaf(7))
        self.assertEqual(solution.compute_formula_tree(t), 42)

    def test_div_only_truncate(self):
        """Division truncates toward zero: 7 / 2 = 3."""
        t = tree(-3, make_leaf(7), make_leaf(2))
        self.assertEqual(solution.compute_formula_tree(t), 3)

    def test_div_exact(self):
        """Exact division: 8 / 2 = 4."""
        t = tree(-3, make_leaf(8), make_leaf(2))
        self.assertEqual(solution.compute_formula_tree(t), 4)

    def test_nested_add_mul(self):
        """(3 + 5) * (10 - 2) = 8 * 8 = 64."""
        left = tree(-1, make_leaf(3), make_leaf(5))
        right = tree(-2, make_leaf(10), make_leaf(2))
        t = tree(-4, left, right)
        self.assertEqual(solution.compute_formula_tree(t), 64)

    def test_nested_deep(self):
        """(2 * 3) + (8 / 2) = 6 + 4 = 10."""
        left = tree(-4, make_leaf(2), make_leaf(3))
        right = tree(-3, make_leaf(8), make_leaf(2))
        t = tree(-1, left, right)
        self.assertEqual(solution.compute_formula_tree(t), 10)

    def test_subtraction_negative_result(self):
        """2 - 5 = -3."""
        t = tree(-2, make_leaf(2), make_leaf(5))
        self.assertEqual(solution.compute_formula_tree(t), -3)

    def test_division_negative_truncate_toward_zero(self):
        """(-3) / 2 should truncate toward zero to -1 (not -2)."""
        left = tree(-2, make_leaf(0), make_leaf(3))  # 0 - 3 = -3
        t = tree(-3, left, make_leaf(2))
        self.assertEqual(solution.compute_formula_tree(t), -1)

    def test_large_leaf(self):
        """Single large leaf value."""
        t = make_leaf(1000000)
        self.assertEqual(solution.compute_formula_tree(t), 1000000)


if __name__ == "__main__":
    unittest.main()
