import cv2
#       Fichier reconnaissance   #
cascadeClassifierPath = 'haarcascade_frontalface_alt.xml'
cascadeClassifier = cv2.CascadeClassifier(cascadeClassifierPath)
cap = cv2.VideoCapture("video.mp4")
#       Reconnaissance de visage         #
while(cap.isOpened()):
	_, frame = cap.read()
	grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	detectedFaces = cascadeClassifier.detectMultiScale(grayImage,  scaleFactor=1.1, minNeighbors=10, minSize=(20, 20))
	for(x,y, width, height) in detectedFaces:
		cv2.rectangle(frame, (x, y), (x+width, y+height), (0,255,0), 3)
#        Affichage du résultat       #
	cv2.imshow("video", frame)
	if cv2.waitKey(30) == ord('q'):
		break

#        Fin       #
cap.release()
cv2.destroyAllWindows()
#        Désolé je me retrouve pas sans commentaire (felicien)       #
