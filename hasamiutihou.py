import math

def f(x):
    return math.exp(x) - 3 * x

def fd(x):
    return math.exp(x) - 3

eps1 = 0.00001
eps2 = 0.00001

a = 0
b = 1

print("n\tc\tf(c)")
n = 1
while True:
    c = (a + b)/2
    print("{}\t{:.5f}\t{:.5f}".format(n, c, f(c)))
    if f(a)*f(c) < 0:
        b = c
    else:
        a = c
    n += 1
    if abs(f(c)) < eps1 or abs(a - b) < eps2:
        break

print("x = %f" % c)
