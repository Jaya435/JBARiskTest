import unittest
from ExpectedDamage import read_file


class TestReadCSV(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.file = read_file.ReadCSV('/Users/Tom/PycharmProjects/JBARisk_test/test/test_depths.csv')

    def test_dataframe_incorrect_size(self):
        self.assertNotEqual(102, self.file.nLines)

    def test_dataframe_correct_size(self):
        self.assertEqual(101, self.file.nLines)


if __name__ == '__main__':
    unittest.main()
