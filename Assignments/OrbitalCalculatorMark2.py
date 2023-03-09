from itertools import count

import matplotlib.animation as animation
import matplotlib.pyplot as plt

dataset = []

def generateCharts(dataset):

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

    
    


    fig, ax = plt.subplots(3,3)

    fig.set_size_inches(18, 10, True)

    fig.delaxes(ax[0][0])
    fig.delaxes(ax[0][2])


    planet, = ax[0,1].plot(xpos, ypos, "go")
    line1, = ax[0,1].plot(xpos, ypos, lw=.5) #xposypos
    ax[0, 1].set_ylim(min(ypos)*1.5, max(ypos)*1.5)
    ax[0,1].set_xlim(min(xpos)*1.5, max(xpos)*1.5)
    ax[0,1].plot(0,0, "yo")
    ax[0,1].grid(visible=True, which='major', axis='both')
    ax[0,1].title.set_text("X Position Vs. Y Positon") 
    ax[0,1].set_xlabel("Time (s?)") 
    ax[0,1].set_ylabel("Y Position (m)")
    #ax1.title("Xpos Vs. YPos")    

    line2, = ax[1,0].plot(time, xpos, lw=.5) #xpostime
    ax[1,0].set_ylim(min(xpos)*1.1, max(xpos)*1.1)
    ax[1,0].set_xlim(min(time)*1.1, max(time)*1.1) 
    ax[1,0].title.set_text("X Position Vs. Time") 
    ax[1,0].grid(visible=True, which='major', axis='both')
    ax[1,0].set_xlabel("Time (s?)") 
    ax[1,0].set_ylabel("X Position (m)")
    #ax2.title("Xpos Vs. Time")    

    line3, = ax[1,1].plot(time, ypos, lw=.5) #ypostime
    ax[1,1].set_ylim(min(ypos)*1.1, max(ypos)*1.1) 
    ax[1,1].set_xlim(min(time)*1.1, max(time)*1.1) 
    ax[1,1].title.set_text("Y Position Vs. Time")
    ax[1,1].grid(visible=True, which='major', axis='both') 
    ax[1,1].set_xlabel("Time (s?)") 
    ax[1,1].set_ylabel("Y Position (m)")
    #ax3.title("Ypos Vs. Time")    

    line4, = ax[1,2].plot(time, xvel, lw=.5) #XVELTIME
    ax[1,2].set_ylim(min(xvel)*1.1, max(xvel)*1.1)
    ax[1,2].set_xlim(min(time)*1.1, max(time)*1.1)
    ax[1,2].title.set_text("X Velocity Vs. Time") 
    ax[1,2].grid(visible=True, which='major', axis='both')
    ax[1,2].set_xlabel("Time (s?)") 
    ax[1,2].set_ylabel("X Velocity (m/s)") 
    #ax4.title("XVel Vs. Time") 

    line5, = ax[2,0].plot(time, yvel, lw=.5) #yveltime
    ax[2,0].set_ylim(min(yvel)*1.1, max(yvel)*1.1)
    ax[2,0].set_xlim(min(time)*1.1, max(time)*1.1) 
    ax[2,0].title.set_text("Y Velocity Vs. Time")
    ax[2,0].grid(visible=True, which='major', axis='both') 
    ax[2,0].set_xlabel("Time (s?)") 
    ax[2,0].set_ylabel("Y Velocity (m/s)") 
    
    line6, = ax[2,1].plot(time, xac, lw=.5) #xactime
    ax[2,1].set_ylim(min(xac)*1.1, max(xac)*1.1)
    ax[2,1].set_xlim(min(time)*1.1, max(time)*1.1)
    ax[2,1].title.set_text("X Acc Vs. Time")
    ax[2,1].grid(visible=True, which='major', axis='both')
    ax[2,1].set_ylabel("X Accelaration (m/s/s)") 
    ax[2,1].set_xlabel("Time (s?)") 

    line7, = ax[2,2].plot(time, yac, lw=.5) #yactime
    ax[2,2].set_ylim(min(yac)*1.1, max(yac)*1.1)
    ax[2,2].set_xlim(min(time)*1.1, max(time)*1.1)
    ax[2,2].title.set_text("Y Acc Vs. Time") 
    ax[2,2].grid(visible=True, which='major', axis='both')
    ax[2,2].set_xlabel("Time (s?)") 
    ax[2,2].set_ylabel("Y Accelaration (m/s/s)") 

    index = count()
    # Animation Variables
    time_animation = []
    xpos_animation = []
    ypos_animation = []
    xvel_animation = []
    yvel_animation = []
    xac_animation = []
    yac_animation = []
    def animate(i):
      
        time_animation.append(time[next(index)])
        xpos_animation.append(xpos[next(index)])
        ypos_animation.append(ypos[next(index)])
        xvel_animation.append(xvel[next(index)])
        yvel_animation.append(yvel[next(index)])
        xac_animation.append(xac[next(index)])
        yac_animation.append(yac[next(index)])

        planet.set_data(xpos_animation[-1], ypos_animation[-1])
        line1.set_data(xpos_animation, ypos_animation)
        line2.set_data(time_animation, xpos_animation)
        line3.set_data(time_animation, ypos_animation)
        line4.set_data(time_animation, xvel_animation)
        line5.set_data(time_animation, yvel_animation)
        line6.set_data(time_animation, xac_animation)
        line7.set_data(time_animation, yac_animation)

        return [planet, line1, line2, line3, line4, line5, line6, line7]

    ani = animation.FuncAnimation(fig, animate, interval=1, save_count=iterC, frames=iterC)

    fig.tight_layout()

    ani.save('Graph Animation (DeltaT = 2).gif', fps=60)
   
    plt.show()




def makeData(time, G, hostMass, initialX, initialY, ViX, ViY, iterC ):
    t = 0

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

    
    generateCharts(dataset)
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

    time = 2
    G = 6.67e-11
    hostMass = 6.00e24
    initialX = 4.00e06
    initialY = 0.00e00
    ViX = 0.00e00
    ViY = 7.00e03

    global iterC

    iterC = 2000

    makeData(time, G, hostMass, initialX, initialY, ViX, ViY, iterC)