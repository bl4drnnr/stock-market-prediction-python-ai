import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from datetime import datetime

import pandas as pd
import numpy as np


def visualize_and_save_crypto_data():
    path = 'data/crypto'
    dir_list = os.listdir(path)

    for file_name in dir_list:
        file_path = f'data/crypto/{file_name}'
        df = pd.read_csv(file_path)

        y = df['open']
        x = [datetime.fromtimestamp(timestamp) for timestamp in (df['timestamp'] / 1000)]
        
        plt.figure(figsize=(12, 6))
        plt.plot(x, y)

        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
        plt.title('Opening Prices Over Time')
        plt.xlabel('Timestamp (UTC)')
        plt.ylabel('Price (USDT)')
        plt.grid(True)

        fig_name = f'{file_name.split(".")[0]}.png'
        plt.savefig(f'visualization/crypto/{fig_name}')
    

visualize_and_save_crypto_data()
