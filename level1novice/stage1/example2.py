import unittest

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by sero is not allowed.")
    return a / b

class TestMathLibrary(unittest.TestCase):

    def test_addition(self):
        result = add(5, 3)
        self.assertEqual(result, 8)

    def test_subtraction(self):
        result = substract(10, 4)
        self.assertEqual(result, 6)

    def test_multiplication(self):
        result = multiply(6, 7)
        self.assertEqual(result, 42)

    def test_division(self):
        result = divide(15, 3)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()


    