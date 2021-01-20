import math
import sympy as sy

######## Metodo de Newton ########

def f1(x, y):
    return 2*x**2-x*y-5*x+1

def f2(x, y):
    return x + 3*math.log(x) - y**2

def df1dx(x, y):
    return 4*x-y-5

def df1dy(x, y):
    return -x

def df2dx(x, y):
    return 1+3/x

def df2dy(x, y):
    return -2*y


def newton(x0, y0, e):
    jacob = df1dx(x0, y0)*df2dy(x0, y0) - df2dx(x0, y0)*df1dy(x0, y0)
    i = 0
    erro1 = e+1
    erro2 = e+1
    while erro1 > e or erro2 > e:
        print(x0, y0, f1(x0, y0), f2(x0, y0), df1dx(x0, y0), df1dy(x0, y0), df2dx(x0, y0), df2dy(x0, y0), '\n')
        xn = x0 - (f1(x0, y0)*df2dy(x0, y0)-f2(x0, y0)*df1dy(x0, y0))/jacob
        yn = y0 - (f2(x0, y0)*df1dx(x0, y0)-f1(x0, y0)*df2dx(x0, y0))/jacob
        erro1 = abs(xn-x0)
        erro2 = abs(yn-y0)
        x0, y0 = xn, yn
        i += 1
    print("Iteration:", i)
    return (xn, yn)


######## Picardo-Peano ########

X, Y = sy.symbols('X, Y')

G1 = sy.sqrt((Y*X+5*X-1)/2)
G2 = sy.sqrt(X+3*sy.log(X))


def g1(x, y):
    return float(G1.subs([(X, x), (Y, y)]))


def g2(x, y):
    return float(G2.subs([(X, x), (Y, y)]))


def check(x, y):
    check1 = float(abs(sy.diff(G1, X).subs([(X, x), (Y, y)])) + abs(sy.diff(G2, X).subs([(X, x), (Y, y)])))
    check2 = float(abs(sy.diff(G1, Y).subs([(X, x), (Y, y)])) + abs(sy.diff(G2, Y).subs([(X, x), (Y, y)])))
    return check1 < 1 and check2 < 1


def picardo_peano(x0, y0, e):
    if not(check(x0, y0)):
        return "Tenta outra transformação"
    i = 0
    erro1 = e + 1
    erro2 = e + 1
    while erro1 > e or erro2 > e:
        xn = g1(x0, y0)
        yn = g2(x0, y0)
        erro1 = abs(xn-x0)
        erro2 = abs(yn-y0)
        x0, y0 = xn, yn
        i += 1
    print("Iteration:", i)
    return (xn, yn)


print(newton(4, 4, 0.00001))
print(picardo_peano(4, 4, 0.00001))
