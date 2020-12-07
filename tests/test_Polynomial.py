"""
Tests For Polynomial class
"""
import src.Polynomial as poly


def test_polynomial_ctor():
    correct = True

    test_coefs = [1, 2, 3, 4, 5, 6]
    p = poly.Polynomial(test_coefs)
    l_t_coefs = len(test_coefs)

    if p.degree + 1 != l_t_coefs:
        correct = False
    for i in range(l_t_coefs):
        if p.coefs[i] != test_coefs[i]:
            correct = False

    assert correct


def test_polynomial_eval():
    correct = True

    p = poly.Polynomial([2, 5, -4, -3])
    x = [-3, -2, -0.5, 0, 1]
    act_y = [0, 9, 0, -3, 0]
    test_y = []

    l = len(x)
    for i in range(l):
        test_y.append(p.eval(x[i]))
    
    for i in range(l):
        if test_y[i] != act_y[i]:
            correct = False

    assert correct
