import requests
import csv
import io

__cities = []


## def __download() -> list[list]:
url = 'https://data.moi.gov.tw/MoiOD/System/DownloadFile.aspx?DATA=CA18EE06-4A50-4861-9D97-7853353D7108'
response = requests.request("GET", url)
print(response.text)
try:
    response.raise_for_status()
except:
    print("連線ERROR")
    raise Exception("連線錯誤", "網路中斷")
else:
    if not response.ok:
        print("下載失敗")
    else:
        print("下載成功")
        file = io.StringIO(response.text)
        csv_reader = csv.reader(file)
        next(csv_reader)
        ## return list[csv_reader]