import cv2
from numpy import asarray
import numpy
import sys
import matplotlib.pyplot as plt
import math


def start_filter(path):
    image_path = path 
    #load in image
    gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img_copy = gray.copy()

    # filter 
    blur = cv2.GaussianBlur(gray, (5,5), 0)

    # apply canny filter
    edged = cv2.Canny(blur, 150, 200)

    contours, hierarchy = cv2.findContours(edged,  
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
   
    cv2.imshow('Contours after canny filter', edged)

    #cropped = crop_image(edged, contours)
    #cv2.imshow('Cropped Image', cropped)

    cv2.waitKey(0) 

    #originX = cropped.shape[1]/2
    #originY = cropped.shape[0]/2

    originX = edged.shape[1]/2
    originY = edged.shape[0]/2

    white_pixels = make_coordinates(edged, originX, originY)
    #print (white_pixels)

    pixels_polar = make_polar(white_pixels)

    x_array = []
    y_array = []
    for i in range(len(pixels_polar)):
        r = pixels_polar[i][0]
        cosine = pixels_polar[i][1]
        sine = pixels_polar[i][2]
        x_array.append(r*cosine)
        y_array.append(r*sine)
    
    plt.plot(x_array, y_array, 'o')
    plt.show()

    return pixels_polar  


#numpydata = asarray(edged)
#print(numpydata) 


# probably won't use
def crop_image (edged, contours):
    minX = math.inf
    maxX = 0
    minY = math.inf
    maxY = 0

    for cntr in contours:
        x,y,w,h = cv2.boundingRect(cntr)
        cv2.rectangle(edged, (x, y), (x+w, y+h), (0, 0, 255), 2)
        print("x,y,w,h:",x,y,w,h)

        maxX = max(maxX, x+w)
        minX = min(minX, x)
        
        maxY = max(maxY, y+h)
        minY = min(minY, y)

    crop_img = edged[minY:maxY, minX:maxX]
    return crop_img


def make_coordinates (cropped, originX, originY):
    h = cropped.shape[0]
    w = cropped.shape[1]

    white_pixels = []
    x_pixels = []
    y_pixels = []
    #make pixels into vectors relative to the origin
    for y in range(0, h):
        for x in range(0, w):
            # threshold the pixel
            if(cropped[y, x]>0):
                #cv2.circle(img, (x, y), radius=0, color=(0, 0, 255), thickness=-1)
                x_pixels.append(x-originX)
                y_pixels.append(originY-y)

                arr = []
                arr.append(x - originX)
                arr.append(originY - y)
                white_pixels.append(arr)
    
    # plt.plot(x_pixels, y_pixels, 'o')
    # plt.show()
    
    return white_pixels

def make_polar (white_pixels):
    length = len(white_pixels)
    polar = []
    for i in range (0, length):
        x = white_pixels[i][0]
        y = white_pixels[i][1]

        arr = []
        r = math.sqrt(x*x + y*y)
        cosine = x/r
        sine = y/r

        arr.append(r)
        arr.append(cosine)
        arr.append(sine)
        polar.append(arr)

        #print(r, cosine, sine)
    return polar

