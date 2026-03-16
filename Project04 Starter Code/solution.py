"""
CSE331 Project 4 SS26
Circular Double-Ended Queue
solution.py
"""

from typing import TypeVar, List

T = TypeVar('T')


class CircularDeque:
    """
    Representation of a Circular Deque using an underlying python list
    """

    __slots__ = ['capacity', 'size', 'queue', 'front', 'back']

    def __init__(self, data: List[T] = None, front: int = 0, capacity: int = 4):
        """
        Initializes an instance of a CircularDeque

        :param data: starting data to add to the deque, for testing purposes
        :param front: where to begin the insertions, for testing purposes
        :param capacity: number of slots in the Deque

        DO NOT MODIFY
        """
        if data is None and front != 0:
            data = ['Start']  # front will get set to 0 by a front enqueue if the initial data is empty
        elif data is None:
            data = []

        self.capacity: int = capacity
        self.size: int = len(data)
        self.queue: List[T] = [None] * capacity
        self.back: int = (self.size + front - 1) % self.capacity if data else None
        self.front: int = front if data else None

        for index, value in enumerate(data):
            self.queue[(index + front) % capacity] = value

    def __str__(self) -> str:
        """
        Provides a string representation of a CircularDeque
        'F' indicates front value
        'B' indicates back value

        :return: the instance as a string

        DO NOT MODIFY
        """
        if self.size == 0:
            return "CircularDeque <empty>"

        str_list = ["CircularDeque <"]
        for i in range(self.capacity):
            str_list.append(f"{self.queue[i]}")
            if i == self.front:
                str_list.append('(F)')
            elif i == self.back:
                str_list.append('(B)')
            if i < self.capacity - 1:
                str_list.append(',')

        str_list.append(">")
        return "".join(str_list)

    __repr__ = __str__

    #
    # Modify Below
    #
    def __len__(self) -> int:
        """
        Returns the amount of elements in the queue

        :return: Amount of elements in the queue
        """
        pass

    def is_empty(self) -> bool:
        """
        Returns true if queue is empty

        :return: Boolean if queue is empty
        """
        pass

    def front_element(self) -> T:
        """
        Returns the element in the front of the queue

        :return: Value in the front of the queue
        """
        pass

    def back_element(self) -> T:
        """
        Returns the element in the back of the queue

        :return: Value in the back of the queue
        """
        pass

    def enqueue(self, value: T, front: bool = True) -> None:
        """
        Adds an element to the deque, either to the front or back.

        :param value: The value to add.
        :param front: If True, insert at the front; otherwise, insert at the back.
        """
        pass


    def dequeue(self, front: bool = True) -> T:
        """
        Removes element to the queue, to the front or back

        :param front: Bool, true if should remove from front, False if should remove from back
        :return: removed item, None if empty
        """
        pass


    def grow(self) -> None:
        """
        Grows the queue
        """
        pass

    def shrink(self) -> None:
        """
        Shrinks the queue
        """
        pass


def find_max_wind_speeds(numbers: List[int], size: int) -> List[int]:
    """
    Takes in a list of numbers and a sliding window size and returns
    a list containing the maximum value of the sliding window at
    each iteration step.

    :param numbers: Elements to find max of sliding window from
    :param size: Size of sliding window
    :return: List with maximum element of window in each iteration
    """
    pass


def max_wind_variability_score(wind_speeds: List[int]) -> int:
    """
    Returns the maximum sum of non-adjacent elements

    :param wind_speeds: List of numbers to add
    :return: Int, max sum of non-adjacent elements
    """
    pass