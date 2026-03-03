# Coding Challenge — Next Greater Element in a Circular Array

## Problem Statement

You are given a list of integers `nums`. For every index `i` in this list, you need to determine the **first number that appears to the right of `i`** (moving forward through the list) that is **strictly greater** than `nums[i]`.

- If you reach the end of the list and have not found a greater number, **wrap around to the front** and keep checking, because the array should be treated as **circular**.
- If no greater element exists even after wrapping around, record `-1` for that position.

Return a new list `result` where `result[i]` is the next greater element for `nums[i]` according to this rule.

---

### Examples

#### Example 1
Input:  [1, 2]

Output: [2, -1]


Explanation:
- For the first element `1`, the next greater number is `2`.
- For the second element `2`, there is no greater number (even after wrapping), so we put `-1`.

#### Example 2
Input:  [2, 5, -3, -4, 6, 7, 2]

Output: [5, 6, 6, 6, 7, -1, 5]

Explanation:
- The list is circular, so after the last element you continue from the beginning.
- For the first `2`, the next greater element is `5`.
- For the last `2` at index 6, we wrap around to the front and the first bigger value we encounter is `5`.

---

## Hints

1. **Brute force idea:**  
   For each index, scan forward (wrapping to the beginning if needed) until you find a bigger value.  
   This works but runs in `O(n^2)` time for an array of length `n`.

2. **Better idea:**  
   Use a **stack** to keep track of indices whose next greater element has not been found yet.

3. **Efficient approach:**  
   - Traverse the array **twice** (to simulate the circular wrap-around).  
   - Maintain a **monotonic stack** of indices where the next greater element hasn’t been recorded.  
   - When the current number is greater than the number at the index on top of the stack, pop that index and record the current number as its next greater element.  
   - Continue until the stack holds only indices of elements still waiting for a larger value.

4. **Goal:**  
   Achieve **O(n) time** and **O(n) extra space**.

---

### What Is a Monotonic Stack?

A **monotonic stack** is a stack that is kept in a specific sorted order as you process elements:

- **Monotonic increasing stack:** values are kept in **increasing order** from bottom to top.  
- **Monotonic decreasing stack:** values are kept in **decreasing order** from bottom to top.

To maintain this order:
1. While the current element would break the stack’s order (e.g., you want increasing but the new element is smaller), **pop** from the stack until the order is restored.
2. Push the current element (or its index).

This pattern is very useful in problems like **Next Greater Element** because:
- Each element is **pushed and popped at most once**, so the whole solution runs in `O(n)` time.
- The stack stores elements that are still waiting to find their next greater (or smaller) value.

Example for `nums = [2, 1, 4, 3]`:
- Start empty. Push `2`.
- Push `1` (stack is [2,1] — decreasing).
- See `4` → greater than `1` → pop `1`. Greater than `2` → pop `2`. Push `4`.
- See `3` → push (stack [4,3]).  
From this we find the next greater for `1` and `2` quickly without scanning the entire array.





## Function Signature

```python
def next_greater_element(nums: list[int]) -> list[int]:
    # Your code here