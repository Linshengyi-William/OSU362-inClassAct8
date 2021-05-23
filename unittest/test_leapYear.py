import unittest
import leapYear

inp1 = 2000
inp2 = 100
inp3 = 1999
inp4 = "2000"

class TestCase(unittest.TestCase):
    def test_inputType1(self):
        self.assertEqual(type(inp1),type(123))
    def test_inputType2(self):
        self.assertEqual(type(inp2),type(123))
    def test_inputType3(self):
        self.assertEqual(type(inp3),type(123))
    def test_inputType4(self):
        self.assertEqual(type(inp4),type(123))
    
    def test_returnType1(self):
        result = leapYear.isLeapYear(inp1)
        self.assertEqual(type(result),type(True))
    def test_returnType2(self):
        result = leapYear.isLeapYear(inp2)
        self.assertEqual(type(result),type(True))
    def test_returnType3(self):
        result = leapYear.isLeapYear(inp3)
        self.assertEqual(type(result),type(True))
    def test_returnType4(self):
        result = leapYear.isLeapYear(inp4)
        self.assertEqual(type(result),type(True))

    def test_correctResult1(self):
        result = leapYear.isLeapYear(inp1)
        correct_result = True
        self.assertEqual(result,correct_result)
    def test_correctResult2(self):
        result = leapYear.isLeapYear(inp2)
        correct_result = False
        self.assertEqual(result,correct_result)
    def test_correctResult3(self):
        result = leapYear.isLeapYear(inp3)
        correct_result = False
        self.assertEqual(result,correct_result)
    def test_correctResult4(self):
        result = leapYear.isLeapYear(inp4)
        correct_result = False
        self.assertEqual(result,correct_result)
    


if __name__ == '__main__':unittest.main()