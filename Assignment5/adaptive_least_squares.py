import sys
import random

def normalize(datafile):
    norml = []

    for i in range(len(datafile[0])):
        norml.append(1)

    for j in range(len(datafile)):
        for k in range(len(datafile[0]) - 1):
            norml[k] += (datafile[j][k]) ** 2

    for i in range(len(datafile)):
        for j in range(len(datafile[0]) - 1):
            datafile[i][j] = (datafile[i][j] / (norml[j]) ** 0.5)

    return datafile

filename = sys.argv[1]
f1 = open(filename, "r")
i = 0
data = []
l = f1.readline()
while (l != ""):
    a = l.split()
    l2 = []
    for j in range(0, len(a), 1):
        l2.append(float(a[j]))
    data.append(l2)
    l = f1.readline()

data = normalize(data)

rows = len(data)
cols = len(data[0])
f1.close()

# Read labels from file
filename = sys.argv[2]
f2 = open(filename, "r")
labels = {}
l2 = f2.readline()
while (l2 != ''):
    b = l2.split()
    labels[int(b[1])] = int(b[0])
    l2 = f2.readline()

f2.close()


# dot product function
def dot_product(arg1, arg2):
    dp1 = 0
    for j in range(0, cols, 1):
        dp1 += arg1[j] * arg2[j]
    return dp1;


# Initialize w
w = []
for j in range(0, cols, 1):
    w.append(float(0.02 * random.random() - 0.01))

eta=0.001
error = 0
stop_condition = 0.001
while True:
    prevobj = error
    # compute gradient
    gradient = []
    for i in range(0, rows, 1):
        if (labels.get(i) != None and labels.get(i) == 0):
            dp = dot_product(w, data[i]);
            for j in range(0, cols, 1):
                gradient.append(float((labels[i] - dp) * data[i][j]))

    # adaptive least square
    eta_list = [1, .1, .01, .001, .0001, .00001, .000001, .0000001, .00000001, .000000001, .0000000001, .00000000001 ]
    bestobj = 1000000000000
    for k in range(0, len(eta_list), 1):
        eta = eta_list[k]

        # update w
        for j in range(0, cols, 1):
            w[j] = w[j] - eta * gradient[j]

        # compute error
        error = 0
        for i in range(0, rows, 1):
            if (labels.get(i) != None and labels.get(i) == 0):
                dp = dot_product(w, data[i]);
                error += (labels[i] - dp) ** 2

        obj=error
        if obj < bestobj:
            bestobj = obj
            best_eta = eta

        for j in range(cols):
            w[j] = w[j] + eta * gradient[j]

    if best_eta != None:
        eta = best_eta

    # update w
    for j in range(0, cols, 1):
        w[j] = w[j] - eta * gradient[j]

    # compute error
    error = 0
    for i in range(0, rows, 1):
        if (labels.get(i) != None and labels.get(i) == 0):
            dp = dot_product(w, data[i]);
            error += (labels[i] - dp) ** 2

    if abs(prevobj - error) <= stop_condition:
        break

# prediction
for i in range(0, rows, 1):
    if (labels.get(i) == None):
        dp = 0
        for j in range(0, cols, 1):
            dp += data[i][j] * w[j]

        if dp > 0:
            print("1,", i)
        else:
            print("0,", i)
