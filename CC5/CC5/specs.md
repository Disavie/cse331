# Array Inversion Analysis (Disorder Metric)

## Description

Write a function that takes an array of integers and returns the number
of **inversions** in the array.

An inversion occurs for any valid indices `i` and `j` such that:

-   `i < j`, and\
-   `array[i] > array[j]`

Intuitively, the number of inversions measures how far the array is from
being sorted in nondecreasing order.

------------------------------------------------------------------------

## Example

Given:

    array = [3, 4, 1, 2]

There are **4** inversions.

The following index pairs represent inversions:

    [0, 2], [0, 3], [1, 2], [1, 3]

------------------------------------------------------------------------

## Sample Input

    array = [2, 3, 3, 1, 9, 5, 6]

## Sample Output

    5

The following pairs of indices represent inversions:

    [0, 3], [1, 3], [2, 3], [4, 5], [4, 6]

------------------------------------------------------------------------

## Constraints

-   1 ≤ n ≤ 200000\
-   Integers may be negative or duplicated\
-   Duplicate values do NOT form inversions with each other

------------------------------------------------------------------------

## Optimal Space & Time Complexity

    O(n log n) time
    O(n) space

Where `n` is the length of the array.

A brute-force O(n²) solution will not pass large test cases.

------------------------------------------------------------------------

# Hints

## Hint 1

The brute-force approach compares every pair of indices in the array and
counts how many of them represent inversions.

This approach takes:

    O(n²)

Can you do better?

------------------------------------------------------------------------

## Hint 2

If the number of inversions measures how unsorted the array is, and it
takes:

    O(n log n)

time to sort an array using an optimal sorting algorithm, can you
determine how unsorted the array is within that same time complexity?

------------------------------------------------------------------------

## Hint 3

Think about solving this problem if, instead of being given one array,
you were given two separate arrays representing the left and right
halves.

The total inversions would equal:

-   Inversions in the left half\
-   Inversions in the right half\
-   Inversions formed while merging the two halves

Recall how Merge Sort works.

------------------------------------------------------------------------

## Hint 4

You can use an algorithm very similar to Merge Sort.

1.  Recursively determine inversions in the left half.
2.  Recursively determine inversions in the right half.
3.  Merge the two sorted halves while counting cross inversions.

Whenever you insert an element from the right half before an element in
the left half during merge, that right element forms inversions with
**all remaining elements in the left half**.

Example:

    left  = [1, 3, 4]
    right = [2, 2, 5]

When merging, inserting `2` before `3` and `4` counts 2 inversions.

------------------------------------------------------------------------

## What We Will Test

-   Correctness on small inputs
-   Handling of duplicates
-   Already sorted arrays
-   Reverse sorted arrays
-   Performance on large inputs

------------------------------------------------------------------------

## Function Signature (Python)

``` python
def count_inversions(array: list[int]) -> int:
    pass
```

------------------------------------------------------------------------

# 📝 Required README.txt Format for CC5

Your `README.txt` must include the points you earned for each test in
`tests.py`.\
This helps us understand your testing process and self-assess how well
your implementation performs.\
Use the format shown below.

------------------------------------------------------------------------

## ✅ Example Format

    Total points for CC5: XX Points

    Detailed points for each test:
    1) test_case_1_sample_mixed_with_duplicates: 20
    2) test_case_2_already_sorted: 20
    3) test_case_3_reverse_sorted_max_inversions: 20
    4) test_case_4_negatives_and_duplicates: 20
    5) test_case_5_large_input_performance: 20

> ✅ Passed test = full points\
> ❌ Failed test = 0 points\
> 🔁 Partial logic passed = give yourself partial credit **only if
> instructed by staff**

------------------------------------------------------------------------

## 🧪 Test Case Breakdown

  -----------------------------------------------------------------------------------------------
  Test Name                                     Description                             Points
  --------------------------------------------- --------------------------------------- ---------
  `test_case_1_sample_mixed_with_duplicates`    Typical mixed input with duplicates     20
                                                (matches sample behavior)               

  `test_case_2_already_sorted`                  Already sorted array → 0 inversions     20

  `test_case_3_reverse_sorted_max_inversions`   Reverse sorted array → maximum          20
                                                inversions                              

  `test_case_4_negatives_and_duplicates`        Handles negatives; duplicates do        20
                                                **not** count as inversions             

  `test_case_5_large_input_performance`         Large reverse-sorted input to           20
                                                discourage O(n²) solutions              

  **Total**                                                                             **100**
  -----------------------------------------------------------------------------------------------

------------------------------------------------------------------------

## 🧠 Why This Matters

We are focusing on **reasoning-first coding** this semester. The
`README.txt` encourages you to:

-   Think beyond just "passing tests"
-   Track how your code handles each case
-   Build self-debugging and test interpretation skills

Just like in real-world engineering teams, **self-reporting** is part of
developing engineering maturity.

--- **Team 331**
