def pollards_rho(n):
    x = 2
    y = 2
    d = 1

    def f(x):
        return (x**2 + 1) % n

    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)

    if d == n:
        return None
    else:
        return d

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

number_to_factorize = 171
result = pollards_rho(number_to_factorize)

if result is None:
    print(f"{number_to_factorize} - просте число.")
else:
    print(f"Знайден дільник {result} для {number_to_factorize}.")
