"""
Solution - compute the distance between the points (x0, y0) and (x1, y1).
"""

x0 = 2

y0 = 3

x1 = 5
y1 = 7

distance = ((x1 - x0) ** 2) + ((y1 - y0) ** 2) ** 0.5

print("The distance from (" + str(x0) + ", " + str(y0) + 
      ") to (" + str(x1) + ", " + str(y1) + ") is " + str(distance) + ".")