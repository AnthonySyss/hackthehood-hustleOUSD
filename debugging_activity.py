# Code Snippet 1
x = 10
y = 2
result = x / y
print("Result:", result)

print("-" * 30)


# Code Snippet 2
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    print(numbers[i])

print("-" * 30)


# Code Snippet 3
def calculate_area(radius):
    area = 3.14 * radius ** 2
    return area

radius = 5
print("Area:", calculate_area(radius))

print("-" * 30)


# Code Snippet 4
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(4))
print(is_even(7))

print("-" * 30)


# Code Snippet 5
for i in range(5):
    print(i)

print("-" * 30)


# Code Snippet 6
def greet(name):
    return "Hello, " + name

print(greet("Alice"))

print("-" * 30)


# Code Snippet 7
numbers = [1, 2, 3, 4, 5]
total = 0
for number in numbers:
    total += number
print("Sum of numbers:", total)

print("-" * 30)


# Code Snippet 8
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

print("-" * 30)


# Code Snippet 9
name = input("Enter your name: ")
if name == "Alice" or name == "Bob":
    print("Hello, " + name)
else:
    print("Hello, stranger!")

print("-" * 30)


# Code Snippet 10
def divide_numbers(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

num1 = 10
num2 = 0
print(divide_numbers(num1, num2))

print("-" * 30)