from ManagerBL import Manager_BL
class Products_DL:
    productsList = []
    
    @staticmethod
    def AddInProductList(products):
        Products_DL.productsList.append(products)
        
    @staticmethod
    def ViewProducts():
        print("Name  Quantity  Price")
        print("-------------------------")
        for p in Products_DL.productsList:
            print(p.GetProductName , " " , (p.GetProductQuantity) , " " , (p.GetProductPrice))
        print("-------------------------")
        
    @staticmethod
    def DeleteProducts(index):
        Products_DL.productsList.pop(index)
    
    @staticmethod
    def GetProductPrice(productname):
        price = 0.0
        for p in Products_DL.productsList:
            if productname == p.GetProductName:
                price = p.GetProductPrice
        return price
    
    @staticmethod
    def GetProductquantity(productname):
        quantity = 0.0
        for p in Products_DL.productsList:
            if productname == p.GetProductName:
                quantity = p.GetProductQuantity
        return quantity
    
    @staticmethod
    def ViewIndex(product):
        index = -1
        for i in range(len(Products_DL.productsList)):
            if product == Products_DL.productsList[i].GetProductName:
                index = i
                break
        return index
    
    @staticmethod
    def GetProductName(index):
        return Products_DL.productsList[index].GetProductName
            
    @staticmethod
    def ChangeQuantity(index, newquantity):
        Products_DL.productsList[index].SetProductQuantity = newquantity
        
    @staticmethod
    def ChangePrice(index, newprice):
        Products_DL.productsList[index].SetProductPrice = newprice
            
    @staticmethod
    def CheckProduct(product):
        flag = False
        for p in Products_DL.productsList:
            if product == p.GetProductName:
                flag = True                
        return flag
    
    @staticmethod 
    def StoreProductsInfile(path):
        with open(path,"w") as pro:
            for u in Products_DL.productsList:
                pro.write(u.GetProductName + ',' + str(u.GetProductQuantity) + ',' + str(u.GetProductPrice) + '\n')
                
    @staticmethod
    def ReadProductFromFile(path):
        with open(path , "r") as pro:
            for p in pro:
                splittedrecord = p.strip().split(',')
                name = splittedrecord[0]
                quantity = splittedrecord[1]
                price = splittedrecord[2]
                products = Manager_BL(name,quantity,price)
                Products_DL.AddInProductList(products)
                