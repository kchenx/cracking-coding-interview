# Remove Dups!
# Write code to remove duplicates from an unsorted linked list.
# How would you solve this problem if a temporary buffer is not allowed?

import unittest


class Node:
    """Node class for LinkedList"""

    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    """Linked list class"""

    def __init__(self, arr=None):
        """Inits linked list with values in `arr`"""
        curr = None
        if arr is not None:
            for i in reversed(range(len(arr))):
                n = Node(arr[i])
                n.next = curr
                curr = n
        self.head = curr

    def remove_dups(self):
        """Removes duplicate vals from linked list"""
        seen = set()
        prev = None
        curr = self.head
        while curr is not None:
            val = curr.val
            if val in seen:
                prev.next = curr.next
            else:
                seen.add(val)
                prev = curr
            curr = curr.next

    def __str__(self):
        vals = []
        curr = self.head
        while curr != None:
            vals.append(str(curr.val))
            curr = curr.next
        return " ".join(vals)


class TestRemoveDups(unittest.TestCase):
    def test_remove_dups(self):
        lst = LinkedList()
        lst.remove_dups()
        self.assertEqual(str(lst), "")
        lst = LinkedList([1, 2, 3, 4, 5])
        lst.remove_dups()
        self.assertEqual(str(lst), "1 2 3 4 5")
        lst = LinkedList([1, 2, 3, 1, 4, 5])
        lst.remove_dups()
        self.assertEqual(str(lst), "1 2 3 4 5")
        lst = LinkedList([1, 2, 3, 4, 4, 4, 5])
        lst.remove_dups()
        self.assertEqual(str(lst), "1 2 3 4 5")
        lst = LinkedList([1, 2, 1, 3, 4, 1, 5, 2, 5, 3])
        lst.remove_dups()
        self.assertEqual(str(lst), "1 2 3 4 5")

    def test_linked_list(self):
        lst = LinkedList()
        self.assertEqual(str(lst), "")
        lst = LinkedList([])
        self.assertEqual(str(lst), "")
        lst = LinkedList([1])
        self.assertEqual(str(lst), "1")
        lst = LinkedList([1, 2, 3, 4, 5])
        self.assertEqual(str(lst), "1 2 3 4 5")


if __name__ == "__main__":
    unittest.main()