from ProductsBL import Products_BL

class Customer_BL(Products_BL):
    __customername = ""
    __IndividualPrice = 0.0
    
    def __init__(self, customername, productname, productquantity, individualPrice):
        super().__init__(productname, productquantity)
        self.__customername = customername
        self.__IndividualPrice = individualPrice
        
    @property
    def GetIndividualPrice(self):
        return self.__IndividualPrice
    
    @GetIndividualPrice.setter
    def SetIndividualPrice(self, value):
        self.__IndividualPrice = value
        
    @property
    def GetCustomerName(self):
        return self.__customername
        