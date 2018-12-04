import tensorflow as tf
from numpy.random import RandomState
from ValueOperation import saveValue

w1 = tf.Variable(tf.random_normal((2, 3), stddev=1, seed=1))
w2 = tf.Variable(tf.random_normal((3, 1), stddev=1, seed=1))

x = tf.placeholder(dtype=tf.float32, shape=(None, 2))
y_ = tf.placeholder(dtype=tf.float32, shape=(None, 1))

a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

batch_size = 8
total_size = 128

rmd = RandomState(1)

x_dataset = rmd.rand(total_size, 2)
y_dataset = [[(int(x1 + x2 < 1))] for x1, x2 in x_dataset]

y = tf.sigmoid(y)
cross_entropy = -tf.reduce_mean(
    y_ * tf.log(tf.clip_by_value(y, 1e-10, 1.0)) + (1 - y_) * tf.log(tf.clip_by_value(1 - y, 1e-10, 1.0))
)

train_step = tf.train.AdagradOptimizer(0.31).minimize(cross_entropy)

STEPS = 10

with tf.Session() as sess:
    initializer = tf.global_variables_initializer()
    sess.run(initializer)

    for i in range(STEPS):
        start = (i * batch_size) % total_size
        end = min(start + batch_size, total_size)
        sess.run(train_step, feed_dict={x: x_dataset[start:end], y_: y_dataset[start: end]})
        if i % 5000 == 0:
            print(sess.run(w1))
            print(sess.run(w2))
    saveValue(sess.run(w1), sess.run(w2), sess.run(w2))
