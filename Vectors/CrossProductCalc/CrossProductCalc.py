print("This program computes the Cross-Product of Two Vectors")
print("Please input the values of vector #1 (vector U)")

Ux = float(input("Ux: "))
Uy = float(input("Uy: "))
Uz = float(input("Uz: "))
print(Ux, Uy, Uz)

print("Please input the values of vector #2 (vector V)")

Vx = float(input("Vx: "))
Vy = float(input("Vy: "))
Vz = float(input("Vz: "))
print(Vx, Vy, Vz)

CrossProductXComponent = ((Uy*Vz)-(Uz*Vy))
CrossProductYCompoent = -((Ux*Vz)-(Uz*Vx))
CrossProductZComponent = ((Ux*Vy)-(Uy*Vx))

print("The resulting vector from U X V is")
print("<",CrossProductXComponent,",", CrossProductYCompoent,"," ,CrossProductZComponent ,">" )