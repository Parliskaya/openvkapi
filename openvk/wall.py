from openvkapi import *


class wall:

    @staticmethod
    def get(client, user_id: int):
        response = http.get(f'https://{client["domen"]}/method/Wall.get?owner_id={user_id}&access_token={client["token"]}')
        return json.loads(response.text)['response']

    @staticmethod
    def get_post(client, post_id: int):
        response = http.get(f'https://{client["domen"]}/method/Wall.getById?posts={post_id}&access_token={client["token"]}')
        return json.loads(response.text)['response']

    @staticmethod
    def post(client, user_id: int, message: str):
        response = http.get(f'https://{client["domen"]}/method/Wall.post?message={message}&owner_id={user_id}&access_token={client["token"]}')
        return json.loads(response.text)['response']