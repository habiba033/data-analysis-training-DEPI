import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

path = 'train.csv'
def read_file(path):
    df = pd.read_csv(path)
    return df.head()
read_file(path)