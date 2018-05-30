import tensorflow as tf
import numpy as np

#AND 연산의 구현
x_data = np.array([[0,0],
                   [0,1],
                   [1,0],
		   [1,1]], dtype = np.float32)
y_data = np.array([[0],
		   [0],
		   [0],
		   [1]], dtype = np.float32)
				  
X = tf.placeholder(tf.float32, [None, 2], name = 'x-input')
Y = tf.placeholder(tf.float32, [None, 1], name = 'y-input')
				  
W = tf.Variable(tf.random_normal([2,1]), name = 'weight') #weight 값
b = tf.Variable(tf.random_normal([1]), name = 'bias') #bias 값

hypothesis = tf.sigmoid(tf.matmul(X, W) + b) #activation function으로 sigmoid 사용

cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1 - Y) * tf.log(1 - hypothesis))
train = tf.train.GradientDescentOptimizer(learning_rate = 0.1).minimize(cost)
# cost값을 최소하하기 위하여 optimizer로 gradientDescent 사용

predicted = tf.cast(hypothesis > 0.5, dtype = tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype = tf.float32))

#sigmoid 함수가 0-1사이의 값을 가지므로 0.5이상일 경우 1로 봄, 그 값을 참값과 비교하고 평균을 잡아서 accuracy로 봄

with tf.Session() as sess:
	sess.run(tf.global_variables_initializer())
	
	for step in range(10001):
		sess.run(train, feed_dict = {X: x_data, Y: y_data})
		
		if step % 100 == 0:
			print(step, sess.run(cost, feed_dict={X: x_data, Y: y_data}), sess.run(W))
			
	h, c, a = sess.run([hypothesis, predicted, accuracy], feed_dict={X: x_data, Y: y_data})
	print("\nHypothesis: ", h, "\nCorrect: ", c, "\nAccuracy: ", a)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
