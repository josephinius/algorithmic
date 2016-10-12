import sorting.sort as sort
import unittest
import random


class RandomNumbers(unittest.TestCase):
    def test_sorting_algorithm(self):
        for test_id in range(2):
            short_length = random.randint(1, 10)
            random_integers = self.random_integers(short_length)
            self.sort_test(random_integers)
            random_floats = self.random_floats(short_length)
            self.sort_test(random_floats)

    def random_integers(self, length):
        integers = []
        for number in range(length):
            integers.append(random.randint(-1000, 1000))
        return integers

    def random_floats(self, length):
        floats = []
        for number in range(length):
            floats.append(random.uniform(-1000.0, 1000.0))
        return floats

    def sort_test(self, test_list):
        sorted_field = sort.shuffle_sort(test_list)  # Here you select which sort function to test
        python_sorted_field = sorted(test_list)
        self.assertEqual(sorted_field, python_sorted_field, "Python sorted list differently")

if __name__ == '__main__':
    unittest.main()
