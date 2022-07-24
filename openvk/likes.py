from openvkapi import *


class likes:

    @staticmethod
    def add(client, owner_id, item_id):
        return http.get(f'https://{client["instance"]}/method/Likes.add?type=post&owner_id={owner_id}&item_id={item_id}&access_token={client["token"]}').json()

    @staticmethod
    def delete(client, owner_id, item_id):
        return http.get(f'https://{client["instance"]}/method/Likes.delete?type=post&owner_id={owner_id}&item_id={item_id}&access_token={client["token"]}').json()

    @staticmethod
    def is_liked(client, user_id, owner_id, item_id):
        return http.get(f'https://{client["instance"]}/method/Likes.remove?user_id={user_id}&type=post&owner_id={owner_id}&item_id={item_id}&access_token={client["token"]}').json()
