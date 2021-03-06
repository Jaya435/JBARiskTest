from .read_file import ReadCSV
import numpy as np
import datetime
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class CalculateRisk(ReadCSV):
    """
    Calculates the risk in a postcode by pixel, based on a vulnerability curve
    """
    def __init__(self, depth_file, risk_file, inundated_pct, pixel_size):
        super().__init__(depth_file)
        self.risk_df = ReadCSV(risk_file).df
        self.inundated_pct = int(inundated_pct)
        self.pixel_size = int(pixel_size)
        self.apply_vulnerability()

    def total_rows(self):
        """
        :return: The total number of pixels in the area
        """
        if self.inundated_pct < 100:
            return ((self.nLines / self.inundated_pct) * (100 - self.inundated_pct)) + self.nLines
        else:
            return self.nLines

    def apply_vulnerability(self):
        """
        Applies the vulnerability curve to the depth of water
        :return: a pandas dataframe of the depth, with an updated column containing the damage cost
        """
        start_time = datetime.datetime.now()
        depth_array = self.df.to_numpy()
        risk_array = self.risk_df.to_numpy()
        risk_max = self.risk_df['DepthUpperBound (m)'].max()
        risk_min = self.risk_df['DepthLowerBound (m)'].min()
        risk = []
        for i in depth_array:
            if i > risk_max:
                logging.info('Depth is {}m, this is greater than the upper limit of the vulnerability curve'.format(i))
                risk.append(np.nan)
            elif i < risk_min:
                logging.info('Depth is {}m, this is less than the lower limit of the vulnerability curve'.format(i))
                risk.append(np.nan)
            else:
                for row in risk_array:
                    if row[0] < i < row[1]:
                        risk.append(row[2])

        self.df['Damage (GBP)'] = risk
        logging.info("Vulnerability calculated in in {} seconds".format(datetime.datetime.now() - start_time))
        return self.risk_df

    def average_inundated_risk(self):
        """
        :return: The average cost of damage in each inundated pixel
        """
        return self.df['Damage (GBP)'].mean().round(0)

    def average_risk_total_area(self):
        """
        :return: The avergae cost of damage across the whole area
        """
        return (self.df['Damage (GBP)'].sum() / self.total_rows()).round(0)

    def total_area(self):
        return self.total_rows() * (self.pixel_size**2)

    def release_memory(self):
        """
        Releases memory during testing
        """
        del self.df
        del self.risk_df
