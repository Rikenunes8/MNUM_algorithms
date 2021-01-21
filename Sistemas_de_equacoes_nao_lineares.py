import math

# Functions

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


def h1(x, y):
    return math.sqrt((y*x+5*x-1)/2)
    
def h2(x, y):
    return math.sqrt(x+3*math.log(x))


# Algorithms

def sis_newton(f1, f2, df1dx, df1dy, df2dx, df2dy, x, y, e):
    erro_x = e+1
    erro_y = e+1
    while erro_x > e or erro_y > e:
        detJacob = df1dx(x,y)*df2dy(x,y)-df1dy(x,y)*df2dx(x,y)
        xn = x - (f1(x,y)*df2dy(x,y)-f2(x,y)*df1dy(x,y))/detJacob
        yn = y - (f2(x,y)*df1dx(x,y)-f1(x,y)*df2dx(x,y))/detJacob
        erro_x = abs(xn-x)
        erro_y = abs(yn-y)
        x = xn
        y = yn
    return xn, yn


def sis_picardo_peano(g1, g2, x, y, e):
    erro_x = e+1
    erro_y = e+1
    while erro_x > e or erro_y > e:
        xn = g1(x, y)
        yn = g2(x, y)
        erro_x = abs(xn-x)
        erro_y = abs(yn-y)
        x = xn
        y = yn
    return xn, yn


# Run

print(sis_newton(f1, f2, df1dx, df1dy, df2dx, df2dy, 4, 4, 0.0001))
print(sis_picardo_peano(h1, h2, 4, 4, 0.0001))




######## Other method for Picardo-Peano ########
import sympy as sy

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

