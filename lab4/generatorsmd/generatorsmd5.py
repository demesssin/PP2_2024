def down_to_0(number):
    while number != 0:
        yield number
        number = number - 1
        if number == 0:
            yield 0

generator = down_to_0(5)

for value in generator:
    print(value, end = " ")