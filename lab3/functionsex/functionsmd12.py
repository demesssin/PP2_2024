def is_prime(san):
    if san < 2:
        return False
    for i in range(2, int(san ** 0.5) + 1):
        if san % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [san for san in numbers if is_prime(san)]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter_prime(numbers))  
