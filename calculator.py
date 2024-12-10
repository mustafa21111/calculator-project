
import math

print(
    """
==================
Area Calculator 📐
==================

"""
)

print("   1) Triangle ")
print("   2)  Rectangle")
print("   3)  Square")
print("   4)  Circle")
print("   5) Quit")

Triangle = 1
Rectangle =2
Square = 3
Circle = 4
Quit = 5

a = int(input("select a number form 1- 5"))

if a ==1 :
    b = float(input("what is the base :"))
    h = float(input("what is the hieght:"))
    tri_area = (b*h)/2
    print("Calculated the area of a triangle: ")
    print( tri_area)

elif a == 2 :
    b = float(input("what is the base :"))
    h = float(input("what is the hieght:"))
    Area = b*h 
    print(f"  {Area}Calculated the area of a Rectangle : ")
    print( Area)
elif a == 3 :
    b = float(input("what is the base :"))
    h = float(input("what is the hieght:"))
    Area = b*h 
    print(f"  {Area}Calculated the area of a Square : ")
    print(  Area)

elif a == 4 :
    r = float(input(" what is the radius :"))
    Area = math.pi * (r**2) 
    print(f"{Area}Calculated the area of a Circle ")
    print( Area)   

else:
    print("wrong input")

