import unittest

import main


class TestMainMethod(unittest.TestCase):

    def test_increment_fib(self):

        self.assertEqual(main.increment_fib(1), 1)

    def test_increment_fib_2(self):

        self.assertEqual(main.increment_fib(1), 2)


if __name__ == '__main__':

    unittest.main()
