#目标：理解三维数组结构、广播机制（Broadcasting）和矩阵点乘运算
"""
任务说明：
1.导入一张彩色图片并将其转换为 NumPy 数组（提示：可结合 matplotlib.image 库读取，彩色图片是一个形状为 (高度, 宽度, 3) 的三维数组）。
2.灰度处理：利用广播和矩阵乘法，将 RGB 图像转换为灰度图。标准加权公式为：$Y = 0.2989 R + 0.5870 G + 0.1140 B$。
3.色彩翻转：创建一个负片效果（即将所有像素值用 255 减去当前值）。
4.图像裁剪：通过数组切片，只保留图片中心区域的像素，将其余部分裁剪掉。
"""

import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtCore import center

#1.导入图片test.jpg
try:
    image = plt.imread('test.jpg')
except FileNotFoundError:
    print("没有找到test.jpg，随机生成一张300×400的随机彩色噪点图进行演示")
    np.random.seed(0)
    image = np.random.randint(0,256,size=(300,400,3),dtype=np.uint8)

#2.灰度处理
weights = np.array([0.2989,0.5870,0.1140])
#利用矩阵点乘，将数组的RGB维度和权重点乘
gray_image = np.dot(image,weights)

#3.色彩反转
negative_image = 255 - image

#4.图像裁剪
h,w = image.shape[:2]
center_h,center_w = h//2,w//2
#对高度和宽度进行切片
cropped_image = image[center_h-50:center_h+50,center_w-50:center_w+50]
print("图像处理完成（使用plt.imshow(gray_image,camp='gray')查看灰度图")

plt.imshow(gray_image,cmap='gray')
plt.axis('off')
plt.show()
