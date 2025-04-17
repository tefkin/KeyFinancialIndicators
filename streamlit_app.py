import streamlit as st

st.title("🎈 My new streamlit app for Richard Updated two")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)


import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# Set the time period
end_date = datetime.today()
start_date = end_date - timedelta(days=90)

# Tickers and labels for key financial indicators
tickers = {
    'INDA (India)': 'INDA',
    'VNM (Vietnam)': 'VNM',
    'EWW (Mexico)': 'EWW',
    'VGK (Europe)': 'VGK',
    'IWM (US Small Cap)': 'IWM',
    'XLI (US Industrials)': 'XLI',
    'SMH (Semiconductors)': 'SMH',
    'KBE (US Banks)': 'KBE',
    'EUFN (Europe Banks)': 'EUFN',
    'CPER (Copper)': 'CPER',
    'USO (Oil)': 'USO',
    'DXY (USD Index)': 'DX-Y.NYB',
    'VIX (Volatility Index)': '^VIX'
}

st.title("Trade Recovery Market Dashboard (Ex-China)")
st.markdown("""
Track financial indicators likely to benefit from easing global trade tensions (excluding China).
""")

selected_tickers = st.multiselect("Select indicators to display:", options=list(tickers.keys()), default=list(tickers.keys())[:5])

@st.cache_data
def fetch_data(ticker):
    df = yf.download(ticker, start=start_date, end=end_date)
    df['Return %'] = (df['Close'] / df['Close'].iloc[0] - 1) * 100
    return df[['Close', 'Return %']]

# Display the selected charts
for label in selected_tickers:
    ticker = tickers[label]
    data = fetch_data(ticker)
    st.subheader(label)
    st.line_chart(data['Return %'], use_container_width=True)

st.markdown("---")
st.markdown("Data from Yahoo Finance. Returns are shown relative to the past 90 days.")