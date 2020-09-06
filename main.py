#!/usr/bin/python

import argparse

from ExpectedDamage.calculate_risk import CalculateRisk

if __name__ == "__main__":
    # create parser
    parser = argparse.ArgumentParser(description='Read a depth CSV, apply a vulnerability curve and output a CSV of '
                                                 'the result')

    # add arguments to the parser
    parser.add_argument('-id', '--input_depth', help='Input depth file name', required=True)
    parser.add_argument('-iv', '--input_vulnerability', help='Input vulnerability curve filename', required=True)
    parser.add_argument('-pct_inun', '--percentage_inundated',
                        help='What percent of the area was inundated, default is 100 percent', default=100)
    parser.add_argument('-pix', '--pixel_size', help='Pixel size', default=10)
    parser.add_argument('-o', '--output', help='Output file name, default is DepthDamage.csv',
                        default='result/DepthDamage.csv')

    args = parser.parse_args()
    risk_df = CalculateRisk(args.input_depth, args.input_vulnerability,
                            args.percentage_inundated, args.pixel_size)
    risk_df.save_to_csv(args.output)
    risk_df.print_statistics()
