while True:
    try:
        num = int(input("How many numbers are you asking about? "))
        break
    except ValueError:
        print("No, I need a numeral!")
valid = 0

while valid == 0:
    select = input("Cool! Do you want all, evens or odds? Say all/evens/odds: ").lower()    
    if select == "evens": 
        for nums in range(num):
            if nums % 2 == 0:
                print(nums)
                valid += 1
    elif select == "odds": 
        for nums in range(num):
            if nums % 2 == 1:
                print(nums)
                valid +=1
    elif select == "all": 
        for nums in range(num):
            print(nums)
            valid +=1
    else:
        print("")
        print("Sorry, didn't catch that!")
        print("")
        
