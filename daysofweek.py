user = input("Who is this? ")
day = int(input('Day (0-6)? '))

def sleep_in(day):
    if day == 0 or day == 6:
        print("Sleep in!")
    else:
        print(f"Jesus fuck {user} you have eight minutes to catch the train! WAKE UP!")
sleep_in(day)