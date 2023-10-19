import yfinance as yf

data=yf.download('00631L.tw',start='2023-01-01')
print(data)