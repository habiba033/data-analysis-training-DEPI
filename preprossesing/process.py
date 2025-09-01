import pandas as pd
import numpy as np

def chk_types(df):
    """
    this function checks the data types and number of unique values in each column of a DataFrame.
    It returns a DataFrame with the data types and number of unique values for each column.
    parm_1 : df
    return : DataFrame
    """
    dtypes = df.dtypes
    n_unique = df.nunique()
    return pd.DataFrame({"Dtype": dtypes, 'n_unique': n_unique})