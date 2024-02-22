import re

def text_match(text):
    pattern = 'a.*?b$'
    if re.search(pattern, text):
        return ("Found a match!")
    else:
        return ("Not found a match!")    

print(text_match("aasdaskfdgdlkb"))
print(text_match("bvkbvkssa"))
print(text_match("aa5878454b"))