# Using Python to get JSON from http and save as json file
# by seaniwei

import requests
import json
data = requests.get(url="https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=4")
print(data)