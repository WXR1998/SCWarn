import os
import pandas as pd
import numpy as np

from util import plot

result_df = pd.read_csv('result/sample.csv')
scores = [list(result_df[_]) for _ in result_df.columns[1:]]
methods = list(result_df.columns[1:])
xdate = result_df[result_df.columns[0]]

data_df = pd.read_csv('data/sample/abnormal.csv')

if __name__ == '__main__':
    plot.plot_data(np.array(data_df[data_df.columns[1:]]), 'sample', scores, methods, data_df.columns[1:], xdate)