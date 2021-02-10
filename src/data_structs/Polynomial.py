

class Polynomial(object):
    def __init__(self, coefs):
        for c in coefs:
            t = type(c).__name__
            if t != "float" and t != "int":
                raise Exception(f"[Polynomial] - cannot create coefs unless of types float or int:  <{c} is {t}>")
        self.Coefs = coefs
        self.Order = len(coefs) - 1
    
    def show(self):
        n = self.Order + 1
        for i in range(n):
            coef = self.Coefs[i]
            if coef == 0:
                continue

            s = '+' if coef > 0 else '-'
            c = abs(coef)
            p = self.Order - i
            if p == n-1:
                if p == 0:
                    print(f"{s}{c}")
                elif p == 1:
                    print(f"{s}{c}x", end=f" ")
                else:
                    print(f"{coef}x^{p}", end=f" ")
            elif p == 1:
                print(f"{s} {c}x", end=f" ")
            elif p == 0:
                print(f"{s} {c}")
            else:
                print(f"{s} {c}x^{p}", end=f" ")
    
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
    

p = Polynomial([1, -3, 1, 3])
p.show()
print(p.evaluate(5))
print(p.integrate(0, 2))
