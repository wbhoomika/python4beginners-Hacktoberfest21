# simple python program plotting graphs depending on input
# requires installation of matplotlib library
import matplotlib.pyplot as plt

a=[1,2,3,4,5,6]
b=[3,6,9,12,15,18]
plt.plot(a,b)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Plot between X and Y axis")
plt.show()
