from __future__ import print_function
from Crypto.Util.number import inverse
from pwn import unhex

def ask_p():
    global p
    try:
        p=int(input("p:"))
    except:
        p="-"
        
def ask_q():
    global q
    try:
        q=int(input("q:"))
    except:
        q="-"

def ask_n():
    global n
    try:
        n=int(input("n:"))
    except:
        n="-"

def ask_t():
    global t
    try:
        t=int(input("t:"))
    except:
        t="-" 

def ask_d():
    global d
    try:
        d=int(input("d:"))
    except:
        d="-"
        
def ask_e():
    global e
    try:
        e=int(input("e:"))
    except:
        e="-"

def ask_c():
    global c
    try:
        c=int(input("c:"))
    except:
        c="-"

def ask_m():
    global m
    try:
        m=int(input("m:"))
    except:
        m="-"
        
def return_p():
    global p
    try:
        p=int(p)
    except:
        try:
            p=int(n/q)
        except:
            p="-"
            
def return_q():
    global q
    try:
        q=int(q)
    except:
        try:
            q=int(n/p)
        except:
            q="-"
            
def return_n():
    global n
    try:
        n=int(n)
    except:
        try:
            n=int(p*q)
        except:
            n="-"

def return_t():
    global t
    try:
        t=int(t)
    except:
        try:
            t=int((p-1)*(q-1))
        except:
            if n!="-":
                z=int(input("Is n a prime number? 0=N or 1=Y?"))
                if z == 1:
                    t=n-1
                else:
                    t="-"

def return_d():
    global d
    try:
        d=int(d)
    except:
        try:
            d=int(inverse(e,t))
        except:
            d="-"
            
def return_e():
    global e
    try:
        e=int(e)
    except:
        try:
            e=int(inverse(d,t))
        except:
            e="-"

def return_c():
    global c
    try:
        c=int(c)
    except:
        try:
            c=int(pow(m,e,n))
        except:
            c="-"

def return_m():
    global m
    try:
        m=int(m)
    except:
        try:
            m=int(pow(c,d,n))
        except:
            m="-"

print("Go to http://factordb.com/index.php to determine p and q or if n is prime.")
ask_p()
ask_q()
ask_n()
ask_t()
ask_d()
ask_e()
ask_m()
ask_c()
return_p()
return_q()
return_n()
return_t()
return_d()
return_e()
return_m()
return_c()
print("p:{}".format(p))
print("q:{}".format(q))
print("n:{}".format(n))
print("t:{}".format(t))
print("d:{}".format(d))
print("e:{}".format(e))
print("m:{}".format(m))
print("c:{}".format(c))

if m!="-":
    flag = unhex(hex(m)[2:])
    print('\nFlag: {}'.format(flag))
