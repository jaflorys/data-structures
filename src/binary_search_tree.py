"""
Binary search tree (BST) class implentation and tests.

This code contains a class definition for a BST and performs
tests to verify the BST's functionatiy.
"""


import numpy as np


class Node:
    """A head node of a binary search tree.

    Attributes:
        val: The value of the node.    
    """

    def __init__(self, *, val: float):
        """
        Initializes node.

        Args:
            val: The value that the node represents.
        """
        self.val = val


class BST:
    """A binary search tree (BST) class.

    Implements functionality for a BST to include insertion, removal, and
    determination of various attributes.

    Attributes:
        head: The head node of the BST.
        left_bst: A reference to a left BST subtree.
        right_bst: A reference to a right BST subtree.
    
    """

    def __init__(self):
        self.head = None
        self.left_bst = None
        self.right_bst = None

    def add_data(self, *, data: list):
        """Adds nodes in a list of data to the BST.

        Args:
            data: List of floats to be added to the BST.
        """
        for val in data:
            self.insert(val=val)

    def remove_data(self, *, data: list):
        """Removes nodes in a list of data from the BST.

        Args:
            data: List of floats to be removed from the BST.
        """
        for val in data:
            self.remove(val=val)

    def insert(self, *, val: float):
        """Inserts a node into the BST.

        Args:
            val: The value of the node to insert.
        """
        if not self.head:
            self.head = Node(val=val)
            return

        if val < self.head.val:
            if not self.left_bst:
                self.left_bst = BST()
            self.left_bst.insert(val=val)
        elif val > self.head.val:
            if not self.right_bst:
                self.right_bst = BST()
            self.right_bst.insert(val=val)

        # If reach here, value is equal to head node value.
        return

    def remove(self, val: float):
        """Removes a node from the BST.

        Args:
            val: The value of the node to remove.
        """
        if self.head.val == val:
            # To do: Special logic if root node is to be removed
            pass

        # Determine whether one of children is the node to be removed.
        child_node_removed = None
        is_left_child = False
        if self.left_bst and self.left_bst.head.val == val:
            child_node_removed = self.left_bst
            is_left_child = True
        if self.right_bst and self.right_bst.head.val == val:
            child_node_removed = self.right_bst

        if child_node_removed:
            if not child_node_removed.left_bst and not child_node_removed.right_bst:
                # If node to be removed has no children, then remove it and update references of current node
                if is_left_child:
                    self.left_bst = None
                else:
                    self.right_bst = None
                del child_node_removed
            elif child_node_removed.left_bst and not child_node_removed.right_bst:
                # If child only has left sub-tree, update sub-tree reference to child's left sub-tree
                new_subtree = child_node_removed.left_bst
                if is_left_child:
                    self.left_bst = new_subtree
                else:
                    self.right_bst = new_subtree
                del child_node_removed
            elif child_node_removed.right_bst and not child_node_removed.left_bst:
                # If child only has right sub-tree, update sub-tree reference to child's right sub-tree
                new_subtree = child_node_removed.right_bst
                if is_left_child:
                    self.left_bst = new_subtree
                else:
                    self.right_bst = new_subtree
                del child_node_removed
            else:
                # If child has both left/right subtree's, update child value to min in child's right sub-stree
                new_val = child_node_removed.right_bst.min_value
                child_node_removed.head.val = new_val
                # Update value so redundant node is later removed
                val = new_val

        if self.left_bst:
            self.left_bst.remove(val=val)
        if self.right_bst:
            self.right_bst.remove(val=val)

    def exists(self, *, val: float) -> bool:
        """Determines whether node is in BST.

        Args:
            val: The node to be searched.

        Returns:
            A boolean indicating whether the node is present.
        """
        if self.head.val == val:
            return True

        if val < self.head.val:
            return self.left_bst.exists(val=val)
        elif val > self.head.val:
            return self.right_bst.exists(val=val)

        return False

    @property
    def size(self) -> int:
        """Returns the number of nodes in the BST.

        Returns:
            Integer equal to the total number of nodes in the BST.
        """
        left_size = self.left_bst.size if self.left_bst else 0
        right_size = self.right_bst.size if self.right_bst else 0
        return 1 + left_size + right_size

    def enumerate_in_order(self) -> list:
        """Enumerates all nodes in the BST in increasing order of value.

        Returns:
            List of node values in increasing order.
        """
        left_part = []
        right_part = []
        if self.left_bst:
            left_part = self.left_bst.enumerate_in_order()
        if self.right_bst:
            right_part = self.right_bst.enumerate_in_order()

        return left_part + [self.head.val] + right_part

    @property
    def depth(self) -> int:
        """Returns depth of the furthest node in the BST from the head node.

        Returns:
            Integer value of depth.
        """
        if not self.left_bst and not self.right_bst:
            return 0

        left_depth = 0
        right_depth = 0
        if self.left_bst:
            left_depth = 1 + self.left_bst.depth

        if self.right_bst:
            right_depth = 1 + self.right_bst.depth

        return max(left_depth, right_depth)

    @property
    def diameter(self) -> int:
        """Determines the diameter of the BST.

        The diameter is the longest path between any two nodes in the BST.

        Returns:
            Integer value the diameter of the BST.
        """
        left_depth = 0
        right_depth = 0
        left_diam = 0
        right_diam = 0
        if self.left_bst:
            left_depth = self.left_bst.depth
            left_diam = self.left_bst.diameter
        if self.right_bst:
            right_depth = self.right_bst.depth
            right_diam = self.right_bst.diameter

        my_diameter = 2 + left_depth + right_depth

        return max(my_diameter, left_diam, right_diam)

    @property
    def balanced(self) -> bool:
        """Determines whether the BST is balanced.

        The BST is balanced if the depth is its left subtree (w.r.t. head node)
        is within one of the depth of its right subtree.

        Returns:
            Boolean indicator of whether tree is balanced.
        """
        left_depth = 0
        right_depth = 0
        if self.left_bst:
            left_depth = self.left_bst.depth
        if self.right_bst:
            right_depth = self.right_bst.depth

        return abs(left_depth - right_depth) <= 1

    @property
    def max_value(self) -> float:
        """Returns the maximum value of a node in the BST.

        Returns:
            Float for the maximum node value.
        """
        max_val = self.head.val

        if not self.right_bst:
            return max_val

        return self.right_bst.max_value

    @property
    def min_value(self) -> float:
        """Returns the minimum value of a node in the BST.

        Returns:
            Float for the minimum node value.
        """
        min_val = self.head.val
        if not self.left_bst:
            return min_val

        return self.left_bst.min_value

    @property
    def valid(self) -> bool:
        """Determines whether the BST is valid.

        The BST is valid if every left (right) child node is less than (greater than)
        its respective parent node.

        Returns:
            Boolean indicator of whether the BST is valid.
        """
        valid = True
        left_valid = True
        right_valid = True
        if self.left_bst:
            if self.left_bst.head.val > self.head.val:
                valid = False
                left_valid = self.left_bst.valid
        if self.right_bst:
            if self.right_bst.head.val < self.head.val:
                right_valid = self.right_bst.vald

        return valid and left_valid and right_valid

    def check_consistancy(self) -> bool:
        """Performs a series of tests to check consistancy of BST.

        Verifies the following:
            (1) BST is valid.
            (2) All nodes of BST can be found.
            (3) In order enumeration is in correct order.
            (4) Max and min functions correct.
            (5) Depth does not exceed diameter.

        Returns:
            Boolean value of 'True' of no tests fail; otherwise, raises exception.
        """
        # Check valid bst.
        if not self.valid:
            raise ValueError("BST is not valid.")

        data = self.enumerate_in_order()

        # Check that every value can be found in BST.
        is_found = [self.exists(val=val) for val in data]
        if not np.sum(is_found) == len(data):
            raise ValueError("Nodes that exist in BST could not be found.")

        # Check in order enumeration.
        deltas = [int((data[i] - data[i - 1]) <= 0) for i in np.arange(1, len(data))]
        if np.sum(deltas) > 0:
            raise ValueError("Error in inorder enumeration.")

        # Check max and min functions.
        if not data[0] == self.min_value:
            raise ValueError("Min value function error.")
        if not data[-1] == self.max_value:
            raise ValueError("Max value function error.")

        # Check size consistent with enumerated output.
        if not self.size == len(data):
            raise ValueError("BST size and inorder enumeration not consistant.")

        # Check depth does not exceed diameter.
        if self.depth > self.diameter:
            raise ValueError("BST depth cannot exceed its diameter.")

        return True


