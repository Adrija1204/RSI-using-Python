#RSI
!pip install yfinance pandas matplotlib --quiet

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def calculate_rsi(data, period=14):
    delta = data.diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=period, min_periods=period).mean()
    avg_loss = loss.rolling(window=period, min_periods=period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    return rsi

symbol = "AAPL"
data = yf.download(symbol, period="6mo", interval="1d")
data['RSI'] = calculate_rsi(data['Close'])

# Plot Close price and RSI
plt.figure(figsize=(14,7))

# Plot Close price
plt.subplot(2, 1, 1)
plt.plot(data['Close'], label=f'{symbol} Close Price')
plt.title(f'{symbol} Close Price')
plt.legend()
plt.grid(True)

# Plot RSI
plt.subplot(2, 1, 2)
plt.plot(data['RSI'], label='RSI', color='orange')
plt.axhline(70, color='red', linestyle='--', label='Overbought (70)')
plt.axhline(30, color='green', linestyle='--', label='Oversold (30)')
plt.title('RSI Indicator')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
