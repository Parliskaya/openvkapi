from openvkapi import *


class news_feed:

    @staticmethod
    def get(client):
        response = http.get(f'https://{client["domen"]}/method/Newsfeed.get?access_token={client["token"]}')
        return json.loads(response.text)['response']