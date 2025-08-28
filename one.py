import os
from datetime import datetime
from unittest.mock import MagicMock

import questionary
import typer

from cli import main, utils
from mdb import table


def run_one(ticker):
    analysis_date = datetime.now().strftime("%Y-%m-%d")
    user_selections = {
        "ticker": ticker,
        "analysis_date": analysis_date,
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
    table.insert_one({'ticker': ticker, 'analysis_date': analysis_date})


if __name__ == '__main__':
    typer.run(run_one)
