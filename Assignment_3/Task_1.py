# Function to calculate factorial using recursion
def fact(number):
    # Base case: factorial of 0 and 1 is 1, recursion stops here
    if number == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        factorial = number * fact(number - 1)
        return factorial

num = int(input("Enter a number: "))
if num <= 0:
    print("The number entered must not be a negative value or zero.\nPlease rerun the program.")
else:
    print(f"Factorial of {num} is: {fact(num)}")