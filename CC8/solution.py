class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def compute_formula_tree(tree):
    """
    Evaluate the arithmetic expression represented by the formula tree.

    Leaf nodes contain non-negative integers. Internal nodes contain operator
    codes: -1 (add), -2 (subtract), -3 (divide, truncate toward zero), -4 (multiply).
    Internal nodes always have two children. The tree is never empty.

    Parameters
    ----------
    tree : BinaryTree
        Root of the formula tree.

    Returns
    -------
    int
        The computed value of the expression.

    TODO
    ----
    Implement this function.
    """
    raise NotImplementedError
