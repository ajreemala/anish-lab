import sys
#from ..data.MyBST import *
sys.path.insert(0, '../data')
from MyBST import *
import unittest


class MyBSTTest(unittest.TestCase):
    def test_find(self):
        t = MyBST()
        
        self.assertEquals(t.find(189), False)

        t.insert(100)
        t.insert(50)
        t.insert(789)
        t.insert(89)
        t.insert(189)
        t.insert(689)
        t.insert(819)
        t.insert(20)

        self.assertEquals(t.find(189), True)
        self.assertEquals(t.find(689), True)
        self.assertEquals(t.find(1890), False)

if __name__ == '__main__':
    unittest.main()
