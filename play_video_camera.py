import cv2
import os


webcam = cv2.VideoCapture(2)

is_recording : bool = True
while is_recording:
	(_, im) = webcam.read()
	cv2.imshow('OpenCV webcam demo', im)
	
	escape_key : int = 27
	key = cv2.waitKey(500)
	if key == escape_key:
		is_recording = False
