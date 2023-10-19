import random
import csv
import yfinance as yf

data=yf.download('00631L.tw',start='2023-01-01')
print(data)
with open('_00631L.csv','w',newline='',encoding='utf-8') as file:
    csvWriter=csv.writer(file)
    for i in range(50):
        scores=[str(i+1)]
        for _ in range(6):
            scores+= [random.randint(1,100)]
        csvWriter.writerow(scores)
print("程式結束")
        
