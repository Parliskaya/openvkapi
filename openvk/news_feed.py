from .openvkapi import *


class news_feed:

    def __init__(self):
        self.client = None
        self.response = None

    def get(self, client):
        self.client = client
        self.response = http.get(f'https://openvk.su/method/Newsfeed.get?access_token={self.client}')
        return json.loads(self.response.text)['response']