from matplotlib import pyplot as plt

class Polynomial(object):
    def __init__(self, coefs):
        for c in coefs:
            t = type(c).__name__
            if t != "float" and t != "int":
                raise Exception(f"[Polynomial] - cannot create coefs unless of types float or int:  <{c} is {t}>")
        self.Coefs = coefs
        self.Order = len(coefs) - 1
    
    def getEqString(self):
        n = self.Order + 1
        polyString = ""
        for i in range(n):
            coef = self.Coefs[i]
            p = self.Order - i
            s = '+' if coef > 0 else '-'

            if coef == 0:
                continue
            elif coef == 1:
                if p == 1:
                    polyString += f"{s} x "
                else:
                    polyString += f"x^{p} "
            else:
                c = abs(coef)
                if p == n-1:
                    if p == 0:
                        polyString += f"{s}{c} "
                    elif p == 1:
                        polyString += f"{s}{c}x "
                    else:
                        polyString += f"{coef}x^{p} "
                elif p == 1:
                    polyString += f"{s} {c}x "
                elif p == 0:
                    polyString += f"{s} {c} "
                else:
                    polyString += f"{s} {c}x^{p} "
        return polyString
    
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

p = Polynomial([1, -3, 1, 3])
print(p.getEqString())
print(p.evaluate(5))
print(p.integrate(0, 2))
p.plot(-1, 5)
