from functools import reduce
from operator import mul

def multiply(numbers):
    if not numbers:
        return 0  
    return reduce(mul, numbers)

numbers_list = [4, 5, 6, 8]

result = multiply(numbers_list)

print(result)
