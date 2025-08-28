import subprocess
import time
from datetime import date, timedelta

from mdb import client

table = client.private.tradingview.最活跃

today = date.today()
yesterday = today + timedelta(days=-1)
yesterday_str = today.strftime('%Y-%m-%d')

if __name__ == '__main__':
    records = table.find_one({'agg_date': yesterday_str})
    # stocks = ['NVDA', 'BABA']
    stocks = [record['ticker'] for record in records[:10]]
    for stock in stocks:
        print(f"{time.time()}: {stock}")
        subprocess.run(
            ["/data/www/TradingAgents/.venv/bin/python",
             "/data/www/TradingAgents/one.py",
             stock])
