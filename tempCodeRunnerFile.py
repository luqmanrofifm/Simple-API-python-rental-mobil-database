import json
import base64
import matplotlib.image as mpimg

img = mpimg.imread('F:\\Backup_picture\\6.jpg')

json_gambar = base64.b64encode(img)