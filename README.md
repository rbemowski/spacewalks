# Spacewalks

## Overview

Spacewalks is a Python analysis tool for researchers to generate visualizations and statistical summaries of NASA's extravehicular activity datasets.

## Features

Key features of Spacewalks:

- Generates a CSV table of summary statistics of extravehicular activity crew sizes
- Generates a line plot to show the cumulative duration of space walks over time

## Pre-requisites

Spacewalks was developed using Python version 3.12

To install and run Spacewalks you will need have Python >=3.12 installed.
You will also need the following libraries:

- [Numpy](https://www.numpy.org) >=2.0.0 - Spacewalks' test suite uses NumPy's statistical functions
- [Matplotlib](https://matplotlib.org/stable/index.html) >=3.0.0  - Spacewalks uses Matplotlib to make plots
- [pytest](https://docs.pytest.org/en/8.2.x/#) >=8.2.0  - Spacewalks uses pytest for testing
- [pandas](https://pandas.pydata.org/) >= 2.2.0 - Spacewalks uses pandas for data frame manipulation


## Installation

- Clone the Spacewalks repository to your local machine using git.
If you don't have Git installed, you can download it from the official Git website.

```
git clone https://github.com/rbemowski/spacewalks.git
cd spacewalks
```

- Install the necessary dependencies
```
python -m pip install -r requirements.txt
```

- To ensure everything is working correctly, run the tests using pytest.
```
python -m pytest
```


## Example Usage

To run an analysis using hte `eva_data_analysis.py` script from the command line terminal, launch the script using Python as follows:

```
python eva_data_analysis.py eva-data.json eva-data.csv
```

The first argument is the path to the JSON data file.
The second argument is the path to the CSV output file.


