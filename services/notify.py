import requests


class Notify:

    def __init__(self):
        self.__base_url = 'https://webhook.site/c6f6155a-1bf0-42a5-ad92-8e958761eb4f'

    def send_event(self, data):
        response = requests.post(
            url=f'{self.__base_url}',
            json=data,
        )
