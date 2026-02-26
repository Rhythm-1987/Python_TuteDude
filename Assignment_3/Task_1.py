def factorial(number):
    answer = 1
    while number > 1:
        answer = answer * number
        number = number - 1
    return answer

num = int(input("Enter a number: "))
print(f"Factorial of {num} is: {factorial(num)}")