#!/usr/bin/env python
import sys
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import pandas
from matplotlib.patches import Rectangle
import matplotlib.colors
from matplotlib.patches import Rectangle
cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", ["white","red","red","red","red"])

OnTAD_raw = pandas.read_table(sys.argv[1],header=None)
OnTAD_rawa = OnTAD_raw.loc[(OnTAD_raw[2]>0),:].values[:,0:2]-1
HiCmat = pandas.read_table(sys.argv[2], header=None)
HiCmat = HiCmat.values
#sp = 1250
#ep = 1400
testregion = HiCmat
#nf = OnTAD_raw[(OnTAD_raw[0] >= 1250) & (OnTAD_raw[1] <= 1400)]
nff = OnTAD_raw.iloc[:,0:2]
ndf = nff
fig, axs = plt.subplots(1,1,figsize=(10,10))
im = axs.imshow(testregion, cmap=cmap)
fig.colorbar(im,ax=axs)
plt.axis('off')
for i in range(len(ndf)):
  x = ndf.iloc[i,0]
  y = ndf.iloc[i,1]
  z = y-x
  axs.add_patch(Rectangle((x,x), z, z,fill=False,edgecolor='gray',linestyle='dashed',linewidth=1.5))
  
#axs.add_patch(Rectangle((157,157), 42, 42,fill=False,edgecolor='red',linestyle='dashed',linewidth=1.5))
#plt.show()
plt.savefig(sys.argv[3], bbox_inches='tight')

