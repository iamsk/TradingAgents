import subprocess
import time

if __name__ == '__main__':
    # get_top_stocks()
    stocks = ['NVDA', 'BABA']
    for stock in stocks:
        print(f"{time.time()}: {stock}")
        subprocess.run(
            ["/Users/zhangbin/workspace/TradingAgents/.venv/bin/python",
             "/Users/zhangbin/workspace/TradingAgents/one.py",
             stock])
