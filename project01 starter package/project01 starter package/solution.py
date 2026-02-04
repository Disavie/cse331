"""
Project 1
CSE 331 SS26
solution.py
"""

from __future__ import annotations
from typing import List, TypeVar, Tuple, Optional

# for more information on type hinting, check out https://docs.python.org/3/library/typing.html
T = TypeVar("T")  # represents generic type
Node = TypeVar("Node")  # represents a Node object (forward-declare to use in Node __init__)
DLL = TypeVar("DLL")

# pro tip: PyCharm auto-renders docstrings (the multiline strings under each function definition)
# in its "Documentation" view when written in the format we use here. Open the "Documentation"
# view to quickly see what a function does by placing your cursor on it and using CTRL + Q.
# https://www.jetbrains.com/help/pycharm/documentation-tool-window.html


class Node:
    """
    Implementation of a doubly linked list node.
    
    DO NOT MODIFY THIS CLASS
    """
    __slots__ = ["value", "next", "prev", "child"]

    def __init__(self, value: T, next: Node = None, prev: Node = None, child: Node = None) -> None:
        """
        Construct a doubly linked list node.

        :param value: value held by the Node.
        :param next: reference to the next Node in the linked list.
        :param prev: reference to the previous Node in the linked list.
        :param child: reference used by the application problem dream_escaper.
        :return: None.

        DO NOT MODIFY
        """
        self.next = next
        self.prev = prev
        self.value = value

        # The child attribute is only used for the application problem
        self.child = child

    def __repr__(self) -> str:
        """
        Represents the Node as a string.

        :return: string representation of the Node.

        DO NOT MODIFY
        """
        return f"Node({str(self.value)})"

    __str__ = __repr__


