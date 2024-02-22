import math

def degree_to_radian(degree):
    to_radians = math.radians(degree)
    return to_radians

degree = int(input())
radians = degree_to_radian(degree)
print(radians)