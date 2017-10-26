import requests
import json

#req = requests.get('http://coincap.io/page/ETH')
req = requests.get('https://uploadbeta.com/api/ipcalc/?cached&s=10.8.52.3')
res = req.json()

#parsed = json.loads(req)
#print(res['price_eur'])

print (res)



