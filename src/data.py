import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from icecream import ic
import datetime

class Data:
    def __init__(self, tickers):
        self.tickerlist = tickers

    def downloadData(self):
        return yf.download(
            tickers=self.tickerlist,
            period='max',
            interval='1d',
            threads=True
        )

    def vwap(self, df):
        cv = 0
        values = []
        for index, rows in df.iterrows():
            current_date = datetime.datetime.strptime(str(index), '%Y-%m-%d %H:%M:%S').weekday()
            cv += rows['Volume']
            typical_price = (rows['High'] + rows["Low"] + rows["Close"])/3
            numerator = typical_price*rows['Volume']
            if cv == 0:
                values.append(float('NaN'))
            else:
                values.append(numerator/cv)
            if current_date == 4:
                cv = 0

        return values

    def saveData(self):
        mixed = self.downloadData()
        columns = ['Adj Close', 'Close', 'High', 'Low', 'Open', 'Volume']
        for ticker in self.tickerlist:
            data = []
            for c in columns:
                data.append(mixed[(c, ticker)])
            df = pd.DataFrame(data).T
            df.columns = columns
            df.dropna(inplace=True)
            df['Date'] = df.index
            df['VWAP'] = self.vwap(df)
            df.dropna(inplace=True)
            df.to_csv(f"../data/company/{ticker}.csv")

    def getData(self):
        for ticker in self.tickerlist:
            df = pd.read_csv(f"../data/company/{ticker}.csv")
            ic(df)
            break

d = Data( [
          "ADM", "BAYRY", "BG", "SMG"
          "AAPL", "BP", "CVX", 
          "XOM", "EPD", "COP", "EOG", "NRG", "XEL",  # energy companies
          "GNRC", "PPSI", "VST" # electronics

         ])
d.getData()
