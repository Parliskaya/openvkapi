from openvkapi import *


class wall:

    @staticmethod
    def get(client, user_id: int, offset=0, count=100, extended=0):
        return http.get(f'https://{client["instance"]}/method/Wall.get?owner_id={user_id}&offset={offset}&count={count}&extended={extended}&access_token={client["token"]}').json()

    @staticmethod
    def get_post(client, post_id: int, fields='', extended=0):
        return http.get(f'https://{client["instance"]}/method/Wall.getById?posts={post_id}&fields={fields}&extended={extended}&access_token={client["token"]}').json()

    @staticmethod
    def post(client, user_id: int, message: str, from_group=0, signed=0):
        return http.get(f'https://{client["instance"]}/method/Wall.post?message={message}&owner_id={user_id}&from_group={from_group}&signed={signed}&access_token={client["token"]}').json()

    @staticmethod
    def repost(client, link: str, message: str):
        return http.get(f'https://{client["instance"]}/method/Wall.repost?object={link}&message={message}&access_token={client["token"]}').json()
