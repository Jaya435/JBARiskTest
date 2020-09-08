import unittest
import os
from ExpectedDamage import calculate_statistics


class TestCalculateStatistics(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.risk = calculate_statistics.CalculateStatistics('/Users/Tom/PycharmProjects/JBARisk_test/test/test_depths.csv',
                                                 '/Users/Tom/PycharmProjects/JBARisk_test/test'
                                                 '/test_vulnerability_curve.csv',
                                                 75, 10)

    def tearDown(self) -> None:
        super().tearDown()
        os.remove("Statistics.csv")
        self.risk.release_memory()

    def test_calculate_average_inundated_depth_correctly(self):
        self.assertEqual(5, int(self.risk.stats[0]))

    def test_calculate_average_total_depth_correctly(self):
        self.assertEqual(4, int(self.risk.stats[3]))

    def test_calculate_average_inundated_volume_correctly(self):
        self.assertEqual(67333, int(self.risk.stats[2]))

    def test_calculate_average_total_area_correctly(self):
        self.assertEqual(53866, int(self.risk.stats[5]))

    def test_calculate_average_cost_inundated_area_correctly(self):
        self.assertEqual(106130, int(self.risk.stats[1]))

    def test_calculate_average_cost_total_area_correctly(self):
        self.assertEqual(78809, int(self.risk.stats[4]))

    def test_calculate_total_cost_of_damage_correctly(self):
        self.assertEqual(10613000, int(self.risk.stats[6]))


if __name__ == '__main__':
    unittest.main()
