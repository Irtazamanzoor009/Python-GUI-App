from MUserBL import MUser_BL

class SignIn_BL(MUser_BL):
    
    def __init__(self,username, password):
        super().__init__(username, password)