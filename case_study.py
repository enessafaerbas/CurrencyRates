# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 15:31:22 2023

@author: Enes Safa
"""
from forex_python.converter import CurrencyRates
import datetime
import pandas as pd

currency_rates = CurrencyRates()

days = 1
data_for_10_days = []

for i in range(10):
    date = datetime.date(2021, 1, days)
    currency_data = currency_rates.get_rates("USD", date)
    days += 1
    new_dict = dict()
    new_dict["date"] = date.strftime('%Y-%m-%d')
    new_dict["currency_data"] = currency_data
    data_for_10_days.append(new_dict)

print(data_for_10_days)

dfs = []

for day_data in data_for_10_days:
    date = day_data['date']
    currency_data = day_data['currency_data']
    df = pd.DataFrame(currency_data.items(), columns=['name', 'value'])
    df['date'] = date
    df = df[['date', 'name', 'value']]
    dfs.append(df)

final_df = pd.concat(dfs, ignore_index=True)

# Export to CSV file
final_df.to_csv('currency_data_for_10_days.csv', index=False)