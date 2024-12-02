
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

alpha = pd.read_csv("C:\\Users\ДОМ\OneDrive\Рабочий стол\pandas\signal03.dat")
start_data = np.array(alpha)

start_data = start_data.reshape(1, start_data.shape[0])
data0 = start_data[0,:]

data = data0.copy()

for i in range(1, start_data.shape[1]):
    if i < 9:
        data[i] = data0[:i+1].mean()
    else:
        data[i] = data0[i-9:i+1].mean()

fig, axs = plt.subplots(nrows = 1, ncols = 2, figsize = (11, 8))
axs[0].plot(data0)
axs[0].set_title("До фильтра")
axs[1].plot(data)
axs[1].set_title("После фильтра")

for ax in axs:
    ax.set_xlabel('№ измерения')
    ax.set_ylabel('Значение')
    ax.set_ylim(0, 32)
    ax.grid()

plt.savefig("C:\\Users\ДОМ\Downloads\\third_grafic.png")
plt.show()