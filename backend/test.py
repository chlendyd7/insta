import requests
from requests import utils
from urllib.parse import unquote
api_key = "/OuacqJ8UUETaMvmR/YU8n3Ne4K3K6vhGBT1oq/xTmKOUoM44X6O5gc56//14W+AZFaXfM7ldALKcGvL8zWLEg=="

# url = 'http://www.culture.go.kr/openapi/rest/publicperformancedisplays/period'
# paramss ={'serviceKey' : api_key, 'keyword' : '', 'sortStdr' : '1', 'ComMsgHeader' : '', 'RequestTime' : '20100810:23003422', 'CallBackURI' : '', 'MsgBody' : '', 'from' : '20100101', 'to' : '20101201', 'cPage' : '1', 'rows' : '10', 'place' : '1', 'gpsxfrom' : '129.101', 'gpsyfrom' : '35.142', 'gpsxto' : '129.101', 'gpsyto' : '35.142' }

# response = requests.request('GET', url, params=paramss)
# print(response.content)

# import requests
# api_key = "/OuacqJ8UUETaMvmR/YU8n3Ne4K3K6vhGBT1oq/xTmKOUoM44X6O5gc56//14W+AZFaXfM7ldALKcGvL8zWLEg=="

# url = 'http://apis.data.go.kr/6260000/BusanBIMS/busStopList'
# paramss ={'serviceKey':api_key, 'pageNo' : '1', 'numOfRows' : '10', 'bstopnm' : '부산시청', 'arsno' : '13708' }

# response = requests.request('GET', url, params=paramss)
# print(response.content)


# Python3 샘플 코드 #

import requests

url = 'http://apis.data.go.kr/6260000/BusanCultureExhibitService/getBusanCultureExhibit'
params ={'serviceKey' : api_key, 'pageNo' : '1', 'numOfRows' : '10' }

response = requests.get(url, params=params)
print(response.content['pay_at'])
