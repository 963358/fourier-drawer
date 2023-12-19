import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt
import math

max_points = 30 

def start_filter(path):
    image_path = path 
    #load in image
    gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # filter 
    blur = cv2.GaussianBlur(gray, (5,5), 0)

    # apply canny filter
    #edged = cv2.Canny(gray, 100, 200)

    ret, thresh = cv2.threshold(blur,127,255, cv2.THRESH_BINARY)    

    edged = cv2.Canny(thresh, 100, 200)

    contours, hierarchy = cv2.findContours(edged,  
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
   
    cv2.drawContours(edged, contours, -1, (255,0,0), 3)

    cv2.imshow('Contours after canny filter', edged)

    cv2.waitKey(0) 


    originX = edged.shape[1]/2
    originY = edged.shape[0]/2



    white_pixels = make_coordinates(edged, originX, originY)
    print("original pixel length: ", len(white_pixels))



    while len(white_pixels) > max_points:
        # delete every 2nd element so that len/2
        del white_pixels[1::2]



    print("truncated length of pixels: ", len(white_pixels))
    

    # pixels_polar = make_polar(white_pixels)
    

    x_array = []
    y_array = []

    for white in white_pixels:
        x_array.append(white.real)
        y_array.append(white.imag)
    
    plt.plot(x_array, y_array, 'o')

    #plt.show()
    
    return np.array(white_pixels), edged.shape




def make_coordinates (cropped, originX, originY):
    h = cropped.shape[0]
    w = cropped.shape[1]

    white_pixels = []
    #make pixels into vectors relative to the origin
    for y in range(0, h):
        for x in range(0, w):
            # threshold the pixel
            if(cropped[y, x]>0):
                white_pixels.append(complex(x - originX, originY - y))
    
    return white_pixels


# delete this function, no need to use 
def make_polar (white_pixels):
    polar = []
    for pixel in white_pixels:
        x = pixel[0]
        y = pixel[1]

        arr = []
        r = math.sqrt(x*x + y*y)
        cosine = x/r
        sine = y/r
        
        r_cos = r*cosine
        r_sin = r*sine
        
        polar.append([r_cos, r_sin])

    return polar

