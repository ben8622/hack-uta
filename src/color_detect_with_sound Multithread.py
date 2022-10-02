import cv2
import numpy as np
import sounddevice as sd
import soundfile as sf
import random
import os
import threading
import signal


os.chdir(os.getcwd() + '/data')

sound_files = ['sussy_baka.wav',
                'sus_music.wav',
                'sus_sound.wav']
sus_detected = False
sus_loop = True

def handler(signum, frame):
    print("Program ending...", flush=True)
    global sus_loop
    sus_loop = False
    t1.join()
    exit(1)

def play_sound():
    global sus_detected
    global sus_loop
    while(sus_loop):
        if(sus_detected):
            i = random.randrange(0,3,1)
            data, fs = sf.read(sound_files[i])
            sd.play(data, fs)
            status = sd.wait()
            sus_detected = False

t1 = threading.Thread(target=play_sound, args=())
t1.start()

# Handle ctrl+c shutdown for cleanup
signal.signal(signal.SIGINT, handler)

# Initialize camera. 2 is for the stereo camera
webcam = cv2.VideoCapture(1)


# # Camera Capture resolution
x_res : int = 1920
y_res : int = 1080

webcam.set(3, x_res)
webcam.set(4, y_res)

# initialize variables

# Color to detect bounds
threshold = 30

# Blue
b_lower_bound = np.array([100,150,0])
b_upper_bound = np.array([140,255,255])
# Green
g_lower_bound = np.array([56-threshold, 255*.336-threshold, 255*.561-threshold])
g_upper_bound = np.array([56+threshold, 255*.336+threshold, 255*.561+threshold])

is_recording : bool = True

# Starting video capture
while is_recording:
    (_, im) = webcam.read()

    # print(im.shape)

    hsv_im = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_im, g_lower_bound, g_upper_bound)

    kernel = np.ones((7,7), np.uint8)

    filtered_mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    filtered_mask_2 = cv2.morphologyEx(filtered_mask, cv2.MORPH_OPEN, kernel)

    segmented_im = cv2.bitwise_and(im, im, mask=filtered_mask_2)

    # Draw a boundary of the detected objects
    contours, heirarchy = cv2.findContours(filtered_mask_2.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 1000):
            sus_detected = True
            
            # print('sus detected')
            x, y, w, h = cv2.boundingRect(contour)
            im = cv2.rectangle(im, (x, y),
                                       (x + w, y + h),
                                       (255, 0, 0), 2)
              
            cv2.putText(im, "Kinda Sus", (x, y),
                        cv2.FONT_HERSHEY_TRIPLEX,
                        1.3, (255, 10, 10))
        else:
            sus_detected = False

    output = cv2.drawContours(segmented_im, contours, -1, (0,0,225), 3)
   
    cv2.imshow("Output", im)

    escape_key : int = 27
    key = cv2.waitKey(500)
    if key == escape_key:
        is_recording = False
