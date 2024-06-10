#!/usr/bin/python3

# params
cc=5 # <-- number of coefficients
pt=[[2,5],[0,-1],[-2,-2]] # <-- set of points to train on
b=0.0001 # <- learning coefficient
it=100

cc+=1
c=[]
# generate default array of coefficients
for i in range(0,cc):
	c.append(1)
print(c)
def f(c,x):
	cc=len(c)
	s=0
	for i in range(cc):
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
	return 2*f(c,pt[0])-2*pt[1]
	
print(lossPrime(pt[0],c))

p=pt[0]
grad=[]
for i in range(len(c)):
	#print(len(c)-i-1)
	grad.append(lossPrime(p,c)*(p[0]**(len(c)-i-1))*(-1)*b)
print(grad)
for i in range(len(c)):
	print(c[i]+grad[i])
