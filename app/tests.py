""" 
Simple tests
"""
from django.test import SimpleTestCase
from app import calc 

class CalcTests(SimpleTestCase):
    """ Test a Calculator module."""
    
    def test_add_numbers(self):
        """ 
        Test adding number together
        """
        result = calc.add(5,6)
        self.assertEqual(result,11)
    
    def test_substract_numbers(self):
        """ Test substract numbers"""
        res = calc.substract_numbers(10,15)
        self.assertEqual(res,5)