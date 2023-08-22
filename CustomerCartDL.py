from CustomerBL import Customer_BL
from ProductsDL import Products_DL
class CustomerCart_DL:
    cartlist = []
    
    @staticmethod
    def AddtoCart(products):
        CustomerCart_DL.cartlist.append(products)
        
    @staticmethod
    def ViewCartIndex(product, GetCustomerName):
        index = -1
        for i in range(len(CustomerCart_DL.cartlist)):
            if product == CustomerCart_DL.cartlist[i].GetProductName and GetCustomerName == CustomerCart_DL.cartlist[i].GetCustomerName:
                index = i
                break
        return index
    
    @staticmethod
    def ViewCart(customerName):
        print("Name  Quantity  Price")
        print("----------------------------")
        for c in CustomerCart_DL.cartlist:
            if customerName == c.GetCustomerName:
                print(c.GetProductName , " " , c.GetProductQuantity , " " , c.GetIndividualPrice)
        print("-------------------------------")
        
    @staticmethod
    def Deleteproduct(index):
        CustomerCart_DL.cartlist.pop(index)
        
    @staticmethod
    def deleteproductfromcart(name, username):
        flag = False
        for item in CustomerCart_DL.cartlist:
            #print("Comparing:", name, item.GetProductName, username, item.GetCustomerName)
            if name == item.GetProductName and username == item.GetCustomerName:
                #print("Match found. Removing item:", item)
                CustomerCart_DL.cartlist.remove(item)
                flag = True
                break
        return flag
            
        
    @staticmethod
    def ChangeQuantity(index, newquantity, productprice):
        CustomerCart_DL.cartlist[index].SetProductQuantity = float(newquantity)
        CustomerCart_DL.cartlist[index].SetIndividualPrice = (float(productprice) * float(newquantity))
        
    @staticmethod
    def GetProductName(index):
        return CustomerCart_DL.cartlist[index].GetProductName
    
    @staticmethod 
    def GetTotalBill(getCustomerName):
        totalBill = 0.0
        for c in CustomerCart_DL.cartlist:
            if getCustomerName == c.GetCustomerName:
                totalBill = totalBill + float(c.GetIndividualPrice)
        return totalBill
    
    @staticmethod
    def GetUserIndexes(GetCustomerName):
        indexes = []
        for i in range(len(CustomerCart_DL.cartlist)):
            if GetCustomerName == CustomerCart_DL.cartlist[i].GetCustomerName:
                indexes.append(i)
        return indexes
    
    @staticmethod
    def ClearCart(indexes):
        indexes = sorted(indexes , reverse=True)
        
        for i in indexes:
            del CustomerCart_DL.cartlist[i]
    
    @staticmethod
    def ViewYourFinalCart(customerName):
        print("Name  Quantity  Price")
        print("---------------------------------")
        for c in CustomerCart_DL.cartlist:
            if customerName == c.GetCustomerName:
                print(c.GetProductName , "  " , c.GetProductQuantity , "  " , c.GetIndividualPrice)
                quantity = Products_DL.GetProductquantity(c.GetProductName)
                for p in Products_DL.productsList:
                    if p.GetProductName == c.GetProductName:
                        p.SetProductQuantity = float(quantity) - float(c.GetProductQuantity)
        print("---------------------------------")
    
    @staticmethod
    def StoreCustomerCart(path):
        with open(path , "w") as file:
            for i in CustomerCart_DL.cartlist:
                file.write(str(i.GetCustomerName) + ',' + str(i.GetProductName) + ',' + str(i.GetProductQuantity) + ',' + str(i.GetIndividualPrice) + '\n')
                
    @staticmethod
    def ReadCustomerCart(path):
        with open(path , "r") as file:
            for i in file:
                splittedrecord = i.strip().split(',')
                GetCustomerName = splittedrecord[0]
                productname = splittedrecord[1]
                productquantity = splittedrecord[2]
                individualprice = splittedrecord[3]
                cart = Customer_BL(GetCustomerName , productname , productquantity , individualprice)
                CustomerCart_DL.AddtoCart(cart)
                
                
                