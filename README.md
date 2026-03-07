
# 📈 Indian Equities Performance Tracker
A specialized Python tool designed for the comparative analysis of Indian stocks. This project solves the "Price Bias" problem by normalizing disparate share prices to a common base of 100, allowing for a true percentage growth comparison.

🚀 Key Features
Live Data Pipeline: Connects to Yahoo Finance API to pull 1-year historical data for NSE-listed companies.

Data Normalization: Uses Pandas .iloc logic to reset all stock prices to a base of 100 on Day 1.

Visual Analytics: Generates multi-line charts comparing major market players (Reliance, TCS, Infosys).

Automated Cleaning: Handles missing market data for holidays and weekends using dropna().

🛠️ Technology Stack
Language: Python

Libraries: Pandas (Data Transformation), yfinance (Market API), Matplotlib (Visualization)

🧠 What I Learned
Through this project, I mastered:

Handling real-world time-series data.

The mathematical logic behind Relative Performance Tracking.

How to manage multiple data columns in a single Pandas DataFrame.

## 📊 Result Preview
![Market Comparison Chart](https://github.com/ded-hub/indian-stock-tracker/blob/main/markets_comparison.png)

Author:Suraj Vishwakarma
Focus:Commerce + Data Analytics

