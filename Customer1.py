class Customer:
    def __init__(self,cid,name,phoneNo,address,order):
        self.cid = cid
        self.name = name
        self.phoneNo = phoneNo
        self.address = address
        self.order = order
    def showCustomer(self):
        return ("Customer ID: {}\nName: {}\nContact No: {}\nAddress: {}".format(self.cid, self.name, self.phoneNo, self.address.showAddress()))

    def showOrder(self):
        print("You ordered:\n")
        return (self.order.show_Order())
        3