from redis import Redis
from json import dumps
import random
import time

def auctions_counter():
    try:
        time.sleep(2.0)
        redis = Redis(host='redis', port=6379)
        counter= redis.llen('auctions')
        return counter
    except Exception as e:
        print(e)
        return 500

def post_auction(bid):
    try:
        redis = Redis(host='redis', port=6379)
        print(bid)
        redis.lpush('auctions', dumps(bid))
        return 201
    except Exception as e:
        print(e)
        return 500