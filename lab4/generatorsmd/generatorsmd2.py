def evens(number):
    for num in range(number):
        if num % 2 == 0:
            yield num

    
number = int(input("Vvedi chislo: "))
generator = evens(number)

for value in generator:
    print(value, end= ", ")