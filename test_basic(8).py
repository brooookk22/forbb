
import unittest
import importlib

module = importlib.import_module('structure_chooser')

class TestProgram(unittest.TestCase):
    def test_import(self):
        self.assertTrue(hasattr(module, '__doc__'))

if __name__ == '__main__':
    unittest.main()
