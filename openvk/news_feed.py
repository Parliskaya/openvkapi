from openvkapi import *


class news_feed:

    @staticmethod
    def get(client, offset=0, count=100, extended=0):
        response = http.get(f'https://{client["instance"]}/method/Newsfeed.get?offset={offset}&count={count}&extended={extended}&access_token={client["token"]}')
        return json.loads(response.text)['response']