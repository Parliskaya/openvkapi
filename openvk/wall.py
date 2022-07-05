from .openvkapi import *


class wall:

    def __init__(self):
        self.client = None
        self.response = None

    def get(self, client, user_id):
        self.client = client
        self.response = http.get(f'https://openvk.su/method/Wall.get?owner_id={user_id}&access_token={self.client}')
        return json.loads(self.response.text)['response']

    def get_post(self, client, post_id: int):
        self.client = client
        self.response = http.get(f'https://openvk.su/method/Wall.getById?posts={post_id}&access_token={self.client}')
        return json.loads(self.response.text)['response']

    def post(self, client, user_id, message: str):
        self.client = client
        self.response = http.get(f'https://openvk.su/method/Wall.post?message={message}&owner_id={user_id}&access_token={self.client}')
        return json.loads(self.response.text)['response']