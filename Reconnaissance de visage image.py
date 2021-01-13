import cv2
#       Fichier reconnaissance   #
imagePath = "image.png"
cascadeClassifierPath = "haarcascade_frontalface_alt.xml"
#       Reconnaissance de visage         #
cascadeClassifier = cv2.CascadeClassifier(cascadeClassifierPath)
image = cv2.imread(imagePath)
grayImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
detectedFaces = cascadeClassifier.detectMultiScale(grayImage)

for(x,y,width,height) in detectedFaces:
    cv2.rectangle(image, (x, y), (x+width, y+height), (0,255,0), 2)
#        Création de l'image       #
cv2.imwrite('al.png',image)
#        Désolé je me retrouve pas sans commentaire (felicien)       #
