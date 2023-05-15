import numpy as np
import matplotlib.pyplot as plt
import math

sigfig = 4

class limint:
    def __init__(self, poly, a, b, n):
        self.poly = poly
        self.a = a
        self.b = b
        self.n = n
        self.lrs = self.lrs()
        self.rrs = self.rrs()
        self.mrs = self.mrs()
        self.trs = self.trs()

    def lrs(self):
        deltaX = (self.b-self.a)/self.n
        i = np.linspace(self.a,self.b-deltaX, self.n)      
        area = np.sum(self.poly(i) * deltaX)
        return area

    def rrs(self):
        deltaX = (self.b-self.a)/self.n
        i = np.linspace(self.a+deltaX,self.b, self.n)      
        area = np.sum(self.poly(i) * deltaX)
        return area

    def mrs(self):
        deltaX = (self.b-self.a)/self.n
        i = np.linspace(self.a+(deltaX/2),self.b-(deltaX/2), self.n)      
        area = np.sum(self.poly(i) * deltaX)
        return area

    def trs(self):
        area = self.lrs+((self.rrs-self.lrs)/2)
        return area

    def plot(self):

        x = np.linspace(self.a,self.b,self.n+1)
        y = self.poly(x)

        X = np.linspace(self.a,self.b,(self.n)**2+1)
        Y = self.poly(X)

        plt.figure(figsize=(10,10))

        plt.subplot(2,2,1)
        plt.plot(X,Y,'g')
        x_left = x[:-1]
        y_left = y[:-1]
        plt.plot(x_left,y_left,'g.',markersize=10)
        plt.bar(x_left,y_left,width=(self.b-self.a)/self.n, alpha=0.2, align='edge', edgecolor='g', color="g")
        plt.title('Left Riemann Sum, Area = {}'.format(round(self.lrs, sigfig)))


        plt.subplot(2,2,2)
        plt.plot(X,Y,'b')
        x_mid = (x[:-1] + x[1:])/2
        y_mid = self.poly(x_mid)
        plt.plot(x_mid,y_mid,'b.',markersize=10)
        plt.bar(x_mid,y_mid,width=(self.b-self.a)/self.n,alpha=0.2,edgecolor='b', color="b")
        plt.title('Midpoint Riemann Sum, Area = {}'.format(round(self.mrs, sigfig)))


        plt.subplot(2,2,3)
        plt.plot(X,Y,'r')
        x_right = x[1:] 
        y_right = y[1:]
        plt.plot(x_right,y_right,'r.',markersize=10)
        plt.bar(x_right,y_right,width=-(self.b-self.a)/self.n,alpha=0.2,align='edge',edgecolor='r', color="r")
        plt.title('Right Riemann Sum, Area = {}'.format(round(self.rrs, sigfig)))


        plt.subplot(2,2,4)

        x = np.linspace(self.a,self.b,self.n+1)
        y = self.poly(x)

        # X and Y values for plotting y=f(x)
        X = np.linspace(self.a,self.b,100)
        Y = self.poly(X)
        plt.plot(X,Y)

        plt.plot(X,Y, "m")

        x_right = x[1:] 
        y_right = y[1:]
        plt.plot(x_right,y_right,'m.',markersize=10)

        for i in range(self.n):
            xs = [x[i],x[i],x[i+1],x[i+1]]
            ys = [0,self.poly(x[i]),self.poly(x[i+1]),0]
            plt.fill(xs,ys,'m',edgecolor='m',alpha=0.2)

        plt.title('Trapezoid Rule, Area = {}'.format(round(self.trs, sigfig)))

        plt.show()



'''
USER INPUT
'''
ll = float(input("Lower Limit: "))
ul = float(input("Upper Limit: "))
n = int(input("N Value: "))

functype = input("Polynomial (p), Trigonometric (t), logarithmic (l), exponential (e): ")

if functype.lower() == "p":
    coefold = input("Input coefficients from largest degree to constant (1 2 3 4): ").split(" ")
    coef = [float(i) for i in coefold]

    func = np.poly1d(coef)

if functype.lower() == "t":
    trigtype = input("Please write the 3 character abreviation for the trig function you would like (cos, sin, sec) or inverse (arcsin, arccos): ")
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    d = float(input("d: "))

    if trigtype.lower() == "sin":
        func = lambda x : a*np.sin(b*x+c)+d
    if trigtype.lower() == "cos":
        func = lambda x : a*np.cos(b*x+c)+d
    if trigtype.lower() == "tan":
        func = lambda x : a*np.tan(b*x+c)+d
    if trigtype.lower() == "csc":
        func = lambda x : 1/a*np.sin(b*x+c)+d
    if trigtype.lower() == "sec":
        func = lambda x : 1/a*np.cos(b*x+c)+d
    if trigtype.lower() == "cot":
        func = lambda x : 1/a*np.tan(b*x+c)+d

    if trigtype.lower() == "arcsin":
        func = lambda x : a*np.arcsin(b*x+c)+d
    if trigtype.lower() == "arccos":
        func = lambda x : a*np.arccos(b*x+c)+d
    if trigtype.lower() == "arctan":
        func = lambda x : a*np.arctan(b*x+c)+d
    if trigtype.lower() == "arccsc":
        func = lambda x : 1/a*np.arcsin(b*x+c)+d
    if trigtype.lower() == "arcsec":
        func = lambda x : 1/a*np.arccos(b*x+c)+d
    if trigtype.lower() == "arccot":
        func = lambda x : 1/a*np.arctan(b*x+c)+d

if functype.lower() == "l":
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    d = int(input("d: "))
    logbase = input("logbase (1, 3, e): ")

    if logbase == "e":
        func = lambda x : a*np.log((b*x)+c) + d

    else:
        func = lambda x : a*np.emath.logn(int(logbase), (b*x)+c) + d

if functype.lower() == "e":
    a = int(input("a: "))
    c = int(input("c: "))
    h = int(input("h: "))
    k = int(input("k: "))
    base = input("base (1, 3, e): ")

    if base == "e":
        func = lambda x : a*(math.e**((x/c)-h))+k

    else:
        func = lambda x : a*(int(b)**((x/c)-h))+k




var = limint(func, ll, ul, n)


print(var.lrs)

print(var.rrs)

print(var.mrs)

print(var.trs)

var.plot()
