from faker import Faker
faker = Faker()
def generate_payload(email=None):
    if email is None:
        email = faker.email()
    
    payload = {
        "name": 'Arnold',
        "email": email,
        "gender": "male",
        "status": "active"
    }
    return payload