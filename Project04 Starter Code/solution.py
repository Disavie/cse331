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
        return self.size

    def is_empty(self) -> bool:
        """
        Returns true if queue is empty

        :return: Boolean if queue is empty
        """
        return self.size == 0

    def front_element(self) -> T:
        """
        Returns the element in the front of the queue

        :return: Value in the front of the queue
        """
        pass
        if self.size == 0: return None
        return self.queue[self.front]

    def back_element(self) -> T:
        """
        Returns the element in the back of the queue

        :return: Value in the back of the queue
        """
        if self.size == 0: return None
        return self.queue[self.back]

    def enqueue(self, value: T, front: bool = True) -> None:
        """
        Adds an element to the deque, either to the front or back.

        :param value: The value to add.
        :param front: If True, insert at the front; otherwise, insert at the back.
        """

        if self.size+1 > self.capacity:
            self.grow()

        if front:
            if self.is_empty():
                self.front = 0
                self.back = 0
            else:
                self.front = (self.front-1) % self.capacity

            self.queue[self.front] = value
        else:
            if self.is_empty():
                self.front = 0
                self.back = 0
            else:
                self.back = (self.back+1) % self.capacity
            self.queue[self.back] = value
        self.size+=1


    def dequeue(self, front: bool = True) -> T:
        """
        Removes element to the queue, to the front or back

        :param front: Bool, true if should remove from front, False if should remove from back
        :return: removed item, None if empty
        """

        item = None 
        if self.is_empty():
            return item

        if front:
            item = self.queue[self.front]
            self.front = (self.front+1) % self.capacity
        else:
            item = self.queue[self.back]
            self.back = (self.back-1) % self.capacity

        self.size-=1

        if self.size <= self.capacity // 4 and self.capacity // 2 >= 4:
            self.shrink()



        return item


    def grow(self) -> None:
        """
        Grows the queue
        """
        old_cap = self.capacity
        self.capacity*=2
        new_queue = [None] * self.capacity
        for i in range(self.size):
                new_queue[i] = self.queue[(self.front+i) % old_cap]
        self.back = self.size-1
        self.front = 0
        self.queue = new_queue

    def shrink(self) -> None:
        """
        Shrinks the queue
        """
        old_cap = self.capacity
        self.capacity = self.capacity//2
        new_queue = [None] * self.capacity
        for i in range(self.size):
                new_queue[i] = self.queue[(self.front+i) % old_cap]
        self.back = self.size-1
        self.front = 0
        self.queue = new_queue


def find_max_wind_speeds(numbers: List[int], size: int) -> List[int]:
    """
    Takes in a list of numbers and a sliding window size and returns
    a list containing the maximum value of the sliding window at
    each iteration step.

    :param numbers: Elements to find max of sliding window from
    :param size: Size of sliding window
    :return: List with maximum element of window in each iteration
    """
    if not numbers:
        return []
    result = []
    dq = CircularDeque()  # store indices

    for i in range(len(numbers)):

        while not dq.is_empty() and dq.front_element() <= i - size:
            dq.dequeue()

        while not dq.is_empty() and numbers[dq.back_element()] < numbers[i]:
            dq.dequeue(False)

        dq.enqueue(i, front=False)

        if i >= size - 1:
            result.append(numbers[dq.front_element()])
    return result


def max_wind_variability_score(wind_speeds: List[int]) -> int:
    """
    Returns the maximum sum of non-adjacent elements

    :param wind_speeds: List of numbers to add
    :return: Int, max sum of non-adjacent elements
    """
    if not wind_speeds:
        return 0
    if len(wind_speeds) == 1:
        return wind_speeds[0]

    dp = [0] * len(wind_speeds)

    dp[0] = wind_speeds[0]
    dp[1] = max(wind_speeds[0], wind_speeds[1])

    for i in range(2, len(wind_speeds)):
        dp[i] = max(dp[i-1], dp[i-2] + wind_speeds[i])

    return dp[-1]
