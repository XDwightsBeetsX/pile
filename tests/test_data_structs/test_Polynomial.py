"""
Tests For Data Structs - Polynomial
"""

from src.data_structs import Polynomial as poly


def test_poly_init():
    correct = True

    # test init
    try:
        # Polynomial requires coefs arg
        p = poly.Polynomial()
        correct = False
    except Exception as e:
        pass
    
    assert correct


def test_poly_getEqString():
    correct = True
    
    coefs1 = [5]
    p1 = poly.Polynomial(coefs1)
    p1s = p1.getEqString()
    p1s_act = "5"
    if (p1s != p1s_act):
        print(f"expected: '{p1s_act}'\nbut got:  '{p1s}'")
        correct = False
    
    coefs2 = [-5, 4]
    p2 = poly.Polynomial(coefs2)
    p2s = p2.getEqString()
    p2s_act = "-5x + 4"
    if (p2s != p2s_act):
        print(f"expected: '{p2s_act}'\nbut got:  '{p2s}'")
        correct = False
    
    coefs3 = [1, 3, -9, -23, -12]
    p3 = poly.Polynomial(coefs3)
    p3s = p3.getEqString()
    p3s_act = "x^4 + 3x^3 - 9x^2 - 23x - 12"
    if (p3s != p3s_act):
        print(f"expected: '{p3s_act}'\nbut got:  '{p3s}'")
        correct = False

    coefs4 = [-3, 0, -12.5, 1, 0]
    p4 = poly.Polynomial(coefs4)
    p4s = p4.getEqString()
    p4s_act = "-3x^4 - 12.5x^2 + x"
    if (p4s != p4s_act):
        print(f"expected: '{p4s_act}'\nbut got:  '{p4s}'")
        correct = False

    assert correct


def test_poly_evaluate():
    correct = True

    # test constant function
    coefs1 = [5]
    p1 = poly.Polynomial(coefs1)
    if (p1.evaluate(30.5) != coefs1[0]):
        correct = False
    
    # test linear function
    # plug in some simple values to check
    coefs2 = [3, -5]
    p2 = poly.Polynomial(coefs2)
    for i in range(5):
        ans = coefs2[0] * i + coefs2[1]
        if (p2.evaluate(i) != ans):
            correct = False
    
    # test higher (4th) order function
    # plug in some sporatic, known values to check
    coefs3 = [1, 3, -9, -23, -12]
    p3 = poly.Polynomial(coefs3)
    if (p3.evaluate(-4) != 0.0):
        correct = False
    if (p3.evaluate(-1) != 0.0):
        correct = False
    if (p3.evaluate(0) != -12.0):
        correct = False
    if (p3.evaluate(1) != -40.0):
        correct = False
    if (p3.evaluate(3) != 0.0):
        correct = False

    assert correct


def test_poly_integrate():
    correct = True
    tol = 0.001
    
    # test constant function
    coefs1 = [5]
    p1 = poly.Polynomial(coefs1)
    l = -3
    u = 10
    i1 = p1.integrate(l, u)
    i1_act = coefs1[0] * (10 - (-3))
    i1_diff = abs(i1 - i1_act)
    if (i1_diff > tol):
        correct = False
    
    # test linear function
    # plug in some simple values to check
    coefs2 = [3, -5]
    p2 = poly.Polynomial(coefs2)
    l = 0
    u = 10
    i2 = p2.integrate(l, u)
    i2_act = 100.0
    i2_diff = abs(i2 - i2_act)
    if (i2_diff > tol):
        correct = False
    
    # test higher (4th) order function
    # plug in some sporatic, known values to check
    coefs3 = [1, 3, -9, -23, -12]
    p3 = poly.Polynomial(coefs3)
    l = 0
    u = 10
    i3 = p3.integrate(l, u)
    i3_act = 23230.0
    i3_diff = abs(i3 - i3_act)
    if (i3_diff > tol):
        correct = False

    assert correct
