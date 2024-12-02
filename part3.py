import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter

data = pd.read_csv("C:\\Users\ДОМ\Downloads\start.dat.txt")
start_func = np.array(data)

tmp = start_func.shape[0]

Matrix = np.zeros((tmp, tmp))
for i in range(tmp):
    for j in range(tmp):
        if i == j or i - j == 1:
            Matrix[i][j] = 0.5
Matrix[0][tmp-1] = 0.5
Matrix = Matrix.T

column = start_func.reshape(1, tmp)
column = column[0,:]

def update(frame):
    global Matrix
    tmp = Matrix.copy()
    for i in range(frame-1):
        tmp = np.dot(tmp, Matrix)
    y = np.dot(column, tmp)
    line.set_ydata(y)
    return line,

fig, ax = plt.subplots(figsize = (11, 8))
line, = ax.plot(column)
ax.grid()

ani = FuncAnimation(fig, update, frames = 255, interval = 75)

writer = PillowWriter(fps = 20)
ani.save("C:\\Users\ДОМ\Downloads\\GIF.gif", writer = writer)
plt.show()
