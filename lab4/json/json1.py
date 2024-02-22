import json

# some JSON:
x =  '{ "name":"Nurhat", "age":18, "city":"Aktau"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
print(y["city"])
