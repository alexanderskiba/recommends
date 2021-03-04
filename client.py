import requests

import time
start_time = time.time() * 1000
url = f'http://localhost:8080/application/json'
rec_item = "QgybZB43EN"
ph_threshold = 0.8

data = {"recommend_item":"QgybZB43EN", "prob_threshold": 0.8}
response = requests.post(url, json=data)
print(response.text)
print()
print("--- %s milliseconds ---" % (time.time()*1000 - start_time))