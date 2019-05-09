import unittest

class TestDevOps(unittest.TestCase):

    def test_conflict(self):
        self.assertEqual('Dev' + 'Ops', 'DdevOps')

if __name__ == '__main__':
    unittest.main()
