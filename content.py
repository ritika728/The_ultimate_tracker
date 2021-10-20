import urllib
import urllib.request
import json                 
from pprint import pprint
import pandas as pd   

url = "https://eonet.sci.gsfc.nasa.gov/api/v2.1/events"
response = urllib.request.urlopen(url)
text = response.read()
json_data = json.loads(text)
df = pd.json_normalize(json_data['events'])
cf=pd.json_normalize(df.geometries[0])
print(cf.coordinates[0])
pf=pd.json_normalize(df.categories[0])
pprint(pf.id)
if pf.id[0]==8:
    print("hello")
