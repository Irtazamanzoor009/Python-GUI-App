from MUserBL import MUser_BL

class SignUp_BL(MUser_BL):
    __Role = ""
    def __init__(self, username, password, role):
        super().__init__(username, password)
        self.__Role = role
        
    def GetRole(self):
        return self.__Role