import requests
from .base_endpoints import BaseEndpoints

# create_user.py
class CreateUser(BaseEndpoints):
    def create_user(self, payload):
        self.response = requests.post(self.users_url, headers=self.headers, json=payload)
        self.response_json = self.response.json()
       