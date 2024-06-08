#!/usr/bin/python3

# params
cc=6 # <-- number of coefficients
pt=[[2,5],[0,-1],[-2,-2]] # <-- set of points to train on
b=0.001 # <- learning coefficient
it=100

c=[]
# generate default array of coefficients
for i in range(0,cc):
	c.append(1)
print(c)

def f(c,x):
	cc=len(c)
	s=0
	for i in range(0,cc):
		s+=(x**(cc-i))*c[cc-i-1]
		print(cc-i)
	return s
# mean square error
def loss(pt,c):
	s=0
	for i in pt:
		s+=(f(c,i[0])-i[1])**2
	return s
# L' in respect to one point
def lossPrime(pt,c):
	return 2*f(c,pt[0])-pt[1]
	
print(lossPrime(pt[0],c))

