import cv2
img=cv2.imread("image.jpg")
cv2.imwrite("extension.png",img)   #saving the image
#gry=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #saving black and white
gry=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)  #
cv2.imwrite("rgb.png",gry)

