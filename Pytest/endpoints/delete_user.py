import requests
from .base_endpoints import BaseEndpoints

class DeleteUser(BaseEndpoints):
    def delete_user_by_id(self, user_id):
        self.response = requests.delete(f'{self.users_url}/{user_id}', headers=self.headers)
        self.response_json = None