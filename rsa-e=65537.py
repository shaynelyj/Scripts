from __future__ import print_function
from pwn import *

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def test_prime():
    global p,q,t
    try:
        p = int(input("p: "))
        q = int(input("q: "))
        t=(p-1)*(q-1)
    except:
        t=n-1

print("Go to https://www.alpertron.com.ar/ECM.HTM to determine p and q")
print("If n is prime, leave blank for p")
c = int(input("c: "))
n = int(input("n: "))
test_prime()
e = int(input("e: "))
d = modinv(e, t)
m = pow(c, d, n)

flag = unhex(hex(m)[2:])
print('Flag: {}'.format(flag))
