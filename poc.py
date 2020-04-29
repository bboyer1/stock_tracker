import yfinance as yf

import matplotlib.pyplot as plt

TICKER = "MSFT"


tick = yf.Ticker(TICKER)

# get stock info
hist = (tick.history("max"))["Open"]

plt.plot(hist)
plt.ylabel("Stock Price")
plt.xlabel("Dates")
plt.title(TICKER)
plt.show()