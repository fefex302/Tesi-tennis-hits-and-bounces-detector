#script usato per unire due dataset

import csv
import sys
import pandas as pd

if(len(sys.argv) != 4):
    print('run as: "python3 append_csv.py <input1.csv> <input2.csv> <output.csv> "')
    exit(1)

input1 = sys.argv[1]
input2 = sys.argv[2]
output = sys.argv[3]

first = pd.read_csv(input1, header=0)
second = pd.read_csv(input2)
print(first)
first.to_csv(output,index=False)

second.to_csv(output,index=False,header=0, mode='a')

