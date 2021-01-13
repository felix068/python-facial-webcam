import numpy as np
import cv2
#	   Fichier reconnaissance   #
cascadeClassifierPath = 'haarcascade_frontalface_alt.xml'
cascadeClassifierPatheye = 'haarcascade_eye.xml'
cascadeClassifier = cv2.CascadeClassifier(cascadeClassifierPath)
cascadeClassifiereye = cv2.CascadeClassifier(cascadeClassifierPatheye)
cap = cv2.VideoCapture(0)


#	   Reconnaissance de visage		 #
print("Veuillez Patienter ...")
while(cap.isOpened()):
        _, frame = cap.read()
        grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        detectedFaces = cascadeClassifier.detectMultiScale(grayImage,  scaleFactor=1.1, minNeighbors=10, minSize=(18, 18))
        detectedeye = cascadeClassifiereye.detectMultiScale(grayImage,  scaleFactor=1.1, minNeighbors=10, minSize=(18, 18))
        for(x,y, width, height) in detectedFaces:
                cv2.rectangle(frame, (x, y), (x+width, y+height), (0,255,0), 3)
                for(x,y, width, height) in detectedeye:
                        cv2.rectangle(frame, (x, y), (x+width, y+height), (0,255,0), 3)
#		Affichage du résultat	   #
        cv2.imshow("video", frame)
        if cv2.waitKey(1) == ord('q'):
                break

#		Fin	   #
cap.release()
cv2.destroyAllWindows()
#		Désolé je me retrouve pas sans commentaire (felicien)	   #
