import os
from GetImageValue import getCVImageValue
import tensorflow as tf
import numpy as np
from ValueOperation import getValue


def veritify():
    x = tf.placeholder(dtype=tf.float32, shape=(None, 360))
    y_ = tf.placeholder(dtype=tf.float32, shape=(None, 33))

    w1, w2, w3 = getValue()
    a1 = tf.sigmoid(tf.matmul(x, w1))
    a2 = tf.sigmoid(tf.matmul(a1, w2))
    y = tf.sigmoid(tf.matmul(a2, w3))

    with tf.Session() as sess:
        path = 'cv Image'
        files = os.listdir(path)
        index = 0
        right = 0
        count = 0
        for cvFile in files:
            imageFiles = os.listdir(path + '/' + cvFile)
            for image in imageFiles:
                test_x, test_y = getCVImageValue(path + '/' + cvFile + '/' + image)
                result = sess.run(y, feed_dict={x: test_x, y_: test_y})
                if np.argmax(result[0]) == index:
                    right += 1
                count += 1
            index += 1
        print(right / count)
