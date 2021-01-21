import math

# Functions

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


# Algorithms

def bissection(f, a, b, e):
    erro = abs(b-a)
    while erro > e:
        x = (a+b)/2
        if (f(a)*f(x)) < 0:
            b = x
        else:
            a = x
        erro = abs(b-a)
    return x

def false_position(f, a, b, e):
    erro= e+1
    x = 10000
    while erro > e:
        xn = (a*f(b)- b*f(a))/(f(b)-f(a))
        if (f(a)*f(x)) < 0:
            b = xn
        else:
            a = xn
        erro = abs(xn-x)
        x = xn
    return xn

def newton(f, df, x0, e):
    erro = e+1
    while erro > e:
        xn = x0 - f(x0)/df(x0)
        erro = abs(xn-x0)
        x0 = xn
    return xn

def picardo_peano(g, dg, x0, e):
    erro = e+1
    if abs(dg(x0)) >= 1:
        return "Impossivel aplicar picardo-peano"
    while erro > e:
        xn = g(x0)
        erro = abs(xn-x0)
        x0 = xn
    return xn


print(bissection(f1, -2, -1, 0.001))
print(false_position(f1, -2, -1, 0.001))
print(newton(f2, df2, 4, 0.001))
print(picardo_peano(g1, dg1, 4, 0.001))
print(picardo_peano(g2, dg2, 4, 0.001))