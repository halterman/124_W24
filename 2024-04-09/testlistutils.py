import unittest
from listutils import selection_sort


class TestListUtils(unittest.TestCase):
    def test_random_list(self) -> None:
        a = [20, 1, 4, 67, 2, 1, 17, 88, 12, 4]
        selection_sort(a)
        self.assertEqual([1, 1, 2, 4, 4, 12, 17, 20, 67, 88], a)

    def test_already_sorted(self) -> None:
        a = [1, 1, 2, 4, 4, 12, 17, 20, 67, 88]
        selection_sort(a)
        self.assertEqual([1, 1, 2, 4, 4, 12, 17, 20, 67, 88], a)

    def test_empty(self) -> None:
        a = []
        selection_sort(a)
        self.assertEqual([], a)

    def test_one(self) -> None:
        a = [10]
        selection_sort(a)
        self.assertEqual([10], a)

    def test_two_1(self) -> None:
        a = [10, 20]
        selection_sort(a)
        self.assertEqual([10, 20], a)

    def test_two_2(self) -> None:
        a = [20, 10]
        selection_sort(a)
        self.assertEqual([10, 20], a)


if __name__ == '__main__':
    unittest.main()