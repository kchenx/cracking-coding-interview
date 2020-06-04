# First Common Ancestor
# Design an algorithm and write code to find the first common ancestor of two
# nodes in a binary tree. Avoid storing additional nodes in a data structure.
# NOTE: This is not necessarily a binary search tree.

from mybinarytree import TreeNode, make_binary_tree
import unittest


def first_common_ancestor(root: TreeNode, u: TreeNode, v: TreeNode) -> TreeNode:
    # modified DFS
    return _first_common_ancestor_util(root, u, v)[0]


def _first_common_ancestor_util(n: TreeNode, u: TreeNode, v: TreeNode) -> (TreeNode, bool, bool):
    if n is None:
        return None, False, False
    leftnode, leftu, leftv = _first_common_ancestor_util(n.left, u, v)
    rightnode, rightu, rightv = _first_common_ancestor_util(n.right, u, v)
    if leftnode is not None:
        return leftnode, True, True
    if rightnode is not None:
        return rightnode, True, True
    uisdescendant = n is u or leftu or rightu
    visdescendant = n is v or leftv or rightv
    if uisdescendant and visdescendant:
        return n, True, True
    return None, uisdescendant, visdescendant


class TestFirstCommonAncestor(unittest.TestCase):
    def test_first_common_ancestor(self):
        tree = make_binary_tree([1, 2, 3, 4, 5, 6, None, 7, 8])
        othertree = make_binary_tree([-1])
        tests = [
            # u, v, ancestor
            [tree, tree, tree],
            [tree.left, tree, tree],
            [tree.right, tree, tree],
            [tree.left.left.left, tree.left.left.right, tree.left.left],
            [tree.right.left, tree.right, tree.right],
            [tree.left.left.right, tree.left.right, tree.left],
            [tree.left.right, tree.right, tree],
            [tree.left.left, None, None],
            [tree.left.left, othertree, None]
        ]
        for u, v, ancestor in tests:
            with self.subTest(u=u.val if u is not None else None, v=v.val if v is not None else None):
                self.assertIs(first_common_ancestor(tree, u, v), ancestor)
                self.assertIs(first_common_ancestor(tree, v, u), ancestor)


if __name__ == "__main__":
    unittest.main()