import json
import base64
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import cv2

img = mpimg.imread('F:\\Backup_picture\\6.jpg')

data = {}
data['img'] = cv2.imencode('.jpg', img)
print(data['img'])
data = base64.b64decode(data['img'])
#plt.imshow(data)