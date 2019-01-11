import sys
import random
import math


def gradient_descent(data, trainLabels, rows, cols, eta):

    w = []
    for i in range(0, cols):
        w.append(0.02 * random.random() - 0.01)

    emp_risk = 0
    diff = 1

    while (diff > 0.001):
        dellf = [0] * cols

        for i in range(0, rows, 1):
            if (trainLabels.get(i) != None):
                a1 = func(w, data[i]) - trainLabels[i]
                for k in range(0, cols):
                    dellf[k] += a1 * data[i][k]

        for j in range(0, cols, 1):
            w[j] -= eta * dellf[j]

        prev = emp_risk
        emp_risk = 0

        for j in range(0, rows):
            if (trainLabels.get(j) != None):
                emp_risk += -1 * (trainLabels[j] * math.log(func(w, data[j])) + ((1 - trainLabels[j]) * math.log(1 - func(w, data[j]))))

            diff = abs(prev - emp_risk)

        print('Objective :', str(emp_risk))
    return w


def func(a1, b1):
    dp = dot(a1, b1)
    sigmoid = 1 / (1 + math.exp(-1 * dp))
    if (sigmoid >= 1):
        sigmoid = 0.999999

    return sigmoid


def dot(a, b):

    list1 = []
    for x, y in zip(a, b):
        mul = x * y
        list1.append(mul)
    return sum(list1)


if __name__ == '__main__':

    datafile = sys.argv[1]

    f = open(datafile)
    data = []
    i = 0
    l = f.readline()

    while (l != ''):
        a = l.split()
        l2 = []
        for j in range(0, len(a), 1):
            l2.append(float(a[j]))
        data.append(l2)
        l = f.readline()

    labelfile = sys.argv[2]
    f = open(labelfile)

    trainLabels = {}

    l = f.readline()

    while (l != ''):
        a = l.split()
        trainLabels[int(a[1])] = int(a[0])
        l = f.readline()


    for i in range(0, len(data)):
        data[i].append(1)

    rows = len(data)
    cols = len(data[0])

    eta = 0.01

    w = gradient_descent(data, trainLabels, rows, cols, eta)

    print('W :', w)
    normw = 0
    for i in range(0, cols - 1):
        normw += w[i] ** 2


    normw = math.sqrt(normw)

    print('||w|| :', normw)

    dist = w[len(w) - 1] / normw
    print('Origin distance: ' + str(dist))


    for i in range(0, rows):
        if (trainLabels.get(i) == None):
            dp = dot(w, data[i])
            if (dp > 0):
                print('1', i)
            else:
                print('0', i)












