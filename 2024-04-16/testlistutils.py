from unittest import TestCase, main
from listutils import selection_sort, is_ascending_2
from random import randrange


class TestListUtils(TestCase):

    def test_sort_1(self):
        a = [randrange(100) for _ in range(20)]
        selection_sort(a)
        self.assertTrue(is_ascending_2(a))

    def test_sort_2(self):
        a = [10, 4, 2, 92, 8, 45]
        selection_sort(a)
        self.assertEqual([2, 4, 8, 10, 45, 92], a)

    def test_sort_3(self):
        a = [10, 4, 2, 45, 8, 92]
        selection_sort(a)
        self.assertEqual([2, 4, 8, 10, 45, 92], a)

# if __name__ == '__main__':
#     main()