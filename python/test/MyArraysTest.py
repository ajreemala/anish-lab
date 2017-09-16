import sys
sys.path.insert(0, '../data')
import unittest
from MyArrays import *

class MyArraysTest(unittest.TestCase):
    def test_search(self):
        test_vector = [2, 6, 1, 9, 4, 8, 1]
        self.assertEquals(MyArrays().search(test_vector,9), True)
        self.assertEquals(MyArrays().search(test_vector,3), False)

    def test_bsearch(self):
        test_vector = [2, 6, 11, 19, 21, 32, 56, 78, 89]
        self.assertEquals(MyArrays().bsearch(test_vector,19), True)
        self.assertEquals(MyArrays().bsearch(test_vector,31), False)

    def test_bubble_sort(self):
        v = [24, 65, 111, 19, 21, 232, 56, 478, 89]
        MyArrays().bubble_sort(v)
        i = 0
        for x in sorted(v):
            self.assertEquals(v[i], x)
            i += 1
    def test_bubble_sort1(self):
        v = [5, 4, 3, 2, 1, 0, 7]
        MyArrays().bubble_sort(v)
        i = 0
        for x in sorted(v):
            self.assertEquals(v[i], x)
            i += 1


if __name__ == '__main__':
    unittest.main()
