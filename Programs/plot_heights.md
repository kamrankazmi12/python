#showing a plot of two families heights
import numpy as np
import matplotlib.pyplot as plt

family1=np.zeros(4)
family2=np.zeros(4)

member = np.zeros(4)

#overwriting the values for family one members
family1[0] = 1.60  
family1[1] = 1.85
family1[2] = 1.75
family1[3] = 1.80

#overwriting the values for family two members
family2[0] = 0.50 
family2[1] = 0.70
family2[2] = 1.90
family2[3] = 1.75

#overwriting the members order

member[0] = 1
member[1] = 2
member[2] = 3
member[3] = 4


#plotting

plt.plot(member, family1, 'r-')
plt.plot(member, family2, 'b-')

#defining plot axis

plt.axis([0, 4, 0, 2])
#plot labeling
plt.xlabel("Family Member")
plt.ylabel("Height (m)")
plt.title("Heights of Two Families")

#showing the plot

plt.grid(True)
plt.show()



<img width="1690" height="798" alt="image" src="https://github.com/user-attachments/assets/ebeaef3f-4089-4132-9e90-386aba2e9a56" />
