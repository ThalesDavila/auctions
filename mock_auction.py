import random
import requests
import time
import string

def ramdom_string():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(12))

def random_int():
    return random.randint(0,3000)

def random_flaot():
    return random.uniform(0, 1)

def generate_bid():
    return {
        "bidderCode": ramdom_string(),
        "width": random_int(),
        "height": random_int(),
        "statusMessage": random.choice(["Bid available", "Bid returned empty or error response"]),
        "adId": ramdom_string(),
        "creative_id": random_int(),
        "cpm": random_flaot(),
        "adUrl": f"https://{ramdom_string()}",
        "requestTimestamp": random_int(),
        "responseTimestamp": random_int(),
        "timeToRespond": random_int(),
        "adUnitCode": ramdom_string(),
        "bidder": ramdom_string(),
        "usesGenericKeys": random.choice([True, False]),
        "size": f"{random_int()}x{random_int()}",
        "adserverTargeting": {
          "hb_bidder": ramdom_string(),
          "hb_adid": ramdom_string(),
          "hb_pb": random_flaot()
        }
    }

if __name__ == "__main__":
    while True:
        requests.post('http://localhost:5000/auction', generate_bid())
        time.sleep(3.0)