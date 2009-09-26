import core
from django.contrib.auth.models import check_password
from japos.crews.models import *

class Login:
    
    def __init__(self):
        pass
    
    def auth(self, username, password):
        self.username = Cashier.objects.get(user__username = username)
        self.valid = check_password(password, self.username.user.password)
        
        return self.username, self.valid