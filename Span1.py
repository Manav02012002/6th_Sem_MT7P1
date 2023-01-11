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
vector = np.array((2,-1,1))
S = np.array([(1,0,2),(-1,1,1)])
is_in_span(vector,S)
