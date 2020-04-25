from matplotlib import pylab as plt
import pandas as pd

air= pd.read_csv("AIR.csv")
boe= pd.read_csv("BA.csv")

air["Date"] = pd.to_datetime(air.Date)
boe["Date"] = pd.to_datetime(boe.Date)

plt.plot(air["Date"], air["Close"], label="Airbus")
plt.plot(boe["Date"], boe["Close"], label="Boeing")

plt.legend("")
plt.title("Boeing vs. Airbus Stock Price")
plt.ylabel("Stock Price in USD")
plt.xlabel("Time")
plt.legend(loc="upper left")
plt.show()