import unittest
import circleArea
from math import pi

class TestcircleArea(unittest.TestCase):
    def test_circleArea(self):
        #Test area when readius> 0
        self.assertAlmostEqual(circleArea.circleArea(1),pi)
        self.assertAlmostEqual(circleArea.circleArea(0),0)
        self.assertAlmostEqual(circleArea.circleArea(2),pi*2**2)
        self.assertTrue(circleArea.circleArea('k'),TypeError)
        self.assertTrue(circleArea.circleArea(2+3j),TypeError)
        self.assertRaises(ValueError, circleArea.circleArea,-2) #This is the way to give arguments for assertRaises



if __name__ == '__main__':
    unittest.main()