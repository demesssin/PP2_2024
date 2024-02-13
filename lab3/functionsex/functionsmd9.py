def p(word):
    palindrome = "".join(reversed(word))
    if palindrome == word:
        print("Its palindrome")
    else:
        print("Not palindrome")

word = input()
p(word)