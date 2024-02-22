import re
def camel_to_snake(text):
        
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', text).lower()

print(camel_to_snake('DemessinAbzal'))