import requests


class BlackboardApi:
    def __init__(self):
        self.BASE_URL = 'https://retoolapi.dev'

    def search_user(self, name):
        # for searching user
        query = f'/Nu1Awa/users?userName={name}'
        return self._make_get_request(query)

    def search_course(self, name):
        # for searching course
        query = f'/wxY3hD/courses?name={name}'
        return self._make_get_request(query)

    def _make_get_request(self, query):
        # make request with query
        res = requests.get(self.BASE_URL + query)
        if res.status_code == 200:
            return res.json()

    def make_post_request(self, course_id, user_id, role):
        # add user to course
        endpoint = f'/learn/api/public/v1/courses/{course_id}/users/{user_id}'
        body = {
            "courseRoleId": role
        }
        res = requests.post(self.BASE_URL + endpoint, data=body)
        if res.status_code:
            return res.json()

    def make_delete_request(self, course_id, user_id):
        # remove user from course
        endpoint = f'/learn/api/public/v1/courses/{course_id}/users/{user_id}'

        res = requests.delete(self.BASE_URL + endpoint)
        if res.status_code:
            return res.json()

