from tabulate import tabulate

class Order:
    def __init__(self, burger, fries, drink):
        self.burger = burger
        self.fries = fries
        self.drink = drink
    
    def show_Order(self):
        k = []
        cost = 0
        for a in range(len(self.burger)):
            at = self.burger[a].show_burger() 
            cost += at[3]
            del at[3]
        
            k.append(at)

        for a in range(len(self.fries)):
            bt = self.fries[a].show_fries()
            cost += bt[3]
            del bt[3]
        
        
            k.append(bt)
        for a in range(len(self.drink)):  
            ct = self.drink[a].show_drink()
            cost += ct[3]
            del ct[3]
            
            k.append(ct)
        
        print (tabulate(k,headers=["Item", "Price   | Qty","Net Price"],tablefmt='orgtbl'))
        return("_________________________________________________\nSum ----------- : Rs.{}/-\nBill(Inc. taxes): Rs.{}/-".format(cost,((0.05*cost)+cost)))
        
    