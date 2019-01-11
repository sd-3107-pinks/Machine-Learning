import sys
import random
import math

filename=sys.argv[1]
f1=open(filename,"r")
i=0
data=[]
l=f1.readline()
while (l != ""):
	a=l.split()
	l2 =[]
	for j in range (0,len(a),1):
		l2.append(float(a[j]))
	data.append(l2)
	l=f1.readline()

rows=len(data)
cols=len(data[0])
f1.close()

#Read labels from file
filename = sys.argv[2]
f2=open(filename,"r")
labels={}
l2=f2.readline()
while (l2 != ''):
	b=l2.split()
	labels[int(b[1])] = int(b[0])
	l2=f2.readline()


f2.close()

#dot product function
def dot_product(arg1,arg2):
        dp1=0
        for j in range(0,cols,1):
                dp1 += arg1[j]*arg2[j]
        return dp1;

#Initialize w
w=[]
for j in range(0,cols,1):
	w.append(float(0.02*random.random()- 0.01))	

#gradient descent iteration
eta=0.0001
stop_condition=0.001
error=0
while True:
	prevobj=error
	#compute gradient and error
	gradient=[]
	error=0
	for i in range (0,rows,1):
		if (labels.get(i) != None and labels.get(i) == 0):
			dp=dot_product(w,data[i]);
			error += (labels[i] - dp)**2
			for j in range (0,cols,1):
				gradient.append(float((labels[i]-dp)*data[i][j]))
	
	if abs(prevobj-error)<=stop_condition:       
	        break 
	#update w
	for j in range (0,cols,1):
		w[j]=w[j]+eta*gradient[j]

#distance from origin calculation
print("w: ", end='')
normw=0
for j in range(0,cols-1,1):
	print(abs(w[j]),'', end='')
	normw += w[j]**2
print()

normw = math.sqrt(normw)
d_origin = abs(w[len(w)-1]/normw)
print("distance from origin: ",d_origin)

#prediction
for i in range(0,rows,1):
    if (labels.get(i) == None):
        dp=0
        for j in range(0,cols,1):
            dp+=data[i][j]*w[j]
            
        if dp>0:
            print("1,",i)
        else:
            print("0,",i)

