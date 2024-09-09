import tensorflow as tf

a = tf.constant(5.0)
b = tf.constant(6.0)
print(a, b)
sum1 = tf.add(a, b)
print(sum1)
with tf.Session() as sess:
    print(sess.run(sum1))
