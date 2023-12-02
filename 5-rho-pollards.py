def rho_pollard(g, h, p):
    def f(x):
        return (x**2 + 1) % p

    x, y, d = 2, 2, 1

    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), p)

    if d != 1:
        inv_x = pow(x -1, p)
        return (log((h * inv_x) % p, g) + log(x, g)) % p + 1
    else:
        raise ValueError("Algorithm failed to find a solution.")

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def log(base, value):
    result, current, i = 1, base, 0
    while result != value and i < p:
        current = (current * base) % p
        result = (result * g) % p
        i += 1

    if result == value:
        return i
    else:
        raise ValueError("Logarithm not found within the group.")

g = 2
h = 8
p = 17

result = rho_pollard(g, h, p)
print(f"The discrete logarithm of {h} to the base {g} modulo {p} is: {result}")
