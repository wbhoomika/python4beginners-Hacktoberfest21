from pythonping import ping
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

xs_min=[0]
ys_min=[5]

def animate(z):
    ping_out = ping('8.8.8.8', count = 1)
    #ping_out = ping('127.0.0.1', count = 1)

    ping_arr = str(ping_out)[len(str(ping_out))-28:].split(" ")
    print(ping_arr)
    for i in range(len(ping_arr)):
        if len(ping_arr[i]) > 10:
            time_min = ping_arr[i].split("/")[0]

    print(time_min)

    xs_min.append(float(len(xs_min)))
    ys_min.append(float(time_min))
    
    #print(xs_min)
    #print(ys_min)

    ax1.clear()
    ax1.plot(xs_min[-50:],ys_min[-50:],linewidth=2)


ani = animation.FuncAnimation(fig, animate, interval=50)
plt.show()

print(xs)
