import numpy as np
import pandas as pd
import cv2
from PIL import Image
import matplotlib.colors
import matplotlib.pyplot as plt
from japanmap import *

df = pd.read_csv("pref202604.csv")
df = df.iloc[:53,:8]
