#Author: Kevin Hines
#Date: 10/19/2021

import math

print("This program will take vector")
print("components and calculate magnitude")

Ux = float(input("Ux: "))
Uy = float(input("Uy: "))
Uz = float(input("Uz: "))

magnitude = (math.sqrt(math.pow(Ux,2) + math.pow(Uy,2) + math.pow(Uz,2)))

print("The magnitude of the line is: ") 
print(magnitude)
