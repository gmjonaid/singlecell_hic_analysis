#!/usr/bin/env python

import sys
import pandas as pd 

df = pd.read_table(sys.argv[1], header = 0)
array = []
for i in range(len(df.columns)):
	array.append(df.iloc[i,i])

with open(sys.argv[2], "w") as f:
	for e in array:
		f.write(str(e))
		f.write("\n")
