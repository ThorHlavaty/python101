#Add items that is a user input
#Ask to what to do next add another, print, remove
#3 functions; remove, add, print
valid = "y"

while valid == "y":

    grocery =''
    grocery_list = [ Milk ]

    grocery_list.append(input("What would you like to add? "))
    print("Cool, your curent list is: ")
    print(grocery_list)

