import unittest
from bubblesort import bubble_sort

class BubbleSortTest(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([0, 5, 2, 3, 2]), [0, 2, 2, 3, 5])

    def test_already_sorted(self):
        self.assertEqual(bubble_sort([0, 2, 2, 3, 5]), [0, 2, 2, 3, 5])

    def test_empty_list(self):
        self.assertEqual(bubble_sort([]), [])

    def test_negative_numbers(self):
        self.assertEqual(bubble_sort([-2, -5, -45]), [-45, -5, -2])

    def test_single_element(self):
        self.assertEqual(bubble_sort([42]), [42])

if __name__ == '__main__':
    unittest.main()
