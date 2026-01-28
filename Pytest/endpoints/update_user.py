import requests
from .base_endpoints import BaseEndpoints

# update_object.py
class UpdateUser(BaseEndpoints):
    def update_user_by_id(self, user_id, changed_params):
        self.response = requests.patch(f'{self.users_url}/{user_id}', headers=self.headers, json=changed_params)
        self.response_json = self.response.json()