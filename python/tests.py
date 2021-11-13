import unittest

import fib


class TestFibMethod(unittest.TestCase):

    def test_increment_fib(self):

        self.assertEqual(fib.increment_fib(1), 1)

    def test_increment_fib_2(self):

        self.assertEqual(fib.increment_fib(1), 2)

    def test_increment_fib_3(self):

        self.assertEqual(fib.increment_fib(1), 3)


if __name__ == '__main__':

    unittest.main()
