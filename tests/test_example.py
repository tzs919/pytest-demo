import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here


print("****111*****", __name__)
if __name__ == '__main__':
    unittest.main()
