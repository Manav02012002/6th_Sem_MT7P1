import sympy as sp
import numpy as np
def is_linear(T,domain_dim):
    x=np.array(sp.symbols(f'x:{domain_dim}'))
    y=np.array(sp.symbols(f'y:{domain_dim}'))
    c=sp.symbols('c')
    lhs = T(c * x+y)
    rhs = c * T(x) + T(y)
    lhs = [sp.expand(i) for i in lhs]
    print(f'T(c*x+y) = {lhs}')
    rhs = [sp.expand(i) for i in rhs]
    print(f'T(c*x+y) = {rhs}')
    if lhs == rhs:
        print("Thus the given map is a linear transformation.")
        return True
    else:
        print("Thus the given map is not a linear transformation.")
        return False
def T(v):
    return np.array([v[0], 2*v[0] + v[1]])
is_linear(T,2)

def T(v):
    return np.array([v[0] - v[1], 2*v[0] , 1])
is_linear(T,3)
