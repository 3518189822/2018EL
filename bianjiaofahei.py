
# coding: utf-8

# In[7]:


import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.cm as cm
from skimage import data, exposure, img_as_float, color
from skimage.morphology import disk
import skimage.filters.rank as sfr

path_file1 = "微信图片 20171220190715.jpg"
path_file = path_file1
'''
#标准像素面积
'''
grey = cv2.imdecode(np.fromfile(path_file,dtype=np.uint8),0) # 灰度
img = cv2.imdecode(np.fromfile(path_file,dtype=np.uint8),1) # 彩色

retval, grey = cv2.threshold(grey, 100, 255, cv2.THRESH_BINARY)#二值化处理，低于阈值的像素点灰度值置为0黑；高于阈值的值置为255白（参数3）
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (50, 50))
closed = cv2.morphologyEx(grey, cv2.MORPH_CLOSE, kernel)
#开运算：先腐蚀后膨胀
#closed = cv2.erode(closed, None, iterations=10)# 腐蚀 黑色多白色少
#grey = cv2.dilate(closed, None, iterations=10)# 膨胀 白色多黑色少
#闭运算：先膨胀后腐蚀
closed = cv2.dilate(closed, None, iterations=1)# 膨胀 白色多黑色少
grey = cv2.erode(closed, None, iterations=1)# 腐蚀 黑色多白色少
#win = cv2.namedWindow('grey', flags=0)
#cv2.imshow('grey', grey)

count = 0
#求面积
width = grey.shape[0]
height = grey.shape[1]
for x in range(width):
    for y in range(height):
        if grey[x-1,y-1] == 255:
            count = count + 1
print(count)# 求出白色的像素点数

'''
#当前输入硅片图
'''
path_file2 = "C://Users//AXNB079//Documents//Aikosolar//IT//Assignment//2-27//ELTD1//REnamepath//101911549296.jpg"
grey2 = cv2.imdecode(np.fromfile(path_file2,dtype=np.uint8),0) # 灰度
img2 = cv2.imdecode(np.fromfile(path_file2,dtype=np.uint8),1) # 彩色

retval2, grey2 = cv2.threshold(grey2, 100, 255, cv2.THRESH_BINARY)#二值化处理，低于阈值的像素点灰度值置为0黑；高于阈值的值置为255白（参数3）
kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (50, 50))
closed2 = cv2.morphologyEx(grey2, cv2.MORPH_CLOSE, kernel2)

#闭运算：先膨胀后腐蚀
closed2 = cv2.dilate(closed2, None, iterations=1)# 膨胀 白色多黑色少
grey2 = cv2.erode(closed2, None, iterations=1)# 腐蚀 黑色多白色少
win = cv2.namedWindow('grey2', flags=0)
cv2.imshow('grey2', grey2)

count2 = 0
#求面积
width2 = grey2.shape[0]
height2 = grey2.shape[1]
for x2 in range(width2):
    for y2 in range(height2):
        if grey2[x2-1,y2-1] == 255:
            count2 = count2 + 1
print(count2)# 求出白色的像素点数

'''
#比较面积
'''
if count2 < count:
    print("边角发黑")

'''
#求轮廓
image, contours, hierarchy = cv2.findContours(grey.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 0, 225), 3)
cv2.imshow('img', img)
'''
cv2.waitKey(0)

