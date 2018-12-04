import urllib.request
import os
from ChangeToGrayImage import changeToGreyImage


imageUrl = 'http://jw.hzau.edu.cn/CheckCode.aspx'
for i in range(499, 502):
    fileName = str(i) + '.jpg'
    imagePath = 'images/' + fileName
    if not os.path.exists(imagePath):
        file = open(imagePath, 'a+')
        file.close()
    req = urllib.request.urlopen(imageUrl)
    f = open(imagePath, 'wb')
    buf = req.read()
    f.write(buf)
    f.close()
    changeToGreyImage(imagePath, i)
