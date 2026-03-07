import yfinance as yf

# 1. Download data for a stable stock (Reliance) and a more volatile one (Zomato)
tickers = ['RELIANCE.NS', 'ADANIENT.NS']
data = yf.download(tickers, period='1y')['Close']

# 2. Calculate Daily Returns
# pct_change() calculates: (Today - Yesterday) / Yesterday
returns = data.pct_change().dropna()

# 3. Calculate Risk (Standard Deviation)
risk = returns.std()

print("Daily Risk Level (Volatility):")
print(risk)

# 1. Define your investment
investment = 100000

# 2. Calculate the "95% Confidence" Risk
# We multiply the risk by 1.65 (a standard math constant for 95% probability)
potential_loss_reliance = investment * (risk['RELIANCE.NS'] * 1.65)
potential_loss_adani = investment * (risk['ADANIENT.NS'] * 1.65)

print(f"--- 1-Day Potential Loss (Worst Case) ---")
print(f"Reliance: ₹{potential_loss_reliance:.2f}")
print(f"Adani: ₹{potential_loss_adani:.2f}")
