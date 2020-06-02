from yfinance import download
import datetime
from pandas import Series
import numpy as np


def get_historical(tickers, period=7):
  period = "{}d".format(period)
  if period == "1d":
    interval = "5m"
  elif period == "7d":
    interval = "1h"
  else:
    interval = "1d"
  data = download(tickers=tickers, period=period, interval=interval)
  return data


def parse_stock_data(data, name='', is_daily=False):
  print(data)
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
        if not out[stock].get('Dates'):
          dates = list(data[col][stock].index.to_pydatetime())
          if is_daily:
            dates = [date.astimezone().strftime("%H:%M") for date in dates]
          else:
            dates = [date.strftime("%m/%d") for date in dates]
          out[stock]['Dates'] = dates
          ind = np.where(np.isnan(data[col][stock]))[0]
          for i in ind[::-1]:
            print(stock)
            out[stock]['Dates'].pop(i)

        values = list(data[col][stock].dropna())
        out[stock][col] = values

    else:
      if data.empty:
        return {}

      if not out[name].get('Dates'):
        dates = list(data[col].index.to_pydatetime())
        if is_daily:
          dates = [date.astimezone().strftime("%H:%M") for date in dates]
        else:
          dates = [date.strftime("%m/%d") for date in dates]
        out[name]['Dates'] = dates
        ind = np.where(np.isnan(data[col]))[0]
        for i in ind[::-1]:
          del dates[i]

      values = list(data[col].dropna())
      out[stocks][col] = values

  return out
