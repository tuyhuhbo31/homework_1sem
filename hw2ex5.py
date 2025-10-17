import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('BTC_data.csv')

df['time'] = pd.to_datetime(df['time'])

plt.figure(figsize=(12, 8))

plt.plot(df['time'], df['close'], linewidth=1.5)

plt.title('Историческая цена Биткоина от времени', fontsize=16)
plt.xlabel('Дата', fontsize=12)
plt.ylabel('Цена закрытия (USD)', fontsize=12)

plt.show()