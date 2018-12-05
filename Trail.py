from ValueOperation import saveValue
import tensorflow as tf
from GetImageValue import getImageValue
from VerityCode import veritify


def train():
    IMAGE_X, IMAGE_Y = getImageValue()

    x = tf.placeholder(dtype=tf.float32, shape=(None, 360))
    y_ = tf.placeholder(dtype=tf.float32, shape=(None, 33))

    w1 = tf.Variable(tf.random_normal((360, 1000), seed=1, stddev=1), dtype=tf.float32)
    w2 = tf.Variable(tf.random_normal((1000, 1000), seed=1, stddev=1), dtype=tf.float32)
    w3 = tf.Variable(tf.random_normal((1000, 33), seed=1, stddev=1), dtype=tf.float32)

    a1 = tf.sigmoid(tf.matmul(x, w1))
    a2 = tf.sigmoid(tf.matmul(a1, w2))
    y = tf.sigmoid(tf.matmul(a2, w3))

    global_step = tf.Variable(0)
    learning_rate = tf.train.exponential_decay(
        0.1, global_step, 100, 0.96, staircase=True
    )

    loss = -tf.reduce_mean(
        y_ * tf.log(tf.clip_by_value(y, 1e-10, 1.0)) + (1 - y_) * tf.log(tf.clip_by_value((1 - y), 1e-10, 1.0))
    ) + tf.reduce_mean(w1 * w1) + tf.reduce_mean(w2 * w2) + tf.reduce_mean(w3 * w3)

    tf.add_to_collection('losses', loss)

    train_step = tf.train.AdamOptimizer(learning_rate).minimize(loss, global_step=global_step)

    with tf.Session() as sess:
        initParam = tf.global_variables_initializer()
        sess.run(initParam)
        STEPS = 100000
        for i in range(STEPS):
            sess.run(train_step, feed_dict={x: IMAGE_X, y_: IMAGE_Y})
            if i % 1000 == 0:
                print(str(i) + '...')
                print(sess.run(loss, feed_dict={x: IMAGE_X, y_: IMAGE_Y}))
                saveValue(sess.run(w1), sess.run(w2), sess.run(w3))
                veritify()
