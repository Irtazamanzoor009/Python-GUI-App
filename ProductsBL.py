class Products_BL:
    __Productname = ""
    __ProductQuantity = 0.0
    
    def __init__(self, productname, productquantity):
        self.__Productname = productname
        self.__ProductQuantity = productquantity
        
    @property
    def GetProductName(self):
        return self.__Productname
    
    @property
    def GetProductQuantity(self):
        return self.__ProductQuantity
    
    @GetProductName.setter
    def SetProductQuantity(self, value):
        if value >= 0.0:
            self.__ProductQuantity = value
            
    @property
    def GetIndividualPrice(self):
        return 1
    
    @property
    def GetCustomerName(self):
        return ""