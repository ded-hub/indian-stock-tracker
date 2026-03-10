import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Page Setup
st.set_page_config(page_title="Risk vs Reward Analyzer",
                   page_icon="⚖️", layout="wide")
st.title("⚖️ Indian Stocks: Risk vs. Reward Analyzer")

# 2. User Input
available_stocks = ['RELIANCE.NS', 'TCS.NS',
                    'HDFCBANK.NS', 'INFY.NS', 'TATAMOTORS.NS', 'ITC.NS']
selected_tickers = st.multiselect("Select Stocks to Compare:", available_stocks, default=[
                                  'RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS'])

# 3. The Engine
if selected_tickers:
    with st.spinner("Crunching the market data..."):
        # Download data
        raw_data = yf.download(selected_tickers, period="1y")

        if 'Close' in raw_data:
            data = raw_data['Close']
        else:
            data = raw_data

        if isinstance(data, pd.Series):
            data = data.to_frame(name=selected_tickers[0])

        # Calculate Risk & Reward
        daily_returns = data.pct_change().dropna()
        reward = daily_returns.mean() * 252 * 100
        risk = daily_returns.std() * np.sqrt(252) * 100

        # 4. The Dashboard Metrics
        st.subheader("📊 Quick Stats")
        cols = st.columns(len(selected_tickers))
        for i, ticker in enumerate(selected_tickers):
            with cols[i]:
                latest_price = data[ticker].iloc[-1]
                t_reward = reward[ticker]
                st.metric(label=f"{ticker} (Latest Price)", value=f"₹{latest_price:.2f}",
                          delta=f"Annual Return: {t_reward:.1f}%")
        st.divider()

        # 5. Drawing the Chart
        st.subheader("The Efficient Frontier")
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.scatter(risk.values, reward.values, color='#00a699',
                   s=150, alpha=0.7, edgecolors='black')

        for i, txt in enumerate(risk.index):
            ax.annotate(txt, (risk.iloc[i], reward.iloc[i]), xytext=(
                8, 5), textcoords='offset points', fontsize=10, fontweight='bold')

        ax.set_title("Risk vs. Reward (1 Year)",
                     fontsize=14, fontweight='bold')
        ax.set_xlabel("Risk (Annualized Volatility %)", fontsize=12)
        ax.set_ylabel("Reward (Annualized Return %)", fontsize=12)
        ax.grid(True, linestyle='--', alpha=0.5)
        st.pyplot(fig)

        # ---------------------------------------------------------
        # 6. NEW: THE CSV DOWNLOAD EXPORT
        # ---------------------------------------------------------
        st.subheader("📁 Export Your Data")

        # We package your math into a clean Pandas DataFrame
        summary_data = pd.DataFrame({
            'Annual Return (%)': reward.round(2),
            'Annual Risk (%)': risk.round(2)
        })

        # We convert that Pandas DataFrame into a raw CSV format
        csv_file = summary_data.to_csv().encode('utf-8')

        # We create a download button for the user
        st.download_button(
            label="📥 Download Summary as CSV",
            data=csv_file,
            file_name="risk_reward_summary.csv",
            mime="text/csv",
        )

else:
    st.warning(
        "Please select at least one stock from the dropdown menu to see the magic.")
