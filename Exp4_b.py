import numpy as np
import sympy as sp
def lt_of_matrix(B1,B2,M):
    k,m = len(B1),len(B2)
    T = [sum(M[j,i]*B2[j] for j in range(m)) for i in range(k)]
    print("The images of basis elements are")
    for i in range(k):
        print("T(", B1[i],") = ",T[i])
    x = sp.symbols(f'x:{k}')
    c = sp.symbols(f'c:{k}')
    for i in range(k):
        x = x-c[i]*B1[i]
    s = sp.solve(x,c)
    trans = 0
    for i,v in enumerate(s):
        trans = trans + s[v]*T[i]
    print("The required linear tranjsformation is ", tuple(trans))
    

B1 = np.array([[1,-1],[1,1]])
B2 = np.array([[1, 0],[0,1]])
M = sp.Matrix([[2,3],[4,-5]])
lt_of_matrix(B1,B2,M)
