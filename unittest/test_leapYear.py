import unittest
import leapYear

inp1 = 2000
inp2 = 100
inp3 = "2000"

class TestCase(unittest.TestCase):
    def test_inputType1(self):
        self.assertEqual(type(inp1),type(123))
    def test_inputType2(self):
        self.assertEqual(type(inp2),type(123))
    def test_inputType3(self):
        self.assertEqual(type(inp3),type(123))
    
    def test_returnType1(self):
        result = leapYear.isLeapYear(inp1)
        self.assertEqual(type(result),type(True))
    def test_returnType1(self):
        result = leapYear.isLeapYear(inp2)
        self.assertEqual(type(result),type(True))
    def test_returnType1(self):
        result = leapYear.isLeapYear(inp3)
        self.assertEqual(type(result),type(True))

if __name__ == '__main__':unittest.main()