import pytest

from data_payload.generate_paylaod import generate_payload
from endpoints.create_user import CreateUser
from endpoints.get_user import GetUser
from endpoints.delete_user import DeleteUser
from endpoints.update_user import UpdateUser

@pytest.fixture()
def create_user_id():
    payload = generate_payload()
    
    user = CreateUser()
    user.create_user(payload)
    user.check_status_code(201)
    
    user_id = user.response_json['id']
    yield user_id

    user = GetUser()
    user.get_user_by_id(user_id)
    
    if user.response.status_code == 200:
        user = DeleteUser()
        user.delete_user_by_id(user_id)
        user.check_status_code(204)