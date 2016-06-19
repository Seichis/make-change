import unittest
import random
from types import IntType
import MakeChange

class MakeChangeTestCases(unittest.TestCase):
    
    def test_float_input(self):
        # Float input
        with self.assertRaises(ValueError):
            MakeChange.MakeChange(random.uniform(0, 200000))
        
    def test_string_input(self):
        # String input
        with self.assertRaises(ValueError):
            MakeChange.MakeChange("3%3")
            
    def test_int_output(self):
        self.assertTrue(type(MakeChange.MakeChange(random.randint(0,200000000))==IntType))
    
    def test_negative_int_input(self):
        with self.assertRaises(ValueError):
            MakeChange.MakeChange(random.randint(-10000,0))
			
if __name__ == "__main__":
	tests=unittest.TestLoader().loadTestsFromTestCase(MakeChangeTestCases)
	unittest.TextTestRunner(verbosity=2).run(tests)
	