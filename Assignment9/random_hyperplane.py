import sys
from math import sqrt
from sklearn.svm import *
import random


def dotProduct(w, x):
    dp = 0.0
    for wi, xi in zip(w, x):
        dp += wi * xi
    return dp


def sign(x):
    if (x > 0):
        return 1
    elif (x < 0):
        return -1
    return 0
dataFile = sys.argv[1]
tngLblFile = sys.argv[2]
testDataFile = sys.argv[3]
k = int(sys.argv[4])

# Read training labels file
labels = []
with open(tngLblFile) as infile:
    labels = list(map(lambda x: int(x.split()[0]), infile.readlines()))

# Read training data file
dataSets = []
with open(dataFile) as f:
    for row in f:
        rowArray = list(map(float, row.split()))
        dataSets.append(rowArray)
f.close()
noCols = len(dataSets[0])
noRows = len(dataSets)
testDataSets = []
with open(testDataFile) as f:
    for row in f:
        rowArray = list(map(float, row.split()))
        testDataSets.append(rowArray)
f.close()

w = []
for i in range(0, k, 1):
    w.append([])
    for j in range(0, noCols, 1):
        w[i].append(random.uniform(-1, 1))

print ("random w " + str(w))

z = []
for i, data in enumerate(dataSets):
    z.append([])
    for j in range(0, k, 1):
        z[i].append(sign(dotProduct(w[j], data)))
print ("z " + str(z))
print ("tngLabels " + str(labels))

z1 = []
for i, data in enumerate(testDataSets):
    z1.append([])
    for j in range(0, k, 1):
        z1[i].append(sign(dotProduct(w[j], data)))

print ("z1 " + str(z1))

print('\n ############## Using_RandomHyperPlanes ################### \n')
svm_model = svm_train(labels, z)
training_labels, training_accuracy, training_values = svm_predict(labels, z, svm_model)
print('training data accuracy = ', training_accuracy)

p_labels, p_acc, p_vals = svm_predict([0] * len(z1), z1, svm_model)

print('\n ############## Predicted labels Using_RandomHyperPlanes ################### \n')
with open('Predicted_Labels_Using_RandomHyperPlanes', 'w') as out:
    for i in range(len(p_labels)):
        out.write(str(int(p_labels[i])) + ' ' + str(i) + '\n')
        print(int(p_labels[i]), i)

print('\n ############## Using_OriginalDataPoints ################### \n')
svm_model = svm_train(labels, dataSets)
training_labels, training_accuracy, training_values = svm_predict(labels, dataSets, svm_model)
print('training data accuracy = ', training_accuracy)

p_labels, p_acc, p_vals = svm_predict([0] * len(testDataSets), testDataSets, svm_model)

print('\n ############## Predicted labels Using_OriginalDataPoints ################### \n')
with open('Predicted_Labels_Using_OriginalDataPoints', 'w') as out:
    for i in range(len(p_labels)):
        out.write(str(int(p_labels[i])) + ' ' + str(i) + '\n')
        print(int(p_labels[i]), i)