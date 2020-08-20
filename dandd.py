#This project is on hold. I have to revamp the allocate area to make it a function. That sucks! That means for each stat I have to calculate what the stat is changing to,
#and then subtract that from pointbuy, return pointbuy, and do it again. It has to work for six stats, not make pointbuy negative, and wait as I'm typing this I got an idea...
#no no no, this is on hold.
#But for future Thor: the idea was that I could make ifs for each stat. So if str is at 8, you can add whatev, but if it's at fourteen ugh I hate this. If it's at 14, you can allocate
#2 points...which will add 1 point to strength. Fuck you 5e pointbuy.


#Our pool of points
pointbuy = 27
#For later
desc = {}
#A list of stats for our users to type later.
statlist = ["str", "dex", "con", "wis", "int", "cha"]
#For our loops
validstr = False
validdex = False
validcon = False
validwis = False
validint = False
validcha = False
#Possible values for a starting attribute.
posvalues = [8,9,10,11,12,13,14,15]

#This will take a users stregnth value, and tell it to the user along with how many points they have left. This is the same for dex and con.
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
    
    return pointbuy

def finddex(dex, pointbuy): 
    if dex == 9:
        pointbuy -= 1
        
    elif dex == 10:
        pointbuy -= 2
        
    elif dex == 11:
        pointbuy -= 3
        
    elif dex == 12:
        pointbuy -= 4
        
    elif dex == 13:
        pointbuy -= 5
        
    elif dex == 14:
        pointbuy -= 7
        
    elif dex == 15:
        pointbuy -= 9
        
    elif dex == 8:
        pass
    print(" ")
    print(f"Okay great! Your dexterity score is now {dex} and you have {pointbuy} points left!")
    print(" ")    
    return pointbuy

def findcon(con, pointbuy): 
    if con == 9:
        pointbuy -= 1
        
    elif con == 10:
        pointbuy -= 2
        
    elif con == 11:
        pointbuy -= 3
        
    elif con == 12:
        pointbuy -= 4
        
    elif con == 13:
        pointbuy -= 5
        
    elif con == 14:
        pointbuy -= 7
        
    elif con == 15:
        pointbuy -= 9
        
    elif con == 8:
        pass
    print(" ")
    print(f"Okay great! Your constitution score is now {con} and you have {pointbuy} points left!")
    print(" ")
    return pointbuy        
    
#For wisdom and ahead, we run into the problem of the user being able to assign more points than we have in the pool. To prevent this, we only allow attributes to be adjusted if there are enough points left.
def findwis(wis, pointbuy): 
    if wis == 9 and pointbuy > 0:
        pointbuy -= 1
        
    elif wis == 10 and pointbuy > 1:
        pointbuy -= 2
        
    elif wis == 11 and pointbuy > 2:
        pointbuy -= 3
        
    elif wis == 12 and pointbuy > 3:
        pointbuy -= 4
        
    elif wis == 13 and pointbuy > 4:
        pointbuy -= 5
        
    elif wis == 14 and pointbuy > 6:
        pointbuy -= 7
        
    elif wis == 15 and pointbuy > 8:
        pointbuy -= 9
        
    elif wis == 8:
        pass
    else:
        print("You doin't have enough points left!")
    print(" ")
    print(f"Okay great! Your wisdom score is now {wis} and you have {pointbuy} points left!")
    print(" ")
    return pointbuy    

def findintel(intel, pointbuy): 
    if intel == 9 and pointbuy > 0:
        pointbuy -= 1
        
    elif intel == 10 and pointbuy > 1:
        pointbuy -= 2
        
    elif intel == 11 and pointbuy > 2:
        pointbuy -= 3
        
    elif intel == 12 and pointbuy > 3:
        pointbuy -= 4
        
    elif intel == 13 and pointbuy > 4:
        pointbuy -= 5
        
    elif intel == 14 and pointbuy > 6:
        pointbuy -= 7
        
    elif intel == 15 and pointbuy > 8:
        pointbuy -= 9
        
    elif intel == 8:
        pass
   
    print(" ")
    print(f"Okay great! Your intelligence score is now {intel} and you have {pointbuy} points left!")
    print(" ")
    return pointbuy


def findcha(cha, pointbuy): 
    if cha == 9 and pointbuy > 0:
        pointbuy -= 1
        
    elif cha == 10 and pointbuy > 1:
        pointbuy -= 2
        
    elif cha == 11 and pointbuy > 2:
        pointbuy -= 3
        
    elif cha == 12 and pointbuy > 3:
        pointbuy -= 4
        
    elif cha == 13 and pointbuy > 4:
        pointbuy -= 5
        
    elif cha == 14 and pointbuy > 6:
        pointbuy -= 7
        
    elif cha == 15 and pointbuy > 8:
        pointbuy -= 9
        
    elif cha == 8:
        pass
    
    print(" ")
    print(f"Okay great! Your charisma score is now {cha} and you have {pointbuy} points left!")
    print(" ")
    return pointbuy
