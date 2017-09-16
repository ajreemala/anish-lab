import sys
sys.path.insert(0, '../data')
import unittest
from LinkedList import *

class LinkedListTest(unittest.TestCase):
    def test_upper(self):
        l = LinkedList()
        self.assertEqual('foo'.upper(), 'FOO')

    def test_insert_front(self):
        l=LinkedList()
        self.assertEqual(l.head, None)
        l.insert_front(Node('bat'))
        self.assertEqual(l.head.data, 'bat')
        self.assertEqual(l.head.next, None)

if __name__ == '__main__':
    unittest.main()
