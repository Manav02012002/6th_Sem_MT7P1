import sympy as sp
def rank_nullity(M, domain_dim):
    rank = M.rank()
    B = M.rref()
    print("Range M is spanned by the first ", rank, "rows of the matrix ",B[0])
    N = M.transpose().nullspace()
    print("The nullspace of M is spanned by the columns of ",N)
    nullity = len(N)
    if domain_dim == rank + nullity:
        print("The rank nullity theorem is verified")
        return True
    else:
        print("You obviously made a mistake because rank nullity theorem has to be true.")
        return False
M = sp.Matrix([[1,-1,0],[2,0,1],[1,1,1]])
rank_nullity(M,3)
