import re
def text_match(text):
        patterns = '^[A-Z]*+_[a-z]+$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("B_c"))
print(text_match("aab_Abbbc"))
print(text_match("Aaab_abbbc"))