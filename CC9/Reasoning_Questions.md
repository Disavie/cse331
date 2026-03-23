# CC9 (CC5) Disjoint Set — Interview Reasoning Questions

**Topic:** Disjoint Set (Union-Find)  
**Source:** specs + solution.py

---

## Question 1 — Explain the representative and why it matters

**Difficulty:** Easy  

**Prompt:**  
"In a disjoint set, what is the *representative* of a set, and why do we need a single representative per set instead of just storing which set each element belongs to?"

**Expected answer (high-level):**
- The representative is one chosen element of the set (e.g., the root in a tree view) that identifies the set.
- Every member of the set must return the *same* representative from `find_representative` so we can tell if two elements are in the same set by comparing representatives.
- Using one representative per set lets us implement union and find efficiently with a parent (or similar) structure; we don’t need to relabel or scan all elements when merging.

**Complexity:** N/A (conceptual).

**Strong answer includes:** Definition of representative, “same set ⇔ same representative,” and why that design supports efficient merge/find.

**Common weak answers:** Saying “it’s the root” without saying why we need a single id; not linking representative to “same set” checks.

---

## Question 2 — Why use rank (or size) when merging?

**Difficulty:** Medium  

**Prompt:**  
"When merging two sets in union-find, we could always make one root point to the other. Why do we use *rank* (or size) and attach the smaller tree under the larger one?"

**Expected answer (high-level):**
- If we always attach arbitrarily, we can end up with a long chain (e.g., a linked list). Then `find_representative` can take O(n) in the worst case.
- By attaching the *smaller* tree under the *larger* (by rank or size), we keep the tree height small (e.g., O(log n) without path compression).
- With path compression, union by rank (or size) helps keep the inverse Ackermann bound: find and merge stay O(α(n)) ≈ O(1) in practice.

**Complexity:** Without rank/size: find can be O(n). With union by rank + path compression: O(α(n)) per operation.

**Strong answer includes:** Risk of linear chain, “smaller under larger” rule, and impact on height and complexity.

**Common weak answers:** “It makes it faster” without saying why; not mentioning tree height or chains.

---

## Question 3 — What is path compression and why do we do it in find?

**Difficulty:** Medium  

**Prompt:**  
"Explain *path compression* in `find_representative`. What do we change, and why does it matter for future operations?"

**Expected answer (high-level):**
- During `find_representative(x)`, we walk from `x` up to the root. Path compression means: for every node along that path, we set its parent (or link) directly to the root.
- So after one find, all visited nodes point to the root; the path is “compressed.”
- Future finds for those nodes (or nodes under them) become one or two steps instead of walking the whole path again. This keeps the effective tree height low and yields O(α(n)) amortized time per operation.

**Complexity:** Amortized O(α(n)) per find with path compression + union by rank.

**Strong answer includes:** “Point nodes on the path to the root,” “flattens the tree,” “speeds up future finds.”

**Common weak answers:** Confusing path compression with union by rank; saying “we compress the path” without saying we repoint nodes to the root.

---

## Question 4 — Dry-run: trace merge and find

**Difficulty:** Medium  

**Prompt:**  
"Start with an empty disjoint set. Do: `add_set(1)`, `add_set(2)`, `add_set(3)`, `merge_sets(1,2)`, `merge_sets(2,3)`. Draw or describe the parent/rank state after each step. Then say what `find_representative(1)` and `find_representative(3)` return and why."

**Expected answer (high-level):**
- After three add_set: each element is its own parent, rank 0: e.g. parents {1:1, 2:2, 3:3}, ranks {1:0, 2:0, 3:0}.
- merge_sets(1,2): same rank so e.g. 2’s root (2) points to 1; rank of 1 becomes 1. parents {1:1, 2:1, 3:3}, ranks {1:1, 2:0, 3:0}.
- merge_sets(2,3): find(2)→1, find(3)→3. Rank 1 > 0, so 3 points to 1. parents {1:1, 2:1, 3:1}, ranks unchanged.
- find_representative(1) → 1 (root). find_representative(3) → 1 (path 3→1). Same representative ⇒ same set.

**Strong answer includes:** Correct parent/rank updates, correct final representatives, and “same set” interpretation.

**Common weak answers:** Wrong parent after merge (e.g. 1 pointing to 2); forgetting to update rank when merging two rank-0 trees.

---

## Question 5 — Edge cases and what merge_sets should do

**Difficulty:** Easy–Medium  

**Prompt:**  
"What should `merge_sets(a, b)` do if (i) `a` was never added, (ii) `a` and `b` are already in the same set? Why is it correct to do nothing in those cases?"

**Expected answer (high-level):**
- (i) If `a` (or `b`) was never added, it has no set. We can’t merge “nothing” with a set, so we do nothing (and optionally ignore or validate).
- (ii) If `a` and `b` are already in the same set, they already share a representative. Merging would be redundant and could break invariants (e.g., double-linking). So we do nothing.
- Correctness: we only merge when both elements exist and their representatives differ; after that, all members of both sets share one representative.

**Strong answer includes:** Both cases, “do nothing,” and brief correctness justification (no set vs. same set).

**Common weak answers:** Merging anyway when one doesn’t exist; not recognizing that “same set” means no-op.

---

## Summary for interviewers

| # | Focus              | Type              | Difficulty |
|---|--------------------|-------------------|------------|
| 1 | Representative     | Explain + justify | Easy       |
| 2 | Union by rank      | Tradeoffs         | Medium     |
| 3 | Path compression   | Explain + justify | Medium     |
| 4 | Merge/find trace   | Dry-run           | Medium     |
| 5 | merge_sets edge cases | Edge cases     | Easy–Medium |

**Rubric (general):** Strong answers give a clear definition or rule, tie it to correctness or complexity, and (for traces) show correct state. Weak answers are vague (“it’s faster”) or miss the invariant (e.g., “same set ⇒ same representative”).
