import random


class Quicksort:

    def quicksort(self, array):
        if len(array) <= 1: return  array
        less = []
        greater = []
        equal = []

        pivot = array[random.randint(0, len(array) - 1)]

        for i in array:
            if i == pivot:
                equal.append(i)
            elif i > pivot:
                greater.append(i)
            else:
                less.append(i)

        return self.quicksort(less) + equal + self.quicksort(greater)

    def partition(self, array, low, high):
        pass


    def inpline_quicksort(self, array, low = 0, high=None):
        pass

