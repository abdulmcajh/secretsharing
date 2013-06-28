#!/usr/bin/python
# Filename: secretsharing.py


import numpy
import re
import warnings
import random
import operator



class SecretSharingSchemaExc(Exception):
	def __init__(self,message):
		self.message_= "K is lower than N, no suitable schema"
		print(message)

class NullSecret(Exception):
	def __init__(self,message1):
		self.message1="The secret should be different from 0, no information in it!!"
		print(message1)


def numLagr(b):    #starting from the list b[]  of people who wants to compute the secret, computes the numLangr
	a=reduce(operator.mul,b,1)
	if (len(b)%2==0):
		print(a)
		return a
	else:
		print(-a)
		return -a	

def denLagr(ID,b):   #computes Lagr interpolation den, IV is the ID 
	for i in range(0,len(b)):
		b[i]=-1*b[i]
	print(b)
	d=numpy.array(b)
	a=ID+d
	print(a)
	print(reduce(operator.mul,a,1))
	return (reduce(operator.mul,a,1))



def LagInterpol(ID,b):  #computes Lagr interpolation coefficient for the IV and the list b (b does not contain ID)
	return (float(numLagr(b))/(denLagr(ID,b)))	
	

def genRandcoeff(k):  #computes the k-1 random coefficient for the k-1 grade poly. The secret is added away in ssSchema(k,m)
	a=[]
	i=0
	while (i<k-1):
		a.append(random.randint(1,100))
		i=i+1
	return a


def ComputeShares(p,x):  #evaluates the poly p in the proper point for every of the x=n people
	a=[]
	i=1
	while (i<x):
		a.append(p(i))
		i=i+1
	return a


def ssSchema(k,m):
	if (k>m):
		#raise SecretSharingSchemaExc(Exception)
		print("k must be greater than n")
		exit()
	else:
		b=[]
		b.append(int(raw_input("Insert your qty:")))
		if (b[0]==0 or b[0]<0):
			print("The secret should be greater than 0")
			exit()
		print(b)
		poly=numpy.poly1d(genRandcoeff(k)+b)
		print(poly)
		print("\n"+"\n")
		print(ComputeShares(poly,m))



#End of secretsharing.py


if __name__== "__main__":
	'''
	p=numpy.poly1d([random.randint(1,100),random.randint(1,100),int(raw_input(">"))])
	print(ComputeShares(p,50))
	print(p)
	'''
	a=int(raw_input(">"))
	b=int(raw_input(">"))
	ssSchema(a,b)
	d=[2,3]
	print(LagInterpol(1,d))
