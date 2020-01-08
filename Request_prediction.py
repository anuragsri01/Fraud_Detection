import requests
import json

url = 'http://127.0.0.1:5000/predict_api'

data = [[14.34, 1.68, 2.7, 25.0, 98.0, 2.8, 1.31, 0.53, 2.7, 13.0, 0.57, 1.96, 660.0, 1.34, 2,45, 1.345, 3.432, 3.456, 8.342, 9.876, 7.736, 6.008, 9.007, 5.892, 4.3240, 5.007, 7.890, 8.091, 7.8]]
j_data = json.dumps(data)
print(j_data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print(r.json())
