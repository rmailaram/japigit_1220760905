import sys
import pandas as pd
from alpha_vantage.timeseries import TimeSeries

API_KEY = 'CQWWYJ56RP4I1G2E'
outFile = open('japi.out', 'w')

def getStockdata(symbol):
    try:
        print("Getting stock price....")
        timeSeries = TimeSeries(key=API_KEY, output_format='pandas')
        data, meta_data = timeSeries.get_intraday(symbol=symbol, interval='1min')
        return str(data.tail(1).iloc[0]['4. close'])
    except:
        return "not found"

userInput = input("Enter Stock Symbol or EXIT to exit: ").upper()
stockData = getStockdata(userInput)
response = 'The current price of '+userInput+' is '+stockData
print(response)
outFile.write(response)

print("“Stock Quotes retrieved successfully!”")