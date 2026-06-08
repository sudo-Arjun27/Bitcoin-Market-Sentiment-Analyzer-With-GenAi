# Sentiment-Driven Crypto Trader With GenAi Implementation

> **AI-Powered Analysis of Trader Performance Under Market Fear & Greed Conditions**

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Gemini](https://img.shields.io/badge/Google-Gemini-green)
![Data Analytics](https://img.shields.io/badge/Data-Analytics-orange)

---

## Project Overview

Financial markets are heavily influenced by investor psychology. Fear and Greed often drive trading behavior, affecting profitability, risk-taking, and market participation.

This project analyzes historical trading activity from Hyperliquid alongside the Bitcoin Fear & Greed Index to uncover how market sentiment impacts trader performance.

To enhance traditional analytics, the project integrates Google's Gemini LLM, transforming raw statistics into professional market intelligence reports and actionable trading insights.

---

## Objectives

* Analyze trader performance under different market sentiments.
* Compare profitability during Fear, Greed, Neutral, and Extreme market conditions.
* Measure trader win rates across sentiment categories.
* Identify top-performing traders.
* Generate AI-powered market analysis reports.
* Enable natural language interaction with trading data.

---

##  Datasets Used

### 1️. Bitcoin Fear & Greed Index

**Features:**

* Date
* Fear & Greed Value
* Classification

  * Extreme Fear
  * Fear
  * Neutral
  * Greed
  * Extreme Greed

### 2. Hyperliquid Historical Trader Data

**Features:**

* Account
* Coin
* Execution Price
* Trade Size
* Trade Direction
* Timestamp
* Closed PnL
* Position Information

---

## Features

### Interactive Analytics Dashboard

Built using Streamlit with:

* Market Sentiment Distribution
* Trading Activity Trends
* Top Performing Traders
* Profitability Analysis
* Win Rate Analysis
* Trading Volume Analysis

---

### AI Market Analyst

Uses Gemini LLM to generate:

* Executive Summary
* Key Findings
* Sentiment Impact Analysis
* Risk Assessment
* Trading Recommendations
* Strategic Conclusions

---

### Ask The Dataset

Users can ask questions such as:

* Which sentiment generated the highest profits?
* What market condition had the best win rate?
* Which traders performed best?
* What risks are visible in the data?

The AI responds using statistics extracted from the dataset.

---

### PDF Report Export

Generate a professional market intelligence report and export it as PDF containing:

* Generated Timestamp
* Dataset Statistics
* AI Analysis
* Trading Recommendations

---

## Dashboard Preview

### Overview

* Total Trades
* Unique Traders
* Total PnL

### Market Sentiment Analysis

* Sentiment Distribution
* Trading Activity Trends

### Trader Performance

* Top Traders
* Average PnL by Sentiment
* Win Rate Analysis

### AI Insights

* Market Intelligence Reports
* Trading Recommendations

---

## Technology Stack

| Component            | Technology       |
| -------------------- | ---------------- |
| Dashboard            | Streamlit        |
| Data Processing      | Pandas           |
| Visualization        | Plotly           |
| Generative AI        | Gemini 2.5 Flash |
| PDF Generation       | ReportLab        |
| Programming Language | Python           |

---

## Sample Questions for AI Analyst

```text
Which sentiment generated the highest profits?

What market condition had the best win rate?

What trading behavior appears most profitable?

Which sentiment appears riskiest for traders?

Summarize the market in one paragraph.
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/crypto-trader-intelligence.git

cd crypto-trader-intelligence
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run crypto_sentiment_analysis_genai.py
```

---

## Project Structure

```text
crypto-trader-intelligence/
│
├── crypto_sentiment_analysis_genai.py
├── fear_greed_index(1).csv
├── historical_data(2).csv
├── requirements.txt
├── README.md
│
└── reports/
    └── AI_Market_Analysis_Report.pdf
```

---

## Key Insights Generated

The system automatically discovers:

* Most profitable market sentiment
* Best performing trader groups
* Sentiment impact on win rates
* Trading activity trends
* Market risk indicators

---

## Why This Project?

This project demonstrates skills across multiple domains:

### Data Analytics

* Data Cleaning
* Exploratory Data Analysis
* KPI Generation
* Statistical Analysis

### Data Visualization

* Interactive Dashboards
* Business Intelligence Reporting

### Generative AI

* Prompt Engineering
* LLM Integration
* AI-Powered Insights

### Software Development

* Streamlit Application Development
* Report Automation
* User Experience Design

---

## Future Improvements

* Sentiment-Based Trade Prediction
* Risk Scoring Engine
* Real-Time Market Data Integration
* Portfolio Optimization
* Automated Strategy Generation
* Multi-LLM Support

---

## Author

### Arjun Sharma

🎓 B.Tech Data Science Student

🏆 National-Level Hackathon Winner

💡 Interests:

* Data Analytics
* Machine Learning
* Generative AI
* Quantitative Finance
* IoT Systems

### Connect With Me

* LinkedIn: https://www.linkedin.com/in/arjun-sharma7749/
* GitHub: https://github.com/sudo-Arjun27

---

## ⭐ Support

If you found this project useful, please consider giving it a star.

**Built with Python, Streamlit, Gemini AI, and a passion for Data Science 🚀**
