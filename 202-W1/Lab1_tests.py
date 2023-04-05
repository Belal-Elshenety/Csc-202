import Lab1
import unittest

class Tests(unittest.TestCase):
    def test_indexOf1(self):
        result = Lab1.indexOf("Mississippi", "sip")
        expected = 6
        self.assertEqual(expected, result)

    def test_indexOf2(self):
        result = Lab1.indexOf("Mississippi", "python")
        expected = -1
        self.assertEqual(expected,result)

    def test_indexOf3(self):
        result = Lab1.indexOf("Mississippi", "Mis")
        expected = 0
        self.assertEqual(expected,result)

    def test_indexOf4(self):
        result = Lab1.indexOf("Mississippi", "ppi")
        expected = 8
        self.assertEqual(expected,result)

    def test_sqrt1(self):
        result = Lab1.sqrt(4)
        expected = 2
        self.assertAlmostEqual(expected,result)

    def test_sqrt2(self):
        result = Lab1.sqrt(9)
        expected = 3
        self.assertAlmostEqual(expected,result)

    def test_sqrt3(self):
        result = Lab1.sqrt(16)
        expected = 4
        self.assertAlmostEqual(expected,result)

    def test_sqrt4(self):
        result = Lab1.sqrt(25)
        expected = 5
        self.assertAlmostEqual(expected,result)

    def test_sqrt5(self):
        result = Lab1.sqrt(36)
        expected = 6
        self.assertAlmostEqual(expected,result)

    def test_sqrt6(self):
        result = Lab1.sqrt(-4)
        expected = "Math error"
        self.assertAlmostEqual(expected,result)

    def test_sqrt7(self):
        result = Lab1.sqrt(81, 200)
        expected = 9
        self.assertAlmostEqual(expected,result)

    def test_sqrt8(self):
        result = Lab1.sqrt(2)
        expected = 1.4142
        self.assertAlmostEqual(expected,result,4)
if __name__ == '__main__':
    unittest.main()




