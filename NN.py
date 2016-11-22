import numpy as np
import math

X = np.array([ [0,0,1],[0,1,1],[1,0,1],[1,1,1]])
y = np.array([[0,0,1,1]]).T
syn0 = 2*np.random.random((3,1)) - 1

def runForward(X, theta):
	return sigmoid(np.dot(X, theta))
def costFunction(X, y, theta):
	m = float(len(X))
	hThetaX = np.array(runForward(X, theta))
	return np.sum(np.abs(y - hThetaX))
def sigmoid(x):
    return 1 / (1 + np.exp(- x))
