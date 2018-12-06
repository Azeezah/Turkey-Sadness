import json
from analyze import analyze
from load_data import load_data

if __name__ == '__main__':
  with open('keys.json') as f:
    key = json.loads(f.read())['usda-api-key']
  load_data(key)
  analyze()
  
