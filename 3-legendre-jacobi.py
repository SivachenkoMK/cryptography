def legendre_symbol(a, p):
    result = pow(a, (p - 1) // 2, p)
    return result if result != p - 1 else -1

def jacobi_symbol(a, n):
    if n % 2 == 0 or n <= 0:
        raise ValueError("The second argument must be an odd positive integer.")
    
    result = 1
    while a != 0:
        while a % 2 == 0:
            a, s = a // 2, 1
            if n % 8 in {3, 5}:
                s = -s
            result *= s

        a, n = n, a
        if a % 4 == n % 4 == 3:
            result = -result

        a %= n

    return result if n == 1 else 0

a = 7
p = 7
print(f"Legendre Symbol ({a}/{p}): {legendre_symbol(a, p)}")

a = 10
n = 21
print(f"Jacobi Symbol ({a}/{n}): {jacobi_symbol(a, n)}")
