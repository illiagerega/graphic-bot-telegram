from re import L
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
import os

def cycle_stat(count, labels):
    font = {'family': 'Verdana', 'weight': 'normal'}
    rc('font', **font)

    y = np.array(count)

    plt.pie(y, labels = labels)
    #plt.show()
    if os.path.isfile('foo.png'):
        os.remove('foo.png')
        plt.savefig('foo.png')
    else:
        plt.savefig('foo.png')

def stat(x, y):
    plt.plot(x, y)
    #plt.show()
    if os.path.isfile('foo.png'):
        os.remove('foo.png')
        plt.savefig('foo.png')
    else:
        plt.savefig('foo.png')


def klitor_stat(groups, counts):
    plt.bar(groups, counts)
    #plt.show()
    if os.path.isfile('foo.png'):
        os.remove('foo.png')
        plt.savefig('foo.png')
    else:
        plt.savefig('foo.png')

def price_stat(x1, x2, y1, y2):
    plt.plot(x1, y1)
    plt.plot(x2, y2)

    plt.legend()

    #plt.show()
    if os.path.isfile('foo.png'):
        os.remove('foo.png')
        plt.savefig('foo.png')
    else:
        plt.savefig('foo.png')

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1]) #Typo was here

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

#print(line_intersection(((0.5, 0.5), (1.5, 0.5)), ((1, 0), (1, 2))))

#cycle_stat([100, 300, 400, 600], ['a', 'b', 'c', 'd'])
#stat(['a', 'b', 'c', 'd'], [100, 200, -300, 150])
#klitor_stat(['a', 'b', 'c', 'd'], [100, 500, -600, 457])
#price_stat(['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd'], [100, 200, -300, 150], [300, 100, 400, 50])
 