import numpy as np
import sympy as sp
def is_basis(S,dim):
    n = len(S)
    a = sp.symbols(f'a:{n}')
    m = 0
    for i in range(n):
        m = m + S[i]*a[i]
    coeff = sp.solve(m,a)
    for i in coeff:
        if coeff[i]!=0:
            print("The Given set is dependent and hence not a basis")
            print("The Scalars are: ",coeff)
            return False
    print("The Given Set is Independent")
    if n == dim:
        print("The Set is a Basis")
        return True
    else:
        print("The Given Set is not a Basis")
        return False
S = np.array([[1,0,0,-1],[0,1,0,-1],[0,0,1,-1],[1,-1,1,-1]])
is_basis(S,4)
