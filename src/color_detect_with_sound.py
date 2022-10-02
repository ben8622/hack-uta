import cv2
import numpy as np
import sounddevice as sd
import soundfile as sf
import random
import os

os.chdir(os.getcwd() + '/data')

sound_files = ['sussy_baka.wav',
                'sus_music.wav',
                'sus_sound.wav']

# Initialize camera. 2 is for the stereo camera
webcam = cv2.VideoCapture(0)


# # Camera Capture resolution
# x_res : int = 640
# y_res : int = 480

# webcam.set(3, x_res)
# webcam.set(4, y_res)


# initialize variables
lower_bound = np.array([100,150,0])
upper_bound = np.array([140,255,255])

is_recording : bool = True
play_sound : bool = False

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

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 400):
            play_sound = True
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(im, (x, y),
                                       (x + w, y + h),
                                       (255, 0, 0), 2)
              
            cv2.putText(im, "Potential Pepsi (Sus)", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (255, 0, 0))


    output = cv2.drawContours(segmented_im, contours, -1, (0,0,225), 3)


    if play_sound:
        cv2.imshow("Output", imageFrame)

        i = random.randrange(0,3,1)
        data, fs = sf.read(sound_files[i])
        sd.play(data, fs)
        status = sd.wait()
    else:
        cv2.imshow("Output", im)


    escape_key : int = 27
    key = cv2.waitKey(500)
    if key == escape_key:
        is_recording = False
