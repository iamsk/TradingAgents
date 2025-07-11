import os
from datetime import datetime
from unittest.mock import MagicMock

import questionary
import typer
from dotenv import load_dotenv

from cli import main, utils

load_dotenv()


def run_one(ticker):
    user_selections = {
        "ticker": ticker,
        "analysis_date": datetime.now().strftime("%Y-%m-%d"),
        "analysts": [questionary.Choice(display, value=value.value) for display, value in utils.ANALYST_ORDER],
        "research_depth": 5,
        "llm_provider": "openai",
        "backend_url": os.getenv('BACKEND_URL'),
        "shallow_thinker": "gpt-4.1-mini",
        "deep_thinker": "o4-mini",
    }
    # print(user_selections)
    main.get_user_selections = MagicMock(return_value=user_selections)
    main.run_analysis()


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
    typer.run(run_one)
    # run_one('ORCL')
    exit()
    # get_top_stocks()
    stocks = ['NVDA', 'MSFT', 'AAPL', 'AMZN',
              # 'GOOG',
              'META',
              # 'TSLA',
              'WMT',
              # 'ORCL',
              'COIN',
              'CRCL',
              'HOOD']
    for stock in stocks:
        run_one(stock)
