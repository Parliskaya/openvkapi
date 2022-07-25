from openvkapi import *


class news_feed:

    @staticmethod
    def get(client, offset=0, count=100, extended=0):
        return http.get(f'https://{client["instance"]}/method/Newsfeed.get?offset={offset}&count={count}&extended={extended}&access_token={client["token"]}').json()
