class Drink:
    def __init__(self,name,price,quant):
        self.name = name
        
        self.price = price
        self.quant = quant
        
    def show_drink(self):

        k = ["{}({})".format(self.name,self.quant),"Rs.{}/- | x {}".format(self.price,self.quant),"Rs.{}/-".format(self.quant*self.price),self.quant*self.price]
        return k
    