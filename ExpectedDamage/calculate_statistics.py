from ExpectedDamage.calculate_risk import CalculateRisk
import pandas as pd


class CalculateStatistics(CalculateRisk):
    def __init__(self, depth_file, risk_file, inundated_pct, pixel_size):
        super().__init__(depth_file, risk_file, inundated_pct, pixel_size)
        self.stats = self.calculate_statistics()
        self.export_statistics_csv()

    def average_inundated_depth(self):
        """
        :return: The average depth of water in the inundated area
        """
        return self.df['Depth (m)'].mean().round(0)

    def average_inundated_risk(self):
        """
        :return: The average cost of damage in each inundated pixel
        """
        return self.df['Damage (GBP)'].mean().round(0)

    def volume_of_water_in_inundated(self):
        """
        :return: The volume of water in the inundated area
        """
        return self.average_inundated_depth() * self.total_area()

    def average_total_depth(self):
        """
        :return: The average depth of water in the whole area
        """
        return (self.df['Depth (m)'].sum() / self.total_rows()).round(0)

    def average_risk_total_area(self):
        """
        :return: The avergae cost of damage across the whole area
        """
        return (self.df['Damage (GBP)'].sum() / self.total_rows()).round(0)

    def volume_of_water_in_total_area(self):
        """
        :return: Volume of water in the total area
        """
        return self.average_total_depth() * self.total_area()

    def total_area(self):
        return self.total_rows() * (self.pixel_size ** 2)

    def calculate_statistics(self):
        return [self.average_inundated_depth(), self.average_inundated_risk(), self.volume_of_water_in_inundated(),
               self.average_total_depth(), self.average_risk_total_area(), self.volume_of_water_in_total_area(),
               self.df['Damage (GBP)'].sum()]

    def export_statistics_csv(self):
        """
        Export the statistics to a CSV
        """
        statistic = ['Average inundated depth (m)', 'Average Expected Damage (£) for the inundated area',
                     'Volume of water in inundated area (m\u00b3)', 'Average total depth (m)',
                     'Average Expected Damage (£) for the total area', 'Volume of water in total area (m\u00b3)'
                     'Total Area (m\u00b2)', 'Total Damage (£)']

        data = {'Statistic': statistic, 'Value': self.stats}
        stat_df = pd.DataFrame(data, columns=['Statistic', 'Value'])
        stat_df.to_csv('statistics.csv')


