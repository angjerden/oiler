__author__ = 'b543840'

from Node import Node
import unittest

class TestNode(unittest.TestCase):
    def setUp(self):
        self.node = Node(1, [2, 4, 5, 6, 8], {2:3, 4:7, 5:9})

    def test_get_values(self):
        self.assertEqual(self.node.get_number(), 1)
        self.assertEqual(self.node.get_direct_rel(), [2, 4, 5, 6, 8])
        self.assertEqual(self.node.get_indirect_rel(), {2:3, 4:7, 5:9})


if __name__ == "__main__":
    unittest.main()