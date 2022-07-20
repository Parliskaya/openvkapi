from .openvkapi import *


class friends:

    @staticmethod
    def get(client, user_id):
        response = http.get(f'https://openvk.su/method/Friends.get?user_id={user_id}&access_token={client}')
        return json.loads(response.text)['response']

    @staticmethod
    def add(client, user_id):
        response = http.get(f'https://openvk.su/method/Friends.add?user_id={user_id}&access_token={client}')
        return json.loads(response.text)['response']

    @staticmethod
    def remove(client, user_id):
        response = http.get(f'https://openvk.su/method/Friends.remove?user_id={user_id}&access_token={client}')
        return json.loads(response.text)['response']

    @staticmethod
    def get_list(client):
        response = http.get(f'https://openvk.su/method/Friends.getLists?access_token={client}')
        return json.loads(response.text)['response']
