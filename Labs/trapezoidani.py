import matplotlib.animation as animation 
import matplotlib.pyplot as plt 
import numpy as np 
  
   
# creating a blank window

def lrs(a, b, n, poly):
    deltaX = (b-a)/n
    i = np.linspace(a,b-deltaX, n)      
    area = np.sum(poly(i) * deltaX)
    return area

def rrs(a, b, n, poly):
    deltaX = (b-a)/n
    i = np.linspace(a+deltaX,b, n)      
    area = np.sum(poly(i) * deltaX)
    return area

def mrs(a, b, n, poly):
    deltaX = (b-a)/n
    i = np.linspace(a+(deltaX/2),b-(deltaX/2), n)      
    area = np.sum(poly(i) * deltaX)
    return area

def trs(a, b, n, poly):
    area = lrs(a,b,n,poly)+((rrs(a,b,n,poly)-lrs(a,b,n,poly))/2)
    return area


a = 0
b = 5
n = 10
poly = lambda x : .2*x**2

fig = plt.figure() 
axis = plt.axes(xlim =(-2, 7),
                ylim =(-10, -10)) 
  
line, = axis.plot([], [], lw = 2) 

X = np.linspace(a,b,(n)**2+1)
Y = poly(X)

plt.figure(figsize=(10,10))

plt.plot(X,Y,'g')

   
# what will our line dataset
# contain?
def init(): 
    line.set_data([], []) 
    return line, 
   
# initializing empty values
# for x and y co-ordinates
xdata, ydata = [], [] 
   
# animation function 
def animate(i):
    x = np.linspace(a, b, 100)
   
    # plots a sine graph
   
      
    return line,
   
# calling the animation function     
anim = animation.FuncAnimation(fig, animate, init_func = init, 
                               frames = 500, interval = 20, blit = True) 
   
# saves the animation in our desktop
plt.show()