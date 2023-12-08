import cv2
from numpy import asarray
import numpy
import sys

img = cv2.imread("premierleagueLOGO.jpeg", cv2.IMREAD_COLOR)
cv2.imshow("image", img)
font = cv2.FONT_HERSHEY_COMPLEX 

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
edged = cv2.Canny(gray, 30, 200) 
cv2.waitKey(0) 

contours, hierarchy = cv2.findContours(edged,  
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
  
cv2.imshow('Canny Edges After Contouring', edged) 
cv2.waitKey(0) 

numpydata = asarray(edged)
print(numpydata) 


#Find edges of contours
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

line_thickness = 2
cv2.line(img, (minX, minY), (maxX, minY), (0, 255, 0), thickness=line_thickness)
cv2.line(img, (minX, minY), (minX, maxY), (0, 255, 0), thickness=line_thickness)
cv2.line(img, (maxX, minY), (maxX, maxY), (0, 255, 0), thickness=line_thickness)
cv2.line(img, (minX, maxY), (maxX, maxY), (0, 255, 0), thickness=line_thickness)

cv2.imshow("bounding_box", img)
cv2.waitKey(0)
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

