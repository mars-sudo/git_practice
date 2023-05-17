# To write a test case for a function, import the unittest module
# and the function you want to test. Then create a class that inherits from 
# unittest.TestCase
# and write a series of methods to test different aspects of your function's behavior. 

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py."""

    def test_first_last_name(self):
        """Do names like 'Gary Duphrane' work?"""
        formatted_name = get_formatted_name('gary','park')
        self.assertEqual(formatted_name, 'Gary Park') 
# Assert methods verify that a result you received matches the result you expect. In this case, we know get_formatted_name()
# is supposed to return a capitalized, spaced full name. We expect the value of formatted_name to be Gary Duphrane. 

if __name__ == '__main__':
    unittest.main()
# The if block looks at a special variable _name_, which is set when the program is executed. If this file is being run
# as the main program, the value of _name_ is set to 'main'. In this case we call unittest.main(), which runs the test
# case . 

