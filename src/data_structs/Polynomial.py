"""
Polynomial equation data structure
Takes in coefs input:
[1, 2, -3, 4] -> x^3 + 2x^2 -3x + 4
"""

from matplotlib import pyplot as plt


class Polynomial(object):
    def __init__(self, coefs):
        if not coefs:
            raise Exception(f"[Polynomial] - cannot create Polynomial() w/o coefs")
        
        if coefs[0] == 0.0:
            raise Exception(f"[Polynomial] - cannot create Polynomial() w/o leading zero coefs")

        for c in coefs:
            t = type(c).__name__
            if t != "float" and t != "int":
                raise Exception(f"[Polynomial] - cannot create coefs unless of types float or int:  <{c} is {t}>")
        self.Coefs = coefs
        self.Order = len(coefs) - 1
    
    def getEqString(self):
        """
        returns: equation string of a polynomial

        (assumes no leading 0 coefs)
        """
        polyString = ""
        
        for i in range(self.Order + 1):
            coef = self.Coefs[i]
            absCoef = abs(coef)
            p = self.Order - i
            s = '+' if coef > 0 else '-'

            # highest order term
            if p == self.Order:
                # coefs of 1 ignored
                if absCoef == 1:
                    if coef > 0:
                        if p == 0:
                            return f"{coef}"
                        elif p == 1:
                            polyString += f"x "
                        else:
                            polyString += f"x^{p} "
                    else:
                        if p == 0:
                            return f"{s}{coef}"
                        elif p == 1:
                            polyString += f"{s}x "
                        else:
                            polyString += f"{s}x^{p} "
                # show abs(coef) if greater than 1
                else:
                    if p == 0:
                        return f"{coef}"
                    elif p == 1:
                        polyString += f"{coef}x "
                    else:
                        polyString += f"{coef}x^{p} "
            # regular term, incorporate coef sign to operation
            else:
                if coef == 0:
                    continue
                # coefs of 1 ignored
                if absCoef == 1:
                    if p == 0:
                        polyString += f"{s} {absCoef}"
                    elif p == 1:
                        polyString += f"{s} x "
                    else:
                        polyString += f"{s} x^{p} "
                # show abs(coef) if greater than 1
                else:
                    if p == 0:
                        polyString += f"{s} {absCoef}"
                    elif p == 1:
                        polyString += f"{s} {absCoef}x "
                    else:
                        polyString += f"{s} {absCoef}x^{p} "

        
        return polyString.strip()
    
    def evaluate(self, x):
        n = self.Order + 1
        tot = 0
        for i in range(n):
            coef = self.Coefs[i]
            p = self.Order - i
            tot += coef*x**p
        return tot

    def integrate(self, lower, upper, n=10**3, method="simpson"):
        """
        Options for integration are:
        "reimann left", "reimann right", "simpson"

        Default n is 10**3
        """
        def riemannLeft(lower, upper, n):
            step = (upper - lower) / n
            tot_y = 0
            for i in range(n):
                y = self.evaluate(lower + i*step)
                tot_y += y
            return tot_y*step
        
        def riemannRight(lower, upper, n):
            step = (upper - lower) / n
            tot_y = 0
            for i in range(1, n+1):
                y = self.evaluate(lower + i*step)
                tot_y += y
            return tot_y*step
        
        def simpson(lower, upper, n):
            h = (upper - lower) / n
            k = 0.0
            x = lower + h
            for _ in range(1 , n//2 + 1):
                k += 4 * self.evaluate(x)
                x += 2*h

            x = lower + 2*h
            for _ in range(1, n//2):
                k += 2*self.evaluate(x)
                x += 2*h
            
            return (h/3)*(self.evaluate(lower) + self.evaluate(upper) + k)

        
        if method == "riemann left":
            return riemannLeft(lower, upper, n)
        elif method == "riemann right":
            return riemannRight(lower, upper, n)
        elif method == "simpson":
            return simpson(lower, upper, n)
        else:
            raise Exception(f"[Polynomial.integrate()] - invalid params: {{{lower}, {upper}, {n}, '{method}'}}")
    
    def plot(self, lower, upper, n=10**3):
        step = (upper - lower) / n
        x_vals = [lower]
        y_vals = [self.evaluate(lower)]

        x = lower
        for _ in range(n):
            x += step
            x_vals.append(x)
            y_vals.append(self.evaluate(x))
        
        plt.plot(x_vals, y_vals)
        plt.axhline(y=0, color='k')
        plt.axvline(x=0, color='k')
        polyString = self.getEqString()
        plt.ylabel(polyString)
        title = f"{polyString} over [{lower}, {upper}]"
        plt.title(title)
        plt.show()

