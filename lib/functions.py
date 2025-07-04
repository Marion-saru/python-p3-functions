#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    return f"Hello, {name}!"

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    return num1 + num2

def halve(number):
    if not isinstance(number, (int, float)):
        return None
    else:
        return f"{number / 2:.2f}"

greet_programmer()

func_greet = greet("Marion")
print(func_greet)

greet_with_default()

sum = add(5,5)
print(sum)

halve_value = halve(10)
print(halve_value)