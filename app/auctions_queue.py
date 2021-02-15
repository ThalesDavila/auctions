from redis import Redis
from json import dumps
import random
import time


def auctions_counter():
    """Get he number of elements in the auction data queue. Return auction data counter if success else 500""" 
    try:
        time.sleep(1.5)
        redis = Redis(host='redis', port=6379)
        counter = redis.llen('auctions')
        return counter
    except Exception as e:
        print(e)
        return 500


def post_auction(bid):
    """Push new aution data to queue. Return 200 if success else 500"""
    try:
        redis = Redis(host='redis', port=6379)
        redis.lpush('auctions', dumps(bid))
        return 200
    except Exception as e:
        print(e)
        return 500
