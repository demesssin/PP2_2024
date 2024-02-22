import math
def area_of_polygon(sides, length_of_side):
    perimeter = sides * length_of_side
    radius = length_of_side / 2
    area = (perimeter * radius) / 2
    area_x = math.ceil(area)
    return area_x

sides = 4
length_of_side = 25
ploshad = area_of_polygon(sides, length_of_side)
print(ploshad)