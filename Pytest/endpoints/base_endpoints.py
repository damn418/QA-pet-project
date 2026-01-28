class BaseEndpoints():
    headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer 3b23a2f6ab776d5c0fd099c2939a840ba46fffb9758eaed23e67eafb7bd6339c'
        }
    
    def __init__(self):
        self.response = None
        self.response_json = None
        self.users_url = 'https://gorest.co.in/public/v2/users'
        
    def check_status_code(self, status_code):
        assert self.response is not None, "Response is not set yet!"
        assert self.response.status_code == status_code, f"{self.response}, {self.response_json}"
        
    def check_user_id(self, user_id):
        assert self.response_json is not None, "Response is not set yet!"
        assert self.response_json['id'] == user_id            
        
    def check_name(self, name):
        assert self.response_json is not None, "Response JSON is not set yet!"
        assert self.response_json['name'] == name   