def f(x):
    return x**2 - x

def itegrate_f(a, b, N):
    s = 0
    dx = (b -a)/N
    for i in range(N):
        s += f(a + i * dx)
    return s * dx
