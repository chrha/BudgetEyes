from os.path import dirname, abspath
from sys import path

d = dirname(dirname(abspath(__file__))) 
path.append(d)

from api import get_historical, parse_stock_data


def test_parse_single():
  data = get_historical(["MSFT"])
  parsed_data = parse_stock_data(data, "MSFT")
  assert(len(parsed_data.keys()) == 1)
  assert("MSFT" in parsed_data.keys())
  assert(len(parsed_data["MSFT"]) == 5)
  

def test_parse_several():
  data = get_historical(["MSFT", "GOOG"])
  parsed_data = parse_stock_data(data)
  assert(list(parsed_data.keys()) == ["GOOG", "MSFT"])
  for stock in parsed_data:
    assert(len(parsed_data[stock]) == 5)
    assert(list(parsed_data[stock].keys()) == ["Dates", "Open", "Close", "High", "Low"])

    #Check that all lists have the same length:
    lists = parsed_data[stock].values()
    it = iter(lists)
    the_len = len(next(it))
    assert(all(len(l) == the_len for l in it))


if __name__ == "__main__":
  data = get_historical(["GOOG"], period=1)
  parsed_data = parse_stock_data(data, name='GOOG',is_daily=True)
