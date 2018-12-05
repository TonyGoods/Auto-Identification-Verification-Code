import os
import urllib.request

from PIL import Image
import numpy as np
import tensorflow as tf
from ValueOperation import getValue

content = ['0', '1', '2', '3', '4', '5', '6', '7', '8', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']


def use(fileName):
    image = Image.open(fileName)
    image.show()
    binary_image = image.convert('1')
    binary_array = np.array(binary_image, dtype='i')
    cutting_array = binary_array[:24, 2:54]

    image_shape = cutting_array.shape
    for i in range(image_shape[0]):
        for j in range(image_shape[1]):
            if cutting_array[i, j] == 0:
                if i - 1 > -1 and cutting_array[i - 1, j] == 0:
                    continue
                elif i + 1 < image_shape[0] and cutting_array[i + 1, j] == 0:
                    continue
                elif j + 1 < image_shape[1] and cutting_array[i, j + 1] == 0:
                    continue
                elif j - 1 > -1 and cutting_array[i, j - 1] == 0:
                    continue
                cutting_array[i, j] = 1
            else:
                if i - 1 > -1 and cutting_array[i - 1, j] == 1:
                    continue
                elif i + 1 < image_shape[0] and cutting_array[i + 1, j] == 1:
                    continue
                elif j + 1 < image_shape[1] and cutting_array[i, j + 1] == 1:
                    continue
                elif j - 1 > -1 and cutting_array[i, j - 1] == 1:
                    continue
                cutting_array[i, j] = 0

    cutting_array_1 = cutting_array[:, :int(image_shape[1] / 4 + 2)]
    cutting_array_2 = cutting_array[:, int(image_shape[1] / 4 - 1): int(image_shape[1] / 4 * 2 + 1)]
    cutting_array_3 = cutting_array[:, int(image_shape[1] / 4 * 2 - 1):int(image_shape[1] / 4 * 3 + 1)]
    cutting_array_4 = cutting_array[:, int(image_shape[1] / 4 * 3 - 2):int(image_shape[1])]

    code = ''
    x = tf.placeholder(dtype=tf.float32, shape=(None, 360))

    w1, w2, w3 = getValue()
    a1 = tf.sigmoid(tf.matmul(x, w1))
    a2 = tf.sigmoid(tf.matmul(a1, w2))
    y = tf.sigmoid(tf.matmul(a2, w3))

    with tf.Session() as sess:
        code += content[np.argmax(
            sess.run(y, {x: cutting_array_1.reshape(1, cutting_array_1.shape[0] * cutting_array_1.shape[1])})[0])]
        code += content[np.argmax(
            sess.run(y, {x: cutting_array_2.reshape(1, cutting_array_2.shape[0] * cutting_array_2.shape[1])})[0])]
        code += content[np.argmax(
            sess.run(y, {x: cutting_array_3.reshape(1, cutting_array_3.shape[0] * cutting_array_3.shape[1])})[0])]
        code += content[np.argmax(
            sess.run(y, {x: cutting_array_4.reshape(1, cutting_array_4.shape[0] * cutting_array_4.shape[1])})[0])]

    print(code)


if __name__ == '__main__':
    imageUrl = 'http://jw.hzau.edu.cn/CheckCode.aspx'
    imagePath = 'test/test.jpg'
    if not os.path.exists(imagePath):
        file = open(imagePath, 'a+')
        file.close()
    req = urllib.request.urlopen(imageUrl)
    f = open(imagePath, 'wb')
    buf = req.read()
    f.write(buf)
    f.close()
    use(imagePath)
