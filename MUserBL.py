class MUser_BL:
    __Username = "" # making attributes private
    __UserPassword = ""
    
    def __init__(self, username, password):
        self.__Username = username
        self.__UserPassword = password
        
    def GetUsername(self):
        return self.__Username
    
    def GetPassword(self):
        return self.__UserPassword
    
    def GetRole(self):
        return "r"
    
    def SetUserName(self, username):
        self.__Username = username
        
    def SetPassword(self, password):
        self.__UserPassword = password
        