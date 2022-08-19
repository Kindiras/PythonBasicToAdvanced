import unittest
import mathcal

class TestMathcal(unittest.TestCase):
    def  test_add(self):
        self.assertEqual(mathcal.add(4,5),9)
        self.assertEqual(mathcal.add(3,-1),2)
        self.assertEqual(mathcal.add(3,6),9)
        self.assertEqual(mathcal.add(2,4+3j),6+3j)
        self.assertTrue(mathcal.add(3,'k'),TypeError)


    def test_substraction(self):
        self.assertEqual(mathcal.subtraction(2,4),-2)
        self.assertEqual(mathcal.subtraction(-2,-3),1)
        self.assertEqual(mathcal.subtraction(-2,-3),1)
        self.assertEqual(mathcal.subtraction(2,'-k'),TypeError)



if __name__ == '__main__':
    unittest.main()