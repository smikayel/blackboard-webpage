import requests


class BlackboardApi:
    def __init__(self):
        self.BASE_URL = 'https://retoolapi.dev'

    def search_user(self, name):
        query = f'/Nu1Awa/users?userName={name}'
        return self._make_request(query)

    def search_course(self, name):
        query = f'/wxY3hD/courses?name={name}'
        return self._make_request(query)

    def _make_request(self, query):
        res = requests.get(self.BASE_URL + query)
        if res.status_code == 200:
            return res.json()