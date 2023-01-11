import numpy as np, sympy as sp


def is_in_span(vector, S):
    variables = sp.symbols(f'a:{len(S)}')
    m = -vector

    for i, var in enumerate(variables):
        m = m + (var * S[i])

    scalars = sp.solve(m, variables, dict=True)
    if len(scalars)==0:
        print("No! The given vector is notin the span of S,")
        return False
    else:
        print("Yes! The given vector is in the span of S")
        print("and the scalars are ", scalars[0])
        return scalars

a1 = [[1,0], [-1,0]]
a2 = [[0,1], [0,1]]
a3 = [[1,1], [0,0]]
b = sp.Matrix([[1,2], [-3,4]])

S = np.array([a1, a2, a3])
is_in_span(b,S)
