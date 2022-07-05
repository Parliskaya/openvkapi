from .openvkapi import *


class groups:

    def __init__(self):
        self.client = None
        self.response = None

    def get(self, client, user_id):
        self.client = client
        self.response = http.get(f'https://openvk.su/method/Groups.get?user_id={user_id}&access_token={self.client}')
        return json.loads(self.response.text)['response']