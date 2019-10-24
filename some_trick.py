import os
import tensorflow as tf
# the parents file of the code which you run 
os.path.dirname(os.path.abspath(__file__))

# decay the learning rate
global_step = tf.Variable(0, trainable=False)
boundaries = [int(epoch * self.train_sample // config.batch_size) for epoch in config.LR_EPOCH]
lr_values = [config.learning_rate * (0.5 ** x) for x in range(0, len(config.LR_EPOCH) + 1)]
learning_rate = tf.train.piecewise_constant(global_step, boundaries, lr_values,name='learning_rate')
tf.summary.scalar('learning_rate', learning_rate)
update_ops = tf.get_collection(tf.GraphKeys.UPDATE_OPS)
with tf.control_dependencies(update_ops):
    train_op = tf.train.RMSPropOptimizer(learning_rate, decay=config.decay_rate, momentum=config.momentum).minimize(loss, global_step=global_step)

# MOVING_AVERAGE_DECAY
MOVING_AVERAGE_DECAY = 0.99
LEARNING_RATE_DECAY = 0.99
LEARNING_RATE_BASE = 0.8
variable_averages = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY, global_step)
variables_averages_op = variable_averages.apply(tf.trainable_variables())
learning_rate = tf.train.exponential_decay(
    LEARNING_RATE_BASE,
    global_step,
    mnist.train.num_examples / BATCH_SIZE, LEARNING_RATE_DECAY,
    staircase=True)
train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss, global_step=global_step)
with tf.control_dependencies([train_step, variables_averages_op]):
    train_op = tf.no_op(name='train')
