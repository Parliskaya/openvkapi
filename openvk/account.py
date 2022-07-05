from .openvkapi import *


class account:

    def __init__(self):
        self.client = None
        self.response = None

    def get_profile(self, client):
        self.client = client
        self.response = http.get(f'https://openvk.su/method/Account.getProfileInfo?access_token={self.client}')
        return json.loads(self.response.text)['response']

    def get_info(self, client):
        self.client = client
        self.response = http.get(f'https://openvk.su/method/Account.getInfo?access_token={self.client}')
        return json.loads(self.response.text)['response']

    def set_online(self, client, status):
        self.client = client
        if status == 0:
            return http.get(f'https://openvk.su/method/Account.setOffline?access_token={self.client}')
        elif status == 1:
            return http.get(f'https://openvk.su/method/Account.setOnline?access_token={self.client}')
        else:
            pass

    def get_permissions(self, client):
        self.client = client
        self.response = http.get(f'https://openvk.su/method/Account.getAppPermissions?access_token={self.client}')
        return json.loads(self.response.text)['response']

    def get_counters(self, client):
        self.client = client
        self.response = http.get(f'https://openvk.su/method/Account.getCounters?access_token={self.client}')
        return json.loads(self.response.text)['response']
