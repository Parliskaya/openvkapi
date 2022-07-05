from .openvkapi import *


class utils:

    @staticmethod
    def get_server_time(client):
        response = http.get(f'https://openvk.su/method/Utils.getServerTime?access_token={client}')
        return json.loads(response.text)['response']