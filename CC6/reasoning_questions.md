# CC6 — Reasoning & Critical Thinking Questions  
## Next Greater Element in a Circular Array

Answer the following in your own words. Reasoning matters more than a single “correct” phrasing.

---

## Questions

### 1. Circular wrap-around

**Question:** For the input `nums = [5, 4, 3, 2, 1]`, what is `result[4]` (the next greater element for the last element, `1`)? Explain why, in one or two sentences.

---

### 2. Role of the stack

**Question:** In the monotonic-stack solution, we store **indices** on the stack, not the actual values. Give one concrete reason why storing indices (rather than values) makes it easier to fill the `result` array correctly.

---

### 3. Why scan twice?

**Question:** The efficient solution loops over indices `0` to `2*n - 1` (i.e., the array is traversed twice). Why is one pass through the array not enough to assign every position its next greater element? Use a small example (e.g., length 2 or 3) to illustrate.

---

### 4. When does an index get its answer?

**Question:** Consider the forward (left-to-right) algorithm that uses a monotonic **decreasing** stack of indices. At the moment we **pop** an index `j` from the stack because `nums[circular_idx] > nums[j]`, we set `result[j] = nums[circular_idx]`. Explain in one short paragraph why the element at `circular_idx` is guaranteed to be the **first** (leftmost, in circular order) greater element for `nums[j]`, and not some later greater element.

---

### 5. Changing the problem

**Question:** Suppose we change the problem to: *“For each index `i`, find the **previous** greater element (the first element to the **left** of `i` that is strictly greater than `nums[i]`), with wrap-around so that we can look left from index 0 by going to the end of the array.”* Would the same idea of “traverse twice with a monotonic stack” still work? If yes, describe how you would adapt the traversal direction and/or the stack condition (what we compare when we pop). If no, explain what goes wrong.

---

---

# Answer Key

### 1. Circular wrap-around

**Answer:** `result[4] = 5`. After the last element `1`, we wrap to the start of the array. The first element we see is `5`, which is strictly greater than `1`, so the next greater element for `nums[4]` is `5`.

---

### 2. Role of the stack

**Answer:** We need to write the answer into `result` at the **position** where we found the next greater element. When we pop an index `j`, we know the current element is the next greater for `nums[j]`, so we must set `result[j] = current_value`. If we only stored values on the stack, we would not know which index `j` to update; storing indices lets us do `result[top] = nums[circular_idx]` correctly.

---

### 3. Why scan twice?

**Answer:** In a circular array, the “next” greater element for an index might lie **after** we wrap from the end back to the beginning. For example, with `nums = [2, 1]`: for index 1, the only element to the right is the end of the array; after wrapping, we see index 0 again. So the next greater for `1` is `2` at index 0. In one pass left-to-right, by the time we process index 0 (at the start), we have not yet “wrapped” to consider index 0 as being to the right of index 1. A second pass simulates wrap-around: when we process index 0 again, we can resolve index 1’s next greater as `2`. So one pass is not enough; we need (conceptually) two passes to allow every position to see elements that appear after wrap-around.

---

### 4. When does an index get its answer?

**Answer:** The stack maintains indices whose next greater element has **not** been found yet, and the stack is monotonic **decreasing** by the values at those indices. So when we are at `circular_idx` and we pop `j` because `nums[circular_idx] > nums[j]`, the key observation is: we process indices in increasing circular order. Any index we already passed and left on the stack has a value **greater than or equal to** `nums[j]` (otherwise we would have popped `j` earlier). So no element we have already passed can be the first greater for `j`. The current element at `circular_idx` is the first we have seen that is strictly greater than `nums[j]`, so it is correct to set `result[j] = nums[circular_idx]`.

---

### 5. Changing the problem

**Answer:** Yes, the same idea works. We adapt it as follows:

- **Traverse right-to-left** (backward) so that “previous” in the circular sense means “we have already seen it” in our traversal. To handle wrap-around, we traverse twice in reverse (e.g., from index `2*n - 1` down to `0`, with `circular_idx = idx % n`).
- **Monotonic stack:** We still want the “next” (in our traversal order) element that is greater. Since we move backward, “next” in time is “to the left” in the array. So we maintain a **monotonic decreasing** stack (by value): when the current element is greater than the value at the top index, we pop and set that index’s **previous** greater to the current element.
- Alternatively, we can think of it as a **monotonic decreasing stack** of indices while scanning backward; when `nums[circular_idx] > nums[stack[-1]]`, we pop and assign `result[stack_top] = nums[circular_idx]`.

So: same “two passes + monotonic stack” idea, with traversal direction reversed and the meaning of “next” changed to “previous” (in the original array order).
