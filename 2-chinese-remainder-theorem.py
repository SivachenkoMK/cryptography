def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Inverse does not exist')
    else:
        return x % m

def chinese_remainder_theorem(congruences):
    M = 1
    for _, mi in congruences:
        M *= mi

    result = 0
    for ai, mi in congruences:
        Mi = M // mi
        xi = mod_inverse(Mi, mi)
        result += ai * xi * Mi

    return result % M

congruences = [(2, 3), (3, 5), (2, 7)]
solution = chinese_remainder_theorem(congruences)
print(f"The solution is: {solution}")
