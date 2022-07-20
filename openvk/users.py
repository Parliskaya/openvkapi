from .openvkapi import *


class users:

    @staticmethod
    def get(client, user_id):
        response = http.get(f'https://openvk.su/method/Users.get?user_ids={user_id}&access_token={client}')
        return json.loads(response.text)['response']

    @staticmethod
    def get_followers(client, user_id):
        response = http.get(f'https://openvk.su/method/Users.getFollowers?user_id={user_id}&access_token={client}')
        return json.loads(response.text)['response']

    @staticmethod
    def search(client, q):
        response = http.get(f'https://openvk.su/method/Users.search?q={q}&access_token={client}')
        return json.loads(response.text)['response']