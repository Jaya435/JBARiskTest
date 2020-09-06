import unittest
from ExpectedDamage import calculate_risk


class TestCalculateRisk(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.risk = calculate_risk.CalculateRisk('/Users/Tom/PycharmProjects/JBARisk_test/test/test_depths.csv',
                                                 '/Users/Tom/PycharmProjects/JBARisk_test/test'
                                                 '/test_vulnerability_curve.csv',
                                                 75, 10)
        
    def tearDown(self) -> None:
        super().tearDown()
        self.risk.release_memory()

    def test_calculate_total_rows_correctly(self):
        self.assertEqual(135.0, round(self.risk.total_rows(), 0))

    def test_total_area_correctly(self):
        self.assertEqual(13467.0, round(self.risk.total_area(), 0))

    def test_calculate_risk_incorrectly(self):
        self.assertNotEqual(50000, self.risk.df['Damage (GBP)'].iloc[10])

    def test_calculate_risk_correctly(self):
        self.assertEqual(132500, self.risk.df['Damage (GBP)'].iloc[0])

    def test_calculate_average_inundated_risk_incorrectly(self):
        self.assertNotEqual(100, self.risk.average_inundated_risk())

    def test_calculate_average_inundated_risk_correctly(self):
        self.assertEqual(106130.0, self.risk.average_inundated_risk())

    def test_calculate_average_risk_incorrectly(self):
        self.assertNotEqual(100, self.risk.average_risk_total_area())

    def test_calculate_average_risk_correctly(self):
        self.assertEqual(78809.0, self.risk.average_risk_total_area())

if __name__ == '__main__':
    unittest.main()
