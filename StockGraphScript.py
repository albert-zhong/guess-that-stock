import yfinance as yf
import matplotlib.pyplot as plot

stockName = input("stock name (ticker): ")
startDate = input("start date (YYYY-MM-DD): ")
endDate = input("end date (YYYY-MM-DD): ")

ticker = yf.Ticker(stockName)

df = ticker.history(start=startDate, end=endDate)

tittle = stockName + "'s stock price"

df['Close'].plot(title=tittle)

png_name = stockName + ".png"

plot.savefig(png_name)
