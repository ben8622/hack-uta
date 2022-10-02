import cv2
import os
import numpy as np


# Initialize camera. 2 is for the stereo camera
webcam = cv2.VideoCapture(0)


# Camera Capture resolution
x_res : int = 640
y_res : int = 480

webcam.set(3, x_res)
webcam.set(4, y_res)


# initialize variables
lower_bound = np.array([100,150,0])
upper_bound = np.array([140,255,255])

is_recording : bool = True

# Starting video capture
while is_recording:
    (_, im) = webcam.read()

    print(im.shape)

    hsv_im = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_im, lower_bound, upper_bound)

    kernel = np.ones((7,7), np.uint8)

    filtered_mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    filtered_mask_2 = cv2.morphologyEx(filtered_mask, cv2.MORPH_OPEN, kernel)

    segmented_im = cv2.bitwise_and(im, im, mask=filtered_mask_2)

    # Draw a boundary of the detected objects
    contours, heirarchy = cv2.findContours(filtered_mask_2.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    output = cv2.drawContours(segmented_im, contours, -1, (0,0,225), 3)

    cv2.imshow("Output", output)

    escape_key : int = 27
    key = cv2.waitKey(500)
    if key == escape_key:
        is_recording = False
