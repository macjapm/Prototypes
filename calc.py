import math


def dist(a, b):

	delta = [a[0]-b[0], a[1]-b[1]]

	return (delta[0]**2 + delta[1]**2)**0.5

def addVec(a, b):

	return [v1+v2 for (v1, v2) in zip(a, b)]

def multVec(m, vec):
	return [m*v for v in vec]