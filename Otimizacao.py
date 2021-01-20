import math


######### Metodo de Aurea ##############


def f(x):
    return (2*x+1)**2-5*math.cos(10*x)

def sim_f(x):
    return -f(x)

def aurea(func, x1, x2, e):
    B = (math.sqrt(5)-1)/2
    A = B**2
    erro = e+1
    while (erro>e):
        x3 = x1 + A * (x2-x1)
        x4 = x1 + B * (x2-x1)
        if func(x3)<func(x4):
            x2 = x4
        else:
            x1 = x3
        erro = abs(x2-x1)
    return (x1, func(x1))
# Get minimum
# print(aurea(f, -1, 0, 0.001))
# Get maximum
# t = aurea(sim_f, -1, 0, 0.001)
# print(t[0], -t[1])


############ Metodo do gradiente #############

def f(x, y):
    return y**2-2*x*y-6*y+2*x**2+12

def dfdx(x, y):
    return -2*y + 4*x

def dfdy(x, y):
    return 2*y - 2*x - 6

def gradiente_min(f, dx, dy, x, y, e, h):
    i = 0
    erro_x = e+1
    erro_y = e+1
    while (erro_x > e or erro_y > e):
        xn = x - h * dx(x, y)
        yn = y - h * dy(x, y)
        if f(xn, yn) < f(x, y):
            h = h*2
            erro_x = abs(xn-x)
            erro_y = abs(yn-y)
        else:
            h = h/2
        x = xn
        y = yn
        i += 1
    print(i)
    return xn, yn, f(xn, yn)

def gradiente_max(f, dx, dy, x, y, e, h):
    i = 0
    erro_x = e+1
    erro_y = e+1
    while (erro_x > e or erro_y > e):
        print(i, h, x, y)
        i += 1
        xn = x + h * dx(x, y)
        yn = y + h * dy(x, y)
        if f(xn, yn) > f(x, y):
            h = h*2
            erro_x = abs(xn-x)
            erro_y = abs(yn-y)
        else:
            h = h/2
        x = xn
        y = yn
    return f(xn, yn)

# print(gradiente_min(f, dfdx, dfdy, 1, 1, 0.001, 1))
# print(gradiente_max(f, dfdx, dfdy, -1, 1, 0.001, 1))



############## Metodo quadratica ##########################

def f(x, y):
    return math.sin(x/2) + x**2 - math.cos(y)

def iHessian(x, y):
    return [[1/(2-math.sin(x/2)/4), 0], [0, 1/math.cos(y)]]

def dfdx(x, y):
    return 2*x + math.cos(x/2)/2

def dfdy(x, y):
    return math.sin(y)
import time
def quadratic(f, dx, dy, x, y, e):
    i = 0
    erro_x = e + 1
    erro_y = e + 1
    while erro_x > e or erro_y > e:
        time.sleep(1)
        i += 1
        m = iHessian(x, y)
        grad_x = dx(x, y)
        grad_y = dy(x, y)
        xn = x - (m[0][0]*grad_x + m[0][1]*grad_y)
        yn = y - (m[1][0]*grad_x + m[1][1]*grad_y)
        erro_x = abs(xn-x)
        erro_y = abs(yn-y)
        print(i)
        print(x, y)
        print(m)
        print(grad_x, grad_y)
        x = xn
        y = yn
    return (xn, yn)

print(quadratic(f, dfdx, dfdy, -3, -1, 0.001))




def LM(f, dx, dy, x, y, e, step):
    h_quad = [0]*2
    h_grad = [0]*2
    X = [x, y]
    Xn = [0]*2
    erro = [e+1, e+1]
    while erro[0] > e or erro[1] > e:
        grad = [dx(X[0], X[1]), dy(X[0], X[1])]
        m = iHessian(X[0], X[1])
        for i in range(2):
            h_quad[i] = m[i][0]*grad[0] + m[i][1]*grad[1]
            h_grad[i] = step*grad[i]
            Xn[i] = X[i] - (h_quad[i] + h_grad[i])
        if f(Xn[0], Xn[1]) < f(X[0], X[1]):
            step *= 2
            erro[0] = abs(Xn[0]-X[0])
            erro[1] = abs(Xn[1]-X[1])
        else:
            step /= 2
        
        X = Xn.copy()
    return f(Xn[0], Xn[1])

print(LM(f, dfdx, dfdy, -10, -1, 0.001, 0.01))


# print()
        
# print(step)

# print(m)
# print([round(n, 5) for n in grad])
# print([round(n, 5) for n in h_grad])
# print([round(n, 5) for n in h_quad])
# print([round(n, 5) for n in X])
# print([round(n, 5) for n in Xn])
# print(f(Xn[0], Xn[1]))