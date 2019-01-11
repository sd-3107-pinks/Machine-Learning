import sys
import random

def gradient_descent(data, trainLabels, rows, cols):

    w = []
    for i in range(0, cols):
        w.append(0.02 * random.random() - 0.01)

    emp_risk = 0
    diff = 1
    eta=0.001

    while (diff > 0.001):
        prev=emp_risk
        dellf = [0] * cols

        # compute gradient
        for i in range(0, rows, 1):
            if (trainLabels.get(i) != None):
                a = trainLabels[i] * dot(w, data[i])
                for j in range(0, cols):
                    if a<1:
                        dellf[j] += -(trainLabels[i] * data[i][j])
                    else:
                        dellf[j] += 0

        # adaptive hinge
        eta_list = [1, .1, .01, .001, .0001, .00001, .000001, .0000001, .00000001, .000000001, .0000000001, .00000000001]
        bestobj = 1000000000000

        for k in range(0, len(eta_list), 1):
            eta = eta_list[k]

            # update w
            for j in range(0, cols, 1):
                w[j] -= eta * dellf[j]

            # calculate error
            emp_risk = 0
            for i in range(0, rows):
                if (trainLabels.get(i) != None):
                    emp_risk += max(0, 1 - (trainLabels.get(i)) * dot(w, data[i]))

            obj = emp_risk
            if obj < bestobj:
                bestobj = obj
                best_eta = eta

            # update w
            for j in range(0, cols, 1):
                w[j] += eta * dellf[j]

        if best_eta != None:
            eta = best_eta

        # update w
        for j in range(0, cols, 1):
            w[j] -= eta * dellf[j]

        emp_risk = 0
        for i in range(0, rows):
            if (trainLabels.get(i) != None):
                emp_risk += max(0, 1 - (trainLabels.get(i)) * dot(w, data[i]))

        diff = abs(prev - emp_risk)

    return w


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

    for i in trainLabels:
        if trainLabels[i] == 0:
            trainLabels[i] = -1

    for i in range(0, len(data)):
        data[i].append(1)

    rows = len(data)
    cols = len(data[0])

    w = gradient_descent(data, trainLabels, rows, cols)

    for i in range(0, rows):
        if (trainLabels.get(i) == None):
            dp = dot(w, data[i])
            if (dp > 0):
                print('1', i)
            else:
                print('0', i)

