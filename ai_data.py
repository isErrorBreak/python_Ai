import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = pd.Series([7,3,5,8],index=['서울','대구','부산','광주'])
print(x)
print(x[['서울', '대구']])
print(x.index)
