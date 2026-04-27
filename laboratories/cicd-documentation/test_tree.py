import unittest

from tree import Tree


class TestTreeFind(unittest.TestCase):
    def setUp(self):
        self.tree = Tree()
        for value in [3, 4, 0, 8, 2]:
            self.tree.add(value)

    def test_find_returns_node_when_value_exists(self):
        node = self.tree._find(8, self.tree.getRoot())
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 8)

    def test_find_returns_none_when_value_does_not_exist(self):
        node = self.tree._find(5, self.tree.getRoot())
        self.assertIsNone(node)


if __name__ == "__main__":
    unittest.main()
