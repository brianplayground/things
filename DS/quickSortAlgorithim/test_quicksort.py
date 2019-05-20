import unittest

from DS.quickSortAlgorithim.quicksort import Quicksort


class QuicksortTest(unittest.TestCase):

    def setUp(self):
        self.quicksort = Quicksort()

    def test_quicksort(self):
        input = [3, 4, 1, 8, 3]
        output = [1, 3, 3, 4, 8]
        self.assertEqual(output, self.quicksort.quicksort(input))

    def test_partion(self):
        pass

    def test_inline_quicksort(self):
        input = [3, 4, 1, 8, 3]
        output = [1, 3, 3, 4, 8]
        self.assertEqual(output, self.quicksort.inpline_quicksort(input, 0, None))
