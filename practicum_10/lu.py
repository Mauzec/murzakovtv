import numpy as np
from numpy.typing import NDArray


def lu(A: NDArray, permute: bool) -> tuple[NDArray, NDArray, NDArray]:
    # A[mxn]
    m = A.shape[0]
    
    L = np.eye(m)
    U = np.copy(A)
    P = np.eye(m)
    
    for j in range(m - 1):
        if permute:
            # search abs-max-element index in j column
            # MARK: search from j row to m
            maxr = np.argmax(abs(U[j:, j])) + j
            
            # U_k <-> U_[maxr] and P_k <-> P_[maxr]
            U[[j, maxr]] = U[[maxr, j]]
            P[[j, maxr]] = P[[maxr, j]]
            if j: L[[j, maxr], :j] = L[[maxr, j], :j]
            
        for i in range(j + 1, m - 1):
            tmp = U[i, j] / U[j, j]
            L[i, j] = tmp
            U[i, j:] -= tmp * U[j, j:]
            
    return L, U, P
    


def solve(L: NDArray, U: NDArray, P: NDArray, b: NDArray) -> NDArray:
    Y = np.linalg.solve(L, P @ b)
    X = np.linalg.solve(U, Y)
    return X


def get_A_b(a_11: float, b_1: float) -> tuple[NDArray, NDArray]:
    A = np.array([[a_11, 1.0, -3.0], [6.0, 2.0, 5.0], [1.0, 4.0, -3.0]])
    b = np.array([b_1, 12.0, -39.0])
    return A, b


if __name__ == "__main__":
    # Let's implement the LU decomposition with and without pivoting
    # and check its stability depending on the matrix elements
    p = 7  # modify from 7 to 16 to check instability
    a_11 = 3 + 10 ** (-p)  # add/remove 10**(-p) to check instability
    b_1 = -16 + 10 ** (-p)  # add/remove 10**(-p) to check instability
    A, b = get_A_b(a_11, b_1)
    # With pivoting
    L, U, P = lu(A, permute=True)
    x = solve(L, U, P, b)
    assert np.all(np.isclose(x, [1, -7, 4])), f"The anwser {x} is not accurate enough"
    # Without pivoting
    L, U, P = lu(A, permute=False)
    x_ = solve(L, U, P, b)
    assert np.all(np.isclose(x_, [1, -7, 4])), f"The anwser {x_} is not accurate enough"
