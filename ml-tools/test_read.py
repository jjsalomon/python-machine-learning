import pandas as pd
import numpy as np
import random

# Sample Size
s = 5
filename = "data/sampledata.csv"
# N = Number of rows in a csv file
n = sum(1 for line in open(filename)) - 1
print(n)
# Reading in the randomized sample into df
skip = sorted(random.sample(range(n),n-s))
df = pd.read_csv(filename,skiprows=skip, header = None)
print(df)
