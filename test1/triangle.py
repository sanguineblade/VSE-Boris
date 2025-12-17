import math
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
C = int(input("Enter angle C(gama): "))
def area():
    surface = 1/2*a*b*round(math.sin(C))
    c = math.floor(math.sqrt(a**2+b**2-(2*a*b*math.cos(C))))
    area = a + b + c 
    return surface, area
triangel = area()
print("surface is: " + math.floor(triangel[0]))
print("area is: " + triangel[1])

