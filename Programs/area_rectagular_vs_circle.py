  ## Consider one circle and one rectangle. The circle has a radius r = 10.6. The
rectangle has sides a and b, but only a is known from the outset. Let a = 1.3
and write a program that uses a while loop to find the largest possible integer b that
gives a rectangle area smaller than, but as close as possible to, the area of the circle.
Run the program and confirm that it gives the right answer

import numpy as np

r = 10.6
a = 1.3

circle_area = np.pi * r**2

b = 1

while a * b < circle_area:
    b = b + 1

b = b - 1

rectangle_area = a * b

print("Circle area =", circle_area)
print("Largest integer b =", b)
print("Rectangle area =", rectangle_area)
