from .openvkapi import *


class news_feed:

    @staticmethod
    def get(client):
        response = http.get(f'https://openvk.su/method/Newsfeed.get?access_token={client}')
        return json.loads(response.text)['response']