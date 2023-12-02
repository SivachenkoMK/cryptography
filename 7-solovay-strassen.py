import random

def mod_exp(base, exponent, modulus):
    result = 1
    base = base % modulus

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus

        exponent = exponent // 2
        base = (base * base) % modulus

    return result

def jacobi_symbol(a, n):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    elif a % 2 == 0:
        return jacobi_symbol(a // 2, n) * ((-1) ** ((n ** 2 - 1) // 8))
    else:
        return jacobi_symbol(n % a, a) * ((-1) ** ((a - 1) * (n - 1) // 4))

def solovay_strassen(n, k=5):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = mod_exp(a, (n - 1) // 2, n)
        if x != 1 and x != n - 1:
            return False

        jacobi = jacobi_symbol(a, n)
        y = mod_exp(a, (n - 1) // 2, n)
        if y % n != jacobi % n:
            return False

    return True

number_to_test = 24
is_prime = solovay_strassen(number_to_test)

if is_prime:
    print(f"{number_to_test} is probably a prime number.")
else:
    print(f"{number_to_test} is composite.")
