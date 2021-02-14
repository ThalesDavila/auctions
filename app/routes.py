from flask import Flask, Response, request
from auctions_queue import post_auction
from stream import auctions_event_stream
import time
from redis import Redis
from json import dumps

# def auctions_event_stream():
#         while True:
#             msg = auctions_counter()
#             yield 'data: {}\n\n'.format(msg)

# def auctions_counter():
#     try:
#         redis = Redis(host='redis', port=6379)
#         counter= redis.llen('auctions')
#         return counter
#     except Exception as e:
#         print(e)
#         return 500

# def post_auction(bid):
#     try:
#         redis = Redis(host='redis', port=6379)
#         print(bid)
#         redis.lpush('auctions', dumps(bid))
#         return 201
#     except Exception as e:
#         print(e)
#         return 500

app = Flask(__name__)

@app.route('/auction', methods=['POST'])
def auction():
    bid = request.args
    status = post_auction(bid)
    response = Response(status=status)
    return(response)

@app.route('/auctions_counter_stream')
def auctions_counter_stream():
    response = Response(auctions_event_stream(), mimetype="text/event-stream")
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)