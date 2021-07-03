import csv
import pandas as pd
import numpy as np
import torch

# load data
data = pd.read_csv("./output/TSLA.csv")

# preprocess
np_data = data[40:].to_numpy()
for i in range(np_data.shape[0]-1):
    np_data[i,0] = np_data[i+1,0] - np_data[i,0]
np_data[-1,0] = 1

# normalize
for i in range(np_data.shape[1]):
    np_data[:,i] = (np_data[:,i] - np.mean(np_data[:,i])) / np.std(np_data[:,i])

print(np_data)




# with open("./output/TSLA_20210601.csv", "w", newline='', encoding='utf8') as tesla:
#     data = csv.reader(tesla)
#     print(data)
#     for row in data:
#         print(row)