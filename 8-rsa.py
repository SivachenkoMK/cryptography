import random
import math

def generate_keypair():
    p = generate_prime_number()
    q = generate_prime_number()

    n = p * q
    totient = (p - 1) * (q - 1)

    e = choose_public_exponent(totient)

    d = mod_inverse(e, totient)

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key

def generate_prime_number():
    return random.choice([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

def choose_public_exponent(totient):
    e = random.randrange(2, totient)
    while math.gcd(e, totient) != 1:
        e = random.randrange(2, totient)
    return e

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

public_key, private_key = generate_keypair()
print("Public Key:", public_key)
print("Private Key:", private_key)

def encrypt(message, public_key):
    e, n = public_key
    cipher_text = [pow(ord(char), e, n) for char in message]
    return cipher_text

message_to_encrypt = "Hello, RSA!"

cipher_text = encrypt(message_to_encrypt, public_key)
print("Encrypted Message:", cipher_text)

def decrypt(cipher_text, private_key):
    d, n = private_key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in cipher_text])
    return decrypted_message

decrypted_message = decrypt(cipher_text, private_key)
print("Decrypted Message:", decrypted_message)