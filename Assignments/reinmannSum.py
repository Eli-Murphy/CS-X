import numpy as np


def main():


    rsumtype = "right"
    poly = np.poly1d([3,2,1])
    a = 2
    b = 4
    sd = int(6 / (b-a))

    if rsumtype == "left":
        lrs(poly, a, b, sd)
    if rsumtype == "right":
        rrs(poly, a, b, sd)
    if rsumtype == "mid":
        mrs(poly, a, b, sd)

def lrs(poly, a, b, sd):
    area = 0
    for i in range(abs(b-a)*sd):
        area += poly(a)*(1/sd)
        a += 1/sd
    print(area)

def rrs(poly, a, b, sd):
    area = 0
    newa = a
    for i in range(abs(b-a)*sd):
        newa += (1/sd)
        area += poly(a)*(1/sd)
    print(area)

def mrs(poly, a, b, sd):
    area = 0
    newa = a + .5
    for i in range(abs(b-a)*sd):
        area += (poly(newa)/sd)
        newa += (1/sd)
    print(area)

if __name__ == "__main__":
    main()