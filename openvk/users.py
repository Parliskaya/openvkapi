from .openvkapi import *


class users:

    def __init__(self):
        self.client = None
        self.response = None

    def get(self, client, user_id):
        self.client = client
        self.response = http.get(f'https://openvk.su/method/Users.get?user_ids={user_id}&access_token={self.client}')
        return json.loads(self.response.text)['response']

    def get_followers(self, client, user_id):
        self.client = client
        self.response = http.get(f'https://openvk.su/method/Users.getFollowers?user_id={user_id}&access_token={self.client}')
        return json.loads(self.response.text)['response']

    def search(self, client, q):
        self.client = client
        self.response = http.get(f'https://openvk.su/method/Users.search?q={q}&access_token={self.client}')
        return json.loads(self.response.text)['response']