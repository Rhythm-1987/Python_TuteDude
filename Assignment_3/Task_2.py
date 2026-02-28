import math

number = int(input("Enter a number: "))

if number<= 0:
    print("Enter a positive value for the square root and logarithm")
else:
    print(f"Square root: {math.sqrt(number)}")
    print(f"Logarithm: {math.log(number, math.e)}")

print(f"Sine: {math.sin(number)}")