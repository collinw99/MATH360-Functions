import math

def trial_factor(n):
    print("Factors of", n, ":")
    count = 0
    for i in range(2, math.floor(math.sqrt(n)), 1):
        if n % i == 0:
            print(i, math.floor(n/i))
            count +=1
    if count == 0:
        print("None,", n , "is prime")

def fermats_method(n):
    root = math.sqrt(n)
    num1 = math.ceil(root)
    num2 = math.floor(math.sqrt(num1**2 % n))

    print("n = ", n)
    print(num1, '^2 mod', n, "=", num1**2 % n)
    print(num2, '^2 mod', n, "=", num2**2 % n)

    factor1 = math.gcd(num1 - num2, n)
    print("gcd(", num1, "-", num2, ",", n, ") =", factor1)
    print(n, "/", factor1, "=", n/factor1)
    print("\nFactors of", n, ":", factor1, math.floor(n/factor1))

def RSA_decrypt(msg, n, d):
    print("Encrypted message: ", msg)
    for x in msg:
        dec = x**d % n
        print(dec)