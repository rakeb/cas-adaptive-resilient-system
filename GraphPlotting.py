import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

day = 0
import math
def update_line(num, data, line):
    data[1][day] = 5 + math.pow(-1,day)*1
    data1 = np.array(data)
    global day
    day += 1
    day %= 10
    print type(data1)
    print type(data1[0])

    line.set_data(data1[..., :num])
    return line,

fig1 = plt.figure()

# data = np.random.rand(2, 5)


data = []
for i in range(2):
    data.append([])
    for j in range(15):
        if i == 0:
            data[i].append(j)
        else:
            data[i].append(10)


l, = plt.plot([], [], 'r-')
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.xlabel('x')
plt.title('test')
line_ani = animation.FuncAnimation(fig1, update_line, 15, fargs=(data, l),
                                   interval=50, blit=True)

# To save the animation, use the command: line_ani.save('lines.mp4')

# fig2 = plt.figure()
#
# x = np.arange(-9, 10)
# y = np.arange(-9, 10).reshape(-1, 1)
# base = np.hypot(x, y)
# ims = []
# for add in np.arange(15):
#     ims.append((plt.pcolor(x, y, base + add, norm=plt.Normalize(0, 30)),))
#
# im_ani = animation.ArtistAnimation(fig2, ims, interval=50, repeat_delay=3000,
#                                    blit=True)
# # To save this second animation with some metadata, use the following command:
# # im_ani.save('im.mp4', metadata={'artist':'Guido'})

plt.show()
