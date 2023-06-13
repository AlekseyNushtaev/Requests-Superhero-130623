import requests
from pprint import pprint

url = 'https://akabab.github.io/superhero-api/api/all.json'

response = requests.get(url)
all_list = response.json()
res_list = []
for hero in all_list:
    if hero['name'] in ['Hulk', 'Captain America', 'Thanos']:
        res_list.append((hero['powerstats']['intelligence'], hero['name']))
res_list.sort()
print(f'Самый умный {res_list[-1][1]}')