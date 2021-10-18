import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from icecream import ic
import datetime
import math
import mplfinance as mpf

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

    def sustain(self, tickername):
        ticker = yf.Ticker(tickername)
        return ticker.sustainability

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

    def deviation(self, df):
        subtract = []
        count = 0
        i = 0
        values = []
        for index, rows in df.iterrows():
            s = rows['Close'] - rows['MA_50']
            subtract.append(s**2) # (x - x')^2
            window = min(count + 1, 50)
            numerator = sum(subtract[i:i+window]) # sigma (x - x')^2
            values.append(math.sqrt(numerator/window))
            count += 1
            if count >= 50:
                i += 1
        
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
            df['MA_5'] = self.movingAvg(df, 5)
            df['MA_50'] = self.movingAvg(df, 50)
            df.loc[df['Open'] == 0] = float('NaN')
            df.dropna(inplace=True)
            df['VWAP'] = self.vwap(df)
            df.dropna(inplace=True)
            df['Uncertainty'] = self.uncertain(df)
            df['Deviation'] = self.deviation(df)
            df.replace([np.inf, -np.inf], np.nan)
            df.dropna(inplace=True)
            df = df.round(4)
            s_df = self.sustain(ticker)
            df.to_csv(f"../data/company/stock/{ticker}.csv")
            if s_df is not None:
                s_df.to_csv(f"../data/company/sustain/{ticker}.csv")

    def getData(self):
        data = []
        for ticker in self.tickerlist:
            df = pd.read_csv(f"../data/company/stock/{ticker}.csv")
            try:
                s_df = pd.read_csv(f"../data/company/sustain/{ticker}.csv")
            except:
                s_df = None
            data.append((df, s_df))
        return data

class Handle:
    def __init__(self, d):
        self.data = d.getData()
        self.disasters = self.getDisasters()
        self.tickerlist = d.tickerlist

    def getDisasters(self):
        return pd.read_csv('../data/disasters.csv')

    def nine_eleven(self):
        # 9/11
        start_date = '2001-08-01'
        end_date = '2001-10-31'
        count = 0
        for data in self.data:
            df = data[0]
            s_df = data[1]
            start_location = np.where(df.Date == start_date)
            end_location = np.where(df.Date == end_date)
            dfrange = df.iloc[start_location[0][0]:end_location[0][0]]
            dfrange['Date']= pd.to_datetime(df['Date'])
            dfrange.index = dfrange['Date']
            mpf.plot(dfrange, type='candle', style='yahoo', mav=(5, 10, 20), volume=True, vlines=dict(vlines='2001-09-10', linewidths=20, alpha=0.4))
            count += 1

    def winter_storm(self):
        # texas
        start_date = '2021-01-04'
        end_date = '2021-03-31'
        count = 0
        for data in self.data:
            df = data[0]
            s_df = data[1]
            start_location = np.where(df.Date == start_date)
            end_location = np.where(df.Date == end_date)
            dfrange = df.iloc[start_location[0][0]:end_location[0][0]]
            dfrange['Date']= pd.to_datetime(df['Date'])
            dfrange.index = dfrange['Date']
            mpf.plot(dfrange, type='candle', style='yahoo', mav=(5, 10, 20), volume=True, vlines=dict(vlines='2021-02-12', linewidths=20, alpha=0.4))
            count += 1

    def katrina(self):
        # hurricanes
        start_date = '2005-07-01'
        end_date = '2005-09-30'
        count = 0
        for data in self.data:
            df = data[0]
            s_df = data[1]
            start_location = np.where(df.Date == start_date)
            end_location = np.where(df.Date == end_date)
            dfrange = df.iloc[start_location[0][0]:end_location[0][0]]
            dfrange['Date']= pd.to_datetime(df['Date'])
            dfrange.index = dfrange['Date']
            mpf.plot(dfrange, type='candle', style='yahoo', mav=(5, 10, 20), volume=True, vlines=dict(vlines='2005-08-23', linewidths=20, alpha=0.4))
            count += 1

    def cali(self):
        # wildfires
        start_date = '2017-08-01'
        end_date = '2018-02-28'
        count = 0
        for data in self.data:
            df = data[0]
            s_df = data[1]
            start_location = np.where(df.Date == start_date)
            end_location = np.where(df.Date == end_date)
            dfrange = df.iloc[start_location[0][0]:end_location[0][0]]
            dfrange['Date']= pd.to_datetime(df['Date'])
            dfrange.index = dfrange['Date']
            mpf.plot(dfrange, type='candle', style='yahoo', mav=(5, 10, 20), volume=True, vlines=dict(vlines='2017-10-09', linewidths=20, alpha=0.4))
            count += 1


food = ["ADM", "BAYRY", "BG", "SMG"]
tech = ["AAPL"]
oilngas = ["BP", "CVX", "XOM"]
energy = ["EPD", "COP", "EOG", "NRG", "XEL"]
elec = ["GNRC", "PPSI", "VST"]
overall = ["SPY", "DIA"]

# d = Data(['SPY', 'DIA', 'ALK'])
# d.saveData()
# h = Handle(d)
# h.nine_eleven()

# d = Data(['SPY', 'NRG'])
# d.saveData()
# h = Handle(d)
# h.winter_storm()

# d = Data(['SPY', 'KMX', 'CHRW'])
# d.saveData()
# h = Handle(d)
# h.katrina()

d = Data(['SPY', 'PCG', 'EIX'])
d.saveData()
h = Handle(d)
h.cali()
