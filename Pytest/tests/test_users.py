import pytest
from faker import Faker
from data_payload.generate_paylaod import generate_payload
from endpoints.create_user import CreateUser
from endpoints.get_user import GetUser
from endpoints.delete_user import DeleteUser
from endpoints.update_user import UpdateUser
from conftests import create_user_id

def test_create_user():
    payload = generate_payload()
    
    user = CreateUser() 
    user.create_user(payload)
    user.check_status_code(201)
    user.check_name(payload['name'])

def test_get_user_by_id(create_user_id):
    user = GetUser()
    user.get_user_by_id(create_user_id)
    user.check_status_code(200)  
    user.check_user_id(create_user_id) 
    
def test_delete_user_by_id(create_user_id):
    user = DeleteUser()
    user.delete_user_by_id(create_user_id)
    user.check_status_code(204)
    
    user = GetUser()
    user.get_user_by_id(create_user_id)
    user.check_status_code(404)
    
def test_update_user_by_id(create_user_id):
    name = "Arsen"
    changed_params = {"name": name}
    
    user = UpdateUser()
    user.update_user_by_id(create_user_id, changed_params)
    user.check_status_code(200)
    user.check_name(name)
    
# negative tests
def test_no_required_fields():
    payload = {}
    user = CreateUser()
    user.create_user(payload)
    user.check_status_code(422)
    
@pytest.mark.parametrize("invalid_email", ['test', 'test@', 'testmail.ru', 'test @mail.ru'])    
def test_invalid_email(invalid_email):
    payload = generate_payload(email=invalid_email)
    user = CreateUser()
    user.create_user(payload)
    user.check_status_code(422)
    
# Контракт
def test_email_without_tld_is_allowed():
    faker = Faker()
    email = f"{faker.user_name()}@{faker.domain_word()}"
    
    payload = generate_payload(email=email)
    user = CreateUser()
    user.create_user(payload)
    user.check_status_code(201)
    
def test_existed_email():
    payload = generate_payload()
    
    user = CreateUser()
    user.create_user(payload)
    user.check_status_code(201)
    
    # Тот же email
    user.create_user(payload)
    user.check_status_code(422)
    
def test_non_existed_user():
    user = GetUser()
    user.get_user_by_id(99999999999)
    user.check_status_code(404)    