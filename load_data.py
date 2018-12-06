from urllib.request import urlopen
from urllib.parse import urlencode

def load_data(key, filepath="data.json"):
  params = {
    'key': key,
    'short_desc' : "TURKEYS, YOUNG, SLAUGHTER, FI - SLAUGHTERED, MEASURED IN HEAD",
    'year__GE' : '1989',
    'year__LE' : '2018',
    'state_alpha' : 'VA',
    'freq_desc' : 'MONTHLY', 
  }
  url = "http://quickstats.nass.usda.gov/api/api_GET/?" + urlencode(params)
  with urlopen(url) as x:
    data = x.read()
  with open(filepath, 'wb') as f:
    f.write(data)
  
