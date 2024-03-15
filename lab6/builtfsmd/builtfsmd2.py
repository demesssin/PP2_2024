def count_upper_lower(text):
    upper_count = sum(1 for char in text if char.isupper())
    lower_count = sum(1 for char in text if char.islower())
    return upper_count, lower_count

text = input("Pishi che to: ")
upper_count, lower_count = count_upper_lower(text)
print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)
