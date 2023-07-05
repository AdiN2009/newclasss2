import cv2


img = cv2.imread("solar-system.jpg")
print(img)

sun= "Sun"
mercury = "Mercury"
venus = "Venus"
earth = "Earth"
mars = "Mars"
jupiter = "Jupiter"
saturn = "Saturn"
uranus = "Uranus"
neptune = "Neptune"


cv2.putText(img,sun,(110,100),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=1.7,color=(255,255,255))
cv2.putText(img,mercury,(122,245),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.4,color=(255,255,255))
cv2.putText(img,venus,(185,260),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.55,color=(255,255,255))
cv2.putText(img,earth,(280,270),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.7,color=(255,255,255))
cv2.putText(img,mars,(375,260),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.8,color=(255,255,255))
cv2.putText(img,jupiter,(560,380),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.8,color=(255,255,255))
cv2.putText(img,saturn,(760,310),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.8,color=(255,255,255))
cv2.putText(img,uranus,(960,290),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.8,color=(255,255,255))
cv2.putText(img,neptune,(1100,290),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.7,color=(255,255,255))

cv2.imshow("New Window",img)
cv2.waitKey(0)

cv2.imwrite("solar-system1.jpg",img)