import unittest
from name_func_2 import get_formatted_name_middle

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py."""

    def test_first_last_name(self):
        """Do names like 'Gary Park' work?"""
        formatted_name = get_formatted_name_middle('gary','park')
        self.assertEqual(formatted_name,'Gary Park') 
    
    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name_middle('wolfgang','mozart','amadeus')
        self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart') # Assert Method

    
if __name__ == '__main__':
    unittest.main()


# Testing a Class
# Assert Methods test whether a condition you believe is true at a specific point in your code is indeed true.

# Assert Methods Available from the unitest Module
# assertEqual(a, b)        Verify that a == b
# assertNotEqual(a, b)     Verify that a != b
# assertTrue(x)            Verify that x is True
# assertFalse(x)           Verify that x is False
# assertIn(item, list)     Verify that item is in list
# assertNotIn(item, list)   Verify that item is not in list
