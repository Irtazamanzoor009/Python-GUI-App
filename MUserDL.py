from SignUpBL import SignUp_BL
import os
class MUser_DL:
    userlist = []
    
    @staticmethod
    def AddInList(user):
        MUser_DL.userlist.append(user)
        
    @staticmethod
    def ViewList():
        print("Name  Password  Role")
        for user in MUser_DL.userlist:
            print(user.GetUsername() , " " , user.GetPassword() , " " , user.GetRole())
    
    @staticmethod
    def GetRole(user):
        role = None
        for u in MUser_DL.userlist:
            if(u.GetUsername() == user.GetUsername() and u.GetPassword() == user.GetPassword()):
                role = u.GetRole()
        return role
    
    @staticmethod
    def CheckUser(user):
        flag = False
        for u in MUser_DL.userlist:
            if(u.GetUsername() == user.GetUsername() and u.GetPassword() == user.GetPassword()):
                flag = True
                break
        return flag
    
    @staticmethod
    def StoreUserInFile(path):
        with open(path , "w") as file:
            for u in MUser_DL.userlist:
                file.write(u.GetUsername() + ',' + u.GetPassword() + ',' + u.GetRole() + '\n')
    
    @staticmethod
    def ReadUserFromFile(path1):
        if os.path.exists(path1):
            with open(path1, "r") as file:
                for u in file:
                    splittedrecord = u.strip().split(',')
                    name = splittedrecord[0]
                    password = splittedrecord[1]
                    role = splittedrecord[2]
                    user = SignUp_BL(name, password, role)
                    MUser_DL.AddInList(user)
                return True
        else:
            return False