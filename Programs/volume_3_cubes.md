 In a program, use the linspace function to compute and print three values of L,
equally spaced on the interval [1, 3].
b) Carry out, by hand, the computation V = L3 when L is an array with three
elements. That is, compute V for each value of L.
c) Modify the program in a), so that it prints out the result V of V = L**3 when L is
an array with three elements as computed by linspace. Compare the resulting
volumes with your hand calculations.
d) Make a plot of V versus L.

#Program to find volume of 3 cubes with array value of length
import numpy as np
import matplotlib.pyplot as plt
L = np.linspace(1, 3, 3) #equally sapced value of L
V = L**3 # volume of cubes
print(V, L)
plt.plot(L, V, 'o-', linewidth=2)
plt.xlabel("L")
plt.ylabel("V")
plt.title("Volume of a Cube")
plt.grid(True)
plt.show()
