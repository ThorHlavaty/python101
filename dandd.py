pointbuy = 27
desc = {}
print("Welcome to your interactive character builder!")
print ("The first thing we're going to do is allocate your stats!")
print("Each stat starts at 8.")
print("And you have a pool of 27 points.")
print("Keep in mind each increase past 13 points costs 2 points each.")
print("Meaning a score of 9 costs 1 point (your base value of 8 plus one point) a score of 13 would cost 5 points, and a score of 15 would cost 9 points (5 points to get to 13, 2 points to get to 14, and 2 more points to get to 15).")
print("15 is as high as a score can go!")
print("Alright, let's get started!")
print(" ")
stresc = int(input("What should we make our strength? Choose a value between 8 and 15: "))
posvalues = [8,9,10,11,12,13,14,15]
def findstre(stresc, pointbuy): 
    if stresc == 9:
        pointbuy -= 1
        
    elif stresc == 10:
        pointbuy -= 2
        
    elif stresc == 11:
        pointbuy -= 3
        
    elif stresc == 12:
        pointbuy -= 4
        
    elif stresc == 13:
        pointbuy -= 5
        
    elif stresc == 14:
        pointbuy -= 7
        
    elif stresc == 15:
        pointbuy -= 9
        
    elif stresc == 8:
        pass
    print(" ")
    print(f"Okay great! Your strenth score is now {stresc} and you have {pointbuy} points left!")
    print(" ")
    
findstre(stresc, pointbuy)
