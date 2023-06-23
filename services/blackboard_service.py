
import requests

# Use the API instance to make requests to the Blackboard API


class BlackboardApi:
    def __init__(self):
        self.BASE_URL = 'https://teesside-test.blackboard.com'
        self.token = 'wHLkkOXONP0YTcAK08DnG0v0bZt5Sntl'
        self.headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }

    def search_user(self, name):
        # for searching user
        query = f'/learn/api/public/v1/users?userName={name}'
        res = self._make_get_request(query)
        if res:
            return [res['results'][0]]
        return []

    def search_course(self, name):
        # for searching course
        query = f'/learn/api/public/v1/courses?name={name}'
        res = self._make_get_request(query)
        if res:
            return [res['results'][0]]
        return []


    def _make_get_request(self, query):
        # make request with query
        res = requests.get(self.BASE_URL + query, headers=self.headers)
        if res.status_code == 200:
            return res.json()

    def make_post_request(self, course_id, user_id, role):

        # add user to course
        endpoint = f'/learn/api/public/v1/courses/{course_id}/users/{user_id}'
        body = {
            "courseRoleId": role
        }
        res = requests.put(self.BASE_URL + endpoint, headers=self.headers, json=body)
        if res.status_code:
            return res.json()

    def make_delete_request(self, course_id, user_id):
        # remove user from course
        endpoint = f'/learn/api/public/v1/courses/{course_id}/users/{user_id}'

        res = requests.delete(self.BASE_URL + endpoint, headers=self.headers)
        if res.status_code:
            return res.json()