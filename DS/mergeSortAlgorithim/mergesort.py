class Mergesort:

    def merge(self, left, right):
        result = []

        left_index, right_index = 0, 0

        while left_index < len(left) and right_index < len(right):

            if left[left_index] < right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1

        if left_index == len(left):
            result.extend(right[right_index:])
        else:
            result.extend(left[left_index:])

        return result

    def merge_sort(self, array):
        if len(array) <= 1:
            return array

        left, right = self.merge_sort(array[:int(len(array) / 2)]), self.merge_sort(array[int(len(array) / 2):])

        return self.merge(left, right)
