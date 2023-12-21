#This is mary's simple code that has made me to understand dictionaries, list and a little of For loop, and print
import requests

url = 'https://informed-data-challenge.netlify.app/api/breweries'

response = requests.get(url)
payload = response.json()
new_pay = payload.get('data')
#print(new_pay[0].items())
new_payload = []
#print(len(new_pay))
for i in range(len(new_pay)):
  #print(i)
  for key, values in new_pay.items():
    print(i, key + ' : ' + values)