#In case they have points left over, this will reallocate them.
def statreallocate(allocate, exchoice):
    while allocate > 0:
        if exchoice == "fillme" and allocate > 0 and allocate < 6 and allocate <= pointbuy:
            pass
        elif exchoice == "fillme" and allocate <= pointbuy and allocate == 7 or allocate == 9 :
            pass
        elif allocate == 6 or allocate == 8 or allocate == 0:
            print("I'm sorry, 0, 6, and 8 aren't applicable values.")
            break
        elif allocate > pointbuy:
            print("I'm sorry, you don't have enough points for that!")
            break
    return allocate


#Instructions on how to use the tool.
print("Welcome to your interactive character builder!")
print ("The first thing we're going to do is allocate your stats!")
print("Each stat starts at 8.")
print("And you have a pool of 27 points.")
print("Keep in mind each increase past 13 points costs 2 points each.")
print("Meaning a score of 9 costs 1 point (your base value of 8 plus one point) a score of 13 would cost 5 points, and a score of 15 would cost 9 points (5 points to get to 13, 2 points to get to 14, and 2 more points to get to 15).")
print("15 is as high as a score can go!")
print("Alright, let's get started!")
print(" ")

#This runs our strenth def in such a way that if the user puts in an inapplicable value, it'll rerun it.
while not validstr: 
    while True:
        try:
            stresc = int(input("What should we make our strength? Choose a value between 8 and 15: "))
            break
        except ValueError:
            print("No, I need a numeral!")    
    if stresc <= 15 and stresc >= 8:
        validstr = True
    elif stresc < 8:
        print("That value is too low! New value:")
    else:
        print("That value is too high! New value: ")
findstre(stresc, pointbuy)

pointbuy = findstre(stresc, pointbuy)
print(" ")
print(f"Okay great! Your stregnth score is now {stresc} and you have {pointbuy} points left!")
print(" ")

while not validdex: 
    while True:
        try:
            dex = int(input("What should we make our dexterity? Choose a value between 8 and 15: "))
            break
        except ValueError:
            print("No, I need a numeral!")    
    if dex <= 15 and dex >= 8:
        validdex = True
    elif dex < 8:
        print("That value is too low! New value:")
    else:
        print("That value is too high! New value: ")


pointbuy = finddex(dex, pointbuy)



while not validcon: 
    while True:
        try:
            con = int(input("What should we make our constitution? Choose a value between 8 and 15: "))
            break
        except ValueError:
            print("No, I need a numeral!")
    if con <= 15 and con >= 8:
        validcon = True
    elif con < 8:
        print("That value is too low! New value:")
    else:
        print("That value is too high! New value: ")

pointbuy = findcon(con, pointbuy)



while not validwis: 
    if pointbuy == 0:
        print("You're out of points! Setting wisdom to 8")
        wis = 8
        break
    while True:
        try:
            wis = int(input("What should we make our wisdom? Choose a value between 8 and 15: "))
            break
        except ValueError:
            print("No, I need a numeral!")
    if wis <= 15 and wis >= 8:
        validwis = True
    elif wis < 8:
        print("That value is too low! New value:")
    else:
        print("That value is too high! New value: ")

pointbuy = findwis(wis, pointbuy)


while not validint: 
    if pointbuy == 0:
        print("You're out of points! Setting intelligence to 8")
        intel = 8
        break
    while True:
        try:
            intel = int(input("What should we make our intelligence? Choose a value between 8 and 15: "))
            break
        except ValueError:
            print("No, I need a numeral!")
    if intel <= 15 and intel >= 8:
        validint = True
    elif intel < 8:
        print("That value is too low! New value:")
    else:
        print("That value is too high! New value: ")

pointbuy = findintel(intel, pointbuy)


while not validcha: 
    if pointbuy == 0:
        print("You're out of points! Setting charisma to 8")
        cha = 8
        break
    while True:
        try:
            cha = int(input("What should we make our charisma? Choose a value between 8 and 15: "))
            break
        except ValueError:
            print("No, I need a numeral!")
    if cha <= 15 and cha >= 8:
        validcha = True
    elif cha < 8:
        print("That value is too low! New value:")
    else:
        print("That value is too high! New value: ")

pointbuy = findcha(cha, pointbuy)
while pointbuy > 0:
    print(f"You have {pointbuy} points left!")
    print("Where would you like to put them?")
    while True:
        try:
            exchoice = input("You can say str, dex, con, wis, int, or cha: ").lower()
            if exchoice not in statlist:
                raise TypeError('needs to be a stat')
            break
        except TypeError:
            print(" ")
            print("No, I need str, dex, con, wis, int, or cha!")
    while True:
        try:
            allocate = int(input("And how many points are we putting there?"))
            if allocate > pointbuy:
                raise TypeError('not enough points.')
            elif allocate == 0:
                raise TypeError('0 point assignment')
            break
        except ValueError:
            print(" ")
            print(f"No, I need a numeral between 1 and {pointbuy}!")
            print(" ")
        except TypeError:
            print(" ")
            print("I'm sorry, either you don't have enough points, or you tried to allocate 0 points.")
            print(" ")

