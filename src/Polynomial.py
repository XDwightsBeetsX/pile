"""
Polynomial class
"""


class Polynomial(object):
    """
    Stores coefficient information about a polynomial

    Construct with list of coefs: [A, B, C, D] -> Ax^3 + Bx^2 + Cx + D

    Offers show() and eval(x) methods
    """

    def __init__(self, coefs):
        l = len(coefs)
        if l != 0:
            self.degree = l - 1
            self.coefs = []
            for i in range(l):
                self.coefs.append(coefs[i])
    
    def show(self):
        """
        Displays Polynomial in form: "Ax^3 + Bx^2 + Cx + D"
        """
        d = self.degree
        if d + 1 != len(self.coefs):
            raise Exception("[ERROR]: in Polynomial.show(), degree + 1 must equal len(coefs)")
        for i in range(self.degree + 1):
            c = self.coefs[i]
            if c == 0:
                c = None
                        
            if d == self.degree:
                if d == 0:
                    print(f"{c}", end="")
                elif d == 1:
                    print(f"{c}x", end=" ")
                else:
                    print(f"{c}x^{d}", end=" ")
            else:
                sign = "+"
                if c < 0:
                    sign = "-"
                    c = abs(c)
                if d == 0:
                    print(sign + f" {c}", end="")
                elif d == 1:
                    print(sign + f" {c}x", end=" ")
                else:
                    print(sign + f" {c}x^{d}", end=" ")
            d -= 1
        print("")
    
    def eval(self, x):
        """
        Evaluates the polynomial at a value 'x'
        """
        d = self.degree
        if d + 1 != len(self.coefs):
            raise Exception("[ERROR]: in Polynomial.eval(), degree + 1 must equal len(coefs)")
        if d == 0:  # constant function
            return self.coefs[self.degree]
        y = 0.0
        d = self.degree
        for i in range(self.degree + 1):
            c = self.coefs[i]
            y += c * x**d
            d -= 1
        return y
