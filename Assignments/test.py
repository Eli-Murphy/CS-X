import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

dataset = []


def generateCharts():

    time = []
    xvel = []
    xac = []
    xpos = []
    yvel = []
    yac = []
    ypos = []
    
    for i in dataset:
            time.append(i[0])
            xvel.append(i[1])
            xac.append(i[2])
            xpos.append(i[3])
            yvel.append(i[4])
            yac.append(i[5])
            ypos.append(i[6])


    

    fig = plt.figure()
    ax1 = plt.subplot(2, 1, 1)
    ax2 = plt.subplot(2, 1, 2)

    data_skip = 0


    def init_func():
        
        
        ax1.set_xlim(min(time), max(time))
        ax1.set_ylim(min(xpos), max(xpos))
        ax2.set_xlim(min(time), max(time))
        ax2.set_ylim(min(ypos), max(ypos))


    def update_plot(i):
        ax1.plot(time[i], xpos[i], color='b', lw=200)
        ax2.plot(time[i], ypos[i], color='b', lw=200)


    anim = FuncAnimation(fig,
                        update_plot,
                        init_func=init_func,
                        interval=1)

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
    

    generateCharts()
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

    time = 38
    G = 6.67e-11
    hostMass = 6.00e24
    initialX = 4.00e06
    initialY = 0.00e00
    ViX = 0.00e00
    ViY = 7.00e03

    global iterC

    iterC = 2000

    makeData(time, G, hostMass, initialX, initialY, ViX, ViY, iterC)