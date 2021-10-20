#Author: Kevin Hines
#Date: 10/20/2021
#This is a calculator that takes vector V and W with an angle and calculates
#the projection of W onto V
import math

print("This is a vector projection calc")
print("(projecting W onto V)")

print("Vector V's components")
Vx = float(input("Vx: "))
Vy = float(input("Vy: "))
Vz = float(input("Vz: "))

print(" ")

print("Vector W's components")
Wx = float(input("Wx: "))
Wy = float(input("Wy: "))
Wz = float(input("Wz: "))

print(" ")

theta = float(input("Theta (rads): "))

magnitudeW = math.sqrt(math.pow(Wx, 2) + math.pow(Wy, 2) + math.pow(Wz, 2))
magnitudeV = math.sqrt(math.pow(Vx, 2) + math.pow(Vy, 2) + math.pow(Vz, 2))

projectionScalar = magnitudeW * (math.cos(theta))/magnitudeV

projX = projectionScalar * Vx
projY = projectionScalar * Vy
projZ = projectionScalar * Vz

print("New Vector: ")
print("X = ", projX)
print("Y = ", projY)
print("Z = ", projZ)





