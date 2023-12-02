def euler_phi(n):
    result = n

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            while n % i == 0:
                n //= i
            result -= result // i

    if n > 1:
        result -= result // n

    return result

def mobius(n):
    if n == 1:
        return 1

    for i in range(2, int(n**0.5) + 1):
        if n % (i*i) == 0:
            return 0

    if n % 4 == 0:
        return -1

    return 1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

num1 = 12
num2 = 19

phi_num1 = euler_phi(num1)
phi_num2 = euler_phi(num2)

mu_num1 = mobius(num1)
mu_num2 = mobius(num2)

lcm_result = lcm(num1, num2)

print(f"Euler Phi({num1}) = {phi_num1}")
print(f"Euler Phi({num2}) = {phi_num2}")
print(f"Möbius({num1}) = {mu_num1}")
print(f"Möbius({num2}) = {mu_num2}")
print(f"LCM({num1}, {num2}) = {lcm_result}")
