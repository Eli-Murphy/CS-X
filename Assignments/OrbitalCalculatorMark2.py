#!/usr/bin/env python
__author__ = "Elijah Murphy"
__copyright__ = "Copyright 2023, CS-X Classwork"
__license__ = "MIT"
__version__ = "2.0.3"
__maintainer__ = "Elijah Murphy"
__email__ = "emurphy24@gcds.net"
__status__ = "Complete, in optimization"

from itertools import count

import matplotlib.animation as animation
import matplotlib.pyplot as plt

dataset = []

def generateCharts(dataset):

    #Storage of each column of data
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


    #Creates the figure and set of axes
    fig, ax = plt.subplots(3,3)

    #Increases size of figure
    fig.set_size_inches(18, 10, True)

    #deletes unnecesarry axes that are not used
    fig.delaxes(ax[0][0])
    fig.delaxes(ax[0][2])


    planet, = ax[0,1].plot(xpos, ypos, "go")                #Defines the planet in the X pos Vs Y Pos graph
    line1, = ax[0,1].plot(xpos, ypos, lw=.5)                #Creates the line of travel of the planet
    ax[0, 1].set_ylim(min(ypos)*1.5, max(ypos)*1.5)         #Scales the axes to 1.5 times the maxes and mins to show the whole graph
    ax[0,1].set_xlim(min(xpos)*1.5, max(xpos)*1.5)          #Same as above but for the X axis
    ax[0,1].plot(0,0, "yo")                                 #Plots the "sun" or orbiter
    ax[0,1].grid(visible=True, which='major', axis='both')  #Creates gridlines
    ax[0,1].title.set_text("X Position Vs. Y Positon")      #Creates graph title
    ax[0,1].set_xlabel("X Position (m)")                    #Creates X axis label
    ax[0,1].set_ylabel("Y Position (m)")                    #Creates Y axis label

    line2, = ax[1,0].plot(time, xpos, lw=.5) 
    ax[1,0].set_ylim(min(xpos)*1.1, max(xpos)*1.1)
    ax[1,0].set_xlim(min(time)*1.1, max(time)*1.1) 
    ax[1,0].title.set_text("X Position Vs. Time") 
    ax[1,0].grid(visible=True, which='major', axis='both')
    ax[1,0].set_xlabel("Time (s?)") 
    ax[1,0].set_ylabel("X Position (m)")

    line3, = ax[1,1].plot(time, ypos, lw=.5) 
    ax[1,1].set_ylim(min(ypos)*1.1, max(ypos)*1.1) 
    ax[1,1].set_xlim(min(time)*1.1, max(time)*1.1) 
    ax[1,1].title.set_text("Y Position Vs. Time")
    ax[1,1].grid(visible=True, which='major', axis='both') 
    ax[1,1].set_xlabel("Time (s?)") 
    ax[1,1].set_ylabel("Y Position (m)")

    line4, = ax[1,2].plot(time, xvel, lw=.5) 
    ax[1,2].set_ylim(min(xvel)*1.1, max(xvel)*1.1)
    ax[1,2].set_xlim(min(time)*1.1, max(time)*1.1)
    ax[1,2].title.set_text("X Velocity Vs. Time") 
    ax[1,2].grid(visible=True, which='major', axis='both')
    ax[1,2].set_xlabel("Time (s?)") 
    ax[1,2].set_ylabel("X Velocity (m/s)") 

    line5, = ax[2,0].plot(time, yvel, lw=.5)
    ax[2,0].set_ylim(min(yvel)*1.1, max(yvel)*1.1)
    ax[2,0].set_xlim(min(time)*1.1, max(time)*1.1) 
    ax[2,0].title.set_text("Y Velocity Vs. Time")
    ax[2,0].grid(visible=True, which='major', axis='both') 
    ax[2,0].set_xlabel("Time (s?)") 
    ax[2,0].set_ylabel("Y Velocity (m/s)") 
    
    line6, = ax[2,1].plot(time, xac, lw=.5) 
    ax[2,1].set_ylim(min(xac)*1.1, max(xac)*1.1)
    ax[2,1].set_xlim(min(time)*1.1, max(time)*1.1)
    ax[2,1].title.set_text("X Acc Vs. Time")
    ax[2,1].grid(visible=True, which='major', axis='both')
    ax[2,1].set_ylabel("X Accelaration (m/s/s)") 
    ax[2,1].set_xlabel("Time (s?)") 

    line7, = ax[2,2].plot(time, yac, lw=.5) 
    ax[2,2].set_ylim(min(yac)*1.1, max(yac)*1.1)
    ax[2,2].set_xlim(min(time)*1.1, max(time)*1.1)
    ax[2,2].title.set_text("Y Acc Vs. Time") 
    ax[2,2].grid(visible=True, which='major', axis='both')
    ax[2,2].set_xlabel("Time (s?)") 
    ax[2,2].set_ylabel("Y Accelaration (m/s/s)") 

    #Itertools count function to make indexing the data simpler
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
            #Adds new data to the animation lists
            time_animation.append(time[next(index)])
            xpos_animation.append(xpos[next(index)])
            ypos_animation.append(ypos[next(index)])
            xvel_animation.append(xvel[next(index)])
            yvel_animation.append(yvel[next(index)])
            xac_animation.append(xac[next(index)])
            yac_animation.append(yac[next(index)])
            
            #Sets the new position for the animation
            planet.set_data(xpos_animation[-1], ypos_animation[-1])
            line1.set_data(xpos_animation, ypos_animation)
            line2.set_data(time_animation, xpos_animation)
            line3.set_data(time_animation, ypos_animation)
            line4.set_data(time_animation, xvel_animation)
            line5.set_data(time_animation, yvel_animation)
            line6.set_data(time_animation, xac_animation)
            line7.set_data(time_animation, yac_animation)

            return [planet, line1, line2, line3, line4, line5, line6, line7]

    #Creates animation
    ani = animation.FuncAnimation(fig, animate, interval=3, save_count=iterC, frames=60)

    #Writer settings for graph
    writergif = animation.PillowWriter(fps = 60)

    fig.tight_layout()

    #writergif.setup(fig, "2D_Schrodinger_Equation.gif", dpi = 300) 

   # ani.save("graph animation.gif", writer = writergif, dpi = 300)

   
    plt.show()


