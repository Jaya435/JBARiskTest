import pandas as pd

class ReadCSV():
    """Reads a CSV and outputs a Pandas Dataframe"""
    def __init__(self, filename):
        self.df = pd.read_csv(filename)
        self.nLines = len(self.df.index)

    def save_to_csv(self, output_filename):
        self.df.to_csv(output_filename, index=True)