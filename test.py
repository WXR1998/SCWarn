import os
import pandas as pd
import datetime

raw_path = os.path.join('data', 'mlops_data', 'sample.csv')
output_path = os.path.join('data', 'mlops_data')

def split_raw():
    df = pd.read_csv(raw_path)
    piv = int(0.875 *len(df))
    df['timestamp'] = df['timestamp'].apply(lambda d: datetime.datetime.fromtimestamp(d))
    piv_time = df.iloc[piv]['timestamp']
    before_change_df = df[df['timestamp'] < piv_time - datetime.timedelta(hours=3)]
    after_change_df = df[df['timestamp'] >= piv_time]

    before_change_df.to_csv(os.path.join(output_path, 'normal.csv'), index=False)
    after_change_df.to_csv(os.path.join(output_path, 'abnormal.csv'), index=False)

if __name__ == '__main__':
    split_raw()