# Compute Formula Tree

## Problem statement

You are given a **binary formula tree** whose structure represents an arithmetic expression. Each node holds an integer:

- **Leaf nodes** store non-negative integers (operands).
- **Internal nodes** store **operator codes** as negative integers. Each internal node has exactly two children (left and right).

Your task is to compute the value of the expression represented by the tree by evaluating it from the leaves to the root.

### Operator codes (internal nodes only)

| Code | Operator | Meaning        |
|------|----------|----------------|
| `-1` | `+`      | Addition       |
| `-2` | `-`      | Subtraction    |
| `-3` | `/`      | Division       |
| `-4` | `*`      | Multiplication |

**Division:** Use integer division that **truncates toward zero** (same as Python's `//` for non-negative operands; negative results also truncate toward zero).

---

## Required API

You must implement:

```python
def compute_formula_tree(tree):
    """
    Evaluate the arithmetic expression represented by the formula tree.

    Parameters
    ----------
    tree : BinaryTree
        Root of the formula tree. Leaves hold non-negative integers;
        internal nodes hold operator codes -1 (add), -2 (sub), -3 (div), -4 (mul).

    Returns
    -------
    int
        The computed value of the expression.
    """
```

**Binary tree class** (provided to students):

```python
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
```

---

## Examples

### Example 1: Single-node tree

A tree with one node (a leaf) simply returns that node’s value.

- Tree: one node with `value = 7`
- **Output:** `7`

### Example 2: Nested operations

Tree structure (value at each node):

```
         -4          (multiply)
        /   \
      -1      -2     (add)  (subtract)
      / \     / \
     3   5   10  2
```

Expression: `(3 + 5) * (10 - 2)` = `8 * 8` = **64**

- **Output:** `64`

### Example 3: Division with truncation toward zero

Tree:

```
       -3            (divide)
      /   \
     7     2
```

Expression: `7 / 2` → integer division truncating toward zero → **3**

- **Output:** `3`

Another division example: `-5 / 2` (if intermediate results could be negative) truncates toward zero to `-2`. For this problem, division-by-zero will not occur.

---

## Constraints and assumptions

- The tree is **always valid**: every internal node has exactly two children; leaves have `left` and `right` equal to `None`.
- The tree is **never empty** (at least one node).
- **Division by zero will not occur.**
- A **single-node tree** (only root) is a leaf; return that node’s value.
- Leaf values are **non-negative integers**. Operator codes are exactly `-1`, `-2`, `-3`, `-4` as above.

---

## Complexity expectations

- **Time:** O(n), where n is the number of nodes in the tree.
- **Auxiliary space:** O(h), where h is the height of the tree (e.g., recursion stack or explicit stack depth).

---

## Clarifications

- **Leaf vs internal node:** A node is a leaf if and only if both `left` and `right` are `None`. Otherwise it is an internal node and its `value` is an operator code.
- **Order of operands:** For subtraction and division, the **left** subtree is the first operand and the **right** subtree is the second (e.g., left − right, left ÷ right).
- **Truncation:** Division must truncate toward zero (e.g., 7 // 2 = 3; -5 // 2 = -2 in languages that support it). For this problem, operands from leaves are non-negative; intermediate results might be negative only if subtraction is used.

---

## Testing and Self-Check (Required)

You are provided with a test suite in `tests.py`. Before submitting, run the tests locally to verify your solution.

In your **`README.md`** you must include a self-check section that lists the test results.

### Required README format

Your README must list **each test from the provided `tests.py` and the points earned for that test**, using the format below.

**Total points for CC8: 100 Points**

**Detailed points for each test:**

1. test_single_node: 8  
2. test_single_node_zero: 8  
3. test_add_only: 8  
4. test_sub_only: 8  
5. test_mul_only: 8  
6. test_div_only_truncate: 8  
7. test_div_exact: 8  
8. test_nested_add_mul: 10  
9. test_nested_deep: 8  
10. test_subtraction_negative_result: 8  
11. test_division_negative_truncate_toward_zero: 10  
12. test_large_leaf: 8  

- Use the **exact test names** from `tests.py`.
- This is the **same README format used for both Coding Challenges and Projects**.
- Points reflect whether you passed that test: **passed** = full points for that test; **failed** = 0 points.

---

## Grading

Your solution will be evaluated using the following test cases.

- `test_single_node` – 8 points  
- `test_single_node_zero` – 8 points  
- `test_add_only` – 8 points  
- `test_sub_only` – 8 points  
- `test_mul_only` – 8 points  
- `test_div_only_truncate` – 8 points  
- `test_div_exact` – 8 points  
- `test_nested_add_mul` – 10 points  
- `test_nested_deep` – 8 points  
- `test_subtraction_negative_result` – 8 points  
- `test_division_negative_truncate_toward_zero` – 10 points  
- `test_large_leaf` – 8 points  

**Total: 100 points**

Partial credit is not awarded within a test case. A test case must pass completely to receive the points assigned to that test.

---

## Final Notes

- Reason first, code second.
- Use failing tests as feedback, not as a reason to guess.
- Clear thinking will outperform rushed implementation on this challenge.

— **Team 331**
