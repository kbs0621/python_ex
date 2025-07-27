import math

def circle_calculator(r):
    return round(math.pi*r**2,2)

def rectangle_calculator(l, w):
    return l*w

def factorial_fucntions(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_fucntions(n-1)

def gcd(x,y):
    while y:
        x,y = y, x % y
    return x


