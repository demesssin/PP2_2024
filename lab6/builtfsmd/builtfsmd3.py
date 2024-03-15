word = input("Napishi slovo: ")
print(word)

if word == word[::-1]:
    print("Its palindrome")
else:
    print("Its not palindrome")