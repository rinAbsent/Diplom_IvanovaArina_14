import data
import configuration
import requests

def create_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=data.order_body)


def get_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_TRACK + "?t=" + str(track))
