## STOCK PRICE APP by github.com/tushar2704

# Importing required libraries
import streamlit as st
import yfinance as yf
import pandas as pd

# Header
st.title("💹👔Stock Price Application💹👔")
st.markdown("Shown are the stock closing price and volume of Google!")

# Defining the ticker symbol, for google =>"GOOGL"
tickerSymbol="GOOGL"
# Getting the data from ticker
tickerData = yf.Ticker(tickerSymbol)
# Getting the historical prices for this ticker

tickerDF = tickerData.history(period='1wk', start='2010-3-31', end='2023-03-31')
# Opening High Low Colse Volume Dividends Stock Splits


st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Volume)


## done and dusted!
## Follow me on github.com/tushar2704