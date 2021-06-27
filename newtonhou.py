import math

def f(x):
    return math.exp(x) - 3 * x

def df(x):
    return math.exp(x) - 3

eps1 = 1e-5

x = 0 # 初期値

print("n\tx\tf(x)\tdf(x)\tdx")
n = 0
while True:
    print("{}\t{:.4f}\t{:.4f}\t{:.4f}\t{:.4f}".format(n, x, f(x), df(x), f(x)/df(x)))
    x -= f(x)/df(x)
    if abs(f(x)) < eps1:
        break
    n += 1

print("x = %f" % x)
