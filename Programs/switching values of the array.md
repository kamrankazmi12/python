##In an interactive session, use linspace from numpy to generate an array x with
the numbers 1.0, 2.0 and 3.0. Then, switch the content of x[0] and x[1], before
checking x to see that your switching worked as planned.

#program to check the values after switching them
import numpy as np

x = np.linspace(1, 3, 3)

print("Before switching:", x)

x[0], x[1] = x[1], x[0]

print("After switching:", x)
