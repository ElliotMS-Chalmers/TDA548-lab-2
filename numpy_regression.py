from numpy import *
import matplotlib.pyplot as plt
import sys

def powers(numbers, lower, upper):
    powers = []
    for n in numbers:
        row = [n**e for e in range(lower, upper + 1)]
        powers.append(row)
    
    return array(powers)

def poly(a,x):
    val = 0
    for i in range(len(a)):
        val += a[i] * (x ** i)
    return val
        
if __name__ == "__main__":
    matrix = loadtxt(sys.argv[1])
    X, Y = transpose(matrix)[0], transpose(matrix)[1]

    Xp  = powers(X, 0, int(sys.argv[2]))
    Yp  = powers(Y, 1, 1)
    Xpt = Xp.transpose()

    a = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
    a = a[:,0]

    X2 = linspace(min(X), max(X), int((max(X)-min(X))/0.2)).tolist()
    Y2 = [poly(a, t) for t in X2]

    plt.plot(X,Y,'ro')
    plt.plot(X2,Y2)
    plt.show()  
    