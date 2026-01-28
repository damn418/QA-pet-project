import requests
from .base_endpoints import BaseEndpoints

# get_object.py      
class GetUser(BaseEndpoints):
    def get_user_by_id(self, user_id):
        self.response = requests.get(f'{self.users_url}/{user_id}', headers=self.headers)
        self.response_json = self.response.json() 