def squares(number):
    while number <= 5:
        yield number
        number = number + 1

generator = squares(1)

for value in generator:
    print(value * value)  
