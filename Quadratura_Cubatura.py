import math

# Functions

def f1(x):
    return math.sin(x)

def f2(x, y):
    return x**2-2*y**2+x*y**3


# Algorithms

def trapezium(f, a, b, h):
    n = round((b-a)/h)
    return h/2*(f(a)+f(b)+2*sum(f(a+h*i) for i in range(1, n)))

def simpson(f, a, b, h):
    n = round((b-a)/(2*h))
    return h/3*(f(a)+f(b)+4*sum(f(a+h*i) for i in range(1, 2*n, 2))+2*sum(f(a+h*i) for i in range(2, 2*n-1, 2)))

def cub_trapeze(f, a, b, A, B):
    hx = (b-a)/2
    hy = (B-A)/2
    E0 = f(a, A) + f(b, B) + f(a, B) + f(b, A)
    E1 = f(a+hx, A) + f(a+hx, B) + f(a, A+hy) + f(b, A+hy)
    E2 = f(a+hx, A+hy)
    return hx*hy/4*(E0+2*E1+4*E2)

def cub_simpson(f, a, b, A, B):
    hx = (b-a)/2
    hy = (B-A)/2
    E0 = f(a, A) + f(b, B) + f(a, B) + f(b, A)
    E1 = f(a+hx, A) + f(a+hx, B) + f(a, A+hy) + f(b, A+hy)
    E2 = f(a+hx, A+hy)
    return hx*hy/9*(E0+4*E1+16*E2)



# Run

print(trapezium(f1, 0, math.pi, math.pi/8))
print(simpson(f1, 0, math.pi, math.pi/8))

print(cub_trapeze(f2, 0, 2, -1, 1))
print(cub_simpson(f2, 0, 2, -1, 1))

