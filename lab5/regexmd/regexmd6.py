import re
text = 'Nurik going to watch Avengers, Spiderman.'
print(re.sub("[ ,.]", ":", text))