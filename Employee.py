from Customer1 import Customer
class Employee(Customer):
    def __init__(self,cid,name,phoneNo,address,order,eid,EDiscount):
        super().__init__(cid,name,phoneNo,address,order)
        self.eid = eid
        self.EDiscount = EDiscount
        
    def showEmployee(self):
        return ("Customer ID: {}\nName: {}\nContact No: {}\nAddress: {}\nEmployee ID: {}\nSpecial Discount: {}".format(self.cid, self.name, self.phoneNo,
                                                                                self.address.showAddress(), self.eid, self.EDiscount))
    

        

        