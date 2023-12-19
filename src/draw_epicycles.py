from matplotlib.animation import FuncAnimation
import fourier
import numpy as np
import matplotlib.pyplot as plt
import math
from copy import deepcopy

all_circles = []

def constructPlane(signal):
        
    DFT_SIGNAL = fourier.dft(signal)

    global sorted_signal

    # sort the circles by its amplitude 
    sorted_signal = sorted(DFT_SIGNAL, key=lambda amp: amp[2])
    sorted_signal.reverse()
    
    offset = drawEpicycles()
    print("offset: ", offset) 
    
    plt.axis('equal')
    plt.xlim(-offset, offset)
    plt.ylim(-offset, offset)

    plt.title('Fourier Epicycles, n = ' +  str(len(sorted_signal)))

#    anim = animate()
    
    #anim.save("/images/animation.gif", writer='imagemagick', fps=15)
    plt.show()

def paramCircle(radius, angle):
    return np.array([radius * math.cos(angle), radius * math.sin(angle)])

def update(angle):
    # angle increments by the frame (0 to 2pi, 300)
    for index in range(len(all_circles)):
        # skip first circle because it does not move
        if index == 0:
            copy = deepcopy(all_circles[0])
            all_circles[0] = copy
            plt.gca().add_patch(all_circles[0])
            continue

        radius = sorted_signal[index-1][2]
        new_x, new_y = paramCircle(radius, angle + sorted_signal[index-1][3])
        
        old_x = all_circles[index].center[0]
        old_y = all_circles[index].center[1]
        
        sum_x = old_x + new_x
        sum_y = old_y + new_y
        
        print("FIRST",all_circles[index].center)
        all_circles[index].set_center([sum_x, sum_y])
        print("SECOND",all_circles[index].center)
        copy = deepcopy(all_circles[index])
        all_circles[index] = copy
        
        plt.gca().add_patch(all_circles[index])
    return all_circles  


def animate():
    fig = plt.gcf()
    
    # 300 evenly spaced from 0 to 2pi
    space = np.linspace(0,2*math.pi, 360, endpoint=False)
    
    #interval = (2*math.pi)/len(sorted_signal)
    
    anim = FuncAnimation(fig, update, interval=10, repeat=True, blit=True, frames=space)
    
    return anim 

def drawEpicycles():
    # 0 complx 
    # 1 freq
    # 2 amp
    # 3 phase


    initial = [0,0]
    
    x_val = []
    y_val = []

    
    for complx in sorted_signal:
        first = initial 
        
        circle = plt.Circle((first[0], first[1]), complx[2], color='r', fill=False)

        # gca = get current axis
        plt.gca().add_patch(circle)

        # store all circles for animation
        all_circles.append(circle)

        # next center of circle is amplitude * cos(phase), cos & sin
        initial[0] += complx[2]*np.cos(complx[3])
        initial[1] += complx[2]*np.sin(complx[3])

        x_val.append([first[0], initial[0]])
        y_val.append([first[1], initial[1]])
        
        if sorted_signal[0] == complx:
            print("wowo")
            plt.plot(x_val, y_val, '-r')
    print(x_val[0], x_val[1])    
    lines = [x_val, y_val]
    
    plt.plot(x_val, y_val, '-r')
   
    return math.sqrt(initial[0]*initial[0] + initial[1]*initial[1])

