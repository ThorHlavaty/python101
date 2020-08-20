valid = "y"
print("What are we doing?")
sums = []
finalsum = 0
def sum_it_up(sums, finalsum):
    for number in sums:
        finalsum += number
    print(finalsum)
def largest(sums, finalsum):
    for num in sums:
        finalsum = sums[0]
        if num > finalsum:
            finalsum = num
    print(finalsum)
def smallest(sums, finalsum):
    for num in sums:
        finalsum = sums[0]
        if num < finalsum:
            finalsum = num
    print(finalsum)
#while valid == False:
what_to_do = input("You can say sum, max, or min: " ).lower()
while valid == 'y':
    if what_to_do == "sum":
        sums = []
        finalsums = 0
        print("")
        while True:
            try:
            
                sums.append(int(input("Give me numbers, one at a time. When done, press q: ")))
            
            except ValueError:
                break
        sum_it_up(sums, finalsum)
        valid = input("Want to do something else? [y/n] ")
        if valid != "y":
            print("Goodbye!")
            break
        what_to_do = input("You can say sum, max, or min: " ).lower()
    elif what_to_do == 'max':
        sums = []
        finalsum = 0
        print("")
        while True:
            try:
            
                sums.append(int(input("Give me numbers, one at a time. When done, press q: ")))
            
            except ValueError:
                break
        largest(sums, finalsum)
        valid = input("Want to do something else? [y/n] ")
        if valid != "y":
            print("Goodbye!")    
            break
        what_to_do = input("You can say sum, max, or min: " ).lower()
    elif what_to_do == 'min':
        sums = []
        finalsum = 0
        print("")
        while True:
            try:
            
                sums.append(int(input("Give me numbers, one at a time. When done, press q: ")))
            
            except ValueError:
                break
        smallest(sums, finalsum)
        valid = input("Want to do something else? [y/n] ")
        if valid != "y":
            print("Goodbye!")
            break
        what_to_do = input("You can say sum, max, or min: " ).lower() 
    else:
        print("")
        print("I'm sorry, I didn't catch that.")
        print("")
        valid = input("Want to do something else? [y/n] ")
        if valid != "y":
            print("Goodbye!")
            break
        what_to_do = input("You can say sum, max, or min: " ).lower()  
