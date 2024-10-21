import random
# using randrange() to generate in range from 20
# to 50. The last parameter 3 is step size to skip
# three numbers when selecting.
x = random.randrange(0, 50)
print("Numarul generat:", x)
nr = int(input("Ghiceste numarul:"))

while(x != nr):
    if(nr > x):
            print("prea mare")
            print("Este intre",nr -1,"si", int(x //1.5))
            nr = int(input("Ghiceste numarul:"))

    if(nr<x):
            print("prea mic")
            print("Este intre",nr +1,"si", int(x *1.5))
            nr = int(input("Ghiceste numarul:"))
if (nr == x):   
            print("FELICITARI!!")
