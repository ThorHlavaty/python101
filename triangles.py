import threading
x = []
y = 0
z = 0

value = int(input("How big is our Triangle? "))
which = input("Do you want all the triangle numbers, or just the one your asking about? Say all or one: ").lower()

if which == "all":
    while y < value:
        y += 1
        z += y
        print(z)
elif which == "one":
    while y < value:
        y += 1
        z += y
    print(z)
else:
    print("Sorry, I didn't recognize that!")
    input("Terminating program in 5")
    input("4")
    input("3")
    input("2")
    input("1")
    print("💥💥💥💥💥💥💥")
    print("💥💥💥💥💥💥💥")
    print("💥💥💥💥💥💥💥")
    print("💥💥💥💥💥💥💥")