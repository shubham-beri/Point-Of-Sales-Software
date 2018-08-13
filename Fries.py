class Fries:
    def __init__(self,type,price,quant):
        self.type = type
        self.price = price
        self.quant = quant
        
    def show_fries(self):
        f = ["Fries({})".format(self.type),"Rs.{}/- | x {}".format(self.price,self.quant),"Rs.{}/-".format(self.quant*self.price),self.quant*self.price]
        return(f) 