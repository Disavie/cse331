

## 🔍 Multi String Search

<img src="img/data1.png" alt="Trie Search Diagram" width="400"/>




### 🧾 Problem Statement

Implement a function that accepts a large string and a list of smaller strings, each shorter than the large string. The function should return a list of boolean values. Each boolean should indicate whether the respective smaller string appears anywhere in the large string.

**Restrictions:**  
You are **not allowed** to use any built-in string search or matching functions provided by your programming language.

---

### 💡 Suggested Approaches

- A straightforward method is to loop over each small string and, for each one, iterate through the characters of the large string to check for a match using nested loops. Consider whether this method is efficient from a time complexity standpoint.

- Another approach is to create a data structure similar to a suffix trie that stores all possible suffixes of the large string. You can then check each small string against this structure. Think about how this impacts both time and memory usage.

- Alternatively, you can construct a trie using all the small strings. Then, traverse the large string character by character, checking whether any substring matches one of the small strings by searching through the trie. Compare the efficiency of this method to the one above.


### 🎤 Interview reasoning (optional practice)

See **`Reasoning_Questions.md`** in this folder for five short reasoning prompts (multi-pattern search, trie tradeoffs, complexity, overlaps, edge cases). Use them to prep for oral / whiteboard discussion; they are not auto-graded unless your instructor says otherwise.


---

✅ **Example 1: Basic Matches**  
```python
big_string = "abcde"
small_strings = ["a", "ab", "e", "de", "xyz"]
```
**Output:**  
```python
[True, True, True, True, False]
```

---

✅ **Example 2: Overlapping Substrings**  
```python
big_string = "abababa"
small_strings = ["aba", "bab", "ab", "ba"]
```
**Output:**  
```python
[True, True, True, True]
```

---

✅ **Example 3: Repeated Queries**  
```python
big_string = "repeatrepeat"
small_strings = ["repeat", "repeat", "eat", "rep"]
```
**Output:**  
```python
[True, True, True, True]
```

## 🧠 Optimal Time & Space Complexity

- **Time Complexity:** O(ns + bs)  
- **Space Complexity:** O(ns)

Where:  
- `n` = total number of small strings  
- `s` = length of the longest small string  
- `b` = length of the large string






<img src="img/API.png" alt="API" width="400"/>

---

## 📝 Required README.txt Format for CC10

Your `README.txt` must include the points you earned for each test in `tests.py`. This helps us understand your testing process and self-assess how well your implementation performs. Use the format shown below.

---

### ✅ Example Format

```
Total points for CC10: XX Points

Detailed points for each test:
1) test_case_1: 15
2) test_case_2_basic_match: 15
3) test_case_3_overlapping_matches: 15
4) test_case_4_repeated_queries: 15
5) test_case_5_empty_string_list: 10
6) test_case_6_empty_big_string: 15
7) test_case_7_case_sensitivity: 15
```

> ✅ Passed test = full points  
> ❌ Failed test = 0 points  
> 🔁 Partial logic = partial credit **only if** your instructor allows it for this assignment

---

## 🧪 Autograder: Test Case Breakdown

| Test Name | Description | Points |
|-----------|-------------|--------|
| `test_case_1` | Primary multi-pattern check (“big string” with mixed hits and misses) | 15 |
| `test_case_2_basic_match` | Basic matches on `"abcde"` (from spec example) | 15 |
| `test_case_3_overlapping_matches` | Overlapping substrings in `"abababa"` | 15 |
| `test_case_4_repeated_queries` | Repeated / shared patterns in `"repeatrepeat"` | 15 |
| `test_case_5_empty_string_list` | Edge: nonempty big string, **empty** list of small strings → `[]` | 10 |
| `test_case_6_empty_big_string` | Edge: empty big string with `""` and other patterns | 15 |
| `test_case_7_case_sensitivity` | Matching is **case-sensitive** | 15 |
| **Total** | | **100** |

---

## 🧠 Why This Matters

We emphasize **reasoning-first coding**: explicit complexity, data-structure choices, and edge cases. The README format ties your self-check to the same weights the autograder uses. Pair it with **`Reasoning_Questions.md`** for interview-style follow-ups.
