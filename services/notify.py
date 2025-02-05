import requests


class Notify:

    def __init__(self):
        self.__base_url = 'http://127.0.0.1:8001/'

    def send_order_event(self, data):
        response = requests.post(
            url=f'{self.__base_url}/ap1/v1/webhooks/order',
            json=data,
        )
