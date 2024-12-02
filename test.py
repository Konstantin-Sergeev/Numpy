from PIL import Image
import numpy as np

# считаем картинку в numpy array
img = Image.open("C:\\Users\ДОМ\OneDrive\Рабочий стол\pandas\lunar03_raw.jpg")
data = np.array(img)

minimal = data.min()
num_of_colors = data.max()-data.min()
xh = np.linspace(0, 255, num_of_colors+1)

updated_data = data
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        updated_data[i][j] = xh[data[i][j]-minimal]

# ... логика обработки

# запись картинки после обработки
res_img = Image.fromarray(updated_data)
res_img.save("C:\\Users\ДОМ\Downloads\\third_image.jpg")