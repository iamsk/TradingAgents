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
        "shallow_thinker": "gpt-5-mini",
        "deep_thinker": "o4-mini-high",
    }
    # print(user_selections)
    main.get_user_selections = MagicMock(return_value=user_selections)
    main.run_analysis()


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
