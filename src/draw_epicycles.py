from matplotlib import animation
import fourier
import numpy as np
import matplotlib.pyplot as plt
import math

def constructPlane(signal):
        

    DFT_SIGNAL = fourier.dft(signal)

    
    offset = drawCircles(DFT_SIGNAL)
    print("offset: ", offset) 

    
    plt.axis('equal')
    plt.xlim(-offset, offset)
    plt.ylim(-offset, offset)

    plt.title('Fourier Epicycles, n = ' +  str(len(DFT_SIGNAL)))

    plt.show()
    

def drawCircles(DFT_signal):
    # 0 complx 
    # 1 freq
    # 2 amp
    # 3 phase

    # sort the circles by its amplitude 
    sorted_signal = sorted(DFT_signal, key=lambda amp: amp[2])
    sorted_signal.reverse()

    initial = [0,0]
    
    x_val = []
    y_val = []

    for complx in sorted_signal:
        first = initial 
        print("first: ", first)
        circle = plt.Circle((first[0], first[1]), complx[2], color='r', fill=False)


        # gca = get current axis
        plt.gca().add_patch(circle)

        
        # next center of circle is amplitude * cos(phase), cos & sin
        initial[0] += complx[2]*np.cos(complx[3])
        initial[1] += complx[2]*np.sin(complx[3])

        x_val.append([first[0], initial[0]])
        y_val.append([first[1], initial[1]])
            
    
    plt.plot(x_val, y_val, '-r')
    return math.sqrt(initial[0]*initial[0] + initial[1]*initial[1])


#def animate(DFT_signal)
