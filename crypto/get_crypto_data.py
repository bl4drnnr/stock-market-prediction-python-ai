'''
WITH USAGE OF BYBIT (https://bybit.com)
'''
from pybit.unified_trading import HTTP
from IPython.display import display

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import time 
import json
import warnings
import os

pd.set_option('expand_frame_repr', False)
pd.options.mode.chained_assignment = None

warnings.simplefilter(action='ignore', category=FutureWarning)

with open('credentials.json', 'r') as file:
    credentials = json.load(file)

key = credentials['api_key']
secret = credentials['api_secret']

session = HTTP(api_key=key, api_secret=secret, testnet=False)


def get_last_timestamp(df):
    return int(df.timestamp[-1:].values[0])


def format_data(response):
    if response['retMsg'] == 'OK':
        data = response.get('result').get('list', None)
    
    if not data:
        return 

    columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume', 'turnover']
    
    data = pd.DataFrame(data,columns=columns)

    data.index = pd.to_datetime(data['timestamp'], unit='ms', utc=True)
    data.index.name = 'timestamp_utc'
    
    return data[::-1].apply(pd.to_numeric)


def get_data(symbol, interval, start, limit, write_data=True):
    try:
        file_path = f'data/crypto/{symbol}.csv'

        df = pd.DataFrame() if not os.path.exists(file_path) else pd.read_csv(file_path, index_col=0, parse_dates=True)
        
        while True:
            # https://bybit-exchange.github.io/docs/v5/market/kline
            response = session.get_kline(
                category='linear', 
                symbol=symbol, 
                start=start,
                interval=interval,
                limit=limit
            )
            
            latest = format_data(response)
            
            if not isinstance(latest, pd.DataFrame):
                break
            
            start = get_last_timestamp(latest)
            
            time.sleep(0.5)
            
            df = pd.concat([df, latest])
            
            print(f'Collecting data from: {dt.datetime.fromtimestamp(start / 1000)}')
            
            if len(latest) == 1: break
        
        df.drop_duplicates(subset=['timestamp'], keep='last', inplace=True)

        if write_data:
            df.to_csv(file_path)
            print(f'File {file_path} has been successfully saved.')

        return df
    except Exception as e:
        print(e)


symbol = 'BTCUSDT'
interval = 'D' # In minutes
limit = 1000
start = int(dt.datetime(2020, 1, 1).timestamp() * 1000)

get_data(symbol, interval, start, limit, write_data=True)

