dataset = []

import matplotlib.animation as animation
import matplotlib.pyplot as plt

#def main(time, G, hostMass, initialX, ViX, ):
    #makechart()

def generateChart(dataset, gentype):
    xval = []
    yval = []

    if gentype == "XposYpos":
        for i in dataset:
            xval.append(i[3])
            yval.append(i[6])
            ti = "X postition Vs. Y Position"
            xl = "X Postion"
            yl = "Y position"

    if gentype == "XposTime":
        for i in dataset:
            xval.append(i[0])
            yval.append(i[3])
            ti = "X postition Vs. Time"
            xl = "Time"
            yl = "X position"

    if gentype == "YposTime":
        for i in dataset:
            xval.append(i[0])
            yval.append(i[6])
            ti = "Y postition Vs. Time"
            xl = "Time"
            yl = "Y position"

    # fig, ax = plt.subplot() 
    # ax.set_xlim(min(xval), max(xval))
    # ax.set_ylim(min(yval), max(yval))
    # plt.plot(x,y) 
    # plt.show()

 

 
    def data():
        for i in range(len(xval)):
            yield xval[i], yval[i]


    def init():
        ax.set_ylim(min(yval)*1.5, max(yval)*1.5)
        ax.set_xlim(min(xval)*1.5, max(xval)*1.5)

        ax.set_ylim(-5e7, 5e7)
        ax.set_xlim(-5e7, 5e7)
        plt.grid(visible=True, which='major', axis='both')
        plt.title(ti)
        plt.xlabel(xl)
        plt.ylabel(yl)
        del xdata[:]
        del ydata[:]
        line.set_data(xdata, ydata)
        return line

    fig, ax = plt.subplots()
    line, = ax.plot([], [], lw=2)
    
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



def singlepoint():

    fig, ax = plt.subplots()

    xval = []
    yval = []

    for i in dataset:
        xval.append(i[3])
        yval.append(i[6])
        ti = "X postition Vs. Y Position"
        xl = "X Postion"
        yl = "Y position"

    def animate(i):
        ax.clear()
        # Get the point from the points list at index i
        # Plot that point using the x and y coordinates

        ax.set_ylim(-1e7, 1e7)
        ax.set_xlim(-1e7, 1e7)
        plt.grid(visible=True, which='major', axis='both')
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
    
    singlepoint()

    generateChart(dataset, gentype="XposYpos")


if __name__ == '__main__':
    # time = float(input("Delta time: "))
    # G = float(input("Gravity Constant (Sci Not): "))
    # hostMass = float(input("Mass of Host (Sci Not): "))
    # initialX = float(input("Initial X Pos (Sci Not): "))
    # initialY = float(input("Initial Y Pos (Sci Not): "))
    # ViX = float(input("Initial X Velocity (Sci Not): "))
    # ViY = float(input("Initial Y Velocity (Sci Not): "))
    # iterC = int(input("How many iterations? (int): "))

    time = 38
    G = 6.67e-11
    hostMass = 6.00e24
    initialX = 4.00e06
    initialY = 0.00e00
    ViX = 0.00e00
    ViY = 7.00e03

    global iterC

    iterC = 2000

    makeData(time, G, hostMass, initialX, initialY, ViX, ViY, iterC )
    #main()