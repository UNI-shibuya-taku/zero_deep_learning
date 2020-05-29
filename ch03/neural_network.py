# coding: utf-8

import numpy as np
import matplotlib.pylab as plt
def step_function(x):
    return np.array(x > 0, dtype = np.int)

def sigmoid(x):
    return 1/ (1 + np.exp(-x))

def ReLU(x):
    return np.maximum(0, x)

# 恒等関数
def identity_function(x):
    return x

def init_network():
    network = {}
    network['w1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['w2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])
    network['w3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])

    return network

def forword(network, x):
    w1, w2, w3 = network['w1'], network['w2'], network['w3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    A1 = np.dot(x, w1) + b1
    z1 = sigmoid(A1) # 次の入力となる

    A2 = np.dot(z1, w2) + b2
    z2 = sigmoid(A2)

    A3 = np.dot(z2, w3) + b3
    Y = identity_function(A3)
    return Y

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a-c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

a = np.array([0.3, 2.9, 4.0])
y = softmax(a)
print(y)
print(np.sum(y))

"""
network = init_network()
x = np.array([1.0, 5.0])
y = forword(network, x)
print(y)
"""
"""
x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x,y)
y = sigmoid(x)
plt.plot(x,y)
y = ReLU(x)

plt.ylim(-0.1, 3.1)
plt.plot(x,y)
plt.show()
"""
