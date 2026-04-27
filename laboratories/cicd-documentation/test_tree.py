import unittest

from tree import Tree

class TreeTestCase(unittest.TestCase):
    def setUp(self):
        self.tree = Tree()
        for value in [5, 3, 7, 2, 4, 6, 8]:
            self.tree.add(value)

    def test_find_returns_left_leaf_node(self):
        node = self.tree._find(2, self.tree.root)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 2)

    def test_find_returns_right_leaf_node(self):
        node = self.tree._find(8, self.tree.root)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 8)

    def test_find_returns_none_for_missing_value(self):
        node = self.tree._find(10, self.tree.root)
        self.assertIsNone(node)


if __name__ == "__main__":
    unittest.main()
