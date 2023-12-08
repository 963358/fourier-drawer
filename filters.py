import cv2
from numpy import asarray
import numpy
import sys
import matplotlib.pyplot as plt

#load in image
img = cv2.imread("premierleagueLOGO.jpeg", cv2.IMREAD_COLOR)
cv2.imshow("image", img)
font = cv2.FONT_HERSHEY_COMPLEX 

#Filters to distinguish edges of image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
edged = cv2.Canny(gray, 30, 200) 
cv2.waitKey(0)

contours, hierarchy = cv2.findContours(edged,  
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
  
cv2.imshow('Canny Edges After Contouring', edged) 
cv2.waitKey(0) 

#Find edges of contours to crop later on
minX = 99999999
maxX = 0
minY = 99999999
maxY = 0
for cntr in contours:
    x,y,w,h = cv2.boundingRect(cntr)
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    print("x,y,w,h:",x,y,w,h)

    maxX = max(maxX, x+w)
    minX = min(minX, x)
        
    maxY = max(maxY, y+h)
    minY = min(minY, y)

#Drawing a box around the area of interest
line_thickness = 2
cv2.line(img, (minX, minY), (maxX, minY), (0, 255, 0), thickness=line_thickness)
cv2.line(img, (minX, minY), (minX, maxY), (0, 255, 0), thickness=line_thickness)
cv2.line(img, (maxX, minY), (maxX, maxY), (0, 255, 0), thickness=line_thickness)
cv2.line(img, (minX, maxY), (maxX, maxY), (0, 255, 0), thickness=line_thickness)


#cv2.imshow("bounding_box", img)
#cv2.waitKey(0)

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

print(white_pixels)
cv2.destroyAllWindows()



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