class DLL:
    """
    Implementation of a doubly linked list without padding nodes.

    Modify only below the indicated line.
    """
    __slots__ = ["head", "tail", "size"]

    def __init__(self) -> None:
        """
        Construct an empty doubly linked list.

        :return: None.

        DO NOT MODIFY
        """
        self.head = self.tail = None
        self.size = 0

    def __repr__(self) -> str:
        """
        Represent the DLL as a string.

        :return: string representation of the DLL.

        DO NOT MODIFY
        """
        result = []
        node = self.head
        while node is not None:
            result.append(str(node))
            node = node.next
        return " <-> ".join(result)

    def __str__(self) -> str:
        """
        Represent the DLL as a string.

        :return: string representation of the DLL.

        DO NOT MODIFY
        """
        return repr(self)

    # MODIFY BELOW #

    def empty(self) -> bool:
        """
        Return boolean indicating whether DLL is empty.

        :return: True if DLL is empty, else False.
        """
        return 1 if self.size == 0 else 0
        pass

    def push(self, val: T, back: bool = True) -> None:
        """
        Create Node containing `val` and add to back (or front) of DLL. Increment size by one.

        :param val: value to be added to the DLL.
        :param back: if True, add Node containing value to back (tail-end) of DLL; if False, add to front (head-end).
        :return: None.
        """
        newNode = Node(val)
        if not self.empty():
            if back:
                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail = newNode
            else:
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
        else:
            self.head = newNode
            self.tail = newNode
        self.size+=1


    def pop(self, back: bool = True) -> None:
        """
        Remove Node from back (or front) of DLL. Decrement size by 1. If DLL is empty, do nothing.

        :param back: if True, remove Node from (tail-end) of DLL; if False, remove from front (head-end).
        :return: None.
        """
        if not self.empty():
            if self.head is self.tail:
                self.head = self.tail = None
            elif back:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                self.head = self.head.next
                self.head.prev = None
            self.size-=1

    def list_to_dll(self, source: List[T]) -> None:
        """
        Construct DLL from a standard Python list.

        :param source: standard Python list from which to construct DLL.
        :return: None.
        """
        self.head = None
        self.tail = None
        self.size = 0
        for val in source:
            self.push(val)

    def dll_to_list(self) -> List[T]:
        """
        Construct standard Python list from DLL.

        :return: standard Python list containing values stored in DLL.
        """
        list = []
        ptr = self.head
        while ptr is not None:
            list.append(ptr.value)
            ptr = ptr.next
        return list
    
    def _find_nodes(self, val: T, find_first: bool = False) -> List[Node]:
        """
        Construct list of Nodes with value val in the DLL and return the associated Node list

        :param val: The value to be found
        :param find_first: If True, only return the first occurrence of val. If False, return all
        occurrences of val
        :return: A list of all the Nodes with value val.
        """
        found_nodes = []
        ptr = self.head
        while ptr is not None:
            if ptr.value == val:
                found_nodes.append(ptr)
                if find_first:
                    break
            ptr = ptr.next
        return found_nodes

    def find(self, val: T) -> Node:
        """
        Find first instance of `val` in the DLL and return associated Node object.

        :param val: value to be found in DLL.
        :return: first Node object in DLL containing `val`. If `val` does not exist in DLL, return None.
        """
        item = self._find_nodes(val,True)
        if item:
            return item[0]
        return None


    def find_all(self, val: T) -> List[Node]:
        """
        Find all instances of `val` in DLL and return Node objects in standard Python list.

        :param val: value to be searched for in DLL.
        :return: Python list of all Node objects in DLL containing `val`. If `val` does not exist in DLL, return an empty list.
        """
        item = self._find_nodes(val,False)
        return item

    def remove_node(self, to_remove: Node) -> None:
        """
        Given a node in the linked list, remove it.

        :param to_remove: node to be removed from the list
        :return: None
        """
        if to_remove is not self.tail:
            to_remove.next.prev = to_remove.prev
        else:
            self.tail = to_remove.prev
            if self.tail:
                self.tail.next = None
        if to_remove is not self.head:
            to_remove.prev.next = to_remove.next
        else:
            self.head = to_remove.next
            if self.head:
                self.head.prev = None
        self.size-=1

    def remove(self, val: T) -> bool:
        """
        Delete first instance of `val` in the DLL. Must call _remove_node.

        :param val: value to be deleted from DLL.
        :return: True if Node containing `val` was deleted from DLL; else, False.
        """

        node_ptr = self.head
        while node_ptr:
            if node_ptr.value == val:
                self.remove_node(node_ptr)
                return True
            node_ptr = node_ptr.next

        return False

    def remove_all(self, val: T) -> int:
        """
        Delete all instances of `val` in the DLL. Must call _remove_node.

        :param val: value to be deleted from DLL.
        :return: integer indicating the number of Nodes containing `val` deleted from DLL; if no Node containing `val` exists in DLL, return 0.
        """
        c=0
        node_ptr = self.head
        while node_ptr:
            if node_ptr.value == val:
                self.remove_node(node_ptr)
                c+=1
            node_ptr = node_ptr.next

        return c

    def reverse(self) -> None:
        """
        Reverse DLL in-place by modifying all `next` and `prev` references of Nodes in the DLL and resetting the `head` and `tail` references.

        :return: None.
        """
        c = self.head
        while c:
            temp = c.next
            c.next = c.prev
            c.prev = temp
            c = c.prev
        temp = self.head
        self.head = self.tail
        self.tail = temp



def dream_escaper(dll: DLL) -> DLL:
    """
    Takes the head of a multi-level DLL and compresses it into a single level DLL.

    :param dll: The dll to turn into a single-level DLL.
    :return: The new DLL.
    """

    """
    Input
    A - B - C
        |
        D - F
        |   |
        E   H
        |
        G

    Output 
    A - B - D - E - G - F - H - C
    """

    new_dll = DLL()
    node_ptr = dll.head

    
    def helper(node_ptr: Node):

        while node_ptr:
            new_dll.push(node_ptr.value)
            if node_ptr.child:
                helper(node_ptr.child)
            node_ptr = node_ptr.next

    helper(dll.head)

    return new_dll