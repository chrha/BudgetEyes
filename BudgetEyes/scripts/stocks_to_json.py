import json




def parse_file(file, data ):
  model = "budgetapi.stock"
  pk = 1
  f = open(file, 'r')
  f.readline()
  for line in f:
    l = line.split("|")
    name = l[2]
    current_abbrs = [d['fields'].get('abbiev') for d in data]
    current_names = [d['fields'].get('name') for d in data]
    if name in current_names:
      continue
    elif l[1] in current_abbrs:
      continue
    if len(name) > 200:
      name = name[:199]

    tmp = {
      "model":model,
      "pk":pk,
      "fields":{
        "name": name,
        "abbriev": l[1]
      }
    }
    data.append(tmp)
    pk += 1
  
  f.close()



if __name__ == "__main__":
  data = []
  parse_file('nasdaqtraded.txt', data)
  with open('../stocks.json', 'w') as fp:
    json.dump(data, fp)