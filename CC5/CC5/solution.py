"""
starter.py

CC5 — Array Inversion Analysis (Disorder Metric)

Implement the function `count_inversions`.

An inversion is a pair of indices (i, j) such that:
    i < j and array[i] > array[j]

Your goal is to return the total number of inversions in the array.

Performance Requirement:
    - Target time complexity: O(n log n)
    - Target space complexity: O(n)

Notes:
    - The input may contain duplicates and negative numbers.
    - Duplicate values do NOT count as inversions (comparison is strict >).
    - You may modify the array if your algorithm requires it.
"""
from __future__ import annotations

from typing import Callable, TypeVar, List

T = TypeVar("T")


def count_inversions(array: List[int]) -> int:

    """
    Return the number of inversions in the array.

    Parameters:
        array (List[int]): A list of integers. The list may include
            duplicate and negative values.

    Returns:
        int: The total number of inversion pairs.

    An inversion is defined as a pair of indices (i, j) such that:
        i < j and array[i] > array[j]

    You are expected to implement an efficient algorithm.
    A naive O(n^2) solution may not pass large test cases.
    """


    def merge(a, b):
        i = 0
        j = 0
        inv = 0
        out = []

        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                out.append(a[i])
                i += 1
            else:
                out.append(b[j])
                inv += len(a) - i   # a[i] >= b[j:len(b)] since a and b are sorted
                j += 1

        # add remaining elements from a and b to the merged list
        while i < len(a):
            out.append(a[i])
            i += 1

        while j < len(b):
            out.append(b[j])
            j += 1

        return out, inv


    def sort(arr):
        if len(arr) <= 1:
            return arr, 0

        mid = len(arr) // 2
        left, leftinv = sort(arr[:mid])
        right, rightinv = sort(arr[mid:])

        merged, x = merge(left, right)

        return merged, leftinv + rightinv + x

    # discard the sorted list only carte about how many inversiosn there were
    _, total = sort(array)
    return total
