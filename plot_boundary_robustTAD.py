#!/usr/bin/env python
import sys
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import pandas as pd

bc = pd.read_csv(sys.argv[1], sep=" ")
t = bc[1250:1400]
c = t['TADscore']
plt.figure(figsize=(16, 6))
plt.plot(c)
plt.savefig(sys.argv[2])