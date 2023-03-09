dataset = []

import matplotlib.animation as animation
import matplotlib.pyplot as plt


def generateChart(dataset, gentype):
    xval = []
    yval = []
    sun = False

    if gentype == "XposYpos":
        for i in dataset:
            xval.append(i[3])
            yval.append(i[6])
            ti = "X postition Vs. Y Position"
            xl = "X Postion"
            yl = "Y position"
        

    elif gentype == "XposTime":

        for i in dataset:
            xval.append(i[0])
            yval.append(i[3])
            ti = "X postition Vs. Time"
            xl = "Time"
            yl = "X position"


    elif gentype == "YposTime":
        for i in dataset:
            xval.append(i[0])
            yval.append(i[6])
            ti = "Y postition Vs. Time"
            xl = "Time"
            yl = "Y position"

    
    elif gentype == "XVelTime":
        for i in dataset:
            xval.append(i[0])
            yval.append(i[1])
            ti = "X Velocity Vs. Time"
            xl = "Time"
            yl = "X Velocity"

    
    elif gentype == "YVelTime":
        for i in dataset:
            xval.append(i[0])
            yval.append(i[4])
            ti = "Y Velocity Vs. Time"
            xl = "Time"
            yl = "Y Velocity"


    elif gentype == "XaTime":
        for i in dataset:
            xval.append(i[0])
            yval.append(i[2])
            ti = "X Accelaration Vs. Time"
            xl = "Time"
            yl = "X Accelaration"


    elif gentype == "YaTime":
        for i in dataset:
            xval.append(i[0])
            yval.append(i[5])
            ti = "Y Accelaration Vs. Time"
            xl = "Time"
            yl = "Y Accelaration"
    if gentype == "XPosYPos":
        xmax = 1e7
        xmin = -1e7
        ymax = 1e7  
        ymin = -1e7
        sun = True
    else:
        xmax = max(xval)*1.5
        xmin = min(xval)*1.5
        ymax = max(yval)*1.5   
        ymin = min(yval)*1.5
 
    def data():
        for i in range(len(xval)):
            yield xval[i], yval[i]


    def init():
        ax.set_ylim(ymin, ymax)
        ax.set_xlim(xmin, xmax)

        if sun:
            ax.plot(0,0, "ro")
        plt.grid(visible=True, which='major', axis='both')
        plt.title(ti)
        plt.xlabel(xl)
        plt.ylabel(yl)
        del xdata[:]
        del ydata[:]
        line.set_data(xdata, ydata)
        return line

    fig, ax = plt.subplots()
    line, = ax.plot([], [], lw=.5)
    
    ax.grid()
    xdata, ydata = [], []


    def run(data):
        # update the data
        t, y = data
        xdata.append(t)
        ydata.append(y)

        xmin, xmax = ax.get_xlim()

        if t >= xmax:
            ax.set_xlim(xmin, 2*xmax)
            ax.figure.canvas.draw()
        line.set_data(xdata, ydata)

        return line,

    # Only save last 100 frames, but run forever
    ani = animation.FuncAnimation(fig, run, data, interval=0, init_func=init,
                                save_count=iterC)
    
    
    plt.show()



def singlepointOrbit():

    fig, ax = plt.subplots()

    xval = []
    yval = []

    for i in dataset:
        xval.append(i[3])
        yval.append(i[6])
        ti = "Animated Orbit Path"
        xl = "X Postion"
        yl = "Y position"

    def animate(i):
        ax.clear()
        # Get the point from the points list at index i
        # Plot that point using the x and y coordinates

        ax.set_ylim(-1e7, 1e7)
        ax.set_xlim(-1e7, 1e7)
        plt.grid(visible=True, which='major', axis='both')
        plt.title("Visualization of orbital Path")
        plt.xlabel(xl)
        plt.ylabel(yl)
        ax.plot(0,0, "ro")
        ax.plot(xval[i], yval[i], color='green', 
                label='original', marker='.', markersize=2)
        # Set the x and y axis to display a fixed range
        
    ani = animation.FuncAnimation(fig, animate, frames=iterC,
                        interval=0, repeat=False)

    plt.show()

def makeData(time, G, hostMass, initialX, initialY, ViX, ViY, iterC ):
    t = 0
    # ViX = ViX
    # initialY = initialY
    # initialX = initialX
    # ViY = ViY
    Aix = (-1*G)*((hostMass*initialX)/(initialX**2)**1.5)#=(-1*$J$4)*(($J$5*$J$6)/($J$6^2)^1.5)
    Aiy = (-1*G)*((hostMass*initialY)/(initialX**2+initialY**2)**1.5)#=(-1*$J$4)*(($J$5*$J$7)/($J$6^2+$J$7^2)^1.5)

    dataset.append([t, ViX, Aix, initialX, ViY, Aiy, initialY])
    print(t, ViX, Aix, initialX, ViY, Aiy, initialY)
    
    for i in range(iterC): #time, x vel, x pos, , y vel, y pos, Ax, Ay
        t = dataset[i][0]+time
        VelX = dataset[i][1]+dataset[i][2]*time
        xPos = dataset[i][3]+VelX*time  
        VelY= dataset[i][4]+dataset[i][5]*time
        yPos = dataset[i][6]+VelY*time
        Ax = (-1*G)*((hostMass*xPos)/(xPos**2+yPos**2)**1.5)#=(-1*$J$4)*(($J$5*D3)/(D3^2+G3^2)^1.5)
        Ay = (-1*G)*((hostMass*yPos)/(xPos**2+yPos**2)**1.5)
        dataset.append([t, VelX, Ax, xPos, VelY, Ay, yPos])

    #for j in range(len(dataset)):
        #print(dataset[j])
    
    singlepointOrbit()

    generateChart(dataset, gentype="YaTime")
    '''
    For X position vs Y position, use "XposYpos"
    For X position vs Time, use "XposTime"
    For Y position vs Time, use "YposTime"
    For X velocity  vs Time, use "XVelTime"
    For Y velocity  vs Time, use "YVelTime"
    For X Accelaration Vs Time, use "XaTime"
    For Y Accelaration Vs Time, use "YaTime"
    '''



if __name__ == '__main__':

    time = 10
    G = 6.67e-11
    hostMass = 6.00e24
    initialX = 4.00e06
    initialY = 0.00e00
    ViX = 0.00e00
    ViY = 7.00e03

    global iterC

    iterC = 2000

    makeData(time, G, hostMass, initialX, initialY, ViX, ViY, iterC)