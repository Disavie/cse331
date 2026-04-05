# CC10 — Multi String Search — Interview Reasoning Questions

**Topic:** Multi-pattern substring search, tries, complexity  
**Source:** `specs.md`, `tests.py`, and your solution approach

---

## Question 1 — Why avoid built-in string search?

**Difficulty:** Easy  

**Prompt:**  
"This problem forbids built-in string search (e.g. `find`, `index`, `in` on substrings, regex). In an interview, how would you justify still implementing the logic yourself, and what is the asymptotic cost of the obvious double-loop solution over the big string for each small string?"

**Expected answer (high-level):**
- We want you to **own the comparison logic** and reason about **nested loops / trie walks**, not hide work inside library calls whose complexity you might not discuss.
- Naive: for **each** of **n** small strings of length up to **s**, scan the big string of length **b** → roughly **O(n · b · s)** in the worst case (or **O(nbs)** depending on how you count character compares), which can blow up when **b** and **n** are large.

**Complexity:** Naive ≈ **O(nbs)**-style; optimal target from specs: **O(ns + bs)**.

**Strong answer includes:** Separation of “library black box” vs explicit scanning; correct order of growth with **b**, **n**, and **s**.

**Common weak answers:** Saying built-ins are “slow” without complexity; claiming naive is **O(n + b)**; ignoring number of small strings.

---

## Question 2 — Trie of all small strings + one pass over the big string

**Difficulty:** Medium  

**Prompt:**  
"One optimal approach builds a trie from the **small** strings, then walks the **big** string once (or scans from each position with a bounded trie walk). Why does the total time end up **O(ns + bs)** (with **n** = count of small strings, **s** = longest small length, **b** = big length) as in the specs?"

**Expected answer (high-level):**
- Building the trie touches **O(total characters in all small strings)**, which is **O(ns)** in the usual bound where **s** is the max length.
- For each position in the big string you advance in the trie **at most O(s)** steps backward along characters of small patterns, and there are **b** positions → **O(bs)** for that phase (sometimes written together as **O(ns + bs)** when **s** is the dominant per-step cap).
- Together: linear-ish in **size of trie** plus **length of big string** times bounded depth **s**.

**Complexity:** Time **O(ns + bs)**; space **O(ns)** for the trie nodes.

**Strong answer includes:** Trie size **O(ns)**; per-position work capped by **s**; not **O(b²)** from rescanning unboundedly.

**Common weak answers:** “We look at each character once” without the trie-depth argument; mixing up **n** with total string length only.

---

## Question 3 — Suffix trie / suffix structure of the **big** string

**Difficulty:** Medium  

**Prompt:**  
"The specs mention building something like a **suffix trie** of the **large** string. What goes wrong with **space** if you materialize all suffixes naïvely, and when might you still mention this idea in an interview despite that drawback?"

**Expected answer (high-level):**
- A naive suffix trie can have **Θ(b²)** nodes (or worse) in the worst case because many suffixes share prefixes but the structure can still be huge relative to **b**.
- That often makes it **impractical for very large b** compared to the **small-string trie** approach (**O(ns)** space).
- In an interview, it’s still a **valid tradeoff story**: good when the **big** string is fixed and queried many times with **few / short** patterns after preprocessing—but poor when **b** is massive or memory matters.

**Complexity:** Naive suffix structure: worst-case space **~O(b²)** (conceptual); contrast **O(ns)** for small trie.

**Strong answer includes:** Space blow-up; reuse vs one-shot query patterns.

**Common weak answers:** Saying suffix trie is always O(b); ignoring quadratic worst-case behavior.

---

## Question 4 — Overlapping matches (e.g. `"aba"` in `"abababa"`)

**Difficulty:** Easy / Medium  

**Prompt:**  
"Patterns overlap in the big string. Does your algorithm need a separate ‘overlap handling’ phase, or does the usual scan / trie walk already report that a substring **occurs** somewhere? Why?"

**Expected answer (high-level):**
- You only need a **boolean per small string**: “does it appear **anywhere**?”
- Overlaps don’t require special counting; starting a check at each position (or folding into a trie walk) naturally sees **all** substring starts, including overlapping ones.
- The extra work is about **how many positions** you consider and **how you cap depth**, not about merging overlap intervals.

**Complexity:** N/A beyond understanding that overlap doesn’t change **existence** queries.

**Strong answer includes:** Difference between “count all occurrences” vs “exists somewhere”; sliding starts cover overlaps.

**Common weak answers:** Claiming overlaps require KMP only for this yes/no problem (not strictly true for existence); saying you must skip ahead past overlap always.

---

## Question 5 — Edge cases: empty list and empty strings

**Difficulty:** Medium  

**Prompt:**  
"`tests.py` includes an **empty list** of small strings and an **empty big** string with patterns like `""`. How should the function behave, and why is `""` a notorious edge case in substring problems?"

**Expected answer (high-level):**
- **Empty list** of queries → return **[]** (nothing to check).
- For **empty big** string: any **non-empty** small string should be **False**; the **empty string** `""` as a pattern is often defined to occur at every position (or treated as vacuously present)—your tests expect **`[False, False, True]`** for `("", ["a", "b", ""])` so **empty pattern ⇒ True** while non-empty cannot match.
- Interview angle: conventions differ by site; **state the convention** you use and **match tests**.

**Complexity:** N/A (correctness / specs).

**Strong answer includes:** Empty list → []; `""` in `""` / substring definitions; agreement with **given** test contract.

**Common weak answers:** Hard-coding without explaining; wrong outcome for `""` pattern.

---

*These questions are for practice and discussion; grading follows `specs.md` (autograder tests + any course policy on reasoning write-ups).*
