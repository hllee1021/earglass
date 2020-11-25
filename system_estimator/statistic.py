import pandas as pd
import numpy as np

def null_count(df):
    total_row = len(df.index)
    col_null = dict()
    for col in df.columns:
        col_null[col] = total_row - df[col].count()
    return col_null

def duplicate_tuple(df):
    total_tuple_num = len(df.index)
    tmp = set()
    for k in range(df.shape[0]):
        tmp.add(tuple(df.iloc[k,:]))
    isol_tuple_num = len(tmp)
    duplicate_rate = 1 - (isol_tuple_num / total_tuple_num)
    return duplicate_rate