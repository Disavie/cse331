def find_unsorted_subarray(array):
    """
    Finds the shortest subarray that needs to be sorted for the entire
    array to become sorted.

    Args:
        array (list of int): The input array of integers.

    Returns:
        list: A list containing two integers representing the start and
        end indices of the shortest subarray that needs to be sorted.
        If the array is already sorted, returns [-1, -1].

    To Do:
        - Students will implement the logic to find the minimum and maximum
        out-of-order elements and determine the boundaries of the subarray
        that must be sorted.
    """
    #edge case empty array
    if not len(array):
        return [-1,-1]
    indicies = [-1,-1]

    #find max value
    curmax = array[0]
    i = 1
    while i < len(array):
        if curmax > array[i]:
            indicies[1]  = i
        else:
            curmax = array[i]
        i+=1
    
    #find min
    curmin = array[-1] #< back of array
    i = len(array)-1
    while i > -1:
        if array[i] > curmin:
            indicies[0] = i
        else:
            curmin = array[i]
        i-=1

        #O(n) + O(n) = O(2n) = O(n) time complexity
        #O(1) space
    return indicies



def is_out_of_order(i, num, array):
    """
    Helper function to determine if an element is out of order in the array.

    Args:
        i (int): The index of the element to check.
        num (int): The element at index i.
        array (list of int): The input array of integers.

    Returns:
        bool: True if the element is out of order, False otherwise.

    This function is a suggestion  to students as a helper function.
    Students are encouraged to implement this function if they find it helpful.
    """
    pass