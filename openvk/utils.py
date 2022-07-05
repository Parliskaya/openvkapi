from .openvkapi import *


class utils:

    def __init__(self):
        self.client = None
        self.response = None

    def get_server_time(self, client):
        self.client = client
        self.response = http.get(f'https://openvk.su/method/Utils.getServerTime?access_token={self.client}')
        return json.loads(self.response.text)['response']