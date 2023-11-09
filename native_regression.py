import matplotlib.pyplot as plt
from matrix import transpose, powers, matmul, invert, loadtxt

if __name__ == "__main__":
    matrix = loadtxt("chirps.txt")
    X, Y = transpose(matrix)[0], transpose(matrix)[1]

    Xp  = powers(X,0,1)
    Yp  = powers(Y,1,1)
    Xpt = transpose(Xp)

    [[b],[m]] = matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp))

    X2 = [t for t in X]
    Y2 = [b + m * t for t in X2]

    plt.plot(X,Y,'ro')
    plt.plot(X,Y2)
    plt.show()
    