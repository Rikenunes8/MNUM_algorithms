import math

# Functions

def f1(x):
    return (2*x+1)**2-5*math.cos(10*x)
def sim_f1(x):
    return -f1(x)

def f2(x, y):
    return y**2-2*x*y-6*y+2*x**2+12
def df2dx(x, y):
    return -2*y + 4*x
def df2dy(x, y):
    return 2*y - 2*x - 6

def f3(x, y):
    return math.sin(x/2) + x**2 - math.cos(y)
def iHessian(x, y):
    return [[1/(2-math.sin(x/2)/4), 0], [0, 1/math.cos(y)]]
def df3dx(x, y):
    return 2*x + math.cos(x/2)/2
def df3dy(x, y):
    return math.sin(y)


# Algorithms

def aurea(f, x1, x2, e):
    B = (5**0.5-1)/2
    A = B**2
    erro = e+1
    while erro > e:
        x3 = x1 + A*(x2-x1)
        x4 = x1 + B*(x2-x1)
        if f(x3) < f(x4):
            x2 = x4
        else:
            x1 = x3
        erro = abs(x2-x1)
    return x1, x2

def gradiente_min(f, dx, dy, x, y, h, e):
    erro_x = e+1
    erro_y = e+1
    while erro_x > e or erro_y > e:
        xn = x - h * dx(x, y)
        yn = y - h * dy(x, y)
        if f(xn, yn) < f(x, y):
            h *= 2
            erro_x = abs(xn-x)
            erro_y = abs(yn-y)
            x, y = xn, yn
        else:
            h /= 2
    return xn, yn

def gradiente_max(f, dx, dy, x, y, h, e):
    erro_x = e+1
    erro_y = e+1
    while erro_x > e or erro_y > e:
        xn = x + h * dx(x, y)
        yn = y + h * dy(x, y)
        if f(xn, yn) > f(x, y):
            h *= 2
            erro_x = abs(xn-x)
            erro_y = abs(yn-y)
            x, y = xn, yn
        else:
            h /= 2
    return xn, yn

def quadratic(iHessian, f, dx, dy, x, y, e):
    erro_x = e+1
    erro_y = e+1
    while erro_x > e or erro_y > e:
        iH = iHessian(x, y)
        xn = x - (iH[0][0]*dx(x,y) + iH[0][1]*dy(x,y))
        yn = y - (iH[1][0]*dx(x,y) + iH[1][1]*dy(x,y))
        erro_x = abs(xn-x)
        erro_y = abs(yn-y)
        x, y = xn, yn
    return xn, yn

def LM(iHessian, f, dx, dy, x, y, h, e):
    erro_x = e+1
    erro_y = e+1
    while erro_x > e or erro_y > e:
        iH = iHessian(x, y)
        hx_quad = iH[0][0]*dx(x,y) + iH[0][1]*dy(x,y)
        hy_quad = iH[1][0]*dx(x,y) + iH[1][1]*dy(x,y)
        hx_grad = h * dx(x,y)
        hy_grad = h * dy(x,y)
        xn = x - (hx_quad + hx_grad)
        yn = y - (hy_quad + hy_grad)
        if (f(xn,yn) < f(x,y)):
            h *= 2
            erro_x = abs(xn-x)
            erro_y = abs(yn-y)
            x, y = xn, yn
        else:
            h /= 2
    return xn, yn



# Run

print(aurea(f1, -1, 0, 0.001))
t = aurea(sim_f1, -1, 0, 0.001)
print(t[0], -t[1])

print(gradiente_min(f2, df2dx, df2dy, 1, 1, 0.001, 1))
print(gradiente_max(f2, df2dx, df2dy, -1, 1, 0.001, 1))
print(quadratic(iHessian, f3, df3dx, df3dy, -3, -1, 0.001))
print(LM(iHessian, f3, df3dx, df3dy, -10, -1, 0.001, 0.01))

