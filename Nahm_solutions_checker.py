# To check whether a set of 3 matrix solutions satisfy the Nahm equations.
# Assuming the form T_i = f_i(s) * J_i where J_i is a nxn matrix
# Nahm equations: dT_1/ds = [T_2, T_3], dT_2/ds = [T_3, T_1], dT_3/ds = [T_1, T_2]

# Imports
import numpy as np

# Commutator function [A,B] = AB - BA
def commutator(A,B):
    AB = np.matmul(A,B)
    BA = np.matmul(B,A)
    return AB - BA

def check_nahm(T1, T2, T3, tol=1e-10):
    # Compute commutators
    comm23 = commutator(T2, T3)
    comm31 = commutator(T3, T1)
    comm12 = commutator(T1, T2)

    # Check Nahm equations (matrix equality up to tolerance)
    eq1 = np.allclose(T1, comm23, atol=tol)
    eq2 = np.allclose(T2, comm31, atol=tol)
    eq3 = np.allclose(T3, comm12, atol=tol)

    if eq1 and eq2 and eq3:
        print("The set is a solution set!")
    else:
        print("The solution set is not valid.")
        
def main():
    T1 = np.array([[0, 1], [1, 0]])
    T2 = np.array([[0, -1j], [1j, 0]])
    T3 = np.array([[1, 0], [0, -1]])

    check_nahm(T1, T2, T3)

