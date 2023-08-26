import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,  
           "Sun",
           (20, 300),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           0.5,  
           (255,255,255)
           )

cv2.putText(img,  
           "Mercury",
           (20, 220),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           0.5,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "Venus",
           (20, 220),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           0.5,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "Earth",
           (20, 220),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           0.5,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "Mars",
           (20, 220),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           0.5,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "Jupiter",
           (20, 220),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           0.5,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "Saturn",
           (20, 220),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           0.5,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "Uranus",
           (20, 220),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           0.5,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "Neptune",
           (20, 220),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           0.5,  
           color=(0,0,255)
           )

cv2.imwrite("solar-system.jpg",img)
cv2.imshow("Display Image",img)

cv2.waitKey(0)