# get the first number
# get the second number

# make an individual function to add, subtract, multiply and divide
# return from each function
# template for add function

def add(num1, num2):
    return (num1 + num2)


def sub(num1, num2):
    return (num1 - num2)


def multiply(num1, num2):
    return (num1 * num2)


def division(num1, num2):
    return (num1 / num2)


num1 = int(input("Enter the First Number"))
num2 = int(input("Enter the Second Number"))

print("The sum of number 1 and number 2 is ", (add(num1, num2)))
print(sub(num1, num2))
print(multiply(num1, num2))
print(division(num1, num2))