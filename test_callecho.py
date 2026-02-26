# test_callecho.py
"""
Tests for CallEcho module.
"""

import unittest
from callecho import CallEcho

class TestCallEcho(unittest.TestCase):
    """Test cases for CallEcho class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CallEcho()
        self.assertIsInstance(instance, CallEcho)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CallEcho()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
