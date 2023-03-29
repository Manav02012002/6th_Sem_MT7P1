from sympy import pi,cos,sin,integrate,pprint,exp
from sympy.abc import x,t
def wave(c,l,f):
    sol=0
    for n in range (1,4):
        a=(2/l)*integrate(f*sin(n*pi*x/l),(x,0,l))
        sol=sol+(a*sin((n*pi*x)/l)*exp((-n**2*pi**2*c**2*t)/l**2))
    print("The solution of the given heat equation is")
    pprint(sol)
wave(2,1,x-x**2)
