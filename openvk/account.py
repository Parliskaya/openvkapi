from .openvkapi import *


class account:

    @staticmethod
    def get_profile(client):
        response = http.get(f'https://openvk.su/method/Account.getProfileInfo?access_token={client}')
        return json.loads(response.text)['response']

    @staticmethod
    def get_info(client):
        response = http.get(f'https://openvk.su/method/Account.getInfo?access_token={client}')
        return json.loads(response.text)['response']

    @staticmethod
    def set_online(client, status):
        if status == 0:
            return http.get(f'https://openvk.su/method/Account.setOffline?access_token={client}')
        elif status == 1:
            return http.get(f'https://openvk.su/method/Account.setOnline?access_token={client}')
        else:
            pass

    @staticmethod
    def get_permissions(client):
        response = http.get(f'https://openvk.su/method/Account.getAppPermissions?access_token={client}')
        return json.loads(response.text)['response']

    @staticmethod
    def get_counters(client):
        response = http.get(f'https://openvk.su/method/Account.getCounters?access_token={client}')
        return json.loads(response.text)['response']
