import os

import pymongo
from dotenv import load_dotenv

load_dotenv()
host = os.getenv('MONGODB_HOST')
port = 3717
client = pymongo.MongoClient(host, port)

table = client.private.tradingagents.records
