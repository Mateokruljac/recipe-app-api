""" 
Simple tests
"""
from django.test import SimpleTestCase
from rest_framework.test import APIClient

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
        
    def test_greeting(self):
        client = APIClient()
        res = client.get("https://learn.microsoft.com/hr-hr/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package")
        self.assertEqual(res.status_code,200)