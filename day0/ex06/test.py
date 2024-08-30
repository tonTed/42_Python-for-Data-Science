import unittest


from ft_filter import ft_filter


def test_filter(func, iterable):
    ft = ft_filter(func, iterable)
    builtin = filter(func, iterable)
    return ft, builtin


def is_adult(age):
    return age >= 18


def is_positive(num):
    return num >= 0


class TestFilter(unittest.TestCase):
    def test_filter(self):
        ages = [5, 12, 17, 18, 24, 32]
        ft, builtin = test_filter(is_adult, ages)
        self.assertEqual(list(ft), list(builtin))

    def test_filter_empty(self):
        ft, builtin = test_filter(is_adult, [])
        self.assertEqual(list(ft), list(builtin))

    def test_filter_is_positive(self):
        numbers = [-1, -2, -3, 0, 1, 2, 3]
        ft, builtin = test_filter(is_positive, numbers)
        self.assertEqual(list(ft), list(builtin))

    # def test_filter_none(self):
    #     none = ft_filter(lambda x: x >= 0, [-1, -2, -3])
    #     self.assertEqual(list(none), [])

    # def test_filter_str(self):
    #     str_ = ft_filter(lambda x: x != 'a', 'abracadabra')
    #     self.assertEqual(list(str_), ['b', 'r', 'c', 'd', 'b', 'r'])

    # def test_filter_tuple(self):
    #     tup = ft_filter(lambda x: x % 2 == 0, (1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    #     self.assertEqual(list(tup), [2, 4, 6, 8, 10])

    # def test_filter_dict(self):
    #     dic = ft_filter(lambda x: x % 2 == 0, {1: 2, 2: 3, 3: 4, 4: 5})
    #     self.assertEqual(list(dic), [2, 4])

    # def test_filter_set(self):
    #     sett = ft_filter(lambda x: x % 2 == 0, {1, 2, 3, 4, 5})
    #     self.assertEqual(list(sett), [2, 4])


if __name__ == "__main__":
    unittest.main()
