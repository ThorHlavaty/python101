valid = "y"
while valid == "y":
    sequence = [1, 1]
    while True:
        try:
            user_input = int(input("How high we going? "))
            if user_input < 0:
                print("Let's be positive!")
                user_input * -1
            break
        except ValueError:
            print("No, I need a numeral!")
    if user_input == 1:
        print(f"[{sequence[1]}]")
    elif user_input > 1:
        for fib in range(1,user_input-1):
            sequence.append(sequence[-1] + sequence[-2])
        print(sequence)
    print("")
    valid = input("Want to go again? [y,n]: ")
    print("")
print("Okay, goodbye.")
print("")
print("")
print("")
print("")
print("❤️❤️❤️ i love you ❤️❤️❤️")