valid = "y"
row1m1 = []
row2m1 = []
row1m2 = []
row2m2 = []
row1m3 = []
row2m3 = []
def matrixmakerrow1(matrix1, matrix2):
    for matrice1 in row1m1:
        for matrice2 in row1m2:
            for matrice3 in row2m1:
                for matrice4 in row2m2: 
                    pass
while valid == "y":
    matrix1 = []
    matrix2 = []    
    while len(matrix1) < 4:
        print("Let's make you first matrix.")
        print("")
        print("What is x?")
        print("")
        print("[ x  - ]")
        while True:
            try:
            
                matrix1.append(int(input("[ -  - ]: ")))
            
            except ValueError:
                print("")
                print("I need a numeral, actually.")
                print("")
        print("What is x?")
        print("")
        print("[ -  x ]")
        while True:
            try:
            
                matrix1.append(int(input("[ -  - ]: ")))
            
            except ValueError:
                print("")
                print("I need a numeral, actually.")
                print("")
        print("What is x?")
        print("")
        print("[ -  - ]")
        while True:
            try:
            
                matrix1.append(int(input("[ x - ]: ")))
            
            except ValueError:
                print("")
                print("I need a numeral, actually.")
                print("")
        print("What is x?")
        print("")
        print("[ -  - ]")
        while True:
            try:
            
                matrix1.append(int(input("[ - x ]: ")))
            
            except ValueError:
                print("")
                print("I need a numeral, actually.")
                print("")
        print("Great job! Let's make your second matrix.")
    while len(matrix2) < 4:    
        print("")
        print("What is x?")
        print("")
        print("[ x  - ]")
        while True:
            try:
            
                matrix2.append(int(input("[ - - ]: ")))
            
            except ValueError:
                print("")
                print("I need a numeral, actually.")
                print("")
        print("What is x?")
        print("")
        print("[ -  x ]")
        while True:
            try:
            
                matrix2.append(int(input("[ - - ]: ")))
            
            except ValueError:
                print("")
                print("I need a numeral, actually.")
                print("")
        print("What is x?")
        print("")
        print("[ -  - ]")
        while True:
            try:
            
                matrix2.append(int(input("[ x - ]: ")))
            
            except ValueError:
                print("")
                print("I need a numeral, actually.")
                print("")
        print("What is x?")
        print("")
        print("[ -  - ]")
        while True:
            try:
            
                matrix2.append(int(input("[ - x ]: ")))
            
            except ValueError:
                print("")
                print("I need a numeral, actually.")
                print("")
    matrixmaker(matrix1,matrix2)
    print("Great! Here's what your new matrix looks like!")
    print("")
    print(f"[ {matrix3[0]} {matrix3[1]} ]")
    print(f"[ {matrix3[2]} {matrix3[3]} ]")
    print("")
    valid = input("Would you like to make another one? [y/n]: ")
    print("Okay, goodbye!")
    print("I love you.")






