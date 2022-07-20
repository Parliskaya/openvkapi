from .openvkapi import *


class groups:

    @staticmethod
    def get(client, user_id):
        response = http.get(f'https://openvk.su/method/Groups.get?user_id={user_id}&access_token={client}')
        return json.loads(response.text)['response']