import re

#Replace the first two occurrences of a white-space character with the digit 9:

txt = "The rain in Spain was dangerous"
x = re.sub("\s", "9", txt, 2)
print(x)
