import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import datetime as dt

import pandas as pd
import numpy as np


def visualize_single_crypto_asset(asset_name, from_date, save_figure=False):
    file_path = f'data/crypto/{asset_name}'
    df = pd.read_csv(file_path)

    year, month, day = [int(i) for i in from_date.split('-')]
    start = int(dt.datetime(year, month, day).timestamp() * 1000)
    df = df[df['timestamp'] > start]
    
    y = df['open']
    x = [dt.datetime.fromtimestamp(timestamp) for timestamp in (df['timestamp'] / 1000)]
    
    plt.figure(figsize=(12, 6))
    plt.plot(x, y)

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
    plt.title('Opening Prices Over Time')
    plt.xlabel('Timestamp (UTC)')
    plt.ylabel('Price (USDT)')
    plt.grid(True)

    if save_figure:
        fig_name = f'{asset_name.split(".")[0]}.png'
        plt.savefig(f'visualization/crypto/{fig_name}')


def visualize_all_crypto_data(from_date):
    path = 'data/crypto'
    dir_list = os.listdir(path)

    for file_name in dir_list:
        visualize_single_crypto_asset(file_name, from_date, True)


visualize_all_crypto_data('2022-01-01')
# visualize_single_crypto_asset('BTCUSDT', '2024-01-01')
