import cv2
import os


webcam = cv2.VideoCapture(2)

is_recording = True
while is_recording:
	(_, im) = webcam.read()
	cv2.imshow('OpenCV webcam demo', im)
	key = cv2.waitKey(10)
	if key == 27:
		break
