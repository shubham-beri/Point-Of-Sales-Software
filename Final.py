import Customer1 as c
import Address as a
import Employee as e
import Burger as b
import Fries as f
import Drink1 as d
import Order as o
from  tabulate import tabulate

address_e = []
burger_list = []
drink_list = []
fries_list = []
od1 = o.Order(burger_list,fries_list,drink_list)

dict_b = {1:["McAloo",25],2:["McVeggie",35],3:["McChicken",50]}
dict_d = {1:["Coke(Large)",50],2:["Fanta(Large)",50],3:["Sprite(Large)",50],4:["Coke(Small)",30],5:["Fanta(Small)",30],6:["Sprite(Small)",30]}
dict_f = {1:["Fries(Large)",60],2:["Fries(Small)",40]}

def show_bmenu():
    print("This is our Burger's Menu:\n")
    print(tabulate([[1,"McAloo","Rs.25/-"],[2,"McVeggie","Rs.35/-"],[3,"McChicken","Rs.50/-"]],headers=("Code","Burger","MRP"),tablefmt='orgtbl'))
    b_choice = int(input("Enter your selected Burger's code: "))
    b_qty = int(input("How many {}'s do you like to have".format(dict_b[b_choice][0])))
    b1 = b.Burger(dict_b[b_choice][0], dict_b[b_choice][1], b_qty)
    burger_list.append(b1)

def show_dmenu():
    print("This is our Drink's Menu:\n")
    print(tabulate([[1, "Coke(Large)", "Rs.50/-"],[2,"Fanta(Large)","Rs.50/-"],[3, "Sprite(Large)", "Rs.50/-"],[4,"Coke(Small)","Rs.30/-"],[5,"Fanta(Small)","Rs.30/-"],[6,"Sprite(Small)","Rs.30/-"]],
                   headers=("Code", "Drink", "MRP"), tablefmt='orgtbl'))
    d_choice = int(input("Enter your selected Drink's code: "))
    d_qty = int(input("How many {}'s do you like to have".format(dict_d[d_choice][0])))
    d1 = d.Drink(dict_d[d_choice][0], dict_d[d_choice][1], d_qty)
    drink_list.append(d1)

def show_fmenu():
    print("This is our Fries Menu:\n")
    print(tabulate([[1, "Fries(Large)", "Rs.60/-"],[2,"Fries(Small)","Rs.40/-"]],
                   headers=("Code", "Fries", "MRP"), tablefmt='orgtbl'))
    f_choice = int(input("Enter your selected Fries's code: "))
    f_qty = int(input("How many {}'s do you like to have".format(dict_f[f_choice][0])))
    f1 = f.Fries(dict_f[f_choice][0], dict_f[f_choice][1], f_qty)
    fries_list.append(f1)



print("WELCOME TO McDONALDS!!! I 'M LOVIN' IT!!")
cid=14577
name_e = input("Enter your name:\n")
no_e = input("{}, Please enter your contact no:\n".format(name_e))
address_e = input("Enter your address:\n").split(',')
ad1 = a.Address(address_e[0], address_e[1], address_e[1])
eorc = input("Employee(E) or NOT(N):\n")





if eorc == "E" or eorc == "e":
    print("You're eligible for our special 20% employee discount.\n")
    eid = 262155
    e1 = e.Employee(cid,name_e,no_e,ad1,od1,eid,20)
elif eorc == "C":
    c1 = c.Customer(cid,name_e,no_e,ad1,od1)
loop = True
while loop:
    att = int(input("What would you like to have?\nPress 1 for Burgers.\nPress 2 for Drinks\nPress 3 for Fries.\n"))
    if att == 1:
        loop1 = True
        while loop1 :
            show_bmenu()
            print("____________________________________________________")
            more_b = input("Would you like to add more Burgers?(Y/N)")

            while more_b == "Y" or more_b == "y":

                show_bmenu()
                print("____________________________________________________")
                more_b = input("Would you like to add more Burgers?(Y/N)")

            else:
                print("Press 4 to generate bill.")
                loop1 = False
    elif att == 2:
        loop2 = True
        while loop2 :
            show_dmenu()
            print("____________________________________________________")
            more_d = input("Would you like to add more Drinks?(Y/N)")
            while more_d == "Y" or more_d == "y":
                show_dmenu()
                print("____________________________________________________")
                more_d = input("Would you like to add more Drinks?(Y/N)")
            else:
                print("Press 4 to generate bill.")
                loop2 = False

    elif att == 3:
        loop3 = True
        while loop3 :
            show_fmenu()
            print("____________________________________________________")
            more_f = input("Would you like to add more Fries?(Y/N)")
            while more_f == "Y" or more_f == "y":
                show_fmenu()
                print("____________________________________________________")
                more_f = input("Would you like to add more Fries?(Y/N)")
            else:
                print("Press 4 to generate bill.")
                loop3 = False


    elif att == 4:
        break


print(e1.showEmployee())
print(e1.showOrder())
