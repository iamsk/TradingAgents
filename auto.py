import os
from datetime import date

from tradingagents.default_config import DEFAULT_CONFIG
from tradingagents.graph.trading_graph import TradingAgentsGraph


def run_one(ticker):
    config = DEFAULT_CONFIG.copy()
    config["llm_provider"] = "openai"  # Use a different model
    config["backend_url"] = os.getenv('BACKEND_URL')
    config["deep_think_llm"] = "o3-mini"  # Use a different model
    config["quick_think_llm"] = "gpt-4.1-mini"  # Use a different model
    config["max_debate_rounds"] = 1  # Increase debate rounds
    config["online_tools"] = True  # Increase debate rounds

    # Initialize with custom config
    ta = TradingAgentsGraph(debug=True, config=config)

    # forward propagate
    today = date.today()
    today_str = today.strftime('%Y-%m-%d')
    _, decision = ta.propagate(ticker, today_str)
    print(decision)


# Memorize mistakes and reflect
# ta.reflect_and_remember(1000) # parameter is the position returns

def get_top_stocks():
    import requests
    # url = "https://financialmodelingprep.com/api/v3/stock_market/actives?apikey=5Gdm45TzVNf2C2nmgFaSg5KJjvEhP2VC"
    url = "https://financialmodelingprep.com/stable/most-actives?apikey="
    response = requests.get(url)
    print(response.json())


def get_top_stocks2():
    import datetime, requests, pandas as pd
    key = ""
    end = datetime.date.today()
    dates = pd.bdate_range(end=end, periods=1)  # 最近 10 个交易日
    frames = []
    for d in dates:
        url = f"https://api.polygon.io/v2/aggs/grouped/locale/us/market/stocks/{d:%Y-%m-%d}?adjusted=true&apiKey={key}"
        data = requests.get(url).json()
        print(data)
        data = data["results"]
        df = pd.DataFrame(data)[["T", "v", "vw"]]
        df["turnover"] = df["v"] * df["vw"]
        df["date"] = d
        frames.append(df)
    out = pd.concat(frames)
    top = (out.groupby("T")["turnover"]
           .sum()
           .nlargest(20))  # 过去 10 日成交额 Top-20
    print(top)


if __name__ == '__main__':
    # get_top_stocks()
    stocks = ['NVDA', 'MSFT', 'AAPL', 'AMZN', 'GOOG', 'META', 'TSLA', 'WMT', 'ORCL', 'COIN', 'CRCL', 'HOOD']
    for stock in stocks:
        run_one(stock)
