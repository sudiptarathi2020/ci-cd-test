from app import add, mul

import unittest

class TestApp(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2,3),5)

    def test_mul(self):
        self.assertEqual(mul(2,3),6)

if __name__ == "__main__":
    unittest.main()
