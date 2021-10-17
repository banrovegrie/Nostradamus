import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from icecream import ic
import datetime

class Data:
    def __init__(self, tickerlist):
        self.tickerlist = tickerlist

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

    def uncertain(self, df):
        values = []
        for index, rows in df.iterrows():
            wick = rows['High'] - rows['Low']
            candle = abs(rows['Open'] - rows['Close'])
            if candle == 0:
                candle = 0.0001
            uncertainty = (wick - candle)/candle
            values.append(uncertainty)
        return values

    def movingAvg(self, df, days):
        return df.iloc[:, 1].rolling(window=days).mean().round(4)

    def saveData(self):
        mixed = self.downloadData()
        columns = ['Adj Close', 'Close', 'High', 'Low', 'Open', 'Volume']
        for ticker in self.tickerlist:
            data = []
            for c in columns:
                data.append(mixed[(c, ticker)])
            df = pd.DataFrame(data).T
            df.columns = columns
            df['MA_5'] = self.movingAvg(df, 5)
            df['MA_50'] = self.movingAvg(df, 50)
            df.loc[df['Open'] == 0] = float('NaN')
            df.dropna(inplace=True)
            df['VWAP'] = self.vwap(df)
            df.dropna(inplace=True)
            df['Uncertainty'] = self.uncertain(df)
            df = df.round(4)
            df.to_csv(f"../data/company/{ticker}.csv")

    def getData(self):
        for ticker in self.tickerlist:
            df = pd.read_csv(f"../data/company/{ticker}.csv")
            ic(df)
            break

food = ["ADM", "BAYRY", "BG", "SMG"]
tech = ["AAPL"]
oilngas = ["BP", "CVX", "XOM"]
energy = ["EPD", "COP", "EOG", "NRG", "XEL"]
elec = ["GNRC", "PPSI", "VST"]
overall = ["SPY", "DIA"]
d = Data(food +
         tech +
         oilngas +
         energy +
         elec + 
         overall)
d.saveData()
