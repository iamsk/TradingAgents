import subprocess
import time
from datetime import datetime, timedelta, timezone

from mdb import client

table = client.private.tradingview.最活跃

beijing = timezone(timedelta(hours=8))
today = datetime.now(beijing)
yesterday = today + timedelta(days=-1)
yesterday_str = yesterday.strftime('%Y-%m-%d')

if __name__ == '__main__':
    records = table.find({'agg_date': yesterday_str})
    # stocks = ['NVDA', 'BABA']
    stocks = [record['ticker'] for record in records[:10]]
    for stock in stocks:
        print(f"{time.time()}: {stock}")
        subprocess.run(
            ["/data/www/TradingAgents/.venv/bin/python",
             "/data/www/TradingAgents/one.py",
             stock])
