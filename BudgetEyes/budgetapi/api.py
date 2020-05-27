from yfinance import download
import datetime
from pandas import Series


def get_historical(tickers, period=7):
  period = "{}d".format(period)
  if period == 1:
    interval = "1m"
  else:
    interval = "1d"
  data = download(tickers=tickers, period=period, interval=interval)
  return data


def parse_stock_data(data, name=''):
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
        dates = [date.strftime("%Y-%m-%d") for date in dates]
        values = list(data[col][stock])
        var = [[dates[i], values[i]] for i in range(len(dates))] 
        out[stock][col] = var
    else:
      dates = list(data[col].index.to_pydatetime())
      dates = [date.strftime("%Y-%m-%d") for date in dates]
      values = list(data[col])
      var = [[dates[i], values[i]] for i in range(len(dates))] 
      out[stocks][col] = var
  return out