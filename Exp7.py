from sympy import*
from sympy.abc import x,t,c,p
def wave(c,l,f,g):
    sol=0
    for n in range(1,4):
        a = (2/l)*integrate(f*sin(n*pi*x/l),(x,0,l))
        b = (2/(n*pi*c))*integrate(g*sin(n*pi*x/l),(x,0,l))
        sol = sol+(a*cos(n*pi*c*t/l)+b*sin(n*pi*c*t/l))*sin(n*pi*x/l)
    print("The solution of the given wave equation is")
    pprint(sol)
        
wave(1,2,(sin(pi*x/2)**3),0)
wave(1,pi,sin(x),0)
wave(c,pi,x**3,0)
