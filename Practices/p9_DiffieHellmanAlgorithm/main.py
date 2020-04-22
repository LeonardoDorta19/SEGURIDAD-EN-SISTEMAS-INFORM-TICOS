


def fast_exponentiation(base, exponent, module):
    result = 1
    while exponent != 1:
        if (exponent % 2) == 0:
            base = (base * base) % module
            exponent /= 2
        else:
            exponent= exponent - 1
            result = (result * base) % module

    exponent = exponent - 1
    result = (result * base) % module
    return  result



p = int(input("enter p: "))
alfa = int(input ("enter alfa: "))
while(alfa >=p):
    alfa = int(input("enter alfa: "))
xa = int(input("enter xa: "))
xb = int(input("enter xb: "))
ya = fast_exponentiation(alfa, xa, p)
yb = fast_exponentiation(alfa, xb, p)
ka = fast_exponentiation(yb, xa, p)
kb = fast_exponentiation(ya, xb, p)
print("p = {:d}, α = {:d}, xa = {:d}, xb = {:d}, ya = {:d}, yb = {:d}, ka = {:d},kb = {:d}".format(p, alfa, xa , xb, ya, yb, ka, kb))