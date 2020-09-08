# JBA Risk Code Challenge

This Repository contains a python project that can read in a CSV containing water depth, apply a vulnerability curve, and calculate the damage per pixel.

## Getting Started

These instructions will let you get a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need to run this programme using Python3. You can follow a guide here to install Python3 on your local machine https://installpython3.com/. Once Python3 is installed, you can run this programme from within a virtual environment. You can do this by creating a virtual environment as below:

```
python3 -m venv /path/to/new/virtual/environment
```
to activate the venv use:
```
source /path/to/new/virtual/environment/bin/activate
```

### Installing

A step by step series of examples that tell you how to get a development env running

Clone the repository onto your local machine
```
https://github.com/Jaya435/JBARiskTest.git
```
Then run
```
python main.py -id depths.csv -iv vulnerability_curve.csv -pix 10 -pct_inun 50 -o test_output.csv
```
The --output flag is optional and defines the name of the output CSV that will be generated.

The -pct_inun corresponds to the percentage of the area that was inundated with water

The -pix flag refers to the size of the grid being used for each depth measurement

The --id flag is mandatory and relates to the file you would like to be read.

```
usage: main.py [-h] -id INPUT_DEPTH -iv INPUT_VULNERABILITY
               [-pct_inun PERCENTAGE_INUNDATED] [-pix PIXEL_SIZE] [-o OUTPUT]

Read a depth CSV, apply a vulnerability curve and output a CSV of the result

optional arguments:
  -h, --help            show this help message and exit
  -id INPUT_DEPTH, --input_depth INPUT_DEPTH
                        Input depth file name
  -iv INPUT_VULNERABILITY, --input_vulnerability INPUT_VULNERABILITY
                        Input vulnerability curve filename
  -pct_inun PERCENTAGE_INUNDATED, --percentage_inundated PERCENTAGE_INUNDATED
                        What percent of the area was inundated, default is 100
                        percent
  -pix PIXEL_SIZE, --pixel_size PIXEL_SIZE
                        Pixel size
  -stats [STATISTICS], --statistics [STATISTICS]
                        Set to True if you want to calculate statistics and
                        save to CSV
  -o OUTPUT, --output OUTPUT
                        Output file name, default is DepthDamage.csv
```

Once the programme is run, you can view the data stored in the system by viewing the CSV file that has been output. Unless specificed this will be called DepthDamage.csv

Additional statistics can be calculated by setting the -stats flag to True

## Running the tests

The automated tests can be run using the below command:
```
python3 -m unittest discover
```

## Authors

* **Tom Richmond** - *Initial work* - [Jaya435](https://github.com/Jaya435/)
