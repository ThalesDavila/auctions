from flask import Response

from auctions_queue import auctions_counter


def auctions_event_stream():
    while True:
        msg = auctions_counter()
        yield 'data: {}\n\n'.format(msg)
