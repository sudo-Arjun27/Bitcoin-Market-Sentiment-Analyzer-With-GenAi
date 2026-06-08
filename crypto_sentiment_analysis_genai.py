import pandas as pd
import streamlit as st
import plotly.express as px
import google.generativeai as genai

st.set_page_config(page_title="Crypto Sentiment Analysis", layout="wide")

SENTIMENT_FILE = "fear_greed_index.csv"
TRADER_FILE = "historical_data.csv"

st.title("📈 Crypto Trader Performance vs Market Sentiment")
st.caption("Hyperliquid Trader Analysis + AI Market Analyst")

# Load Data
try:
    sentiment_df = pd.read_csv(SENTIMENT_FILE)
    trader_df = pd.read_csv(TRADER_FILE)
except Exception as e:
    st.error(f"Could not load CSV files: {e}")
    st.info("Make sure fear_greed_index.csv and historical_data.csv are in the same folder as this app.")
    st.stop()

sentiment_df.columns = sentiment_df.columns.str.strip()
trader_df.columns = trader_df.columns.str.strip()

# Preprocessing
sentiment_df["Date"] = pd.to_datetime(sentiment_df["date"]).dt.date

trader_df["Date"] = pd.to_datetime(
    trader_df["Timestamp IST"],
    dayfirst=True,
    errors="coerce"
).dt.date

merged_df = pd.merge(
    trader_df,
    sentiment_df[["Date", "classification", "value"]],
    on="Date",
    how="left"
)

merged_df["Closed PnL"] = pd.to_numeric(
    merged_df["Closed PnL"],
    errors="coerce"
).fillna(0)

st.success("Datasets loaded and merged successfully!")

# Overview
st.header("📊 Overview")

total_trades = len(merged_df)
total_traders = merged_df["Account"].nunique()
total_pnl = merged_df["Closed PnL"].sum()

c1, c2, c3 = st.columns(3)
c1.metric("Total Trades", f"{total_trades:,}")
c2.metric("Unique Traders", f"{total_traders:,}")
c3.metric("Total PnL", f"{total_pnl:,.2f}")

# Dataset Preview
with st.expander("View Raw Data"):
    st.dataframe(merged_df.head(100))

# Sentiment Distribution
st.header("Market Sentiment Distribution")

sentiment_counts = merged_df["classification"].value_counts().reset_index()
sentiment_counts.columns = ["Sentiment", "Count"]

fig = px.pie(
    sentiment_counts,
    names="Sentiment",
    values="Count",
    title="Market Sentiment Distribution"
)
st.plotly_chart(fig, use_container_width=True)

# Trading Activity
st.header("📈 Trading Activity")

daily_trades = merged_df.groupby("Date").size().reset_index(name="Trades")

fig = px.line(
    daily_trades,
    x="Date",
    y="Trades",
    title="Trades Per Day"
)
st.plotly_chart(fig, use_container_width=True)

# Top Traders
st.header("🏆 Top Traders")

trader_perf = (
    merged_df.groupby("Account")["Closed PnL"]
    .agg(["sum", "mean", "count"])
    .reset_index()
)

trader_perf.columns = [
    "Trader",
    "Total PnL",
    "Average PnL",
    "Trades"
]

top_traders = trader_perf.sort_values(
    "Total PnL",
    ascending=False
).head(10)

fig = px.bar(
    top_traders,
    x="Trader",
    y="Total PnL",
    title="Top 10 Traders by Profit"
)
st.plotly_chart(fig, use_container_width=True)

# Average PnL by Sentiment
st.header("💰 Profitability vs Sentiment")

avg_pnl_sentiment = (
    merged_df.groupby("classification")["Closed PnL"]
    .mean()
    .reset_index()
)

fig = px.bar(
    avg_pnl_sentiment,
    x="classification",
    y="Closed PnL",
    title="Average PnL by Sentiment"
)
st.plotly_chart(fig, use_container_width=True)


# Win Rate Analysis
st.header("🎯 Win Rate by Sentiment")

merged_df["TradeResult"] = merged_df["Closed PnL"].apply(
    lambda x: "Win" if x > 0 else "Loss"
)

win_rate = (
    merged_df.groupby("classification")["TradeResult"]
    .apply(lambda x: (x == "Win").mean() * 100)
    .reset_index(name="Win Rate (%)")
)

fig = px.bar(
    win_rate,
    x="classification",
    y="Win Rate (%)",
    title="Win Rate by Sentiment"
)
st.plotly_chart(fig, use_container_width=True)

# Trading Volume

st.header("📦 Trading Volume by Sentiment")

volume = (
    merged_df.groupby("classification")
    .size()
    .reset_index(name="Number of Trades")
)

fig = px.bar(
    volume,
    x="classification",
    y="Number of Trades",
    title="Number of Trades by Sentiment"
)
st.plotly_chart(fig, use_container_width=True)

# Key Insights

st.header("📝 Statistical Insights")

best_sentiment = avg_pnl_sentiment.loc[
    avg_pnl_sentiment["Closed PnL"].idxmax(),
    "classification"
]

best_win = win_rate.loc[
    win_rate["Win Rate (%)"].idxmax(),
    "classification"
]

st.write(f"✅ Highest average profitability: **{best_sentiment}**")
st.write(f"✅ Highest win rate: **{best_win}**")
st.write(f"✅ Traders analyzed: **{total_traders:,}**")
st.write(f"✅ Trades analyzed: **{total_trades:,}**")

# GenAI Section

st.header(" AI Market Analyst")

api_key = ""

summary = f"""
Total Traders: {total_traders}
Total Trades: {total_trades}
Total PnL: {total_pnl}

Average PnL by Sentiment:
{avg_pnl_sentiment.to_string(index=False)}

Win Rate by Sentiment:
{win_rate.to_string(index=False)}

Trading Volume by Sentiment:
{volume.to_string(index=False)}

Top Traders:
{top_traders.to_string(index=False)}
"""

if api_key and st.button("Generate AI Report"):
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-2.5-flash")

        prompt = f"""
        You are a professional crypto market analyst.

        Analyze this dataset summary and provide:

        1. Executive Summary
        2. Key Findings
        3. Impact of Fear and Greed on Trader Performance
        4. Risk Analysis
        5. Actionable Trading Recommendations

        Dataset:

        {summary}
        """

        with st.spinner("Generating report..."):
            response = model.generate_content(prompt)

        st.markdown(response.text)

    except Exception as e:
        st.error(f"LLM Error: {e}")

st.header("💬 Ask the Dataset")

question = st.text_input(
    "Ask a question about the trading data"
)

if api_key and question:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-2.5-flash")

        prompt = f"""
        Use ONLY the dataset summary below.

        Dataset:
        {summary}

        User Question:
        {question}
        """

        response = model.generate_content(prompt)

        st.markdown(response.text)

    except Exception as e:
        st.error(f"Chat Error: {e}")
