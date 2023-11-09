def empty(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]

def transpose(matrix):    
    rows = len(matrix)
    cols = 0 if rows == 0 else len(matrix[0])

    transposed = empty(cols, rows)
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed

def powers(numbers, lower, upper):
    powers = []
    for n in numbers:
        row = [n**e for e in range(lower, upper + 1)]
        powers.append(row)
    
    return powers

def matmul(A, B):
    rows = len(A)
    cols = 0 if rows == 0 else len(B[0])

    C = empty(rows, cols)
    for i in range(rows):
        for j in range(cols):
            C[i][j] = sum([a * b for a, b in zip(A[i], transpose(B)[j])])

    return C

def invert(matrix):
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    det = a*d - b*c
    return [
        [d/det,-b/det],
        [-c/det, a/det]
    ]

def loadtxt(path):
    file = open(path)
    lines = file.read().splitlines()
    matrix = []

    for line in lines:
        row = [eval(n) for n in line.split()]
        matrix.append(row)
    
    return matrix