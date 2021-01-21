# Data

A1 = [[7, 2, 6], [4, 10, 1], [5, -2, 8]]
b1 = [24, 27, 27]

A2 = [[3, 1, 1], [1, 4, 2], [0, 2, 5]]
b2 = [7, 4, 5]


# Algorithms

def cholesky(A, b):
    B = [[0]*3 for _ in range(len(A))]
    C = [[0]*3 for _ in range(len(A))]
    
    def C1j(j):
        return A[0][j]/B[0][0]
    def Bij(i, j):
        return A[i][j]-sum(B[i][k]*C[k][j] for k in range(j))
    def Cij(i, j):
        return (A[i][j]-sum(B[i][k]*C[k][j] for k in range(i)))/B[i][i]
    
    for i in range(3):
        C[i][i] = 1
    for i in range(3):
        B[i][0] = A[i][0]
        C[0][i] = C1j(i)

    for j in range(1, 3):
        for i in range(j, 3):
            B[i][j] = Bij(i, j)
        for i in range(j+1, 3):
            C[j][i] = Cij(j, i)

    Y = [0]*3
    for i in range(3):
        Y[i] = (b[i]-B[i][0]*Y[0]-B[i][1]*Y[1])/B[i][i]
    X = [0]*3
    for i in range(2, -1, -1):
        X[i] = (Y[i]-C[i][2]*X[2]-C[i][1]*X[1])/C[i][i]
    return X


def jacobi(A, b, x, y, z, e):
    X = [x, y, z]
    Xn = [x, y, z]
    erro = [e+1]*3
    while any(er > e for er in erro):
        for i in range(3):
            Xn[i] = (b[i]-sum(A[i][j]*X[j] for j in range(3) if j != i))/A[i][i]
        erro = [abs(Xn[i]-X[i]) for i in range(3)]
        X = Xn.copy()
    return Xn


def seidel(A, b, x, y, z, e):
    X = [x, y, z]
    Xn = [x, y, z]
    erro = [e+1]*3
    while any(er > e for er in erro):
        for i in range(3):
            Xn[i] = (b[i]-sum(A[i][j]*Xn[j] for j in range(3) if j != i))/A[i][i]
        erro = [abs(Xn[i]-X[i]) for i in range(3)]
        X = Xn.copy()
    return Xn


# def jacobi(A, b, x0, y0, z0, e):
#     erro1, erro2, erro3 = e+1, e+1, e+1
#     while erro1 > e or erro2 > e or erro3 > e:
#         xn = (b[0] - y0*A[0][1] - z0*A[0][2])/A[0][0]
#         yn = (b[1] - x0*A[1][0] - z0*A[1][2])/A[1][1]
#         zn = (b[2] - x0*A[2][0] - y0*A[2][1])/A[2][2]
#         erro1 = abs(xn-x0)
#         erro2 = abs(yn-y0)
#         erro3 = abs(zn-z0)
#         x0, y0, z0 = xn, yn, zn
#     return (round(xn), round(yn), round(zn))

# def seidel(A, b, x0, y0, z0, e):
#     erro1, erro2, erro3 = e+1, e+1, e+1
#     while erro1 > e or erro2 > e or erro3 > e:
#         xn = (b[0] - y0*A[0][1] - z0*A[0][2])/A[0][0]
#         yn = (b[1] - xn*A[1][0] - z0*A[1][2])/A[1][1]
#         zn = (b[2] - xn*A[2][0] - yn*A[2][1])/A[2][2]
#         erro1 = abs(xn-x0)
#         erro2 = abs(yn-y0)
#         erro3 = abs(zn-z0)
#         x0, y0, z0 = xn, yn, zn
#     return (round(xn), round(yn), round(zn))


# Run

print(cholesky(A1, b1))
print(jacobi(A2, b2, 0, 0, 0, 0.00001))
print(seidel(A2, b2, 0, 0, 0, 0.00001))

