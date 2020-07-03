import requests
bitcoin_api_url = 'https://api.coindesk.com/v1/bpi/currentprice/huf.json'
while True:
  input('Nyomj Entert új információkhoz')
  valasz = requests.get(bitcoin_api_url)
  json_valasz = valasz.json()
  arfolyam = json_valasz['bpi']['HUF']['rate_float']
  print(f'A bitcion értéke Forintban:  {arfolyam}')