def makeData(time, G, hostMass, initialX, initialY, ViX, ViY, iterC ):
    
    t = 0

    #Generates the first row accelarations which require a different formula than the rest.
    Aix = (-1*G)*((hostMass*initialX)/(initialX**2)**1.5)#=(-1*$J$4)*(($J$5*$J$6)/($J$6^2)^1.5)
    Aiy = (-1*G)*((hostMass*initialY)/(initialX**2+initialY**2)**1.5)#=(-1*$J$4)*(($J$5*$J$7)/($J$6^2+$J$7^2)^1.5)

    dataset.append([t, ViX, Aix, initialX, ViY, Aiy, initialY])

    #Calculates the n number of lines of data
    for i in range(iterC-1): 
        t = dataset[i][0]+time
        VelX = dataset[i][1]+dataset[i][2]*time
        xPos = dataset[i][3]+VelX*time  
        VelY= dataset[i][4]+dataset[i][5]*time
        yPos = dataset[i][6]+VelY*time
        Ax = (-1*G)*((hostMass*xPos)/(xPos**2+yPos**2)**1.5)#=(-1*$J$4)*(($J$5*D3)/(D3^2+G3^2)^1.5)
        Ay = (-1*G)*((hostMass*yPos)/(xPos**2+yPos**2)**1.5)
        dataset.append([t, VelX, Ax, xPos, VelY, Ay, yPos])

    
    generateCharts(dataset)

if __name__ == '__main__':


    #Modifiable Variables for Orbit
    time = 3
    G = 6.67e-11
    hostMass = 6.00e24
    initialX = 4.00e06
    initialY = 0.00e00
    ViX = 0.00e00
    ViY = 7.00e03

    global iterC

    iterC = 2000

    makeData(time, G, hostMass, initialX, initialY, ViX, ViY, iterC)



# Copyright (c) 2023 Elijah A. Murphy
# Distributed under the terms of the MIT License. 
# SPDX-License-Identifier: MIT
# This code is part of my CS-X Classwork (https://github.com/Eli-Murphy/CS-X)  