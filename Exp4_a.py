import numpy as np
def matrix_of_lt(B1,B2,T):
    print("The basis of the domain is ", B1)
    print("The basis of the codomain is ", B2)
    w = [T(i) for i in B1]
    v = [np.linalg.solve(B2.T, w[i]) for i in range(len(w))]
    M = np.array(v)
    print("The matrix of the linear transformations is ", M.T)

B1 = np.array([[-1,1,0],[5,-1,2],[1,2,1]])
B2 = np.array([[1,1,0],[0,0,1],[1,5,2]])
def T(x):
    return [x[0]-x[1]+x[2], 2*x[0] + 3*x[1]-(1/2)*x[2], x[0]+x[1] - 2*x[2]]
matrix_of_lt(B1,B2,T)
