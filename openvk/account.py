from openvkapi import *


class account:

    @staticmethod
    def get_profile(client):
        return http.get(f'https://{client["instance"]}/method/Account.getProfileInfo?access_token={client["token"]}').json()

    @staticmethod
    def get_info(client):
        return http.get(f'https://{client["instance"]}/method/Account.getInfo?access_token={client["token"]}').json()

    @staticmethod
    def set_online(client, status):
        if status == 0:
            return http.get(f'https://{client["instance"]}/method/Account.setOffline?access_token={client["token"]}')
        elif status == 1:
            return http.get(f'https://{client["instance"]}/method/Account.setOnline?access_token={client["token"]}')
        else:
            pass

    @staticmethod
    def get_permissions(client):
        return http.get(f'https://{client["instance"]}/method/Account.getAppPermissions?access_token={client["token"]}').json()

    @staticmethod
    def get_counters(client):
        return http.get(f'https://{client["instance"]}/method/Account.getCounters?access_token={client["token"]}').json()
