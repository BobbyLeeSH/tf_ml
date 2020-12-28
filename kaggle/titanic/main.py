# Let's get started with my very first kaggle competition
import numpy as np
import tensorflow as tf
import pandas as pd

train = pd.read_csv("train.csv")
print(train.columns)
print(train.head())

print(train.corr())
