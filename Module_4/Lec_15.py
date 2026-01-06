"""Area of triangle when all the sides of the triangle are known"""

a = float(input("Please enter your first side: "))
b = float(input("Please enter your second side: "))
c = float(input("Please enter your third side: "))
s =(a+b+c)/2
area = (s * (s-a) * (s - b) * (s - c)) ** 0.5
print("The area of the triangle with given sides is", round(area,2))

"""Simple Intrest"""

p = float(input("Please enter your principal amount: "))
r = float(input("Please enter your rate of intrest: "))
t = float(input("Please enter your time: "))
si = (p * r * t) / 100
print("The simple intrest is", round(si,2))

"""Compound interest"""

cp = float(input("Please enter your principal amount: "))
cr = float(input("Please enter your rate of intrest: "))
ct = float(input("Please enter your time: "))
ca = cp * pow((1 + ( cr / 100)), ct)
ci = ca - cp
print("The compound interest is", round(ci,2))

"""Are of a right angled triangle"""\

base = float(input("Please enter your base length: "))
height = float(input("Please enter your height length: "))
rtarea = (base * height) / 2
print("The area of the triangle is", round(rtarea,2))