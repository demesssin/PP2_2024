import re

def check_string(string):
    if re.search('ab{2,3}' , string):
        print(f"'{string}' соответствует условию.")
    else:
        print(f"'{string}' не соответствует условию.")

test_strings = ["abbziz", "abbbdusalyam", "Malik", "Zayn"]

for test_str in test_strings:
    check_string(test_str)
