from openvkapi import *


class utils:

    @staticmethod
    def get_server_time(client):
        return http.get(f'https://{client["instance"]}/method/Utils.getServerTime?access_token={client["token"]}').json()['response']
