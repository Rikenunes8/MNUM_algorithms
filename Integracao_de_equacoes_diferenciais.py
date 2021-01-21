import math


# Convergence Quotient and Errors

def qc(met, f, a, b, h):
    s = met(f, a, b, h)
    sl = met(f, a, b, h/2)
    sll = met(f, a, b, h/4)
    return (sl-s)/(sll-sl)
def erro(met, f, a, b, h, ordem):
    sll = met(f, a, b, h/4)
    sl = met(f, a, b, h/2)
    return (sll-sl)/(2**ordem-1)


def qc_sis(met, dy, dz, a, b, h, i):
    s = met(dy, dz, a, b, h)[i]
    sl = met(dy, dz, a, b, h/2)[i]
    sll = met(dy, dz, a, b, h/4)[i]
    return (sl-s)/(sll-sl)
def erro_sis(met, dy, dz, a, b, h, ordem, i):
    sll = met(dy, dz, a, b, h/4)[i]
    sl = met(dy, dz, a, b, h/2)[i]
    return (sll-sl)/(2**ordem-1)


# Functions

def df(x, y):
    return x**2 + y**2

def dydx1(x, y, z):
    return z*y+x
def dzdx1(x, y, z):
    return z*x+y


def dydx2(x, y, z):
    return -2*y+4*math.e**(-x)
def dzdx2(x, y, z):
    return -y*z**2/3


# Algorithms


# Equações diferenciais

def euler(f, a, b, h):
    x, y = 0, 0
    for n in range(round((b-a)/h)):
        xn = x + h
        yn = y + h*f(x, y)
        x, y = xn, yn
    return yn

def euler_modificado(f, a, b, h):
    x, y = 0, 0
    y_older = 0
    for n in range(round((b-a)/h)):
        p = y_older+2*f(x, y)*h
        p = f(x+h, p)
        hy = (p+f(x,y))*h/2
        xn = x + h
        yn = y + hy
        y_older = y
        x, y = xn, yn
    return yn

def rk2(f, a, b, h):
    x, y = 0, 0
    for n in range(round((b-a)/h)):
        hy = h * f(x+h/2, y+h/2*f(x, y))
        xn = x + h
        yn = y + hy
        x, y = xn, yn
    return yn

def rk4(f, a, b, h):
    x, y = 0, 0
    for n in range(round((b-a)/h)):
        dy1 = h * f(x, y)
        dy2 = h * f(x+h/2, y+dy1/2)
        dy3 = h * f(x+h/2, y+dy2/2)
        dy4 = h * f(x+h, y+dy3)
        hy = dy1/6 + dy2/3 + dy3/3 + dy4/6
        xn = x + h
        yn = y + hy
        x, y = xn, yn
    return yn


# Sistema de equações diferenciais

def sis_euler(dy, dz, a, b, h):
    x, y, z = 0, 1, 1
    for n in range(round((b-a)/h)):
        hy = h * dy(x, y, z)
        hz = h * dz(x, y, z)
        xn = x + h
        yn = y + hy
        zn = z + hz
        x, y, z = xn, yn, zn
    return yn, zn

def sis_rk2(dy, dz, a, b, h):
    x, y, z = 0, 1, 1
    for n in range(round((b-a)/h)):
        hy = h * dy(x+h/2, y+h/2*dy(x, y, z), z+h/2*dz(x,y,z))
        hz = h * dz(x+h/2, y+h/2*dy(x, y, z), z+h/2*dz(x,y,z))
        xn = x + h
        yn = y + hy
        zn = z + hz
        x, y, z = xn, yn, zn
    return yn, xn

def sis_rk4(dy, dz, a, b, h):
    x, y, z = 0, 2, 4
    for i in range(round((b-a)/h)):
        dy1 = h*dy(x, y, z)
        dz1 = h*dz(x, y, z)
        dy2 = h*dy(x+h/2, y+dy1/2, z+dz1/2)
        dz2 = h*dz(x+h/2, y+dy1/2, z+dz1/2)
        dy3 = h*dy(x+h/2,y+dy2/2, z+dz2/2)
        dz3 = h*dz(x+h/2,y+dy2/2, z+dz2/2)
        dy4 = h*dy(x+h, y+dy3, z+dz3)
        dz4 = h*dz(x+h, y+dy3, z+dz3)
        hy = (dy1/6 + dy2/3 + dy3/3 + dy4/6)
        hz = (dz1/6 + dz2/3 + dz3/3 + dz4/6)
        xn = x + h
        yn = y + hy
        zn = z + hz
        x, y, z = xn, yn, zn
    return (xn, round(yn, 5), round(zn, 5))


# Run

print(euler(df, 0, 1.4, 0.1))
print(euler_modificado(df, 0, 1.4, 0.1))
print(rk2(df, 0, 1.4, 0.1))
print(rk4(df, 0, 1.4, 0.1))

print(qc(euler, df, 0, 1.4, 0.1))
print(qc(euler_modificado, df, 0, 1.4, 0.1))
print(qc(rk2, df, 0, 1.4, 0.025))
print(qc(rk4, df, 0, 1.4, 0.1))


print("Sis_euler")
print(sis_euler(dydx1, dzdx1, 0, 0.5, 0.05))
print("QC y:", qc_sis(sis_euler, dydx1, dzdx1, 0, 0.5, 0.005, 0))
print("Erro y:", erro_sis(sis_euler, dydx1, dzdx1, 0, 0.5, 0.05, 2, 0))
print("QC z:", qc_sis(sis_euler, dydx1, dzdx1, 0, 0.5, 0.005, 1))
print("Erro z:", erro_sis(sis_euler, dydx1, dzdx1, 0, 0.5, 0.05, 2, 1))

print("\nSis_rk2")
print(sis_rk2(dydx1, dzdx1, 0, 0.5, 0.05))
print("QC y:", qc_sis(sis_rk2, dydx1, dzdx1, 0, 0.5, 0.005, 0))
print("Erro y:", erro_sis(sis_rk2, dydx1, dzdx1, 0, 0.5, 0.05, 2, 0))
print("QC z:", qc_sis(sis_rk2, dydx1, dzdx1, 0, 0.5, 0.005, 1))
print("Erro z:", erro_sis(sis_rk2, dydx1, dzdx1, 0, 0.5, 0.05, 2, 1))

print(sis_rk4(dydx2, dzdx2, 0, 0.2, 0.2))
