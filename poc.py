import yfinance as yf

import matplotlib.pyplot as plt


msft = yf.Ticker("MSFT")

# get stock info
hist = (msft.history("max"))["Open"]

plt.plot(hist)
plt.show()