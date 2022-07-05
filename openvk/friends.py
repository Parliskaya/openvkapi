from .openvkapi import *


class friends:

    def __init__(self):
        self.client = None
        self.response = None

    def get(self, client, user_id):
        self.client = client
        self.response = http.get(f'https://openvk.su/method/Friends.get?user_id={user_id}&access_token={self.client}')
        return json.loads(self.response.text)['response']

    def add(self, client, user_id):
        self.client = client
        self.response = http.get(f'https://openvk.su/method/Friends.add?user_id={user_id}&access_token={self.client}')
        return json.loads(self.response.text)['response']

    def remove(self, client, user_id):
        self.client = client
        self.response = http.get(f'https://openvk.su/method/Friends.remove?user_id={user_id}&access_token={self.client}')
        return json.loads(self.response.text)['response']

    def get_list(self, client):
        self.client = client
        self.response = http.get(f'https://openvk.su/method/Friends.getLists?access_token={self.client}')
        return json.loads(self.response.text)['response']
