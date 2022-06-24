import cv2

img = "C:/Users/Aaditya Paul/Documents/WhiteHat/Projects/c104/solar-system.jpg"

read = cv2.imread(img)
cv2.putText(read,"Sun",(100,400),cv2.FONT_HERSHEY_PLAIN,5,(0,255,0),10)
cv2.imshow("Solar System",read)
cv2.waitKey(0)
cv2.imwrite("SolarSystem_withName.png",read)
