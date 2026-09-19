import math

def sin_taylor(x, terms):
    return sum(((-1)**k)*x**(2*k+1)/math.factorial(2*k+1) for k in range(terms))

x=1.0
truth=math.sin(x)
for n in range(1,7):
    a=sin_taylor(x,n)
    print(n, a, abs(a-truth))
