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
  assert(len(parsed_data["MSFT"]) == 4)
  

def test_parse_several():
  data = get_historical(["MSFT", "GOOG"])
  parsed_data = parse_stock_data(data)
  assert(list(parsed_data.keys()) == ["GOOG", "MSFT"])
  for stock in parsed_data:
    assert(len(parsed_data[stock]) == 4)
    assert(list(parsed_data[stock].keys()) == ["Open", "Close", "High", "Low"])
    for key in parsed_data[stock]:
      assert(len(parsed_data[stock][key])==7)
  


if __name__ == "__main__":
  data = get_historical(["APEN", "BUL"], period=1)
  parsed_data = parse_stock_data(data, "APEN", is_daily=True)
  print(parsed_data)
  