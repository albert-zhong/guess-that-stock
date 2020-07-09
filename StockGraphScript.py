"""
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
"""

# Import yfinance
import yfinance as yf  
# Get the data for the stock Apple by specifying the stock ticker, start date, and end date
data = yf.download('AAPL','2016-01-01','2018-01-01')
# Plot the close prices
import matplotlib.pyplot as plt
data.Close.plot()
plt.show()
