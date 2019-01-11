import sys
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
mean0=[]
mean1=[]
for i in range (0,cols,1):	
	mean0.append(1)
	mean1.append(1)

num0=0.000000001
num1=0.000000001
for i in range(0,rows,1):
	if (labels.get(i) != None and labels.get(i) == 0):
		num0+=1
		for j in range (0,cols,1):
			mean0[j] += data[i][j]
	if (labels.get(i) != None and labels.get(i) == 1):
		num1+=1
		for j in range (0,cols,1):
			mean1[j] += data[i][j]
for j in range (0,cols,1):
	mean0[j] /= num0
	mean1[j] /= num1


sd0=[]
sd1=[]
for i in range (0,cols,1):
	sd0.append(0.000000001)
	sd1.append(0.000000001)

for i in range(0,rows,1):
	if (labels.get(i) != None and labels.get(i) == 0):
		for j in range (0,cols,1):
			sd0[j] += ((mean0[j] - data[i][j])**2)
	if (labels.get(i) != None and labels.get(i) == 1):
		for j in range (0,cols,1):
			sd1[j] += ((mean1[j] - data[i][j])**2)

for j in range (0,cols,1):
	sd0[j] /= num0
	sd1[j] /= num1


for i in range (0,rows,1):
	w0=0
	w1=0	
	if (labels.get(i) == None):
		for j in range (0,cols,1):
			w0 += ((mean0[j] - data[i][j])**2)/sd0[j]
			w1 += ((mean1[j] - data[i][j])**2)/sd1[j]		
		if (w0 > w1):	
			print("1",i)
		else:
			print("0",i)
