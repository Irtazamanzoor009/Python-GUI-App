from ProductsBL import Products_BL

class Manager_BL(Products_BL):
    ProductPrice = 0.0
    
    def __init__(self, productname, productquantity, productprice):
        super().__init__(productname, productquantity)
        self.ProductPrice = productprice
        
    @property
    def GetProductPrice(self):
        return self.ProductPrice
    
    @GetProductPrice.setter
    def SetProductPrice(self, value):
        if value > 0:
            self.ProductPrice = value