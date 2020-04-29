import random

def is_prime_number(number):
    for i in range(2,number-1):
        if (number % i) == 0:
            return False
    return True

def fiat_shamir():
    str_outputs = []
    p = int(input("enter p: "))
    while (is_prime_number(p) == False):
        p = int(input("enter p: "))
    q = int(input("enter q: "))
    while (is_prime_number(q) == False):
        q = int(input("enter q: "))
    N = p * q
    s = int(input("enter s, must be 0 < s < N and prime with N: "))
    while(0 >= s or s >= N):
        s = int(input("enter s, must be 0 < s < N and prime with N: "))
    i = int(input("enter i"))
    v = pow(s, 2) % N
    str_y_comprobation = ""
    for j in range (0, i):
        x = int(input("enter x, must be 0 < x < N and prime with N: "))
        while (0 >= x or x >= N):
            x = int(input("enter x: "))
        a = pow(x, 2) % N
        e = int(input("enter e : "))
        ''' e should be random'''
        if e == 0:
            y = x % N
            if pow(y,2) % N == a % N:
                str_y_comprobation = "  {:d} ^ 2 = {:d} mod ({:d}), {:d} = {:d}, iteración válida".format(y,a,N,pow(y,2) % N,a % N)
        else:
            y = (x * s) % N
            if pow(y,2) % N == (a * v) % N:
                str_y_comprobation = "  {:d} ^ 2 = {:d} * {:d}  mod ({:d}),  {:d} = {:d}, iteración válida".format(y,a,v,N,pow(y,2) % N, (a * v) % N)
        str_outputs.append("{:d} iteracion, a = {:d}, y = {:d}, comprobación: que {:s} ".format(j,a,y,str_y_comprobation))
    print("N = {:d}".format(N))
    print("v = {:d}".format(v))
    for i in str_outputs:
        print(i)

fiat_shamir()