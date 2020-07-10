import yfinance as yf
import matplotlib.pyplot as plot
import datetime

# use as a function internally to determine whether or not, the prices have
# increased in the last 2 weeks

stockName = input("stock name (ticker): ")
startDate = input("start date (YYYY-MM-DD): ")
endDate = input("end date (YYYY-MM-DD): ")

d = datetime.timedelta(days=14)
oldEnd = datetime.datetime.strptime(endDate, '%Y-%m-%d')
newEnd = oldEnd + d

ticker = yf.Ticker(stockName)

noPrediction = ticker.history(start=startDate, end=endDate)
postPrediction = ticker.history(start=startDate, end=newEnd)

latestMarketValue = len(postPrediction['Close'])
oldLastMarketVal = len(noPrediction['Close'])

title = stockName + "'s stock price with 2 week addition"

postPrediction['Close'].plot(title=title)
noPrediction['Close'].plot(title=title)

# add this into the hidden {{ data }} param in order to show the final
# graph once user has guessed

# plot.show()

# this comparison should be used to evaluate if the market value after 2 weeks
# is greater than the old value (use this to evaluate whether the user
# response was correct)
if latestMarketValue > oldLastMarketVal:
    print("Greater")
elif latestMarketValue == oldLastMarketVal:
    print("Equals")
else:
    print("Less")

