import requests

url='https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'

try:
    response=requests.request('get',url)
    # print(response)
    response.raise_for_status()
except:
    print('網路有問題')
else:
    if response.status_code==200:
        print("下載UBike 資料成功")

