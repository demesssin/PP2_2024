import time
import math

def square_root(x):
    return math.sqrt(x)

milliseconds = int(input("Enter the number of milliseconds to wait: "))
time.sleep(milliseconds / 1000)

number = float(input("Enter a number to find its square root: "))
result = square_root(number)
print(f"The square root of {number} after {milliseconds} milliseconds is {result}")
