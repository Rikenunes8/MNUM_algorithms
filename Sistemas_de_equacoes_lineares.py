# Khaleski

def C1j(A, B, j):
    return round(A[0][j]/B[0][0], 3)

def Bij(A, B, C, i, j):
    return round(A[i][j] - sum([B[i][k]*C[k][j] for k in range(0, j)]), 3)

def Cij(A, B, C, i, j):
    return round(1/B[i][i]*(A[i][j]-sum([B[i][k]*C[k][j] for k in range(0, i)])), 3)


def khaleski():
    A = [[7, 2, 6], [4, 10, 1], [5, -2, 8]]
    B = [[0]*3 for _ in range(len(A))]
    C = [[0]*3 for _ in range(len(A))]

    for i in range(len(A)):
        C[i][i] = 1

    for i in range(3):
        B[i][0] = A[i][0]
        C[0][i] = C1j(A, B, i)
    for j in range(1, 3):
        for i in range(j, 3):
            B[i][j] = Bij(A, B, C, i, j)
        for i in range(j+1, 3):
            C[j][i] = Cij(A, B, C, j, i)
    return (B, C)


# print(khaleski())
B, C = khaleski()

b = [24, 27, 27]

Y = [0] * 3
for i in range(3):
    Y[i] = (b[i]-B[i][0]*Y[0]-B[i][1]*Y[1])/B[i][i]
# print(Y)

X = [0]*3
for i in range(2, -1, -1):
    X[i] = (Y[i]-C[i][2]*X[2]-C[i][1]*X[1])/C[i][i]
    
# print(X)


# Jacobi

# def jacobi(x0, y0, z0, e):
#     A = [[3, 1, 1], [1, 4, 2], [0, 2, 5]]
#     b = [7, 4, 5]
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

def jacobi(X0, e):
    Xn = [0]*3
    A = [[3, 1, 1], [1, 4, 2], [0, 2, 5]]
    b = [7, 4, 5]
    erro = [e+1]*3
    while erro[0] > e or erro[1] > e or erro[2] > e:
        for i in range(3):
            Xn[i] = (b[i]-sum([A[i][j]*X0[j] for j in range(3) if i != j]))/A[i][i]
        erro = [abs(Xn[i]-X0[i]) for i in range(3)]
        X0 = Xn.copy()
    return Xn

print(jacobi([0, 0, 0], 0.00001))


# Seidel

# def seidel(x0, y0, z0, e):
#     A = [[3, 1, 1], [1, 4, 2], [0, 2, 5]]
#     b = [7, 4, 5]
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

def seidel(Xn, e):
    X0 = [1, 1, 1]
    A = [[3, 1, 1], [1, 4, 2], [0, 2, 5]]
    b = [7, 4, 5]
    erro = [e+1]*3
    while erro[0] > e or erro[1] > e or erro[2] > e:
        for i in range(3):
            Xn[i] = (b[i]-sum([A[i][j]*Xn[j] for j in range(3) if i != j]))/A[i][i]
        erro = [abs(Xn[i]-X0[i]) for i in range(3)]
        X0 = Xn.copy()
    return Xn

# print(seidel([0, 0, 0], 0.00001))
