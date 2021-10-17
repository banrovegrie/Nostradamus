import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from icecream import ic

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
            df.to_csv(f"../data/company/{ticker}.csv")

d = Data( [
          "ADM", "BAYRY", "BG", "SMG"
          "AAPL", "BP", "CVX", 
          "XOM", "EPD", "COP", "EOG", "NRG", "XEL",  # energy companies
          "GNRC", "PPSI", "VST" # electronics

         ])
d.saveData()
