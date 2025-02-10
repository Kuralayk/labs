import math 
#1`
degree = int(input("degree: "))
radians = (degree * (math.pi / 180))
print("radians: ", radians)

#2
height = int(input("height: "))
base1 = int(input("base1: "))
base2 = int(input("base2: "))
area = 0.5 * (base1 + base2) * height
print("area: ", area)

#3
n = int(input("Number of slides: "))
s = int(input("Length: "))
area = (n * (s**2))// (4 * math.tan(math.pi / n))
print("The area: ", area)

#4
a = float(input("Length: "))
b = float(input("Height: "))
area = a * b 
print("Area: ", area)
