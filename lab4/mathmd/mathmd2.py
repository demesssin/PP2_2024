def area_of_trapezoid(height, first_base, second_base):
    midline = (first_base + second_base) / 2
    area = midline * height
    return area

height = 5
first_base = 5
second_base = 6
ploshad = area_of_trapezoid(height, first_base, second_base)
print(ploshad)