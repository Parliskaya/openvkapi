from openvkapi import *


class account:

    @staticmethod
    def get_profile(client):
        response = http.get(f'https://{client["instance"]}/method/Account.getProfileInfo?access_token={client["token"]}')
        return json.loads(response.text)

    @staticmethod
    def get_info(client):
        response = http.get(f'https://{client["instance"]}/method/Account.getInfo?access_token={client["token"]}')
        return json.loads(response.text)

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
        response = http.get(f'https://{client["instance"]}/method/Account.getAppPermissions?access_token={client["token"]}')
        return json.loads(response.text)

    @staticmethod
    def get_counters(client):
        response = http.get(f'https://{client["instance"]}/method/Account.getCounters?access_token={client["token"]}')
        return json.loads(response.text)
