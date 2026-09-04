# test_orbitquill.py
"""
Tests for OrbitQuill module.
"""

import unittest
from orbitquill import OrbitQuill

class TestOrbitQuill(unittest.TestCase):
    """Test cases for OrbitQuill class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OrbitQuill()
        self.assertIsInstance(instance, OrbitQuill)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OrbitQuill()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
