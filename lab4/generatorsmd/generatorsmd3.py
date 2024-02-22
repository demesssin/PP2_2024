def divisions(number):
    for num in range(number):
        if num % 3 == 0 and num % 4 == 0:
            yield num

    
number = int(input("Vvedi chislo: "))
generator = divisions(number)

for value in generator:
    print(value, end= " ")