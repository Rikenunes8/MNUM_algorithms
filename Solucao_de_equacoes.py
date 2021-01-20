import math

def f1(x):
    return 5.5*x**2+6.2*x-2.1

def f2(x):
    return x**2-x-1.2

def df2(x):
    return 2*x-1

def g1(x):
    return x**2-1.2

def dg1(x):
    return 2*x

def g2(x):
    return math.sqrt(x+1.2)

def dg2(x):
    return 1/(2*math.sqrt(x+1.2))


def bissection(a, b, e, f):
    i = 0
    while abs(b-a) > e:
        xn = (b+a)/2
        if f(a) * f(xn) < 0:
            b = xn
        else:
            a = xn
        i += 1
    print("Iteration:", i)
    return (a, b)


def false_position(a, b, e, f):
    i = 0
    x0 = 100000
    erro = e +1
    while erro > e:
        xn = (f(b)*a-f(a)*b)/(f(b)-f(a))
        if f(a) * f(xn) < 0:
            b = xn
        else:
            a = xn
        # erro = abs(b-a)
        erro = abs(xn-x0)
        x0 = xn
        i += 1
    print("Iteration:", i)
    # return (a, b)
    return xn


def newton(x0, e, f, df):
    i = 0
    erro = e+1
    while erro > e:
        # print(round(x0, 3), round(f(x0), 3), round(df(x0), 3), i)
        xn = x0-(f(x0)/df(x0))
        erro = abs(xn-x0)
        x0 = xn
        i += 1
    print("Iteration:", i)
    return xn


def picardo_peano(x0, e, g, dg):
    i = 0
    erro = e +1
    if abs(dg(x0)) >= 1:
        return "Impossivel aplicar picardo-peano"
    while erro > e:
        print(round(x0, 3), round(g(x0), 3), i)
        xn = g(x0)
        erro = abs(xn-x0)
        x0 = xn
        i += 1
    print("Iteration:", i)
    return xn

print(bissection(-2, -1, 0.001, f1))
print(false_position(-2, -1, 0.001, f1))

print(newton(4, 0.001, f2, df2))
print(picardo_peano(4, 0.001, g1, dg1))
print(picardo_peano(4, 0.001, g2, dg2))