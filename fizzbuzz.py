#Function that takes all number between 1 and input
#Arbitrary fake input to test.
valid = "y"
while valid == "y":

    user_input = 0
    start = 0
    fizzorbuzz = []
    def counter(start, user_input):
        while start < user_input:
            start +=1
            if start % 3 == 0 and start % 15 != 0:
                print("fizz")
            elif start % 5 == 0 and start % 15 != 0:
                print("buzz")
            elif start % 15 == 0:
                print("fizzbuzz")
            else:
                print(start)

    while True:
        try:
            user_input = int(input("How high we  going? "))
            break
        except ValueError:
            print("No, I need a numeral!")
    counter(start, user_input)

    valid = input("Want to do another? [y/n]: ")
    print("Okay, goodbye!")