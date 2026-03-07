import yfinance as yf
import matplotlib.pyplot as plt

# 1. Pick a mix of Stable and Volatile stocks
tickers = ['RELIANCE.NS', 'ADANIENT.NS', 'TCS.NS', 'INFY.NS', 'HDFCBANK.NS']
print("Fetching market data...")
data = yf.download(tickers, period='1y')['Close']

# 2. Calculate the "Reward" (Total % Growth over 1 year)
# Formula: (Last Price - First Price) / First Price
reward = (data.iloc[-1] - data.iloc[0]) / data.iloc[0]

# 3. Calculate the "Risk" (Daily Volatility / Standard Deviation)
daily_returns = data.pct_change().dropna()
risk = daily_returns.std()

# --- THE VISUALIZATION ---

plt.figure(figsize=(10, 6))

# plt.scatter draws the dots based on (x=Risk, y=Reward)
plt.scatter(risk, reward, color='teal', s=100)

# This loop writes the name of the stock next to its dot
for i, ticker in enumerate(tickers):
    plt.annotate(ticker, (risk[ticker], reward[ticker]),
                 xytext=(8, 5), textcoords='offset points')

# Add professional labels
plt.title("Risk vs. Reward Analysis (1-Year)", fontsize=14, fontweight='bold')
plt.xlabel("Risk (Daily Volatility)", fontsize=12)
plt.ylabel("Reward (Total Return %)", fontsize=12)

# Draw a dotted line at 0% return so we can see who lost money
plt.axhline(0, color='red', linestyle='--', alpha=0.5)

# Save it!
plt.savefig("risk_reward_matrix.png", dpi=300)
print("Success! Saved as 'risk_reward_matrix.png'")

plt.show()
