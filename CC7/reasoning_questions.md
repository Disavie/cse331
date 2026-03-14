# CC7 — Reasoning & Critical Thinking Questions  
## Tree Branch Summation

Answer the following in your own words. Reasoning matters more than a single "correct" phrasing.

---

## Questions

### 1. Branches and leaves

**Question:** The problem asks for the sum of each **branch**, where a branch is a path from the root to a **leaf**. Why do we only append the running sum to the result list when we reach a leaf node? What would go wrong if we appended the sum at every node we visit?

---

### 2. Order of branches in the output

**Question:** The spec requires branch sums to be listed **from the leftmost branch to the rightmost branch**. In the recursive solution we always recurse on the left child before the right child. Explain in one or two sentences why that order guarantees the output list is in the correct left-to-right order.

---

### 3. Passing the running sum

**Question:** The helper function receives a **running sum** as a parameter and passes `running_sum + node.value` to each recursive call. Why is it important to pass the updated sum as an argument (and possibly use a new variable like `new_running_sum`) instead of, say, updating a single global or mutable variable that gets modified as we traverse?

---

### 4. Recursion depth and space

**Question:** The space complexity is O(n), partly due to the **recursion call stack**. Describe a binary tree shape (e.g., "a tree that looks like a single chain") for which the recursion depth is as large as possible in terms of the number of nodes \(n\). What is that maximum depth, and why does it make the stack space O(n)?

---

### 5. Changing the problem

**Question:** Suppose we change the problem to: *"Return a list of the sum of values on **every** path from the root to **any** node (not only leaves)."* So for a tree with nodes 1, 2, 3 where 1 is root and 2 and 3 are left and right children, we would return something like [1, 3, 4] (root-only, root+left, root+right). What would you change in the recursive algorithm? Specifically: when would you append to the result list, and would you still need to recurse into both children?

---

---

# Answer Key

### 1. Branches and leaves

**Answer:** A branch is defined as a path from the root to a **leaf**. Only leaf nodes are the end of such a path. If we appended the sum at every node, we would be recording partial paths (e.g., root-only or root-to-internal-node) as if they were branches, and we would get duplicate or incorrect sums. The problem asks only for root-to-leaf path sums, so we append only when we have reached a leaf (no left and no right child).

---

### 2. Order of branches in the output

**Answer:** Recessing left before right means we fully explore the left subtree (and thus all leaves on the left) before we ever visit any node in the right subtree. So we discover and append leftmost branches first, then branches to their right, and so on. That matches the required "leftmost branch to rightmost branch" order in the output list.

---

### 3. Passing the running sum

**Answer:** Each branch from root to leaf is independent. When we recurse left and then right, the right subtree must use the same "sum from root to current node" that we had when we entered this node—it must not include values that were added while traversing the left subtree. If we used a single global or mutable variable and updated it as we go, we would have to "undo" or overwrite it when returning from the left subtree before going right, which is error-prone. Passing the running sum by value (as an argument) gives each recursive call its own correct sum for the path from root to the current node, so left and right subtrees do not interfere.

---

### 4. Recursion depth and space

**Answer:** The worst case is a tree that is a **single chain** (each node has at most one child), e.g., root → left → left → … → leaf. In such a tree, the depth (number of edges from root to the deepest leaf) is \(n - 1\) for \(n\) nodes, so the recursion can go \(n\) levels deep (one call per node). The call stack therefore uses O(n) space. So the recursion stack contributes O(n) to space complexity.

---

### 5. Changing the problem

**Answer:** We would append the running sum at **every** node we visit, not only at leaves: after updating the running sum with the current node's value, we append it to the result list. We would still recurse into both children (when they exist), because every node is the end of some root-to-node path. The only change is removing the "if leaf then append" condition and instead appending at each node right after we compute the new running sum (and we might need to append before recursing so that the current node's path is recorded). We still recurse left before right if we want a consistent left-to-right order in the output.
