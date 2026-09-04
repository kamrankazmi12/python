#Write a program that takes a positive integer N as input and then draws N random
integers from the interval [1, 6]. In the program, count how many of the numbers,
M, that equal 6 and print out the fraction M/N. Also, print all the random numbers
to the screen so that you can check for yourself that the counting is correct. Run the
program with a small value for N (e.g., N = 10) to confirm that it works as intended.
Hint Use random.randint(1,6) to draw a random integer between 1 and 6.

  
import random

N = 10
M = 0

for i in range(N):
    number = random.randint(1, 6)
    print(number)

    if number == 6:
        M = M + 1

fraction = M / N

print("M =", M)
print("M/N =", fraction)
