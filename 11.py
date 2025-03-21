# 代码2-8 将RGB空间的人脸图像转换为灰度空间
import cv2
import os

# 修改：添加文件路径检查和错误处理
image_path = r'D:\下载\xixi\pythonProject\venv\Lib\代码&图像\第2章\data\baby_GT.bmp'
if not os.path.exists(image_path):
    print(f"错误：无法找到图像文件 {image_path}")
    print("请检查文件路径是否正确，或文件是否存在")
    exit(1)

img = cv2.imread(image_path)
if img is None:
    print(f"错误：无法读取图像文件 {image_path}")
    print("请检查文件格式是否支持，或文件是否损坏")
    exit(1)

img_1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('input_image', img)
cv2.imshow('gray_image', img_1)
cv2.waitKey(0)
cv2.destroyAllWindows()



# 代码2-9 将RGB空间转换为HSV空间
import cv2

img = cv2.imread('../data/baby_GT.bmp')
img_1 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
B, G, R = cv2.split(img)
cv2.imshow('B', B)
cv2.imshow('G', G)
cv2.imshow('R', R)
cv2.imshow('input_image', img)
cv2.imshow('hsv_image', img_1)
cv2.waitKey(0)
cv2.destroyAllWindows()