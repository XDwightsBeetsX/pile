

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

    def integrate(self, lower, upper, n=100, method="riemann right"):
        if method == "riemann left":
            return self.riemannLeft(lower, upper, n)
        elif method == "riemann right":
            return self.riemannRight(lower, upper, n)
    
    def riemannLeft(self, lower, upper, n):
        step = (upper - lower) / n
        tot_y = 0
        for i in range(n):
            y = self.evaluate(lower + i*step)
            tot_y += y
        return tot_y*step
    
    def riemannRight(self, lower, upper, n):
        step = (upper - lower) / n
        tot_y = 0
        for i in range(1, n+1):
            y = self.evaluate(lower + i*step)
            tot_y += y
        return tot_y*step

p = Polynomial([1, -3, 1, 3])
p.show()
print(p.evaluate(5))
print(p.integrate(0, 2))
