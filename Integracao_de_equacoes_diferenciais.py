def df(x, y):
    return x**2 + y**2

def qc(f, df, a, b, h):
    q = (f(df, a, b, h/2)-f(df, a, b, h))/(f(df, a, b, h/4)-f(df, a, b, h/2))
    return q

# Equações diferenciais

def euler(f, a, b, h):
    x, xn = 0, 0
    y, yn = 0, 0
    for i in range(round((b-a)/h)):
        xn = x + h
        yn = y + f(x, y)*h
        x = xn
        y = yn
    return yn
print("Euler")
print(euler(df, 0, 1.4, 0.1))
print(euler(df, 0, 1.4, 0.05))
print(euler(df, 0, 1.4, 0.025))

print(qc(euler, df, 0, 1.4, 0.1))


def euler_modificado(f, a, b, h):
    x, y, yn_1 = 0, 0, 0
    for i in range(round((b-a)/h)):
        xn = x + h
        yn = y + (f(xn, yn_1+2*f(x, y)*h) + f(x, y))/2*h
        yn_1 = y
        x, y = xn, yn
    return yn

print("Euler modificado")
print(euler_modificado(df, 0, 1.4, 0.1))
print(euler_modificado(df, 0, 1.4, 0.05))
print(euler_modificado(df, 0, 1.4, 0.025))

print(qc(euler_modificado, df, 0, 1.4, 0.1))

def rk2(f, a, b, h):
    x, xn, y, yn = 0, 0, 0, 0
    for i in range(round((b-a)/h)):
        xn = x + h
        yn = y + h * f(x+h/2, y+h/2*f(x, y))
        #print(round(xn,2), round(yn, 4))
        x = xn
        y = yn
    return yn;

print("RK2")
print(rk2(df, 0, 1.4, 0.1))
print(rk2(df, 0, 1.4, 0.05))
print(rk2(df, 0, 1.4, 0.025))

print(qc(rk2, df, 0, 1.4, 0.025))


def delta(n, f, h, x, y):
    if n == 1:
        return h*f(x, y)
    elif n == 2:
        return h*f(x+h/2, y+delta(1, f, h, x, y)/2)
    elif n == 3:
        return h*f(x+h/2, y+delta(2, f, h, x, y)/2)
    elif n == 4:
        return h*f(x+h, y+delta(3, f, h, x, y))


def rk4(f, a, b, h):
    x, xn, y, yn = a, 0, 0, 0
    for i in range(round((b-a)/h)):
        xn = x + h
        yn = y + delta(1, f, h, x, y)/6+delta(2,f,h,x,y)/3+delta(3,f,h,x,y)/3+delta(4,f,h,x,y)/6
        #print(round(xn,2), round(yn, 4))
        x = xn
        y = yn
    return yn
print("RK4")
print(rk4(df, 0, 1.4, 0.1))
print(rk4(df, 0, 1.4, 0.05))
print(rk4(df, 0, 1.4, 0.025))

print(qc(rk4, df, 0, 1.4, 0.1))



# Sistema de equações diferenciais

def qc(f, dy, dz, a, b, h, i):
    s = f(dy, dz, a, b, h)[i]
    sl = f(dy, dz, a, b, h/2)[i]
    sll = f(dy, dz, a, b, h/4)[i]
    q = (sl-s)/(sll-sl)
    return round(q, 5)

def erro(f, j, dy, dz, a, b, h, i):
    sl = f(dy, dz, a, b, h/2)[i]
    sll = f(dy, dz, a, b, h/4)[i]
    return round((sll-sl)/(2**j-1), 5)

def dydx(x, y, z):
    return z*y+x
def dzdx(x, y, z):
    return z*x+y

def sis_euler(dy, dz, a, b, h):
    x, y, z = 0, 1, 1
    xn, yn, zn = 0, 0, 0
    for i in range(round((b-a)/h)):
        xn = x + h
        yn = y + h * dy(x, y, z)
        zn = z + h * dz(x, y, z)
        # if round(xn, 2) == 0.1 or round(xn, 2) == 0.5:
        #     print(round(xn, 2), round(yn, 5), round(zn, 5))
        x = xn
        y = yn
        z = zn
    return (yn, zn)

print("Sis_euler")
print(sis_euler(dydx, dzdx, 0, 0.5, 0.05))
print("QC y:", qc(sis_euler, dydx, dzdx, 0, 0.5, 0.005, 0))
print("Erro y:", erro(sis_euler, 2, dydx, dzdx, 0, 0.5, 0.05, 0))
print("QC z:", qc(sis_euler, dydx, dzdx, 0, 0.5, 0.005, 1))
print("Erro z:", erro(sis_euler, 2, dydx, dzdx, 0, 0.5, 0.05, 1))




def sis_rk2(dy, dz, a, b, h):
    x, y, z = 0, 1, 1
    xn, yn, zn = 0, 0, 0
    for i in range(round((b-a)/h)):
        xn = x + h
        yn = y + h*dy(x+h/2, y+h/2*dy(x,y,z), z+h/2*dz(x,y,z))
        zn = z + h*dz(x+h/2, y+h/2*dy(x,y,z), z+h/2*dz(x,y,z))
        # if round(xn, 2) == 0.1 or round(xn, 2) == 0.5:
        #     print(round(xn, 2), round(yn, 5), round(zn, 5))
        x = xn
        y = yn
        z = zn
    return (yn, zn)

print("\nSis_rk2")
print(sis_rk2(dydx, dzdx, 0, 0.5, 0.05))
print("QC y:", qc(sis_rk2, dydx, dzdx, 0, 0.5, 0.005, 0))
print("Erro y:", erro(sis_rk2, 2, dydx, dzdx, 0, 0.5, 0.05, 0))
print("QC z:", qc(sis_rk2, dydx, dzdx, 0, 0.5, 0.005, 1))
print("Erro z:", erro(sis_rk2, 2, dydx, dzdx, 0, 0.5, 0.05, 1))




import math

def dydx(x, y):
    return -2*y+4*math.e**(-x)
def dzdx(y,z):
    return -y*z**2/3

def sis_rk4(dy, dz, a, b, h):
    x, y, z = 0, 2, 4
    xn, yn, zn = 0, 0, 0
    for i in range(round((b-a)/h)):
        dy1 = h*dy(x, y)
        dz1 = h*dz(y, z)
        dy2 = h*dy(x+h/2, y+dy1/2)
        dz2 = h*dz(y+dy1/2, z+dz1/2)
        dy3 = h*dy(x+h/2,y+dy2/2)
        dz3 = h*dz(y+dy2/2, z+dz2/2)
        dy4 = h*dy(x+h, y+dy3)
        dz4 = h*dz(y+dy3, z+dz3)
        hy = (dy1/6 + dy2/3 + dy3/3 + dy4/6)
        hz = (dz1/6 + dz2/3 + dz3/3 + dz4/6)
        xn = x + h
        yn = y + hy
        zn = z + hz
        x = xn
        y = yn
        z = zn
    return (xn, round(yn, 5), round(zn, 5))

print(sis_rk4(dydx, dzdx, 0, 0.2, 0.2))
