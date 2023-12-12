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
    cv2.imshow('Canny Edges After Contouring', edged) 
   
    cropped = crop_image(edged, contours)
    cv2.imshow('Cropped Image', cropped)

    cv2.waitKey(0) 

    originX = cropped.shape[1]/2
    originY = cropped.shape[0]/2

    white_pixels = make_coordinates(cropped, originX, originY)
    #print (white_pixels)

    pixels_polar = make_polar(white_pixels)
    print(pixels_polar)

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


#numpydata = asarray(edged)
#print(numpydata) 

def crop_image (edged, contours):
    minX = 99999999
    maxX = 0
    minY = 99999999
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

    #print(white_pixels.shape[0], white_pixels.shape[1])

#Find edges of contours
# minX = 99999999
# maxX = 0
# minY = 99999999
# maxY = 0
#for cntr in contours:
#    x,y,w,h = cv2.boundingRect(cntr)
#    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
#    print("x,y,w,h:",x,y,w,h)
#
#    maxX = max(maxX, x+w)
#    minX = min(minX, x)
        
#    maxY = max(maxY, y+h)
#    minY = min(minY, y)

#Drawing a box around the area of interest
#line_thickness = 2
#cv2.line(img, (minX, minY), (maxX, minY), (0, 255, 0), thickness=line_thickness)
#cv2.line(img, (minX, minY), (minX, maxY), (0, 255, 0), thickness=line_thickness)
#cv2.line(img, (maxX, minY), (maxX, maxY), (0, 255, 0), thickness=line_thickness)
#cv2.line(img, (minX, maxY), (maxX, maxY), (0, 255, 0), thickness=line_thickness)


#cv2.imshow("bounding_box", img)
#cv2.waitKey(0)
"""
#Crop image to only include the contours (excess space gone)
crop_img = edged[minY:maxY, minX:maxX]
originX = (int)((maxX-minX)/2)
originY = (int)((maxY-minY)/2)

#Drawing origin + Axis (just for visualization)
#cv2.circle(crop_img, (originX, originY), radius=10, color=(0, 0, 255), thickness=-1)
#cv2.line(crop_img, (originX, 0), (originX, maxY), (0, 255, 0), thickness=line_thickness)
#cv2.line(crop_img, (0, originY), (maxX, originY), (0, 255, 0), thickness=line_thickness)

cv2.imshow("cropped", crop_img)
cv2.waitKey(0)
print(crop_img)
print(crop_img.shape)
#numpydata = asarray(crop_img)
#print(numpydata)
#print(numpydata.shape)

h = crop_img.shape[0]
w = crop_img.shape[1]

white_pixels = []
x_pixels = []
y_pixels = []
#make pixels into vectors relative to the origin
for y in range(0, h):
        for x in range(0, w):
            # threshold the pixel
            if(crop_img[y, x]>0):
                #cv2.circle(img, (x, y), radius=0, color=(0, 0, 255), thickness=-1)
                # x_pixels.append(x-originX)
                # y_pixels.append(originY-y)

                arr = []
                arr.append(x - originX)
                arr.append(originY - y)
                white_pixels.append(arr)

# plt.plot(x_pixels, y_pixels, 'o')
# plt.show()

#for x in range(1000):

#print(white_pixels)
#cv2.destroyAllWindows()



#Find edges of contours
# minX = 99999999
# maxX = 0
# minY = 99999999
# maxY = 0

# numpy.set_printoptions(threshold=sys.maxsize)
# numpydata = asarray(edged)
# print(numpydata)

# for cnt in contours : 
  
#     approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True) 
  
#     # draws boundary of contours. 
#     #cv2.drawContours(edged, [approx], 0, (0, 0, 255), 5)  
  
#     # Used to flatted the array containing 
#     # the co-ordinates of the vertices. 
#     n = approx.ravel()  
#     i = 0
  
#     for j in n : 
        
#         x = n[i] 
#         y = n[i + 1] 

#         maxX = max(maxX, x)
#         minX = min(minX, x)
        
#         maxY = max(maxY, y)
#         minY = min(minY, y)
  
#         # if(i == 0): 
#         #      # text on topmost co-ordinate. 
#         #     cv2.putText(edged, "Arrow tip", (x, y), 
#         #                         font, 0.5, (255, 0, 0))  
#         # else: 
#         #     # text on remaining co-ordinates. 
#         #     cv2.putText(edged, string, (x, y),  
#         #                   font, 0.5, (0, 255, 0))  
#         i = i + 1


# Showing the final image. 
# cv2.imshow('image2', edged) 
# cv2.waitKey(0)
"""
