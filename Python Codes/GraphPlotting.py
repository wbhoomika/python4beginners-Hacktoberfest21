import matplotlib.pyplot as plt
import numpy as np
x1 = np.array([2,3,5,9])
y1 = np.array([4,3,6,2])
x2 = np.array([1,2,3,4])
y2 = np.array([4,2,5,1])
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.title('plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()
