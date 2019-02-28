import cv2
cap=cv2.VideoCapture(0)
while(cap.isOpened()):
	f,frame=cap.read()
	if f:
		cv2.imwrite('example.png',frame);
		faceCascade=cv2.CascadeClassifier('./haarcascade_frontalface_default.xml');
		image=cv2.imread('./example.png');
		gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY);
		faces=faceCascade.detectMultiScale(
		        gray,
		        scaleFactor=2,
		        minNeighbors=2,
		        minSize=(30,30),
		        flags=cv2.IMREAD_GRAYSCALE
		)
		for(x,y,w,h) in faces:
		    cv2.circle(image,((x+x+w)/2,(y+y+h)/2),w/2,(0,255,0),2);
		cv2.imshow('example.png',image);
		cv2.waitKey(1)
