

---




## 🧠 Dynamic Programming Challenge: Grid Paths

### ❓ Problem Definition

Given a grid with a specified `width` and `height`, write a function that computes the number of unique paths from the **top-left corner** to the **bottom-right corner**, moving only **right** or **down** at each step.

---

### 🔧 Function Signatures

```python
def number_of_ways_to_get_to_end(width: int, height: int) -> int:
```

You may also implement the solution using a **combinatorics** approach:

```python
def number_of_ways_to_get_to_end_permutation(width: int, height: int) -> int:
```

---

### 🧮 What Is Combinatorics and Why Does It Work Here?

In this problem, you always need to make:

- `(width - 1)` right moves  
- `(height - 1)` down moves  

No matter which path you take, you'll always make exactly that many of each move — only the **order** of those moves changes.

The total number of distinct ways to arrange these moves is given by the **combinatorics formula**:

```
Total Paths = (R + D)! / (R! * D!)
```

Where:
- `R = number of right moves = width - 1`
- `D = number of down moves = height - 1`

This formula counts the number of ways to **choose R positions for right moves** out of a total of `R + D` moves.

#### Example:

For a grid with `width = 4` and `height = 3`, you need:
- `3` right moves
- `2` down moves

So the total number of unique paths is:

```
Total Paths = (3 + 2)! / (3! * 2!) = 5! / (3! * 2!) = 120 / (6 * 2) = 10
```

This is a faster and more elegant solution than dynamic programming when you don’t need to generate the actual paths.

---

### 📥 Input

- `width` (int): Number of columns (must be ≥ 1)
- `height` (int): Number of rows (must be ≥ 1)

### 📤 Output

- Returns an integer representing the total number of unique paths from the top-left to the bottom-right corner.

---

### ✅ Constraints

- Only right and down movements are allowed.
- You cannot move left or up.
- Grid is always at least 1×1.

---

### 🔍 Examples

#### Example 1

```python
number_of_ways_to_get_to_end(4, 3)
```

**Output:** `10`  
**Explanation:**  
There are 10 unique ways to reach the bottom-right corner of a 4×3 grid using only right and down moves.

---

#### Example 2

```python
number_of_ways_to_get_to_end(3, 3)
```

**Output:** `6`  
**Explanation:**  
You need 2 right and 2 down moves (4 total steps). The number of unique permutations of those steps is:

```
Total Paths = 4! / (2! * 2!) = 6
```

---

#### Example 3

```python
number_of_ways_to_get_to_end(2, 2)
```

**Output:** `2`  
**Explanation:**  
Only two paths: Right → Down, or Down → Right.

---
---

### 🕒 Runtime Analysis

#### 1. `number_of_ways_to_get_to_end(width, height)`

This is the **dynamic programming** approach. It typically uses a 2D table (or optimized 1D array) to build up the number of ways to reach each cell.

- **Time Complexity:** `O(width * height)`  
  You compute the number of paths for each cell in the grid once.
  
- **Space Complexity:**  
  - `O(width * height)` if using a 2D array  
  - `O(width)` if using a single row and updating in-place

---

#### 2. `number_of_ways_to_get_to_end_permutation(width, height)`

This is the **combinatorics-based** approach using the formula:

```
Total Paths = (R + D)! / (R! * D!)
```

Where `R = width - 1` and `D = height - 1`.

- **Time Complexity:** `O(R + D)` = `O(width + height)`  
  Assuming factorials are computed efficiently and only once. Python's `math.comb()` does this in constant time using internal optimizations.

- **Space Complexity:** `O(1)`  
  No extra memory is used apart from a few variables.

---

## 📝 Required README.txt Format for CC11

Your `README.txt` must include the points you earned for each test in `tests.py`. This helps us understand your testing process and self-assess how well your implementation performs. Use the format shown below.

---

### ✅ Example Format

```
Total points for CC11: XX Points

Detailed points for each test:
1) test_number_of_ways_traverse: 25
2) test_number_of_ways_traverse_permutations: 25
3) test_square_grid: 20
4) test_one_direction_only: 15
5) test_small_grid: 15
```

> ✅ Passed test = full points  
> ❌ Failed test = 0 points  
> 🔁 Partial logic = partial credit **only if** your instructor allows it for this assignment

---

## 🧪 Autograder: Test Case Breakdown

| Test Name | Description | Points |
|-----------|-------------|--------|
| `test_number_of_ways_traverse` | DP solution: `4×3` grid → `10` paths (matches **Example 1** in this spec) | 25 |
| `test_number_of_ways_traverse_permutations` | Combinatorics solution: same `4×3` case → `10` | 25 |
| `test_square_grid` | `3×3` grid → `6` paths (**Example 2**) | 20 |
| `test_one_direction_only` | Edge cases: single row or column (`1×5` and `5×1`) → `1` path each | 15 |
| `test_small_grid` | `2×2` grid → `2` paths (**Example 3**) | 15 |
| **Total** | | **100** |

---

## 🧠 Why This Matters

We emphasize **reasoning-first coding**: DP table meaning, equivalence to the combinatorics formula, and edge cases (degenerate grids). The README format ties your self-check to the same weights the autograder uses.

---

