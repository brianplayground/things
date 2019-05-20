import unittest

from DS.mergeSortAlgorithim.mergesort import Mergesort
class MergesortTest(unittest.TestCase):

    def setUp(self):
        self.mergesort = Mergesort()

    def test_merge(self):
        array1 = [1,2,3]
        array2 = [4,5,6]
        output = [1,2,3,4,5,6]
        self.assertEqual(output, self.mergesort.merge(array1, array2))

    def test_actual_sort(self):
        input = [2,5,3,7,8,5]
        output = [2,3,5,5,7,8]
        self.assertEqual(output, self.mergesort.merge_sort(input))
