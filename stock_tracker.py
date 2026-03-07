import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

print("Fetching data for Reliance,TCS and Infosys...")

# ==========================================
# 1. DATA EXTRACTION (Multi-Ticker)
# ==========================================
# We use a Python list (in brackets) to ask for multiple stocks
tickers = ['RELIANCE.NS', 'TCS.NS', 'INFY.NS']

# Download 1 year of data. We immediately slice just the ['Close'] prices for both.
price_data = yf.download(tickers, period="1y")['Close']

# Drop any days where the market was closed or data is missing
price_data = price_data.dropna()
normalized_data = price_data / price_data.iloc[0] * 100

print("Data fetched! Generating comparison chart...")

# ==========================================
# 2. VISUALIZATION (Plotting Multiple Columns)
# ==========================================
plt.figure(figsize=(12, 6))

# Plot Reliance in Blue
plt.plot(normalized_data.index, normalized_data['RELIANCE.NS'],
         label='Reliance', color='blue', linewidth=2)

# Plot TCS in Green
plt.plot(normalized_data.index, normalized_data['TCS.NS'],
         label='TCS', color='green', linewidth=2)

# Plot Infosys in Red
plt.plot(normalized_data.index, normalized_data['INFY.NS'],
         label='Infosys', color='red', linewidth=2)

# Add titles and labels
plt.title('Reliance vs. TCS vs. Infosys: 1-Year Price Comparison',
          fontsize=14, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Price (INR)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)

# The legend will automatically use the labels we set above
plt.legend(loc='upper left')

# Show the chart
plt.show()
