#Author: Kevin Hines
#Date: 10/19/2021

import math
print("This program uses two vectors to calculate the dot product")

desiredMethod = 1
while(desiredMethod != 0):
    print("What method for calculating would you like?")
    print("1 for component")
    print("2 for magnitude")
    desiredMethod = int(input("0 cancel: "))

    if(desiredMethod == 1):
        print("Vector #1")
        Ux = float(input("Ux: "))
        Uy = float(input("Uy: "))
        Uz = float(input("Uz: "))

        print("Vector #2")
        Vx = float(input("Vx: "))
        Vy = float(input("Vy: "))
        Vz = float(input("Vz: "))

        dotProduct = (Ux * Vx)+(Uy * Vy)+(Uz * Vz)
        print("The dot product is: ")
        print(dotProduct)

    elif(desiredMethod == 2):
        print("Please input the below values")
        print("Input 0 for the value you're trying to solve")
        print(" ")

        MagU = float(input("Vector #1 Magnitude: "))
        MagV = float(input("Vector #2 Magnitude: "))
        theta = float(input("Angle between vectors in rads: "))
        dotProduct = float(input("Dot product total: "))
        if(theta == 0):
            theta = math.acos(dotProduct/(MagU*MagV))
            print("Theta is equal to (rads) ")
            print(theta)
        if(dotProduct == 0):
            dotProduct = MagU * MagV * math.cos(theta)
            print("The dot product is ")
            print(dotProduct)
    elif(desiredMethod == 0):
        print("Finished!")
    else:
        print("That input wasn't recongnized")
