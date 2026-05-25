import numpy as np
import pandas as pd
import cv2
from PIL import Image
import matplotlib.colors
import matplotlib.pyplot as plt
from japanmap import *

df = pd.read_csv("pref202604.csv")
df = df.iloc[:53,:8]

num_dict={}

for k,n in zip(df["運輸支局"], df["乗用車"]):
    if k in ["札幌", "函館", "旭川", "室蘭", "釧路", "帯広", "北見"]:
        tmp=1
    else:
        tmp = pref_code(k)
    tmp = pref_names[tmp]
    #print(k,tmp)
    if tmp not in num_dict:
        num_dict[tmp] = n
    else:
        num_dict[tmp] += n

n_min = min(num_dict.values())
n_max = max(num_dict.values())

# print(n_min)
# print(n_max)

cmap = plt.cm.rainbow
norm = matplotlib.colors.Normalize(vmin=n_min, vmax=n_max)

def color_scale(r):
    tmp = cmap(norm(r))
    return (tmp[0]*255, tmp[1]*255, tmp[2]*255)

for k,v in num_dict.items():
    num_dict[k] = color_scale(v)

plt.figure(figsize=(10,8))
plt.imshow(picture(num_dict))

sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
plt.colorbar(sm)
plt.show()
