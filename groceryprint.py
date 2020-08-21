#print grocery list
#each item numbered

grocery_list = ["banana", "bread", "bananabread", "breadbanana"]
def print_stuff(grocery_list):
    item_num = 0
    for grocery in grocery_list:
        item_num += 1
        new_list = str(item_num) + ': ' + grocery
        print(new_list)