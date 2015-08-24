#coding=utf-8
import sys
import os

class Algorithm(object):
	"""docstring for Algorithm"""
	def __init__(self, numA, numB):
		self.numA = numA
		self.numB = numB

class Add(Algorithm):
	"""docstring for Add"""
	def __init__(self, numA, numB):
		self.numA = numA
		self.numB = numB
	def get_result(self):
		return self.numA + self.numB

class Minus(Algorithm):
	"""docstring for Add"""
	def __init__(self, numA, numB):
		self.numA = numA
		self.numB = numB
	def get_result(self):
		return self.numA - self.numB
		
class Multiply(Algorithm):
	"""docstring for Add"""
	def __init__(self, numA, numB):
		self.numA = numA
		self.numB = numB
	def get_result(self):
		return self.numA * self.numB

class Divide(Algorithm):
	"""docstring for Add"""
	def __init__(self, numA, numB):
		self.numA = numA
		self.numB = numB
	def get_result(self):
		return self.numA / self.numB

class Factory(object):
	"""docstring for Factory"""
	def __init__(self, numA, numB, operator):
		self.operator = operator
		self.mapping = {}
		self.mapping['+'] = Add(numA, numB)
		self.mapping['-'] = Minus(numA, numB)
		self.mapping['*'] = Multiply(numA, numB)
		self.mapping['/'] = Divide(numA, numB)
	def result(self):
		return self.mapping[self.operator].get_result()


if __name__ == '__main__':
	a = 2
	b = 1
	c = '+'
	f = Factory(a,b,c)
	f.result()
	print f.result()
		
		
