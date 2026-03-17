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

    if tree.left is None and tree.right is None:
       return tree.value 

    left = compute_formula_tree(tree.left)
    right = compute_formula_tree(tree.right)

    symbol = tree.value
    

    if symbol == -1:      # add
        return left + right
    elif symbol == -2:    # subtract
        return left - right
    elif symbol == -3:    # divide (truncate toward zero)
        return int(left / right)
    elif symbol == -4:    # multiply
        return left * right

