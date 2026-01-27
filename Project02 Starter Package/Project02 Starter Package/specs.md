 # Project 2: Sorting Algorithms

**Due Monday, February 9th @ 11:59 PM ET**

_This is not a team project, do not copy someone else's work._

_Make sure to read the entire project description, especially the grading policies._

## Background Information

![](img/sorting_comparison.png)

A **sorting algorithm** is an algorithm that puts elements in
a [certain order](https://en.wikipedia.org/wiki/Total_order). Such algorithms are often used to organize an array or
list in numerical or lexicographical order. However, their use is not limited in scope to such simple orderings, a fact
that will be demonstrated in this project.

Throughout the 20th century, as the domain of problems to which computers were applied grew, so too did the size of data
sets that required sorting. This resulted in the rapid development of sorting algorithms. Simple _O($n^2$)_ algorithms,
such as selection and bubble sort, were supplemented by faster _O(n log(n))_ algorithms, such as quick or merge sort.
Still, these _O($n^2$)_ algorithms have their place to this day because they are often faster for sorting small sets of
data. Optimized modern sorting methods use hybrid techniques, which leverage the recursive nature of quicksort or merge
sort by using these algorithms for large sets of data, but which use an algorithm such as insertion sort for the
smaller fragments of data that the input ends up being separated into.

This project will expose you to insertion sort, selection sort, bubble sort, merge sort, and quicksort. Additionally, it
will include a hybrid sort using merge and insertion sorts. Python's built in `list.sort` is actually based on
a merge/insertion hybrid sort.

In addition to the overviews of each sort presented below, we encourage you to refer to the relevant sections in Zybooks.

### Bubble Sort

![](img/bubble_sort.png)

Bubble sort is one of the simplest sorting algorithms, and it works by repeatedly traversing a list and swapping
adjacent elements whenever it finds two that are out of order. This traversal is then repeated until a complete
traversal is completed without having to do any swaps, which indicates that the list has been sorted.

Like selection and insertion sorts, it has _O($n^2$)_ worst/average case
time complexity, and can operate in-place for _O(1)_ auxiliary space complexity. Bubble sort, however, tends to be the
slowest of the sorting algorithms mentioned here in practice.

### Insertion Sort

![](img/insertion_sort.png)

Insertion sort works by keeping track of sorted and unsorted portions of the list, and building up the sorted portion on
the lefthand side of the list. To start, the first element is considered sorted (a single-element list is always
sorted), and the remainder of the list is the unsorted portion. Next, the first element of the unsorted portion is
compared to each element of the sorted portion in reverse order until its proper place in the sorted portion is found.
Finally, the element from the unsorted portion is _inserted_ into the list at the proper spot, which for arrays requires
a series of swaps. Each of these insertion steps increases the size of the sorted section by one, allowing the algorithm
to proceed with a new "first element of the unsorted section" until the entire list has been sorted.

Insertion sort has _O(n^2)_ worst/average case _O(n)_ for the best case, and the same space complexity as bubble sort, but ittends to be a bit faster in practice. Insertion sort is especially well suited to sorting small lists.

### Selection Sort

![](img/selection_sort.png)

Selection sort works quite similarly to insertion sort, keeping a sorted and unsorted portion of the list, and building up the sorted portion one element at a time. The difference with selection sort is that instead of taking the first
element of the unsorted portion and inserting it at the proper spot, selection sort _selects_ the smallest element of the unsorted portion on each pass, and puts it at the end of the sorted portion. This time, the entire list starts out
as the unsorted portion instead of the first element being sorted–the starting element of the sorted portion has to befound from the list like every other element since elements don't move after being put in the sorted portion.

To highlight the difference: insertion sort picks a spot for the next element by searching through the sorted portion,
selection sort picks an element for the next spot by searching through the unsorted portion.

Selection sort has identical time/space complexity for the worst case just like bubble and insertion sorts, and like insertion sort is faster than
bubble sort. Still, insertion sort is usually preferred for small-data sorting.

### Merge Sort

![](img/merge_sort.png)

Merge sort is a more efficient algorithm than the three mentioned above. It works on the principle of [Divide and Conquer](https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm), repeatedly breaking down a list
into several sublists until each sublist consists of a single element, then repeatedly merging pairs of these sublists
in a manner that results in a sorted list.

Unlike bubble, insertion, and selection sorts, merge sort is worst case _O(n log(n))_, so it scales much better to large
lists. While there are ways to write an in-place merge sort, the typical space complexity is [_O(n)_](https://stackoverflow.com/a/28641693).

### Quicksort

Quicksort is an advanced sorting algorithm which works differently from the others we've seen so far. Like merge sort,
it is recursive, but for each step a "pivot" element from the list is selected, and elements to the left and right of the pivot are swapped as needed so that the list is partitioned into elements less than the pivot and elements greater
than or equal to the pivot. Quicksort is then applied recursively to these partitions until the list is fully sorted.

Like merge sort, quicksort is average case _O(n log(n))_, but its worst case performance is _O(n^2)_.
The performance of quicksort depends heavily on the method used for pivot selection, with the
[median-of-three pivot selection algorithm](https://stackoverflow.com/a/7560859)
helping to avoid pitfalls common in more naive (e.g., random, first, last) selection techniques.

In practice, quicksort is still popular because it performs well on array-backed lists by exploiting optimizations for [locality of reference](https://en.wikipedia.org/wiki/Locality_of_reference).
Merge sort may outperform it for very large data sets, and is usually preferred for linked lists. Both of these algorithms are significant improvements on the average case _O(n^2)_ algorithms mentioned above.

### Hybrid Sorting

While merge sort has a better runtime complexity than insertion sort, it has some overhead from not being an in-place
sort, and insertion sort tends to be faster for sorting small amounts of data. This means that it is more efficient to
combine the two algorithms into a hybrid sorting routine, where the recursive list partitions that merge sort creates
are sorted by insertion sort instead of merge sort once they get small enough.

### **Auxiliary Space Complexity: An Overview**

Auxiliary space complexity refers to the amount of additional space, aside from the input, that an algorithm or a method requires to execute. This is especially important when evaluating the efficiency of algorithms. It's different from the space complexity in that it doesn't consider the space required by the inputs; instead, it looks only at the extra space (temporary space) taken up, typically for variables, temporary structures, etc.

## Project Details

### **"There's a term for people who don't read the project details: unemployed" - Dr. Owen**

### Overview

In this project, you will be fixing: the bubble, insertion, selection, and merge sort algorithms. We will provide the completed code for the quicksort algorithm for your reference. While you don't have any assignment relating to the quicksort code on this project, we recommend looking through it to familiarize yourself with that algorithm. *Multiple questions regarding quick sort
will appear on your exam*, so it is in your best interest to take some time to understand it. The merge sort that you implement will be a hybrid merge sort which defers to insertion sort for handling small lists.

All the sorting algorithms should accept a custom `comparator` argument which substitutes for `<` when comparing
items to put in the list. If calling `comparator(a, b)` returns `True`, you should read that result as "`a` should come before `b` in a sorted list."

There is also an argument `descending` which defaults to `False`. If
the `descending` argument is `True`, you should sort the list in descending order. Since you can sort the list in
descending order by flipping the order of the inputs of the comparator and leaving the other logic the same, it might be
helpful for you to fix the _helper function_, called `do_comparison`. The current implementation of the sorting algorithms uses this method, but it is also not complete. The purpose of this function is that it takes elements `a` and `b`, the `comparator`, and `descending` as arguments, and tells you whether or not to put `a` before `b` in the sorted list. This helper function should only be a few lines!
Fixing this function is **highly recommended** as it greatly simplifies the logic in your sorting functions.

It is important to note that **_the comparator means strictly `<` and not `<=`_**, so for descending you should
consider `comparator(b, a)` instead of `not comparator(a, b)`, since the second one would give you `a >= b` instead of
`a > b`. If you did it the second way, your bubble sort might never stop swapping!

You can call the argument `comparator` the same as any other function, and the underlying function that gets called will
be whatever function was passed in for this argument. This takes advantage of the fact that Python has what are
called [first-class functions](https://en.wikipedia.org/wiki/First-class_function), meaning functions can be stored and
passed around the same way as any other type of value. The type of `comparator` is explained by this diagram:

![](img/comparator_diagram.png)

Also note that some arguments will be specified after the pseudo-argument `*,`.
The arguments following the asterisk `*` are ["keyword-only" arguments](https://www.python.org/dev/peps/pep-3102/).
Keyword-only arguments are designed to prevent accidental miscalls that can occur with positional parameters.

```python
# Note the "argument" *, which some of the other arugments come after
def some_func(a, b, *, c, d):
	pass

# Ok
some_func(1, 2, c=3, d=4)

# will raise TypeError: some_func() takes 2 positional arguments but 4 were given
some_func(1, 2, 3, 4)
```

### Tips, Tricks, and Notes

- There are different ways to implement merge sort, but make sure you are aiming for a solution that will fit the time
  complexity! If your recursive calls are some form of `hybrid_merge_sort(data[1:])`, this will not be _O(n log(n))_, as this does not divide the input list in half.
- A recursive implementation of merge sort will be the easiest to write. As you split the arrays, you should switch to
  insertion sort as soon as the split arrays get smaller than threshold. This means each of the recursive calls should
  be using the same threshold, such that the threshold is considered at each recursive call.
- Make sure to pass `comparator` and `descending` properly for all recursive calls as well.
- Try these web applications to visualize sorting algorithms:
  - <https://visualgo.net/bn/sorting>
  - <https://opendsa-server.cs.vt.edu/embed/mergesortAV> (good merge sort visualization)
  - <https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html>

### Assignment Specs

You will be given one file to edit, `solution.py`. You must fix the following functions. Take note of
the specified return values and input parameters.

**_DO NOT USE BUILT-IN SORT FUNCTIONS LIKE `list.sort()` or `sorted()` FOR THIS PROJECT IN ANY FUNCTION! ANY FUNCTION THAT USES A BUILT-IN SORT WILL LOSE ALL POINTS FOR THAT FUNCTION._**

**_Do not change the function signatures, including default values._**

**_If you implement a function that passes the tests but does not use the specified sorting algorithm for that function_,
\*you will not get **any** points for that function.\***

Make sure to consult the lectures, Zybooks, and other resources available if you are not sure how a given sorting algorithm works. Check the required time and space complexity. Using the right algorithm will help!

**solution.py:**

- **selection_sort(data: List[T], \*, comparator: Callable[[T,T], bool], descending: bool = False)**

  - Given a list of values, sort that list in-place using the selection sort algorithm and the provided comparator,
	and perform the sort in descending order if `descending` is `True`.
  - **param data**: List of items to be sorted
  - **param comparator**: A function which takes two arguments of type `T` and returns `True` when the first argument
	should be treated as less than the second argument.
  - **param descending**: Perform the sort in descending order when this is `True`. Defaults to `False`.
  - Time Complexity: _O($n^2$)_
  - Aux.Space Complexity: _O(1)_

- **bubble_sort(data: List[T], \*, comparator: Callable[[T,T], bool], descending: bool = False)**

  - Given a list of values, sort that list in-place using the bubble sort algorithm and the provided comparator,
	and perform the sort in descending order if `descending` is `True`.
  - **param data**: List of items to be sorted
  - **param comparator**: A function which takes two arguments of type `T` and returns `True` when the first argument
	should be treated as less than the second argument.
  - **param descending**: Perform the sort in descending order when this is `True`. Defaults to `False`.
  - Time Complexity: _O($n^2$)_
  - Aux.Space Complexity: _O(1)_

- **insertion_sort(data: List[T], \*, comparator: Callable[[T,T], bool], descending: bool = False)**

  - Given a list of values, sort that list in-place using the insertion sort algorithm and the provided comparator,
	and perform the sort in descending order if `descending` is `True`.
  - **param data**: List of items to be sorted
  - **param comparator**: A function which takes two arguments of type `T` and returns `True` when the first argument
	should be treated as less than the second argument.
  - **param descending**: Perform the sort in descending order when this is `True`. Defaults to `False`.
  - Time Complexity: _O($n^2$)_
  - Aux.Space Complexity: _O(1)_

- **hybrid_merge_sort(data: List[T], \*, threshold: int = 12, comparator: Callable[[T,T], bool], descending: bool = False)**
  - Given a list of values, sort that list using a hybrid sort with the merge sort and insertion sort
	algorithms and the provided comparator, and perform the sort in descending order if `descending` is `True`.
	The function should use `insertion_sort` to sort lists once their size is less than or equal to `threshold`, and
	otherwise perform a merge sort. DO NOT hardcode the threshold check such as `if threshold == {any value}`. Hint: Think about what should happen for lists with only one item.
  - **IMPORTANT**: Every semester there are students that don't actually implement a hybrid sort. These students generally make one of these mistakes:
	1. Check the threshold only once in hybrid*sort, and not for \_every* recursive call of merge_sort (if implemented separately).
	2. Call insertion_sort in each recursive call of merge sort, regardless of threshold
	3. Call merge_sort regardless of threshold
	4. Forget to pass threshold to each call of merge_sort
  - **param data**: List of items to be sorted
  - **param threshold**: Maximum size at which insertion sort will be used instead of merge sort. **Students frequently make mistakes with this, so be careful!**
  - **param comparator**: A function which takes two arguments of type `T` and returns `True` when the first argument
	should be treated as less than the second argument.
  - **param descending**: Perform the sort in descending order when this is `True`. Defaults to `False`.
  - Time Complexity: _O(n log(n))_
  - Aux. Space Complexity: _O(n)_












## Application Problem: Product Recommendation on an E-Commerce Platform

### Background:

E-Commerce Platforms like Amazon, eBay, and Alibaba recommend products based on the customer's search query keywords. Machine learning models calculates the relevance of each product to the user’s search query. The Platform then selects the most relevant products and present them to the customer. Additionally, e-commerce Platforms allow customers to choose how they would like the relevant products to be sorted. For example, customers can require to sort by price, from low to high.

In this project, you are provided with the price, rating, and relevance of all products for a given customer query. Your task is to select the relevant products and sort them based on customer-specified criteria.

### Challenge:

To select the most relevant products and sort them by customer-specified criteria, you will need to complete two tasks:

1. Select the top 30% of products based on relevance. If the resulting number of selected products is not an integer, round it to the nearest whole number. If multiple products share the same relevance score and you can only keep a portion due to the 30% limit, it doesn’t matter which specific products are kept.
2. Sort the selected products according to the customer-specified criterion.

There are three different criteria for customers to choose:

1.  **Sort by price from low to high**: When sorting by price, products should be ordered from the lowest to the highest price. If two products have the same price, they should be further sorted by rating in descending order (i.e., higher-rated products appear first).
2.  **Sort by price from high to low**: When sorting by price, products should be ordered from the highest to the lowest price. If two products have the same price, they should be further sorted by rating in descending order.
3.  **Sort by rating from high to low**: When sorting by rating, products should be ordered from the highest to the lowest rating. If two products have the same rating, they should be further sorted by price in ascending order (i.e., lower-priced products appear first).

You are given the class Product described below. **DO NOT** modify this class - any modification will result in zero for this portion of the project.

<hr>

**class Product:**

_DO NOT MODIFY the following attributes/functions._

- **Attributes:**

  - **price**: **float**: The price of the product.
  - **rating**: **int**: The rating of the product.
  - **relevance**: **float**: The relevance of the product to the customer search query. A higher value indicates a stronger match between the product and the search query.

- **\_\_init\_\_(self, price: int, rating: int) -> None**

  - Constructs a **Product** object.
  - **param price**: value to assign as price.
  - **param rating**: value to assign as rating.
  - **param relevance**: value to assign as relevance.
  - **return: None**

- **\_\_eq\_\_(self, other) -> bool**

  - Returns True if two products are equal, False otherwise.
  - **return: bool**

- **\_\_repr\_\_(self) -> str**

  - Returns the Product as a string representation (for debugging).
  - **return: string**

- **\_\_str\_\_(self) -> str**
  - Returns the Product as a string representation.
  - **return: string**

**_MODIFY BELOW_**:

<hr>

We will implement the following method to recommend products to customers.

```python
def recommend_products(products: List[Product], sort_by: str) -> T:
```

- This method will select the top 30% of products based on relevance and sort them according to customer-specified criteria.

- **Input**:
  - **products: List[Product]**: A list of Product objects representing the price, rating and relevance of each product.
  - **sort_by: str**: A string object representing which criterion the customer specifies to sort. If it is 'price_low_to_high', sort products by price in ascending order; if two products have the same price, then sort by rating in descending order. If it is 'price_high_to_low', sort products by price in descending order; if two products have the same price, then sort by rating in descending order. If it is 'rating', sort by rating in descending order; if two products have the same rating, then sort by price in ascending order. If two products share the same price and rating, their order doesn't matter.
- **Output**:

  - []: if the input **products** is empty.
  - **List[Product]**: sorted list of input products.

- **Complexity**:
  - Time: _O(nlogn)_. You will need to call hybrid_merge_sort() to achieve this time complexity. When calling it, please use the default value 12 for the **threshold** parameter.
  - Space: _O(n)_



### Sample Scenarios:

#### Scenario 1

```python
products = [Product(10, 1, 1),
            Product(20, 3, 2),
            Product(30, 5, 4),
            Product(10, 5, 3),
            Product(20, 5, 7),
            Product(30, 5, 5),
            Product(10, 5, 6),
            Product(10, 1, 8),
            Product(20, 5, 9),
            Product(30, 3, 10)]

"""
The top 30% relevant products would be:
relevant_products = [Product(10, 1, 8),
                     Product(20, 5, 9),
                     Product(30, 3, 10)]
"""
output = recommend_products(products, 'price_high_to_low')
"""
Expected = [Product(30, 3, 10),
            Product(20, 5, 9),
            Product(10, 1, 8)]
"""
```

**Explanation**: Among relevant products, no products share the same price, thus we simply sort products by their prices from high to low.

#### Scenario 2

```python
products = [Product(10, 1, 1),
            Product(20, 3, 2),
            Product(30, 5, 4),
            Product(10, 5, 3),
            Product(20, 5, 7),
            Product(30, 5, 5),
            Product(10, 5, 6),
            Product(10, 1, 8),
            Product(7, 4, 9),
            Product(40, 4, 10)]
"""
The top 30% relevant products would be:
relevant_products = [Product(10, 1, 8),
                     Product(7, 4, 9),
                     Product(40, 4, 10)]
"""

output = recommend_products(products, 'rating')
"""
Expected = [Product(7, 4, 9),
            Product(40, 4, 10),
            Product(10, 1, 8)]
"""
```

**Explanation**: Product(7, 4, 9) and Product(40, 4, 10) share the same rating, thus we sort them by price from low to high.

## **Application Problem Notes:**

- Keep in mind that objects of the Product class are custom objects with multiple attributes. In order to sort custom objects in Python (within the scope of this project), you **MUST** pass a custom comparator to the desired sorting method.

- There are various approaches to creating a custom comparator that can be used by the sorting methods implemented in this project; You could use <a href="https://www.w3schools.com/python/python_lambda.asp">Python Lambda functions</a>, helper functions, or even inner functions.

> An extra note on lambda functions... <br>
> Lambda functions are an easy way to specify a **very** small function, usually a few arguments, and one line at most.
> Lets see how two functions could be implemented, one using lambda functions, one using regular functions
>
> ```
> # Using regular functions
> def return_addition(x, a):
>   return x + a
>
> # Using lambda function
> lambda_addition = lambda x, a: x + a
>
> print(return_addition(3,5)) # prints 8
> print(lambda_addition(3,5)) # also prints 8
> ```
>
> Notice the lambda "anatomy". `lambda x, a:` defines the argument(s) of the function. Everything after the `:` will be returned by that function.

- Refer to the default parameters of the various sorting functions implemented in this project (except quicksort) to see a basic example of a comparator.














---


## **Grading** 



**1. Important Notes to Avoid Receiving 0 Points:**
- Using a different sorting algorithm than the one specified for some function will result in the loss of all points for that function.
- Not making the merge sort **_hybrid_** will result in the loss of half of all points for that function.
- You will not receive any points for that function if you use Python's built-in sorting functions or sorting functions imported from any library.
- You will not receive any points on the project if you use any list-reversing function such as `reversed`, `list.reverse`, or a homemade alternative to these. You must sort the lists in ascending or descending order directly.
- You must call hybrid_merge_sort function for the application problem. If you opt to use QuickSort, all points will be deducted.



**2. Auto Graded Tests (100 points)** 
  - Selection: \_\_/15
    - test_selecton_sort_basic: \_\_/4
    - test_selection_sort_comparator: \_\_/4
    - test_selection_sort_descending: \_\_/4
    - test_selection_sort_comprehensive: \_\_/3
  - Bubble: \_\_/15
    - test_bubble_sort_basic: \_\_/4
    - test_bubble_sort_comparator: \_\_/4
    - test_bubble_sort_descending: \_\_/4
    - test_bubble_sort_comprehensive: \_\_/3
  - Insertion: \_\_/15
    - test_insertion_sort_basic: \_\_/4
    - test_insertion_sort_comparator: \_\_/4
    - test_insertion_sort_descending: \_\_/4
    - test_insertion_sort_comprehensive: \_\_/3
  - Hybrid Merge: \_\_/25
    - test_hybrid_merge_sort_basic: \_\_/5
    - test_hybrid_merge_sort_threshold: \_\_/5
    - test_hybrid_merge_sort_comparator: \_\_/5
    - test_hybrid_merge_sort_descending: \_\_/5
    - test_hybrid_merge_sort_comprehensive: \_\_/5
    - test_hybrid_merge_sort_speed: \_\_/0
      - This test helps checking if your hybrid merge sort is implemented properly to make sure your code time complexity is correct
    - test_hybrid_merge_actually_hybrid: \_\_/0
      - This test is similar to test_hybrid_merge_sort_speed, but it checks if your hybrid merge sort function is a true hybrid merge sort or not.
      - NOTE: one way to fail this test is if `hybrid_merge_sort` doesn't call itself recursively (e.g. if you have a separate `merge_sort` helper function). In this case, you must take extra care and ensure that your overall algorithm **is actually hybrid** to avoid losing points.
  - Application Problem: \_\_/30
    - test_get_relevant_songs: \_\_/30





**3. Late penalty:** Projects submitted late incur a 10% deduction per hour past the deadline, applied to the earned project score. Late submissions are accepted only until the accumulated penalty reduces the score to 0; beyond that point, submissions will no longer be graded.
For example, 1 hour late → 10% deduction, 5 hours late → 50% deduction, 10 hours late → 100% deduction (grade = 0). After 10 hours → submission not accepted.



**4. No submission = -100:** No submission or submission of the exact starter code will result in a score of −100.

## **Submission Guidelines**

### **Deliverables:**

Projects are submitted through the D2L Assignment tool.
The submission link allows two separate file uploads, so no folders or ZIP files are required.
Students must upload exactly two files:
1. solution.py – the Python implementation
2. README.txt – a brief, structured self-report

Both files must be uploaded directly to the appropriate D2L assignment link.


### **README.txt:**
Projects are graded primarily on completion and honest reporting.
Failure to upload the required README.txt file by the assignment deadline will result in a 5% deduction per hour until the README is submitted.
This policy is in place to ensure that both required files are uploaded and that students practice complete and professional submission habits.
If a student is found to have been dishonest in the README (e.g., misreporting which unit tests passed or failed), the earned score for that coding challenge will be reduced by 50% on the first occurrence.
If the same student is found to be dishonest again on a subsequent coding challenge, the score for that assignment will be 0 (−100%).


You may copy and paste the following format into your README.txt and fill in the points you earned for each test case:

```
Total points for Project01: ___

Detailed points for each test case:
  1) Selection Sort 
    - test_selecton_sort_basic: 
    - test_selection_sort_comparator: 
    - test_selection_sort_descending: 
    - test_selection_sort_comprehensive: 
  2) Bubble Sort
    - test_bubble_sort_basic: 
    - test_bubble_sort_comparator: 
    - test_bubble_sort_descending: 
    - test_bubble_sort_comprehensive: 
  3) Insertion Sort
    - test_insertion_sort_basic:
    - test_insertion_sort_comparator: 
    - test_insertion_sort_descending: 
    - test_insertion_sort_comprehensive: 
  4) Hybrid Merge Sort
    - test_hybrid_merge_sort_basic:
    - test_hybrid_merge_sort_threshold: 
    - test_hybrid_merge_sort_comparator:
    - test_hybrid_merge_sort_descending: 
    - test_hybrid_merge_sort_comprehensive: 
  5) Application Problem
    - test_get_relevant_songs: 
```


### **How to Work on a Project Locally:**
1. 🖥️ Ensure PyCharm is installed.
2. 📦 **Download** the starter package from the *Projects* tab on D2L. *(See the tutorial video on D2L if needed)*.
3. 📝 Write your code and run **tests.py**, once ready, 📤 **upload** your `solution.py` and `READ.txt` to D2L. 



---


## **Outside resources:** 
Note students can not use Chegg or similar sites, see syllabus for details, use of outside resources for the application problem is strictly forbidden, use of outside resources is limited to max of 2 functions in a project.





