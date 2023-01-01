"""
Linked list class implementation and tests.

This implements a class for a linked list and includes a series of tests
to verify functionality.
"""

import numpy as np


class Node:
    """A class for node in the linked list.

    Here the node only stores value and child references. 
    Additional data attributes can be added for functionality
    in an actual application.

    Attributes:
        val: The value of the node.
        child: A reference a child node.
    
    """

    def __init__(self, *, val: float):
        """Initializes the node.

        Args:
            val: The value of the node.
        """
        self.val = val
        self.child = None


class LinkedList:
    """A linked list class.

    Implements functionality for a linked list. This implementation
    inserts a new node a the list's head.

    Attributes:
        head: The head node of the linked list.
    """

    def __init__(self):
        self.head = None

    def add_data(self, *, data: list):
        """Adds nodes from a list of values to the linked list.

        Args:
            data: List of node values to be added.
        
        """
        for val in data:
            self.insert(val=val)

    def remove_data(self, *, data: list):
        """Removes nodes from a list of values to the linked list.

        Args:
            data: List of node values to be remoed.
        
        """
        for val in data:
            self.remove(val=val)

    def insert(self, *, val: float):
        """Inserts a node into the linked list.

        Args:
            val: The value of the node to be inserted.
        """
        new_node = Node(val=val)
        if self.head:
            new_node.child = self.head
        self.head = new_node

    def remove(self, *, val: float):
        """Removes a node into the linked list.

        Args:
            val: The value of the node to be removed.
        """
        while self.head.val == val:
            new_head = self.head.child
            del self.head
            self.head = new_head

        curr_node = self.head
        while curr_node and curr_node.child:
            if curr_node.child.val == val:
                remove_node = curr_node.child
                curr_node.child = curr_node.child.child
                del remove_node
            curr_node = curr_node.child

    def enumerate(self):
        """Returns a list of all node values.
        """
        node = self.head
        vals = []
        while node:
            vals.append(node.val)
            node = node.child
        return vals

    def find(self, val: float) -> Node:
        """Returns a node in the linked list with the specified value.

        Args:
            val: The value of the node to be returned.

        Returns:
            The node with the specified value. If no node is found, returns 'None'.
        
        """
        return_node = None
        node = self.head
        while node:
            if node.val == val:
                return_node = node
                node = None
            else:
                node = node.child

        return return_node

    def reverse(self):
        """Reverses the order of nodes in the linked list. 
        """
        last_node = self.head
        curr_node = self.head.child
        while curr_node:
            next_node = curr_node.child
            curr_node.child = last_node
            last_node = curr_node
            curr_node = next_node

        self.head.child = None
        self.head = last_node

    @property
    def size(self) -> int:
        """Determines the number of nodes in the linked list.

        Returns:
            An integer corresponding to the number of nodes.
        """
        node = self.head
        size = 0
        while node:
            size += 1
            node = node.child
        return size


def test_linked_list():
    """Implements tests of the linked lists functionality. If a test fails, an
    assertion error occurs.

    Verifies the following:
        (1) Nodes can be inserted and found.
        (2) Nodes can be enumerated.
        (3) Nodes can be removed.
        (4) Linked list can be reversed.
        (5) Size function is correct.
    """
    ll = LinkedList()
    data = list(np.random.choice(a=np.arange(10000), size=10000, replace=False))
    ll.add_data(data=data)

    # Check all data can be found.
    for val in data:
        assert not (ll.find(val=val) == None)

    # Check enumeration.
    data.reverse()
    assert ll.enumerate() == data

    # Check removal function by removing some random nodes.
    remove_data = list(np.random.choice(a=np.asarray(data), size=1000, replace=False))
    ll.remove_data(data=remove_data)
    for val in remove_data:
        assert ll.find(val=val) == None

    # Check enumeration after removal.
    for val in remove_data:
        data.remove(val)
    assert ll.enumerate() == data

    # Check reverse function.
    ll.reverse()
    data.reverse()
    assert ll.enumerate() == data

    # Check size function.
    assert ll.size == len(data)


def main():
    test_linked_list()


if __name__ == "__main__":
    main()
