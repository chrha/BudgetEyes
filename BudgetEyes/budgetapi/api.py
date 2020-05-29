from yfinance import download
import datetime
from pandas import Series
import numpy as np


def get_historical(tickers, period=7):
  period = "{}d".format(period)
  if period == "1d":
    interval = "5m"
  else:
    interval = "1d"
  data = download(tickers=tickers, period=period, interval=interval)
  return data


def parse_stock_data(data, name='', is_daily=False):
  if not isinstance(data.Close, Series):
    stocks = list(data.Close.columns)
    out = {s: {} for s in stocks}
  else:
    stocks = name
    out = {name: {}}
  keys = ["Open", "Close", "High", "Low"]
  for col in keys:
    if isinstance(stocks, list):
      for stock in stocks:
        dates = list(data[col][stock].index.to_pydatetime())

        if is_daily:
          dates = [date.strftime("%H:%M:%S") for date in dates]
        else:
          dates = [date.strftime("%Y-%m-%d") for date in dates]

        ind = np.where(np.isnan(data[col][stock]))[0]
        values = list(data[col][stock].dropna())
        for i in ind[::-1]:
          dates.pop(i)
        var = [[dates[i], values[i]] for i in range(len(dates))] 
        out[stock][col] = var
    else:
      if data.empty:
        return {}
        
      dates = list(data[col].index.to_pydatetime())
      if is_daily:
        dates = [date.strftime("%H:%M:%S") for date in dates]
      else:
        dates = [date.strftime("%Y-%m-%d") for date in dates]
      
      ind = np.where(np.isnan(data[col]))[0]
      for i in ind[::-1]:
        del dates[i]
      values = list(data[col])
      var = [[dates[i], values[i]] for i in range(len(dates))] 
      out[stocks][col] = var
  
  return out