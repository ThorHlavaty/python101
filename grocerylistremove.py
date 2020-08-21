user_input = ""
grocery_list = []
commands = ["add", "remove", "print", "exit"]
valid = "y"

def want_another():
    validadd = "y"
    while validadd == "y":
        grocery = input("What would you like to add to your list? ")
        grocery_list.append(grocery)
        print("You have added ", grocery, "to the list")
        print("Your current list is: ")
        print_stuff(grocery_list)
        validadd = input("Would you like to add another item? [y/n] ")
    return grocery_list




def itemremover( grocery_list):
    forloopexit = "y"
    validremove = "y"
    while validremove == "y":
        print("Your list is currently:")
        print_stuff(grocery_list)
        while forloopexit == 'y':
            remove_this = int(input("What number item would you like to remove? "))
                #for grocery in grocery_list:
            grocery_list.pop(remove_this - 1)
            print("Your new list: ")
            print_stuff(grocery_list)
            forloopexit = 'n'
        validremove = input("Want to remove something else? [y/n] ")

def print_stuff(grocery_list):
    item_num = 0
    for grocery in grocery_list:
        item_num += 1
        new_list = str(item_num) + ': ' + grocery
        print(new_list)


print("Welcome to Thor, Katherine, and Jafar's grocery list builder!\n")
while valid == "y":
    print("What would you like to say?\n")
    while True:
        try:
            user_input = input("You can say add, remove, print, or exit! ")
            if user_input not in commands:
                raise TypeError("not in commands")
            break
        except TypeError:
            print("I didn't catch that; please try again!\n")
    if user_input == "add":
        want_another()
    elif user_input == "remove":
        itemremover(grocery_list)
    elif user_input == "print":
        print_stuff(grocery_list)
    else:
        print("Goodbye!\n\n\n\n\n\n")
        print('❤️❤️❤️ i love u ❤️❤️❤️')
        valid = "n"

