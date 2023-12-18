import math

PI = math.pi
signal = []

y_fourier = fft(y)

x_fourier = fft(x)



N = len(signal)

for point in y_fourier:
    y_old = y

    n = i * 2 + 1
    radius = 75 * (4/(n*PI))
    
    # connect vectors
    y += radius * cos(n*time)



def dft(signal):
        # k is the number of elements in the signal (frequency)
        # N is the length of the signal
        # x is the signal 
        # n is the nested for-loop with length N  
        
        fourier = []
        N = len(signal)
        
        for k in range(len(N)):
            
            initial = complex(0,0)
        
            for n in range(len(N)):
                
                # from dft formula, substitute angle inside cos and sine
                angle = (2 * PI * k * n) / N
                
                comp = complex(math.cos(angle), -sin(angle))

                # dot product of two complex numbers: dot((a + bi), (c + di)) = ac + adi + bci + bdi^2, bdi^2 = - bdi
                initial += signal[k]*comp
            
            # normalizing 
            initial = initial/N 
            
            # discrete frequency components
            freq = k 

            # length of the complex vector
            amp = sqrt(initial.real*initial.real + initial.imag*initial.imag)

            # angle of the vector
            phase = math.atan2(initial.imag, initial.real)


            fourier.append(initial, freq, amp, phase)
        
    return fourier


        # change in time
        dt = (2*PI) / len(y_fourier)
        time += dt


# draw loop

for i in range(len(y_fourier))
