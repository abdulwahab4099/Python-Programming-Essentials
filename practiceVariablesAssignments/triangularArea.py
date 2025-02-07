"""
Solution - Compute the area of a triangle (using Heron's formula),
       given its side lengths.
"""
x0, y0 = 2, 3
x1, y1 = 4, 6
x2, y2 = 7, 9

side1 = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
side2 = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
side3 = ((x2 - x0) ** 2 + (y2 - y0) ** 2) ** 0.5

s = (side1 + side2 + side3) / 2

area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5

print("The area of the triangle is", area, "square units.")