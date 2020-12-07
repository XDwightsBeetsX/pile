"""
Matrix LU Solver Methods
"""
import numpy as np


def Lsolve(L, b, tol=1.0e-12):
    """
    Lower triangle matrix solution
    """
    n = len(b)
    for k in range(n):
        if abs(L[k, k]) < tol:
            raise RuntimeError('Matrix L was singular.')

    # solve [L]{x} = {b} for {x} via forward substitution
    x = np.copy(b)
    x[0] = x[0] / L[0, 0]
    for k in range(1, n):
        x[k] = (x[k] - np.dot(L[k, 0:k], x[0:k])) / L[k, k]

    return x


def Usolve(U, b, tol=1.0e-12):
    """
    Upper triangle matrix solution
    """
    n = len(b)
    for k in range(n):
        if abs(U[k, k]) < tol:
            raise RuntimeError('Matrix U was singular.')

    # solve [U]{x} = {b} for {x} via backward substitution
    x = np.copy(b)
    x[n-1] = x[n-1] / U[n-1, n-1]
    for k in range(n-2, -1, -1):
        x[k] = (x[k] - np.dot(U[k, k+1:n], x[k+1:n])) / U[k, k]
    
    return x


def LUSolve(L, U, b, tol=1.0e-12):
    """
    Implements both Lsolve and Usolve to solve system of equations
    """
    # solve [L]{y} = {b} for {y}
    y = Lsolve(L, b, tol)
    # solve [U]{x} = {y} for {x}
    x = Usolve(U, y, tol)

    return x
