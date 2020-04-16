import math
import sympy

# Functions for MATH360

def trial_factor(n):
    print("Testing values from 2 to", math.floor(math.sqrt(n)))
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
    print("Encrypted message:", msg)
    chars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    finalMsg = ""
    for x in msg:
        # dec = x**d % ns
        dec = pow(x,d,n)
        print(x, "^", d, "mod", n, "=", dec)
        strDec = str(dec)
        if len(strDec) % 2 != 0:
            strDec = "0" + strDec
        charCount = math.floor(len(strDec)/2)
        for i in range(0, charCount, 1):
            subStr = strDec[2*i:2*i+2]
            print(subStr, "=", chars[int(subStr)-1])
            finalMsg = finalMsg + chars[int(subStr)-1]
    print("Decrypted message:", finalMsg)
    return finalMsg

def RSA_encrypt(msg, n, e, split = 3):
    print("Message:", msg)
    chars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    finalMsg = []
    tempStr = ""
    for c in msg:
        val = chars.index(c)+1
        strVal = str(val)
        if len(strVal) % 2 != 0:
            strVal = "0" + strVal
        print(c, "=", strVal)
        tempStr = tempStr + strVal
    for i in range(0, len(tempStr), 2*split):
        finalMsg.append(tempStr[i:i+2*split])
    print("Split message every", split, "charaters:", finalMsg)
    for i in range(0, len(finalMsg), 1):
        x = int(finalMsg[i])
        # finalMsg[i] = x**e % n
        finalMsg[i] = pow(x,e,n)
    print("Encrypted message:", finalMsg)        
    return finalMsg



def mult_inverse(b, n):
    gcdRes = math.gcd(b, n)
    print("a *", b, "= 1 mod", n)
    print("gcd(", b, ",", n, ") =", gcdRes)
    if gcdRes == 1:
        inv = sympy.mod_inverse(b, n)
        print("Multiplicative inverse: a =", inv)
        return inv
    else:
        print("No multiplicative inverse")

def phi(n):
    tot = sympy.totient(n)
    print("phi(", n, ") =", tot)
    return tot

# Brute force method
# a = g^x mod p
def discrete_log(a, g, p): 
	for x in range(0, p, 1):
		if(pow(g, x, p) == a):
			print(a, "=", g, "^", x, "mod", p)
			return x
	print("No x found...")
