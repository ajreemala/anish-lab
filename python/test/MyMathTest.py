import sys
sys.path.insert(0, '../data')
import unittest
from MyMath import *

class MyMathTest(unittest.TestCase):
    def test_max(self):
        l = [123, 883, 627, 99223, 556472]
        m = MyMath()
        v = m.max(l)
        self.assertEquals(v, 556472)

    def test_min(self):
        l = [123, 883, 627, 99223, 556472]
        m = MyMath()
        v = m.min(l)
        self.assertEquals(v, 123)

    def test_power_1(self):
        self.assertEquals(MyMath().power(2,3), 8)
        self.assertEquals(MyMath().power(5,2), 25)
        self.assertEquals(MyMath().power(5,0), 1)
        self.assertEquals(MyMath().power(5,1), 5)
        self.assertEquals(MyMath().power(10,5), 100000)

    def test_mult(self):
        self.assertEquals(MyMath().mult(2,3), 6)
        self.assertEquals(MyMath().mult(7,2), 14)
        self.assertEquals(MyMath().mult(10,5), 50)

    def test_factorial(self):
        self.assertEquals(MyMath().factorial(2), 2)
        self.assertEquals(MyMath().factorial(3), 6)
        self.assertEquals(MyMath().factorial(4), 24)
        self.assertEquals(MyMath().factorial(0), 1)

    def test_taylor_series(self):
        self.assertAlmostEqual(MyMath().taylor_series(0), 1)
        self.assertAlmostEqual(MyMath().taylor_series(1), 2)
        self.assertAlmostEqual(MyMath().taylor_series(2), 2.5)
        self.assertAlmostEqual(MyMath().taylor_series(3), 2.666666666666)


if __name__ == '__main__':
    unittest.main()
