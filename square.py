chars = input("Give me a character! " )
num = int(input("How big do ya want it? " ))
x = 0
valid = False
while not valid:
    if x < num and len(chars) == 1:
        valid = True
        while x < num: 
            print( chars * num )
            x += 1
    else:
        print("Come on, don't be silly.")
        break
    
