import unittest
from main import get_sum


class MyTestCase(unittest.TestCase):
    def test1_get_sum(self):
        sum = get_sum(12,4)
        self.assertEqual(sum , 16,"Test Pass")

    def test2_get_sum(self):
        sum = get_sum(12,4)
        self.assertFalse(sum > 110,"Test Pass")

    def test3_get_sum(self):
        sum = get_sum(12,4)
        self.assertTrue(sum < 2, "Test Pass")

if __name__ == '__main__':
    unittest.main()