def bst_summary(*, bst: BST):
    """Summarizes the attributes of a BST.
    """
    print("BST info: ")
    print("valid: ", bst.valid)
    print("depth: ", bst.depth)
    print("diameter: ", bst.diameter)
    print("balanced: ", bst.balanced)
    print("______________")
    print("\n")


def test_bst(*, num_tests: int, n: int, m: int):
    """Tests functionality of the BST class.

    Performs a sequence of random insertion/deletion operations and
    checks consistancy of BST after each operation.

    Args:
        num_tests: The length of the random test sequence.
        n: The size of the set of potential nodes for insertion/deletion.
        m: Upper limit of the number of randomly-selected nodes to insert/remove for each test.
    """
    data = list(np.random.choice(a=np.arange(n), size=m, replace=False))
    bst = BST()
    bst.add_data(data=data)
    data = set(data)

    for i in np.arange(num_tests):
        print(
            "Test " + str(i + 1) + " of " + str(num_tests) + ".", end="\r", flush=True
        )
        assert bst.check_consistancy()
        assert data == set(bst.enumerate_in_order())

        # Randomly decide whether to add or remove data.
        add_data = np.random.rand() >= 0.5
        sample_size = np.random.randint(low=1, high=m + 1)
        sample = list(np.random.choice(a=np.arange(n), size=sample_size, replace=False))
        if bst.head.val in sample:
            sample.remove(bst.head.val)
        if add_data:
            bst.add_data(data=sample)
            data = data.union(set(sample))
        else:
            bst.remove_data(data=sample)
            data = data.difference(set(sample))


def main():
    test_bst(num_tests=20, n=100000, m=10000)


if __name__ == "__main__":
    main()

