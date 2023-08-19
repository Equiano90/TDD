import unittest

def concatenate_strings(a, b):
    return a + b

class TestStringManipulation(unittest.TestCase):

    def test_concatenate_empty_strings(self):
        result = concatenate_strings("", "")
        self.assertEqual(result, "")

    def test_concatenate_non_empty_strings(self):
        result = concatenate_strings("Hello, ", "world!")
        self.assertEqual(result, "Hello, world!")
    
    def test_concatenate_mixed_strings(self):
        result = concatenate_strings("Numbers: ", str(123))
        self.assertEqual(result, "Numbers: 123")

if __name__ == '__main__':
    unittest.main()