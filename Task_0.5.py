from math import sqrt

def area_of_triangle(s1, s2, s3):
    semiperimeter = 0.5 * (s1 + s2 + s3)
    area = sqrt(semiperimeter * (semiperimeter - s1) * (semiperimeter - s2) * (semiperimeter - s3))
    return area

area = area_of_triangle(3, 4, 5)
print(str(area) + " square units")