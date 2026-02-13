# 🇮🇳 Indian Market Data Gateway (NSE/BSE)

A Python-based **Indian stock market data gateway** designed to fetch live Last Traded Prices (LTP) from NSE/BSE using broker APIs (example: Dhan API).

This project marks the transition from global crypto markets to **regulated Indian equity markets** for systematic and quantitative trading research.

---

## 🎯 Project Objective

To build a reliable gateway that can:

- Connect to Indian broker APIs
- Authenticate using API tokens
- Fetch real-time stock prices
- Serve as the data layer for systematic trading systems

---

## 🚀 What This Project Does

- Connects to the Dhan market data API
- Authenticates via access token
- Fetches Last Traded Price (LTP)
- Supports NSE/BSE exchanges
- Streams live stock prices in intervals
- Prepares infra for Indian quant trading

---

## 🧠 Why This Matters

Unlike crypto:

- Indian markets are regulated
- Require broker authentication
- Use security IDs instead of symbols
- Have fixed trading hours

This gateway handles those constraints.

---

## 🛠️ Tech Stack

- Python 3.8+
- Requests
- REST APIs
- Broker authentication (token-based)

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/PranavVetkar/NSE-Data-Gateway.git
cd NSE-Data-Gateway
