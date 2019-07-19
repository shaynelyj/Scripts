from __future__ import print_function
from Crypto.Util.number import inverse, long_to_bytes
from pwn import *

e= 3
n= 374159235470172130988938196520880526947952521620932362050308663243595788308583992120881359365258949723819911758198013202644666489247987314025169670926273213367237020188587742716017314320191350666762541039238241984934473188656610615918474673963331992408750047451253205158436452814354564283003696666945950908549197175404580533132142111356931324330631843602412540295482841975783884766801266552337129105407869020730226041538750535628619717708838029286366761470986056335230171148734027536820544543251801093230809186222940806718221638845816521738601843083746103374974120575519418797642878012234163709518203946599836959811
c= 2205316413931134031046440767620541984801091216351222789180582564557328762455422721368029531360076729972211412236072921577317264715424950823091382203435489460522094689149595951010342662368347987862878338851038892082799389023900415351164773

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
                z=int(input("Is n a prime number? 0=N or 1=Y? "))
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
            if e == 3:
                m=find_invpow(c,e)
            else:
                m=int(pow(c,d,n))
        except:
            m="-"

def find_invpow(x,n):
    high = 1
    while high ** n < x:
        high *= 2
    low = high/2
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid**n < x:
            low = mid
        elif high > mid and mid**n > x:
            high = mid
        else:
            return mid
    return mid + 1

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
print("c:{}".format(c))
print("m:{}".format(m))

if m!="-":
    print("\nFlag: %s"%long_to_bytes(m))
